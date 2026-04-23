import json
data = '''
{
      "user":{
      "id": 1,
      "name": "Donald Smith"
      "email": "Donaldsmith@icloud.com"
      "adress":{
        "city":"Freetown"
        "Country":"Sierraleone"
      }
}
}'''
  json_data=json.loads  
  #access values
  print(json_data["use"]["name"])#Alice
  print(json_data["user"]["adress"]["city"])#freetown
