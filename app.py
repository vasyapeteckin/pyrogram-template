import os

from pyrogram import Client
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

Client(
    name='session_name',
    api_id=int(api_id) if api_id else None,
    api_hash=api_hash,
    workdir='sessions',
    plugins=dict(root='src')
).run()
