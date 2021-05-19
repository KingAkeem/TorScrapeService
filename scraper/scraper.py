import os
import grpc
import asyncio
import aiohttp

from grpc import aio
from bs4 import BeautifulSoup
from aiohttp_socks import ProxyConnector

import scrape_pb2_grpc
from scrape_pb2 import ScrapeResponse, TokenType

def create_tor_connector(settings):
    url = 'socks5://@{host}:{port}'.format(host=settings['host'], port=settings['port'])

    if 'username' in settings or 'password' in settings:
        if 'username' not in settings or 'password' not in settings:
            raise Exception('Username and password required.')
        url = 'socks5://{username}:{password}@{host}:{port}'.format(
            username=settings['username'], password=settings['password'],
            host=settings['host'], port=settings['port'])

    return ProxyConnector.from_url(url)


async def scrape(client, url, depth):
    response = await client.get(url)
    html_content = await response.text()
    soup = BeautifulSoup(html_content, 'html.parser')

    if depth == TokenType.DOCUMENT:
        return [soup.text.encode('utf-8')]
    elif depth == TokenType.TAG:
        return [tag.encode('utf-8') for tag in soup()]
    elif depth == TokenType.ATTRIBUTE:
        return [str(tag.attrs).encode('utf-8') for tag in soup()]

class ScraperService(scrape_pb2_grpc.ScraperServicer):
    def __init__(self, session):
        self.session = session;

    async def Scrape(self, request, context):
        if not request.url or request.type == None:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, 'Missing required argument.');
        try:
            links = await scrape(self.session, request.url, request.type)
        except Exception as err:
            print('Unable to handle request.', err)

        return ScrapeResponse(tokens=links, type=request.type)

async def serve():
    port = os.getenv('SOCKS5_PORT', '9050')
    host = os.getenv('SOCKS5_HOST', '127.0.0.1')
    connector = create_tor_connector({
        'host': host,
        'port': port,
        'username': os.getenv('SOCKS5_USERNAME', ''),
        'password': os.getenv('SOCKS5_PASSWORD', '')
    })
    print("Attempting to connect to Tor on {host}:{port}".format(host=host, port=port))
    async with aiohttp.ClientSession(connector=connector) as session:
        print('Tor connected.')
        server = aio.server()
        scrape_pb2_grpc.add_ScraperServicer_to_server(ScraperService(session), server)
        server.add_insecure_port("[::]:50051")
        print('Starting gRPC server on port 50051')
        await server.start()
        await server.wait_for_termination()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(serve())
