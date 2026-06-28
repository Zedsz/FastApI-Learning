from fastapi import APIRouter, HTTPException

# 创建一个独立的路由器实例
router = APIRouter()


@router.get("/news/{news_id}")
async def read_news(news_id: int):
    if news_id <= 0:
        # 抛出 HTTP 异常，FastAPI 会自动转成 JSON 响应
        raise HTTPException(status_code=404, detail="新闻不存在")
    return {"news_id": news_id, "title": "示例新闻"}
