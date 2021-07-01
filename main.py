from codecs import encode
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestForm
from fastapi.security.oauth2 import OAuth2PasswordBearer
import jwt
from jwt.exceptions import PyJWTError
from pydantic import BaseModel
from passlib.context import CryptContext

SECRET_KEY = "jsalkdifuouqajweflk234kjlknsallasj0oafius0as"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# 模拟数据库
fake_user_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "opjsodfjlslkmnl3rlwer0wwelw",
        "disabled": False
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token')

app = FastAPI()

# 校验密码


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 密码哈希


def get_password_hash(password):
    return pwd_context.hash(password)

# 模拟从数据库读取用户信息


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

# 用户信息校验:username和passowrd分别校验


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# 生成token,带有过期时间


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow()+expires_delta
    else:
        expire = datetime.utcnow()+timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post('/token', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # 首先校验用户信息
    user = authenticate_user(
        fake_user_db, form_data.username, form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect usrename or password",
            headers={"WWW-AUthenticate": "Bearer"},
        )
    # 生成并返回token信息
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": "test"}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-AUthenticate": "Bearer"}
    )
    try:
        pyload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = pyload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except PyJWTError:
        raise credentials_exception
    user = get_user(fake_user_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


@app.get('/users/me', response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
