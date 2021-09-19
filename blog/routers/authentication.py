
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
  tags=["Authentication"]
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
  # 3:23:00~ なぜemailとusernameがイコールなのかを解説
  user = db.query(models.User).filter(models.User.email == request.username).first()
  if not user:
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Invalid Credentials")
  if not Hash.verify(request.password, user.password):
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Incorrect email or password")
  # generate a jwt token and return
  return user
