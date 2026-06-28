from fastapi import FastAPI,Path,Query
from pydantic import BaseModel,Field

# 导入各学习模块的路由器
from exception_response_handling import router as exception_router
from middleware import router as middleware_router, register_middleware

#创建FastAPI实例
app = FastAPI()

# 注册中间件
register_middleware(app)

# 挂载各模块的路由器
app.include_router(exception_router)
app.include_router(middleware_router)


@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/{user_id}")
async def read_user(user_id: int = Path(..., title="The ID of the user to get", gt=0, le=1000)):
    return {"user_id": user_id}

@app.get("/author/{user_name}")
async def read_author(user_name: str = Path(..., title="The name of the user to get", min_length=2, max_length=10)):
    return {f"作者是{user_name}"}

@app.get("/news/news_list")
async def read_news_list(skip: int = Query(0, description="The number of items to skip before returning the first item", ge=0), limit: int = Query(10, description="The number of items to return", ge=0)):
    return {"skip": skip, "limit": limit}

class User(BaseModel):
    username: str = Field(default="张三", description="The username of the user", min_length=2, max_length=10)
    password: str = Field(default="123456", description="The password of the user")

@app.post("/register/")
async def register(user: User):
    return user

@app.get("/username/{user_name}",response_model=User)
async def read_user(user_name: str = Path(..., title="The name of the user to get", min_length=2, max_length=10)):
    return {"username": user_name, "password": f"{user_name}123"}
