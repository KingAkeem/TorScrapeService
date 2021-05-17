# TorScrapeService
A service that provides web scraping functionality for Tor sites via gRPC protocol

### Compiling 
In order to view changes made to the proto file, you'll need to compile the file using the command below:
- `python3 -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/scrape.proto` (from the `protobufs` directory)

### Run Server
After compiling the proto file, you'll be able to start the server by running `python3 ./protobufs/scraper.py` (from the root directory)
* If you're having trouble with starting the server then you may need to upgrade `protobuf` using `pip3 install --upgrade protobuf`


### Connecting a client
In order to connect a client you'll need to import the `grpc` package along with the client `protobufs`, an example is provided below:
```python3
import grpc
from scrape_pb2_grpc import ScraperStub
from scrape_pb2 import ScrapeRequest, TokenType

channel = grpc.insecure_channel('localhost:50051')
client = ScraperStub(channel)
request = ScrapeRequest(type=TokenType.DOCUMENT, url='http://www.propub3r6espa33w.onion')
client.Scrape(request)
```
