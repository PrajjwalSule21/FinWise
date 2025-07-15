from fastapi import FastAPI
from api.routes import router


app = FastAPI(title="FinWise")

app.include_router(router)

# if __name__ == "__main__":
#     uvicorn.run(app=app, reload=True)