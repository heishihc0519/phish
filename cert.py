import ssl
import urllib
from urlparse import urlparse


url = 'google.com'
hostname = urlparse(url).hostname
port = 443
cert = ssl.get_server_certificate((url, port), ssl_version=2)
print cert
