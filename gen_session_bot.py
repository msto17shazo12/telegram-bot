from pyrogram import Client

API_ID = 26892563   # API_ID خۆت
API_HASH = "26d1cda20091a12062f5b512c2573dfb"  # API_HASH خۆت

with Client(name="gen_session", api_id=API_ID, api_hash=API_HASH) as app:
    print(app.export_session_string())