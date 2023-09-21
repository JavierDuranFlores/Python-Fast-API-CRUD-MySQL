from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://root:1234@localhost:3306/libros")

Base = declarative_base()

SessionLocal=sessionmaker(bind=engine)