from pymongo import MongoClient

# MongoDB bağlantısını başlat
def get_mongo_client():
    client = MongoClient("mongodb+srv://islimocalan23:2VAi8qIdGg3Dgdba@cluster1.u72we.mongodb.net/?retryWrites=true&w=majority")
    db = client['eCommerce']
    products_collection = db['products']
    return products_collection
