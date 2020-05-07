from pymongo import MongoClient
from pymongo import version
from pprint import pprint

print(version)

client = MongoClient(port=27017)

db = client.inventorydb

print('The total number of Documents in the Products data')
total_documents = db.products_bestselling.find({}).count()
pprint(total_documents)

filter_query = {"name": "Amazon Fire TV"}
print('The total number of Documents in the Products data - Amazon Fire TV')
document_amazon_fire_tv = db.products_bestselling.find(filter_query)
# print(document_amazon_fire_tv)
for doc in document_amazon_fire_tv:
    pprint(doc)

print('The total number of Documents in the Products data WITH PRICE > 100')
total_documents_after_filtering = db.products_bestselling.find({"current_price": {"$gt": 100}})
print(total_documents_after_filtering)

for doc in total_documents_after_filtering:
    # print((doc))
    # print((doc[u'name']))
    pprint(doc)

print('#####update Document####')

result = db.products_bestselling.update({"name": 'Amazon Fire TV'}, {"$set": {"name": 'Amazon Fire 2018'}})
pprint(result)

print('################Insert Document###############')

result = db.products_bestselling.insert(
    {"prod_id": 8, "name": "Cactaki Water Bottle With Time Marker", "current_price": 19.99, "instock": 6000,
     "search_key": ["water", "bottle", "health", "Fitness"], "min_max_sales": [500, 900]})
pprint(result)

print('################Delete Document###############')

result = db.products_bestselling.delete_one({"name": "Cactaki Water Bottle With Time Marker"})
pprint(result)
