from pymongo import MongoClient
from pymongo import InsertOne
from pprint import pprint



client = MongoClient(port=27017)

db = client.inventorydb

result = db.products_bestselling.bulk_write(
    [

        InsertOne (
                {"prod_id": 9, "name": "KNEX Revolution Ferris Wheel Building Set ", "current_price": 19.99,
                 "instock": 300,
                 "search_key": ["Ferris", "toy", "building set", "stem", "knex"], "min_max_sales": [70, 87]}),
        InsertOne(
                {"prod_id": 10, "name": "KNEX Looping Light-Up Roller Coaster Building Set ", "current_price": 38.27,
                 "instock": 500, "search_key": ["Roller Coaster", "toy", "building set ", "stem", "knex"],
                 "min_max_sales": [89, 160]}),
        InsertOne(
                {"prod_id": 11, "name": "KNEX 70 Model Building Set", "current_price": 20.48, "instock": 400,
                 "search_key": ["CLASSIC PIECES", "toy", "building set ", "stem", "knex"],
                 "min_max_sales": [78, 140]})
    ]
)

pprint(result)
