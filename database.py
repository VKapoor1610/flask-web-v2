from sqlalchemy import create_engine, text

import os

# imprt sqlalchemy create engine and text

# create engine is used for estb a connection or creating a connection object

# print(os.environ['CONN_STR'])

my_secret = os.environ['CONN_STR']

engine = create_engine(
  # go to mysql alcemy site https://docs.sqlalchemy.org/en/20/dialects/mysql.html for getting the connection then for secure connection search for ssl and add floowing
  my_secret,
  connect_args={"ssl": {
    "ssl_ca": "/etc/ssl/cert.pem",
  }})
# print(sqlalchemy.__version__)


def returning():
  with engine.connect() as conn:

    result = conn.execute(text("select * from employee"))
    all_result = list(result.all())

    l = []

    for row in all_result:
      l.append(list(row))

    return l
