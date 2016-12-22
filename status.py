import vk
import time
from datetime import datetime, timedelta, date, time as dt_time
session = vk.Session()
#ОБЯЗАТЕЛЬНОЕ ПОЛЕ: в поле access_token - ваш токен вк, подробнее на https://vk.com/dev
api = vk.API(session, access_token='', v='5.60', lang='ru')
#На случай использования даты
#d = datetime.now()+timedelta(hours=8)
#d.strftime('%y-%m-%d %H:%M')
#Некоторая переменная (константа, не меняющее значение)
i = 1
while i == 1:
    #Кулдаун между сменой в секундах
    time.sleep(60)
    #В параметре text укажите в скобках ваше сообщение, в group_id - айди нужной группы (целое число)
    api.status.set(group_id=47320246, text="Будьте счастливы с нами :))")
    #Консольное сообщение, ничего не делает.
    print("New status set! New status id = 1")
    time.sleep(60)
    api.status.set(group_id=47320246, text="Ваш статус 2")
    print("New status set! New status id = 2")
    time.sleep(60)
    api.status.set(group_id=47320246, text="Ваш статус 3")
    print("New status set! New status id = 3")
    time.sleep(60)
    api.status.set(group_id=47320246, text="Ваш статус 4")
    print("New status set! New status id = 4")
    time.sleep(60)
    api.status.set(group_id=47320246, text="Ваш статус 5")
    print("New status set! New status id = 5")
    time.sleep(60)
    api.status.set(group_id=47320246, text="Ваш статус 6")
    print("New status set! New status id = 6")
    time.sleep(60)
    api.status.set(group_id=47320246, text="Ваш статус 7")
    print("New status set! New status id = 7")
    time.sleep(60)
    api.status.set(group_id=47320246, text="Ваш статус 8")
    print("New status set! New status id = 8")
    time.sleep(60)
    api.status.set(group_id=47320246, text="Ваш статус 9")
    print("New status set! New status id = 9")
    #Продолжайте бесконечно создавать строчки:
    #
    #time.sleep(60)
    #api.status.set(group_id=47320246, text="Ваш статус ...")
    #print("New status set! New status id = ...")
