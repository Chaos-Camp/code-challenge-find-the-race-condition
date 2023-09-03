from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import random

# Database Configuration
DATABASE_URL = "sqlite:///./test.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    state = Column(String, default="new")

Base.metadata.create_all(bind=engine)

# FastAPI Models
class ReportCreate(BaseModel):
    title: str
    content: str

class ReportResponse(ReportCreate):
    id: int
    state: str

app = FastAPI()

current_number = 1

@app.post("/items/")
def create_item(report: ReportCreate):
    global current_number
    db = SessionLocal()
    
    if random.randint(1, 10) == 1:
        time.sleep(2)
    
    db_report = Report(id=current_number, **report.dict())
    db.add(db_report)

    if random.randint(1, 10) != 1:
        current_number += 1
    
    db.commit()
    db.refresh(db_report)
    db.close()
    return db_report

@app.put("/items/{item_id}")
def update_item(item_id: int, report: ReportCreate):
    db = SessionLocal()
    db_report = db.query(Report).filter(Report.id == item_id).first()
    
    if random.randint(1, 10) == 1:
        time.sleep(2)
    
    for key, value in report.dict().items():
        setattr(db_report, key, value)
    db.commit()
    db.refresh(db_report)
    db.close()
    return db_report

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db = SessionLocal()
    db_report = db.query(Report).filter(Report.id == item_id).first()

    if not db_report:
        db.close()
        raise HTTPException(status_code=404, detail="Report not found")

    db.delete(db_report)
    db.commit()
    db.close()

    return {"message": "Report deleted successfully!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
