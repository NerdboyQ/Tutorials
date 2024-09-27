import json
import pprint
import requests
import pandas as pd
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
    salesBatch(limit:100 offset:){
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

class SALE:
  cost: float
  country: str
  countryCode: str
  design: str
  saleDate: str
  user: str

def json_to_df(jobj: json) -> None:
  sales = []
  for r in jobj:
    # print("\t-",r)
    sale = SALE()
    sale.cost=r['income']['cents']
    sale.country=r['orderCountry']['name']
    sale.countryCode=r['orderCountry']['code']
    sale.design=r['creation']['name']
    sale.saleDate=r['createdAt']
    sale.user=r['user']['nick']
    sales.append(sale.__dict__)
    print("\t-",sales[-1])
  
  return sales

sales = []
# Per Cults3D CTO, their graphQL api is limited to
# 100 results, but if looped w/ an offset to 100
# the full list of results can be rettrieved. The 
# loop can end when no more results are found
offset = 0
while True:
  r = requests.post("https://cults3d.com/graphql", headers=headers, auth=credentials, data=pyld.replace("offset:",f"offset:{offset}"))
  # print(r)
  j = json.loads(r.text)
  jResults = j['data']['myself']['salesBatch']['results']
  if not len(jResults): break
  sales+=json_to_df(jResults)
  offset+=100
  # pprint.pprint(j)

df = pd.DataFrame(sales)
df.to_csv("cults3D_sales.csv", index=False)
# print(df)
print("done")
