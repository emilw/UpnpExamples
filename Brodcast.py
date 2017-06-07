import socket
import requests
import time


msg = \
    'M-SEARCH * HTTP/1.1\r\n' \
    'HOST:239.255.255.250:1900\r\n' \
    'ST:upnp:rootdevice\r\n' \
    'MX:2\r\n' \
    'MAN:"ssdp:discover"\r\n'

# Set up UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.settimeout(2)
s.sendto(msg, ('239.255.255.250', 1900) )

try:
    while True:
        data, addr = s.recvfrom(65507)
        print addr, data
except socket.timeout:
    pass


playMessage = '<?xml version="1.0" encoding="utf-8"?>'
playMessage += '<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">'
playMessage += '<s:Body>'
playMessage += '<u:Play xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">'
playMessage += '<InstanceID>0</InstanceID>'
playMessage += '<Speed>1</Speed>'
playMessage += '</u:Play>'
playMessage += '</s:Body>'
playMessage += '</s:Envelope>'

print(playMessage)

address = 'http://192.168.10.104:1400/MediaRenderer/AVTransport/Control'

playHeaders = {'SOAPACTION': 'urn:schemas-upnp-org:service:AVTransport:1#Play', 'CONTENT-TYPE':'text/xml'}

response = requests.post(address, data=playMessage, headers=playHeaders)

print(response.status_code)
print(response.text)

time.sleep(5)

stopMessage = '<?xml version="1.0" encoding="utf-8"?>'
stopMessage += '<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">'
stopMessage += '<s:Body>'
stopMessage += '<u:Stop xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">'
stopMessage += '<InstanceID>0</InstanceID>'
stopMessage += '</u:Stop>'
stopMessage += '</s:Body>'
stopMessage += '</s:Envelope>'

print(stopMessage)

address = 'http://192.168.10.104:1400/MediaRenderer/AVTransport/Control'

stopHeaders = {'SOAPACTION': 'urn:schemas-upnp-org:service:AVTransport:1#Stop', 'CONTENT-TYPE':'text/xml'}

response = requests.post(address, data=stopMessage, headers=stopHeaders)

print(response.status_code)
print(response.text)
