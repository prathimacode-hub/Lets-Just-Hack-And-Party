
import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from dotenv import load_dotenv

load_dotenv()
SECURE_BUNDLE = os.getenv(key='SECURE_BUNDLE')
username = os.getenv(key='username')
password = os.getenv(key='password')

cloud_config= {
        'secure_connect_bundle': SECURE_BUNDLE
}

auth_provider = PlainTextAuthProvider(username=username, password=password)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")
