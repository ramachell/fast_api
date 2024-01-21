from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# url = urlparse(DATABASE_URL)

# DATABASE_URL=mysql+pymysql://user:password@localhost:33306/company

# 연결 설정
# connection = pymysql.connect(
#     host=url.hostname,
#     user=url.username,
#     password=url.password,
#     database=url.path[1:],
#     port=url.port
# )
print("----------------------")
print("----------------------")
# print(connection)
print("----------------------")
print("----------------------")
engine =create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()