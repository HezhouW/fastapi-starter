from fastapi import FastAPI


def register_middleware(app: FastAPI):
    # @app.middleware("http")
    # async def db_session_middleware(request: Request, call_next):
    #     request.state.db = SessionLocal()
    #     response = await call_next(request)
    #     request.state.db.close()
    #     return response