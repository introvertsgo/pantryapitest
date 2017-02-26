#import modules for handling api
import httplib, urllib, base64
#import module for parceing json information
import json

# Function for getting the GTIN number from the given tpnb number
def gettin(tpnb):

	params = urllib.urlencode({
	    # Request parameters
	    'gtin': '{string}',
	    'tpnb': tpnb,
	    'tpnc': '{string}',
	    'catid': '{string}',
	})

	try:
	    conn = httplib.HTTPSConnection('dev.tescolabs.com')
	    conn.request("GET", "/product/?%s" % params, "{body}", headers)
	    response = conn.getresponse()
	    data = response.read()
	    
	    conn.close()
	except Exception as e:
	    print("[Errno {0}] {1}".format(e.errno, e.strerror))
	pdata = json.loads(data)

	gtin = pdata["products"][0]["gtin"]
	return str(gtin)

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'xxxxxxxxxxxxxxxxxxxxxxxxx',
}

params = urllib.urlencode({
})

#Ask user to input search query
query = raw_input("Search:")
query = query.replace(" ","&")



try:
    conn = httplib.HTTPSConnection('dev.tescolabs.com')
    conn.request("GET", "/grocery/products/?query=" + query + "&offset=0&limit=10&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print data
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
jdata = json.loads(data)

#loop i from 0 to 10 and list top 10 results
for i in range(0,10):

	name = jdata["uk"]["ghs"]["products"]["results"][i]["name"]
	tpnb = jdata["uk"]["ghs"]["products"]["results"][i]["tpnb"]
	price = jdata["uk"]["ghs"]["products"]["results"][i]["price"]

	print "GTIN:"+ gettin(str(tpnb)) + " - " + str(name) + " - " + unichr(163) + str(price)











