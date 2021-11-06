from pyrogram import Client
from datetime import datetime 
import asyncio
import shelve
import random
import time


app = Client("chelik")


successsSendUserReplay = 0
async def main():
   async with app:
        
        while True:
            successsSendUserReplay = 0
            
            processed_message = shelve.open('processed_userID.db', writeback=True)
            chat_id = await app.get_dialogs()
            for i in range(len(chat_id)):
                try:  
                    uid = chat_id[i]["chat"]["id"]
                    if(str(uid)[0] != '-'):
                        name = chat_id[i]["chat"]["first_name"]
                        if str(uid) in processed_message:
                            print(f'Пропускаем уже обработанного пользователя ={uid}')
                            continue
                        processed_message[str(uid)] = True
                        await app.send_message(uid,"Привет, я уже запустила для тебя прриватную трансляцию, хочу тебе показать себя. Переходи быстрее, а то мне одной скучно) Вот ссылка на мою трансляцию: http://dtgfm.com/BKyK")
                        print(f"Сообщемние было отправленно USER_ID:{uid}, имя {name}")
                        successsSendUserReplay = successsSendUserReplay + 1
                    await asyncio.sleep(30)
                except:
                    print(f"Исключение KeyError. Скорее всего пользователю нельзя писать!")
            
            print(f"\nУспешных реплаев {successsSendUserReplay}")
            await asyncio.sleep(3600)
        

app.run(main())