from openfoodfacts_requests import OpenFoodFactsRequest


PARAMS = {
    "search_terms"  :'riz',
    "search_simple" : '1',
    "action"        :'process',
    "json"          : '1'
}


    #print(result_json['products'])

    #with open('datas.json', 'w') as f:
        #f.write(json.dumps(result_json, indent=4))

a = OpenFoodFactsRequest()

a.connexion("https://ssl-api.openfoodfacts.org/cgi/search.pl", PARAMS)





