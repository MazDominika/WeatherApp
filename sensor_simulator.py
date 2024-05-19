from sqlalchemy import create_engine, insert, MetaData, Table, Column, Integer, select 
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
import sqlalchemy as sa
import sqlalchemy.orm as so
import random
import time
import datetime 

#połączenie sie z bazą danych
connection_string = 'mysql+mysqlconnector://mazdomin:3B2GccHfjm3KuA8K@mysql.agh.edu.pl/mazdomin'
engine = create_engine(connection_string, echo=True)
connection =  engine.connect()

metadata = MetaData()
measurements = Table('measurments', metadata, autoload_with=engine)

#stowrzenie nowej sesji
for i in range(1000):
    new_measurement = {'temperature': random.randint(0,40), 'humidity': random.randint(0,40), 'pressure': random.randint(1000,1300), 'date': datetime.datetime.now()}
    stmt = insert(measurements).values(new_measurement)
    #stmt = select(measurements).order_by(measurements.c.date.desc()).limit(2)

    with engine.connect() as connection:
        result = connection.execute(stmt)
        #data = result.fetchall()
        connection.commit()  # Commit the transaction if necessary
    time.sleep(0.5)
connection.close()
