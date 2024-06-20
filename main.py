from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import declarative_base

# Создание объекта FastAPI
app = FastAPI()

# Настройка базы данных MySQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://isp_p_Zobov:12345@77.91.86.135/isp_p_Zobov"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Определение модели SQLAlchemy для пользователя
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)  # Указываем длину для VARCHAR
    email = Column(String(100), unique=True, index=True)  # Указываем длину для VARCHAR

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Определение Pydantic модели для пользователя
class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршрут для получения пользователя по ID
@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Маршрут для создания нового пользователя
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")

#
#
#
#
#

# Определение модели SQLAlchemy для пользователя
class Publications(Base):
    __tablename__ = "publications"

    id = Column(Integer, primary_key=True, index=True)
    views = Column(String(50), index=True)  # Указываем длину для VARCHAR
    name = Column(String(100), unique=True, index=True)  # Указываем длину для VARCHAR
    price = Column(String(100), unique=True, index=True)  # Указываем длину для VARCHAR

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Определение Pydantic модели для пользователя
class PublicationsCreate(BaseModel):
    views: str
    name: str
    price: str

class PublicationsResponse(BaseModel):
    id: int
    views: str
    name: str
    price: str

    class Config:
        orm_mode = True

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршрут для получения пользователя по ID
@app.get("/publications/{publications_id}", response_model=PublicationsResponse)
def read_publications(publications_id: int, db: Session = Depends(get_db)):
    publications = db.query(Publications).filter(Publications.id == publications_id).first()
    if publications is None:
        raise HTTPException(status_code=404, detail="Publications not found")
    return publications

# Маршрут для создания нового пользователя
@app.post("/publications", response_model=PublicationsResponse)
def create_publications(publications: PublicationsCreate, db: Session = Depends(get_db)):
    db_publications = Publications(views=publications.views, name=publications.name, price=publications.price)
    print(publications)
    try:
        db.add(db_publications)
        db.commit()
        db.refresh(db_publications)
        return db_publications
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Publications already registered")
    
#
#
#
#
#
#
#
class Sub(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    index = Column(String(50), index=True)  # Указываем длину для VARCHAR
    term = Column(String(100), unique=True, index=True)  # Указываем длину для VARCHAR
    dateStart = Column(String(100), unique=True, index=True)  # Указываем длину для VARCHAR
    year = Column(String(100), unique=True, index=True)  # Указываем длину для VARCHAR

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Определение Pydantic модели для пользователя
class SubCreate(BaseModel):
    index: str
    term: str
    dateStart: str
    year: str

class SubResponse(BaseModel):
    id: int
    index: str
    term: str
    dateStart: str
    year: str

    class Config:
        orm_mode = True

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршрут для получения пользователя по ID
@app.get("/subscriptions/{subscriptions_id}", response_model=SubResponse)
def read_subscriptions(subscriptions_id: int, db: Session = Depends(get_db)):
    subscriptions = db.query(Sub).filter(Sub.id == subscriptions_id).first()
    if subscriptions is None:
        raise HTTPException(status_code=404, detail="Subscriptions not found")
    return subscriptions

# Маршрут для создания нового пользователя
@app.post("/subscriptions/", response_model=SubCreate)
def create_subscriptions(subscriptions: SubCreate, db: Session = Depends(get_db)):
    db_subscriptions = Sub(index=subscriptions.index, term=subscriptions.term, dateStart=subscriptions.dateStart, year=subscriptions.year)
    try:
        db.add(db_subscriptions)
        db.commit()
        db.refresh(db_subscriptions)
        return db_subscriptions
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Subscriptions already registered")








