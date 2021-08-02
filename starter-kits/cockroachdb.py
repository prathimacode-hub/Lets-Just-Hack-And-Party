# For full set of example code in all available programming languages, visit:
# https://www.cockroachlabs.com/docs/v21.1/example-apps.html

from sqlalchemy import create_engine
import os

def connect(db_uri):
    engine = create_engine(db_uri)
    engine.connect()
    print('Hey! You successfully connected to your CockroachDB cluster.')

if __name__ == '__main__':

    conn_string = input('Enter your node\'s connection string:\n')
    # For cockroach demo:
    # cockroachdb://demo:<demo_password>@127.0.0.1:26257/defaultdb?sslmode=require
    # For CockroachCloud:
    # cockroachdb://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>

    try:
        connect(os.path.expandvars(conn_string))
    except Exception as e:
        print('Failed to connect to database.')
        print('{0}'.format(e))
