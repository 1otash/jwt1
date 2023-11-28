# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI
from passlib.context import CryptContext


SECRET_KEY = 'ejofiejewjoewweoii'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


#Swagger
app = FastAPI(docs_url='/home')

@app.get('/')
async def home():
    return 'This is home page'

@app.post('/register')
async def register():
    return 'Registration page'

@app.post('/login')
async def login():
    return 'Login page'