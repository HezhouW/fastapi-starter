import logging
from fastapi import APIRouter, HTTPException
from src.common.response import OkResponse
router = APIRouter()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
@router.get("/test2")
def test():
    try:
        logger = logging.getLogger(__name__)
        logger.info("logging---hello")
        1/0
    except:
        raise HTTPException(status_code=404, detail="Item not found")
    return OkResponse(msg="test ok")