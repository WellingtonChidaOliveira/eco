import asyncio
import uvicorn
from fastapi import FastAPI
from src.login.infrastructure.init_db import init_db
from src.chatbot.infrastructure.init_db_chat import init_db_chat
from src.login.api import authentication as login_auth
from src.chatbot.api import chat as websocket_chat
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file

init_db()
init_db_chat()

app = FastAPI()

app.include_router(login_auth.router, prefix="/auth")
app.include_router(websocket_chat.router, prefix="/chat")

async def main():
    config = uvicorn.Config(app, host="localhost", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())