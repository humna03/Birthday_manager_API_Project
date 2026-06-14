#import fastapi 
from fastapi import FastAPI,Depends,HTTPException
from schemas import BirthdayCreate,BirthdayResponse,GiftRequest,GiftideaResponse
from database import SQLModel,engine,get_session,Birthday
from sqlmodel import Session,select
from dotenv import load_dotenv
from groq import Groq
import os
load_dotenv()
app = FastAPI()
client =Groq(api_key=os.getenv("GROQ_API_KEY"))
@app.on_event("startup")
def startup():
    SQLModel.metadata.create_all(engine)
@app.post("/birthdays")
def add_birthday(
    data:BirthdayCreate,
    session:Session = Depends(get_session)
):
     birthday = Birthday(
     name = data.name,
     birthday = data.birthday,
     relationship = data.relationship,
     phone = data.phone,
     notes = data.notes
     )
     session.add(birthday)
     session.commit()
     session.refresh(birthday)
     
     return birthday
@app.get("/birthdays")
def getall_birthdays(
     session:Session = Depends(get_session)
):
     birthdays = session.exec(select(Birthday)).all()
     if not birthdays:
          raise HTTPException(
               status_code=404,
               detail="not Found"
          )
     return birthdays
@app.get("/birthdays/{birthday_id}")
def get_birthdays(birthday_id:int,session:Session = Depends(get_session)):
     birthday = session.get(Birthday,birthday_id)
     if not birthday:
          raise HTTPException(status_Code=404,detail=" not found ")
     return birthday
@app.put("/birthday/{birthday_id}")
def update_birthday(birthday_id:int,updated:BirthdayCreate,session:Session=Depends(get_session)):
     birthday = session.get(Birthday,birthday_id)
     if not birthday:
          raise HTTPException(status_code=404,detail="not found")
     birthday.name=updated.name
     birthday.date =updated.date
     session.commit()
     session.refresh(birthday)
     return birthday
@app.delete("/birthday/{birthday_id}")
def delete_birthday(birthday_id:int,session:Session=Depends(get_session)):
     birthday = session.get(Birthday,birthday_id)
     if not birthday:
          raise HTTPException(status_code=404,detail="not found")
     session.delete(birthday)
     session.commit()
     return{"record":"deleted successfully"}
@app.post("/birthday/{birthday_id}/gift_ideas")
def gift_ideas(
     birthday_id:int,
     request:GiftRequest,
     session:Session=Depends(get_session)
     ):
  birthday = session.get(Birthday, birthday_id)
  if not birthday:
        raise HTTPException(status_code=404, detail="Birthday not found")

  completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"Suggest 3 gift ideas for {birthday.name} who is {request.age} years old, my {birthday.relationship}, and likes {request.interests}. Give only 3 ideas, one per line."
            }
        ]
    )
  raw =completion.choices[0].message.content
  ideas = raw.split("/n")
  ideas = [i for i in ideas if i !=""]
  ideas = ideas[:3]
  return GiftideaResponse(
      name = birthday.name,
      relationship=birthday.relationship,
      gift_ideas=ideas
  )
