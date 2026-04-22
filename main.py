from fastapi import FastAPI
from core.database import Base,engine
from models.user import User

app = FastAPI()

Base.metadata.create_all(bine=engine)

@app.get("/")
def root():
	return {"message":"Hello,Fastapi on Manjaro"}
