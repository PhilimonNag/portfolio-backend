from pymongo.mongo_client import MongoClient
from config import config
conn=MongoClient(config.mongo_url,
                 tls=True,
                 tlsAllowInvalidCertificates=True)
db=conn[config.db_name]
