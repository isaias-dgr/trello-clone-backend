# app/main.py
from fastapi import FastAPI
# from app.adapters.http import task_route
from app.adapters.graphql import task_route


# Base.metadata.create_all(bind=engine)

app = task_route.app
