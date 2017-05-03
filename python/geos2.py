from owslib.wms import WebMapService
try:
	wms = WebMapService('http://10.14.1.164:8080/geoserver/wms', version='1.1.1')
	if wms is None:
		print('not a geoserver')
	else:
		print('its a geoserver')
except:
	print('its not a geoserver')