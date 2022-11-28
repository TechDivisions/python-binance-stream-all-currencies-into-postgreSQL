# python-binance-stream-all-currencies-into-postgreSQL

--- Do not forget to install --- Dependencies:

schedule: pip install schedule

urllib: pip install urllib

psycopg2: pip install psycopg2


# SQL QUERIES:

# Create a New User for "ALL_CURRENCIES" Database:
    create user py with encrypted password '111';
    grant all privileges on database "ALL_CURRENCIES" to py;
    grant all privileges on table "Tickers" TO py;

# Selects everything from table "Tickers":
    SELECT * FROM public."Tickers";

# Deletes all data in the table "Tickers":
    delete from public."Tickers"

# Selects everything from table "Tickers" and orders by "DateTime":
    SELECT * FROM public."Tickers" where "Symbol" = 'BTCUSDT' order by "DateTime";

# Selects everything from table "Tickers" and orders by "DateTime" descending:
    SELECT * FROM public."Tickers" where "Symbol" = 'BTCUSDT' order by "DateTime" desc;

# In case you want to delete user:
    DROP OWNED BY py; 
    DROP USER py;

# ------------------
#  HAPPY CODING !!!
# ------------------