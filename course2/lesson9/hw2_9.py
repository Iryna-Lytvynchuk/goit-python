from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.sql import select


engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('surname', String),
    Column('adress', String),
    Column('note', String),
    Column('tag', String),
    Column('email', String),
    Column('phone', Integer),
    Column('birthday', String)
)

metadata.create_all(engine)

ins = users.insert().values(name='jack', surname='Jones', adress='gfghf', note='ggjhg', tag='gffgjhj', email='hghgh@net.ua', phone='0964772283', birthday='10 09 1985')
print(str(ins))

conn = engine.connect()
result = conn.execute(ins)


s = select(users)
r = conn.execute(s)
for row in r:
    print(row)
    
conn.close()