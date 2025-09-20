from pyrogram import Client
import asyncio
from datetime import datetime
import pytz
import random

API_ID = 26892563
API_HASH = "26d1cda20091a12062f5b512c2573dfb"
SESSION_STRING = "AgGaWRMATy2Jdt0KyNKWOHzmvSR9OW5Hertsqplz2Z8H_bVVhXokh1-4vPP4YYM5DBiVhDxAH-RxajiwCWHRygdk5vgVuJScR-BusrT0khs5Qkg5MHuztO34NP5V9umw5MhrguOdbqm8lwOOiWzi04rwZYbzcZVORMbUivV4TpsJtmTFnvRmvcMq2U0EtcrBJcEBPaxJBu6BdMQNVAH96AHtlmEhWyXzyfDf2CzTLVusM8pbAfRojbTFtOOu-1yfkMUvhVAvO8E7L9Wqhfwqp8pzmGHE1IdiCXsQaWi57sTeC5SGZQCeQgiY_wo9vZsfy31ma98fLG09XG69N1obl0UVpT4kFQAAAAB9ja6oAA"  # SESSION_STRING خۆت لێرە بنووسە

hawler_tz = pytz.timezone("Asia/Baghdad")

emojis = ["💖", "❄️", "✨", "💎", "⭐", "🎵", "✔️", "🍀", "☀️", "🎆", "👑", "⭐️"]

app = Client("update_name_bot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

async def update_name(client: Client):
    while True:
        now = datetime.now(hawler_tz).strftime("%A %H:%M")  # رۆژ + کات
        emoji = random.choice(emojis)  # هەموو جار emoji نوێ هەڵبژێرە
        new_name = f"{emoji} banu {now}"

        try:
            await client.update_profile(first_name=new_name)
            print(f"[+] ناو نوێکرایەوە بۆ: {new_name}")
        except Exception as e:
            print(f"[!] هەڵە: {e}")

        await asyncio.sleep(60)  # هەموو 1 خولەک جارێک نوێ بکەوە

async def main():
    async with app:
        await update_name(app)

asyncio.run(main())