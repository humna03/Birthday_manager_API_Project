from sqlmodel import SQLModel,create_engine,Session,Field
from typing import Optional
from datetime import date
DATABASE_URL = "sqlite:///birthdays.db"
engine = create_engine(
    DATABASE_URL,
    echo=True
)

class Birthday(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str
    birthday: date
    relationship: str
    phone: Optional[str] = None
    notes: Optional[str] = None
def get_session():
    with Session(engine)as session:
        yield session
