from os import environ

from fastapi import BackgroundTasks, FastAPI
from neomodel import config

app = FastAPI()
config.DATABASE_URL = (
    f"bolt://{environ['NEO4J_AUTH_USER']}:{environ['NEO4J_AUTH_PASS']}@tb-db:7687"
)


@app.get("/")
def read_root():
    return "Compute Server for Travel Buddy"


trigger_count = 0


def generate_recommendations():
    print("Updating recommendations!")


@app.get("/trigger")
async def trigger_workflow(background_tasks: BackgroundTasks) -> int:
    global trigger_count
    trigger_count += 1
    if trigger_count >= 10:
        trigger_count = 0
        background_tasks.add_task(generate_recommendations)
    return trigger_count
