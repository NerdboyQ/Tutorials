import json
import pprint
import requests
from requests.auth import HTTPBasicAuth
from private_config import *

api_username = API_USERNAME
api_password = API_PASSWORD
graphql_query = """
{
  creationsBatch(limit: 3) {
    total
    results {
      name
      url
      price(currency: USD) {
        cents
      }
    }
  }
}
"""
# my personal query
# NOTE : According to cults3d graphql site, queries are limited to 100
# TODO : Speak w/ CTO
graphql_query = """
{
    myself {
    salesBatch(limit:100){
      total
      results{
        createdAt
        orderCountry{
          name
          code
        }
        income(currency: USD){
          cents
        }
        user {
          nick
        }
        creation{
          name
        }
      }
    }
  }
}"""
# graphql_query = """
#     {
#       creationsBatch(limit: 10) {
#         total
#         results {
#           name
#           url
#         }
#       }
#     }
# """
# result = client.execute(graphql_query, {'username':api_username,'password':api_password})
credentials = HTTPBasicAuth(username=api_username, password=api_password)
pyld = "query="+graphql_query
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
r = requests.post("https://cults3d.com/graphql", headers=headers, auth=credentials, data=pyld)
j = json.loads(r.text)
pprint.pprint(j)