import grpc
import argparse

from bs4 import BeautifulSoup

from scrape_pb2 import ScrapeRequest, TokenType
from scrape_pb2_grpc import ScraperStub


def print_document(tokens):
    document = tokens[0]
    soup = BeautifulSoup(document, 'html.parser')
    print(soup.prettify())

def print_tokens(tokens):
    for index, token in enumerate(tokens):
        print('{index}. {token}'.format(index=index+1, token=token))

printers = {
    TokenType.DOCUMENT: print_document,
    TokenType.TAG: print_tokens,
    TokenType.ATTRIBUTE: print_tokens
}

class ScraperClient: 
    def __init__(self, channel = grpc.insecure_channel('localhost:50051')):
        self.client = ScraperStub(channel)
    
    def scrape(self, url, type):
        request = ScrapeRequest(type=type, url=url)
        response = self.client.Scrape(request)
        return response.tokens

def main():
    parser = argparse.ArgumentParser(description='Provide a url to scrape.')
    parser.add_argument('url', type=str, help="The HTML of this document will be used for scraping.")
    parser.add_argument('--type', type=int, default=TokenType.DOCUMENT, help='The available types are 0, 1, 2. 0 will print the entire document, 1 will print the parsed HTML tags, 2 will print the parsed HTML attributes.')
    args = parser.parse_args()

    client = ScraperClient()
    tokens = client.scrape(args.url, args.type)
    printers[args.type](tokens)

if __name__ == '__main__':
    main()
