import time

from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/middleware")
async def read_middleware():
    """测试端点：访问它会触发下面的中间件。"""
    return {"message": "Middleware example"}


def register_middleware(app):
    """用 @app.middleware 注解方式注册一个简易中间件。"""

    @app.middleware("http")
    async def log_request(request: Request, call_next):
        # 1. 请求进入：记录开始时间
        start = time.time()
        # 2. 调用下一层（其他中间件 / 路由处理函数）
        response = await call_next(request)
        # 3. 响应返回：打印日志
        print(f"{request.method} {request.url.path} -> {response.status_code} ({time.time() - start:.4f}s)")
        return response
