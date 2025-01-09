from fastapi import FastAPI
from src.core.register_logger import register_logger
from src.core.handle_exception import register_exception_handler
from src.core.load_routers import register_routes
from src.config.config import settings
# 初始化app需要的一些依赖，譬如中间件、路由等
def init_app(app:FastAPI) -> FastAPI:
    register_logger()
    register_exception_handler(app)
    register_routes(app)
    return app





