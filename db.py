import datetime
import psycopg2
import uuid

host = '127.0.0.1'
dbname = 'ALL_CURRENCIES'
user = 'py'
password = '111'

def save_all_data(data):
    print(datetime.datetime.now())
    print('Amount of currencies: ' + str(len(data)))

    con = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port='5432')
    con.autocommit = True
    cur = con.cursor()

    now = datetime.datetime.now()

    for item in data:
        cur.execute('''INSERT INTO "Tickers" ("Id", "Symbol", "Price", "DateTime") VALUES (%s, %s, %s, %s)''', (str(uuid.uuid4()), item["symbol"], item["price"], now))

    con.commit()
    con.close()