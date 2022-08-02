from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from .. import schemas, models, utils, oauth2
from ..database import get_db


router = APIRouter(
    tags=['Authentication']
)

# below endpoint is with pydantic approach

"""
@router.post('/login')
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):

    
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
        
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Invalid credentials")
    
    # create token
    # return token
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})

    return {"access token": access_token, "token_type": "bearer"}

"""

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    # request form returns only two things in the format as
    # it doesnt care what is in there it can be id name or email but in field - username
    # {
    #    "username": "blah"
    #    "password": "blah"
    # }
    
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"Invalid credentials")
    
    # create token
    # return token
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}