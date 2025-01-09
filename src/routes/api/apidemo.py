from loguru import logger
from fastapi import APIRouter
from src.common.response import OkResponse
router = APIRouter()


@router.get("/test")
def test():
    logger.info("helol")
    return OkResponse(msg="test ok")