import reflex as rx
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

usuario = "sa"
password = "password123"
host = "localhost"
db = "master"
port = 1433

db_uri = f"mssql+pyodbc://{usuario}:{password}@{host}:{port}/{db}?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(db_uri)

Session = sessionmaker(bind=engine)
session = Session()

result = session.execute(text('SELECT * FROM [master].[dbo].[tUser]'))
for row in result:
    print(row)