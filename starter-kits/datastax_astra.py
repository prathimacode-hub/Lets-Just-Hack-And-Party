
# For full reference for this example code, visit:
# https://docs.datastax.com/en/astra/docs/using-the-datastax-python-driver-to-connect-to-your-database.html

#  Set the cloud_config parameter for the Cluster initialization as shown in the following example. 
# The secure_connect_bundle must include the absolute path to your Astra DB database credentials (secure-connect-database_name.zip).

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': '/path/to/secure-connect-database_name.zip'
}
auth_provider = PlainTextAuthProvider('username', 'password')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")
