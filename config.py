import os

BOT_TOKEN = "5653692437:AAGG84CedUAx1fh4s7qr78ADx7yGpl1mkos"
API_ID = int(22464094)
API_HASH = "068433765c898289e3a78ab67aa2230a"
LOG_CHANNEL = int(-1823536404)
AUTH_USERS = {'rishabhjava'}
DB_URL = "mongodb+srv://rishabh:<FKqD4gCLb7BFQcnM>@cluster0.y8kmqmb.mongodb.net/test"
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
