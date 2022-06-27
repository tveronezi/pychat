import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from pychat import api_system;


schema = strawberry.Schema(api_system.Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.get("/v1/system/ping")
async def root():
    return {"message": "pong"}
