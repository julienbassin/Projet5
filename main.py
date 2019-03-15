import requests
import json



URL = "https://ssl-api.openfoodfacts.org/cgi/search.pl"

PARAMS = {
    "search_terms"  :'riz',
    "search_simple" : '1',
    "action"        :'process',
    "json"          : '1'
}

try:
    search_result = requests.get(URL, params=PARAMS, timeout=3)
    search_result.raise_for_status()
    result_json = search_result.json()
    print(result_json.products)

    #with open('datas.json', 'w') as f:
        #f.write(json.dumps(result_json, indent=4))
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)






