from . import SessionLocal
from .models import ToDoItem
from .schemas import ToDoItemCreate, ToDoItemUpdate
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    # close() 그냥 쓰고나서 닫아주는작업 안닫으면 계속 메모리에 남아있고 메모리낭비임
        
    # yield : 리스트? 의 개념 제너레이트
    # return 을 하게되면 결과를 전부 한번에 저장해놓고 쓰기때문에 메모리 낭비, 아까움
    # yield 를 쓰게되면 한번에 1개씩 불러올수가있어서 메모리저장 측면에서도 데이터 연산 속도에서도 이득
    # 만약 처리하는데 1초가 걸리는 연산을 20번 실행할시 return 을 하면 20초가 걸리고결과가 나오지만, yield 로 하게되면 데이터를 불러올떄 1초의 연산을 하고 데이터를 불러옴 

def get_todo_items(db: Session):
    return db.query(ToDoItem).all()

def create_todo_item(db: Session, item: ToDoItemCreate):
    new_item = ToDoItem(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update_todo_item(db: Session, item_id: int, item: ToDoItemUpdate):
    db_item = db.query(ToDoItem).filter(ToDoItem.id == item_id).one()
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()

def delete_todo_item(db: Session, item_id: int):
    db_item = db.query(ToDoItem).filter(ToDoItem.id == item_id).one()
    db.delete(db_item)
    db.commit()

def get_todo_item(db: Session, item_id: int):
    return db.query(ToDoItem).filter(ToDoItem.id == item_id).one()