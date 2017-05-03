# http://"+10.14.81.6:8080+"/iitkgp-geoservices/wms

from owslib.wms import WebMapService

# ip address for geo-servers
ip1 = "10.14.1.163:8080"
ip2 = "10.14.91.34:8080"


server = 'http://'+ip1+'/geoserver/wms'
server1 = 'http://10.14.81.6:8080/iitkgp-geoservices/wms'
print(server)

wms = WebMapService( server1, version='1.1.1')
print(wms.identification.type)
for i in wms.contents:
    print(i)

