import uvicorn
import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Query:
    @strawberry.field
    def ping(self) -> str:
        return "pong"

schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.get("/v1/system/ping")
async def root():
    return {"message": "pong"}

def start():
    uvicorn.run("try_fastapi.main:app", host="0.0.0.0", port=8000, reload=True)
    
