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
request = ScrapeRequest(type=TokenType.TAG, url='http://www.propub3r6espa33w.onion')
respones = client.Scrape(request) 
print(response.type) # 1
print(response.tokens)
"""
['<a href="/impact/">Impact</a>', '<li><a href="/awards/">Awards</a></li>', '<a href="/awards/">Awards</a>', '<li><a href="/corrections/">Corrections</a></li>', '<a href="/corrections/">Corrections</a>', '<div class="collapsible collapsible-collapsed collapsible-expandwhenwide" data-collapsible-set="footer-links">\n<h3>Policies</h3>\n<ul>\n<li><a href="/code-of-ethics/">Code of Ethics</a></li>\n<li><a href="/advertising/">Advertising Policy</a></li>\n<li><a href="/legal/">Privacy Policy</a></li>\n</ul>\n</div>', '<h3>Policies</h3>', '<ul>\n<li><a href="/code-of-ethics/">Code of Ethics</a></li>\n<li><a href="/advertising/">Advertising Policy</a></li>\n<li><a href="/legal/">Privacy Policy</a></li>\n</ul>', '<li><a href="/code-of-ethics/">Code of Ethics</a></li>', '<a href="/code-of-ethics/">Code of Ethics</a>', '<li><a href="/advertising/">Advertising Policy</a></li>', '<a href="/advertising/">Advertising Policy</a>', '<li><a href="/legal/">Privacy Policy</a></li>', '<a href="/legal/">Privacy Policy</a>', '<div>\n<div class="collapsible collapsible-collapsed collapsible-expandwhenwide" data-collapsible-set="footer-links">\n<h3>Follow</h3>\n<ul>\n<li><a href="/newsletters/">Newsletters</a></li>\n<li><a href="/series/trump-inc/">Podcast</a></li>\n<li><a href="https://itunes.apple.com/us/app/propublica/id355298887?mt=8">iOS</a> and <a href="https://play.google.com/store/apps/details?id=com.propublica&amp;hl=en">Android</a></li>\n<li><a href="//feeds.p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/propublica/main">RSS Feed</a></li>\n</ul>\n</div>\n<div class="collapsible collapsible-collapsed collapsible-expandwhenwide" data-collapsible-set="footer-links">\n<h3>More</h3>\n<ul>\n<li><a href="/tips/">Send Us Tips</a></li>\n<li><a href="/steal-our-stories/">Steal Our Stories</a></li>\n<li><a href="http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion">Browse via Tor</a></li>\n<li><a href="/contact/">Contact Us</a></li>\n<li><a href="https://donate.propublica.org/">Donate</a></li>\n<li><a href="/support/other-ways-to-give/">More Ways to Give</a></li>\n</ul>\n</div>\n</div>', '<div class="collapsible collapsible-collapsed collapsible-expandwhenwide" data-collapsible-set="footer-links">\n<h3>Follow</h3>\n<ul>\n<li><a href="/newsletters/">Newsletters</a></li>\n<li><a href="/series/trump-inc/">Podcast</a></li>\n<li><a href="https://itunes.apple.com/us/app/propublica/id355298887?mt=8">iOS</a> and <a href="https://play.google.com/store/apps/details?id=com.propublica&amp;hl=en">Android</a></li>\n<li><a href="//feeds.p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/propublica/main">RSS Feed</a></li>\n</ul>\n</div>', '<h3>Follow</h3>', '<ul>\n<li><a href="/newsletters/">Newsletters</a></li>\n<li><a href="/series/trump-inc/">Podcast</a></li>\n<li><a href="https://itunes.apple.com/us/app/propublica/id355298887?mt=8">iOS</a> and <a href="https://play.google.com/store/apps/details?id=com.propublica&amp;hl=en">Android</a></li>\n<li><a href="//feeds.p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/propublica/main">RSS Feed</a></li>\n</ul>', '<li><a href="/newsletters/">Newsletters</a></li>', '<a href="/newsletters/">Newsletters</a>', '<li><a href="/series/trump-inc/">Podcast</a></li>', '<a href="/series/trump-inc/">Podcast</a>', '<li><a href="https://itunes.apple.com/us/app/propublica/id355298887?mt=8">iOS</a> and <a href="https://play.google.com/store/apps/details?id=com.propublica&amp;hl=en">Android</a></li>', '<a href="https://itunes.apple.com/us/app/propublica/id355298887?mt=8">iOS</a>', '<a href="https://play.google.com/store/apps/details?id=com.propublica&amp;hl=en">Android</a>', '<li><a href="//feeds.p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/propublica/main">RSS Feed</a></li>', '<a href="//feeds.p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/propublica/main">RSS Feed</a>', '<div class="collapsible collapsible-collapsed collapsible-expandwhenwide" data-collapsible-set="footer-links">\n<h3>More</h3>\n<ul>\n<li><a href="/tips/">Send Us Tips</a></li>\n<li><a href="/steal-our-stories/">Steal Our Stories</a></li>\n<li><a href="http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion">Browse via Tor</a></li>\n<li><a href="/contact/">Contact Us</a></li>\n<li><a href="https://donate.propublica.org/">Donate</a></li>\n<li><a href="/support/other-ways-to-give/">More Ways to Give</a></li>\n</ul>\n</div>', '<h3>More</h3>', '<ul>\n<li><a href="/tips/">Send Us Tips</a></li>\n<li><a href="/steal-our-stories/">Steal Our Stories</a></li>\n<li><a href="http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion">Browse via Tor</a></li>\n<li><a href="/contact/">Contact Us</a></li>\n<li><a href="https://donate.propublica.org/">Donate</a></li>\n<li><a href="/support/other-ways-to-give/">More Ways to Give</a></li>\n</ul>', '<li><a href="/tips/">Send Us Tips</a></li>', '<a href="/tips/">Send Us Tips</a>', '<li><a href="/steal-our-stories/">Steal Our Stories</a></li>', '<a href="/steal-our-stories/">Steal Our Stories</a>', '<li><a href="http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion">Browse via Tor</a></li>', '<a href="http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion">Browse via Tor</a>', '<li><a href="/contact/">Contact Us</a></li>', '<a href="/contact/">Contact Us</a>', '<li><a href="https://donate.propublica.org/">Donate</a></li>', '<a href="https://donate.propublica.org/">Donate</a>', '<li><a href="/support/other-ways-to-give/">More Ways to Give</a></li>', '<a href="/support/other-ways-to-give/">More Ways to Give</a>', '<div class="site-copyright">\n<a class="logo" href="/">\n<svg height="75" role="img" width="574">\n<use xlink:href="#propublica-logo"></use>\n<text class="a11y">ProPublica</text>\n</svg>\n</a>\n<p class="slogan">Journalism in the Public\xa0Interest</p>\n<small>© Copyright 2021 Pro Publica Inc.</small>\n</div>', '<a class="logo" href="/">\n<svg height="75" role="img" width="574">\n<use xlink:href="#propublica-logo"></use>\n<text class="a11y">ProPublica</text>\n</svg>\n</a>', '<svg height="75" role="img" width="574">\n<use xlink:href="#propublica-logo"></use>\n<text class="a11y">ProPublica</text>\n</svg>', '<use xlink:href="#propublica-logo"></use>', '<text class="a11y">ProPublica</text>', '<p class="slogan">Journalism in the Public\xa0Interest</p>', '<small>© Copyright 2021 Pro Publica Inc.</small>', '<div class="squelch" id="wayfinding">\n<span id="current-site">Current site</span>\n<span id="current-page">Current page</span>\n</div>', '<span id="current-site">Current site</span>', '<span id="current-page">Current page</span>', '<script data-delay="3" data-endpoint="http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion//partials/newsletter-roadblock-big-story.html" data-stylesheet="http://assets.p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/static/prod/v4/css/deploy/syndicated-newsletter.css" data-syndicate="" data-target="l/125411/2019-04-26/6m938v" src="http://assets.p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/static/no-op.js">\n</script>', '<script src="https://www.google.com/recaptcha/api.js?onload=grecaptchaLoaded&amp;render=6LdI1rAUAAAAACI0GsFv-yRpC0tPF5ECiIMDUz2x"></script>', '<script type="application/ld+json">{"@context":"http://schema.org","@graph":[{"@type":"WebPage","author":{"@id":"http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion#identity"},"copyrightHolder":{"@id":"http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion#identity"},"copyrightYear":"2019","creator":{"@id":"http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion#creator"},"dateModified":"2021-05-14T16:02:11-04:00","datePublished":"2019-10-31T13:02:00-04:00","description":"ProPublica is an independent, non-profit newsroom that produces investigative journalism in the public interest.","headline":"ProPublica — Investigative Journalism and News in the Public Interest","image":{"@type":"ImageObject","url":"http://assets.p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/2017-pp-open-graph-1200x630.jpg"},"inLanguage":"en-us","mainEntityOfPage":"http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/","name":"ProPublica — Investigative Journalism and News in the Public Interest","publisher":{"@id":"http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion#creator"},"url":"http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion"},{"@id":"http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion#identity","@type":"NewsMediaOrganization","address":{"@type":"PostalAddress","addressCountry":"US","addressLocality":"New York","addressRegion":"NY","postalCode":"10013","streetAddress":"155 Avenue of the Americas, 13th Floor"},"description":"ProPublica is an independent, non-profit newsroom that produces investigative journalism in the public interest.","email":"info@propublica.org","name":"ProPublica","sameAs":["https://twitter.com/propublica","https://www.facebookcorewwwi.onion/propublica/","https://en.wikipedia.org/wiki/ProPublica","https://www.youtube.com/user/propublica","https://github.com/propublica","https://www.linkedin.com/company/propublica/","https://www.instagram.com/propublica","https://www.pinterest.ie/propublica","https://vimeo.com/propublica"],"telephone":"1-212-514-5250","url":"http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion"},{"@id":"#creator","@type":"Organization"},{"@type":"BreadcrumbList","description":"Breadcrumbs list","itemListElement":[{"@type":"ListItem","item":"http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion","name":"Homepage","position":1}],"name":"Breadcrumbs"}]}</script>']
"""
```


### Here's an example of utilizing the service with the CLI
![Testing Scrape CLI](https://user-images.githubusercontent.com/13573860/118857455-10bf8180-b8a6-11eb-83b6-7920e3785ecd.gif)
