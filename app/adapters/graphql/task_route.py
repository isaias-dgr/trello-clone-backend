from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from app.adapters.graphql.task_schema import schema
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.add_route("/graphql", GraphQLApp(schema, on_get=make_graphiql_handler()))

