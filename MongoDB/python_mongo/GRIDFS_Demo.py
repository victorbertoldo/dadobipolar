from pymongo import MongoClient
from pprint import pprint
import gridfs
from bson import objectid


client = MongoClient(port=27017)

db = client.inventorydb



fs = gridfs.GridFS(db)

path_in = 'C:/Success_courses_300k_lifelight/mongodb-top4NOSQL/gridfs-demo/How-to-Save-a-Life-Study-Manual.pdf'



with open(path_in,'rb') as filein:
    result = fs.put(filein, content_type='application/pdf', filename='How-to-Save-a-Life-Study-Manual.pdf')
    pprint(result)

path_in = 'C:/Success_courses_300k_lifelight/mongodb-top4NOSQL/gridfs-demo/languagenow_english.jpg'
path_out = 'C:/Success_courses_300k_lifelight/mongodb-top4NOSQL/gridfs-demo/OUTPUT_languagenow_english.jpg'


with open(path_in,'rb') as filein:
    result = fs.put(filein, filename='languagenow_english.jpg')
    pprint(result)

file = fs.find_one({'filename': 'languagenow_english.jpg'})
image = file.read()
with  open(path_out,"wb") as output_file:
    output_file.write(image)
    output_file.close();



