import asyncio
from telethon import TelegramClient, sync, events
from random import randint
import time
from time import sleep
from telethon.tl.types import MessageEntityTextUrl, KeyboardButtonRow
from telethon import Button
import requests
from bs4 import BeautifulSoup
import random
import datetime
import math
from script.modules.gps.gpsGo import gps, station_Names
import re
from operator import itemgetter, attrgetter

api_id = 4889182
api_hash = "38ea074a004c2927bddf31c96f9c03e0"

client = TelegramClient('MW_bot', api_id, api_hash)
state = 'none'
game = 'metro_wars_bot'
gameId = 1745526034
state = 'none'
energy = 150
direction = 1
nick = ''
prof = ''
imhere = ''
stepBack = 0
trap_cd = False
rico_cd = False
knockback_cd = False
PL = False
almostRun = False
AutoRun = False
notEnoughNRG = False
needsReload = False
chatControl = 0
AutoGet = True
AutoFight = False
toLockParty = False
mod = 0
hardMode = 0
m2Fights = 0
m2Targets = 0
m2Babies = 0
m2Tickets = 0
m2Ticket1 = 0
m2Ticket2 = 0
m2Ticket3 = 0
weapon = '🟧[👁‍🗨]MM TAC-50 Славы Ⅲ (🔸+8) 📦[👁‍🗨]['
stationNames = station_Names()

@client.on(events.NewMessage)
async def normal_handler(event):
    global AutoGet,state,game,gameId,state,energy,direction,nick,prof,imhere,stepBack,trap_cd,rico_cd,knockback_cd,PL,almostRun,weapon,mod,AutoRun,chatControl,notEnoughNRG,needsReload,hardMode,AutoFight,toLockParty,m2Fights,m2Babies,m2Tickets,m2Targets,m2Ticket1,m2Ticket2,m2Ticket3
    me = await client.get_me()
    s_user_id = event.message.from_id
    messag = event.message.to_dict()['message']
    sender = event.message.sender
    chatFrom = event.message.peer_id
    if hasattr(chatFrom,'user_id'):
        fromChat = event.message.peer_id.user_id
    elif hasattr(chatFrom,'channel_id'):
        fromChat = event.message.peer_id.channel_id
    # if hasattr(event.message.reply_markup, 'rows'):
    # print(event.message.reply_markup.rows[0].buttons[0].text)
    if messag.startswith('.test') and fromChat == me.id:
        state = 'test'
    if messag == '.set_chat' and sender == me:
        chatControl = fromChat
    if messag.startswith('.use_tea ') and fromChat == me.id:
        if messag == '.use_tea on':
            teaUse = True
        elif messag == '.use_tea off':
            teaUse = False
    if messag.startswith('.tea ') and nick in messag and teaUse == True:
        await client.send_message(game,'/use_Food64')
        await asyncio.sleep(1)
        m = await client.get_messages(game, limit=1)
        if 'Предмет отсутствует в рюкзаке' in m[0].message:
            await asyncio.sleep(1)
            await client.send_message(game,'/use_Food21')
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            if 'Предмет отсутствует в рюкзаке' in m[0].message:
                teaUse = False
        await asyncio.sleep(1)
        m = await client.get_messages(game, limit=1)
        if teaUse == True and 'Предмет отсутствует в рюкзаке' not in m[0].message and 'чай' in m[0].message and 'увеличивает характеристики персонажа' in m[0].message:
            await m[0].click(0)
    if messag.startswith('.adr ') and nick in messag:
        await asyncio.sleep(random.randint(1,5))
        await client.send_message(game,'/h')
        await asyncio.sleep(0.5)
        adrText = ''
        m = await client.get_messages(game, limit=1)
        buttonsDir = m[0].reply_markup
        for r in range(len(buttonsDir.rows)):
            buttonsInRow = buttonsDir.rows[r].buttons
            for b in range(len(buttonsInRow)):
                if 'Адреналин' in buttonsInRow[b].text:
                    adrText = buttonsInRow[b].text
        if adrText == '':
            event.message.reply('У меня закончился Адреналин')
        else:
            await m[0].click(text=adrText)
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            buttonsDir = m[0].reply_markup
            for r in range(len(buttonsDir.rows)):
                buttonsInRow = buttonsDir.rows[r].buttons
                for b in range(len(buttonsInRow)):
                    partStatus = buttonsInRow[b].text
                    if 'Назад' not in partStatus and int(re.findall('[0-9]+', partStatus)[0]) < 31:
                        await m[0].click(text=partStatus)
                        await asyncio.sleep(0.8)
    if messag.startswith('.hardmode') and fromChat == me.id:
        hardMode = int(messag.split(' ')[1]) -1
    if messag.startswith('.auto') and fromChat == me.id:
        if AutoFight == False:
            AutoFight = True
            await client.send_message(me, 'Режим Автобой включен')
        else:
            AutoFight = False
            await client.send_message(me, 'Режим Автобой выключен')
    if messag.startswith('.broke') and fromChat == me.id and state == 'none':
        state = 'broke'
        mod = int(messag.split(' ')[1]) - 1
        await client.send_message(game,'📤 Выбрать предмет')
        await asyncio.sleep(1)
        m = await client.get_messages(game, limit=1)
        await m[0].click(mod)
    if 'Добавьте предмет' in messag and fromChat == gameId and state == 'broke':
        await asyncio.sleep(1.5)
        m = await client.get_messages(game, limit=1)
        await m[0].click(0)
        await asyncio.sleep(1.5)
        m = await client.get_messages(game, limit=1)
        fin = m[0].message
        while 'Доступная' not in fin and 'Недостаточно средств' not in fin and state == 'broke':
            m = await client.get_messages(game, limit=1)
            await m[0].click(0)
            m = await client.get_messages(game, limit=1)
            await asyncio.sleep(1.5)
            await m[0].click(0)
            m = await client.get_messages(game, limit=1)
            await asyncio.sleep(1.5)
            await m[0].click(0)
            await asyncio.sleep(1)
            fin = await client.get_messages(game, limit=1)

        state = 'none'
        print('end broke')
        mod = 0
    if messag.startswith('.stats') and (fromChat == me.id or fromChat == chatControl):
        if messag == '.stats m2':
            txt = ('**Проведено боёв в М2:** '+str(m2Fights)
                   + '\n**Найдено Чёрных Детёнышей:** '+str(m2Babies)+' из '+str(m2Targets)+' мобов __('+str("{:0.2f}".format((m2Babies/m2Targets)*100))+'%)__'
                   +'\n**Получено частей пропуска Д-6:** '+str(m2Tickets)+' __('+str("{:0.2f}".format((m2Tickets/m2Babies)*100))+'%)__'
                   +'\n\n🇳🇵ч.1 пропуска Д-6 ₓ'+str(m2Ticket1)+'\n🇳🇵ч.2 пропуска Д-6 ₓ'+str(m2Ticket2)+'\n🇳🇵ч.3 пропуска Д-6 ₓ'+str(m2Ticket3))
            await event.message.reply(txt)
    if messag.startswith('.synt ') and fromChat == me.id and state == 'none':
        state = 'synt'
        mod = int(messag.split(' ')[1])
        print(mod)
        await client.send_message(game,'📤 Выбрать предмет')
    if 'Добавьте первый модуль' in messag and fromChat == gameId and state == 'synt' and mod > 0:
        print(mod)
        await asyncio.sleep(1)
        m = await client.get_messages(game, limit=1)
        await m[0].click(mod-1)
        await asyncio.sleep(1)
        m = await client.get_messages(game, limit=1)
        fin = m[0].message
        if 'Доступные для синтеза модули отсутствуют' not in fin:
            m = await client.get_messages(game, limit=1)
            await asyncio.sleep(1)
            await m[0].click(0)
            m = await client.get_messages(game, limit=1)
            await asyncio.sleep(1)
            await m[0].click(0)
            m = await client.get_messages(game, limit=1)
            await asyncio.sleep(1)
            await client.send_message(game,'📤 Выбрать предмет')
        else:
            state = 'none'
            mod = 0
    if messag.startswith('.box') and fromChat == me.id and state == 'none':
        if messag == '.box':
            state = 'box'
            await client.send_message(game,'/other')
        elif messag == '.box c':
            fin = ''
            state = 'open'
            while 'отсутствует в рюкзаке' not in fin and 'Рюкзак переполнен' not in fin and state == 'open':
                await asyncio.sleep(1.5)
                await client.send_message(game,'/use_ClothesBoxIV')
                await asyncio.sleep(1)
                m = await client.get_messages(game, limit=1)
                fin = m[0].message
                if 'отсутствует в рюкзаке' not in fin:
                    await asyncio.sleep(1)
                    await event.message.click(0)
                    await asyncio.sleep(1)
                    await event.message.click(0)
                    m = await client.get_messages(game, limit=1)
                    fin = m[0].message
            state = 'none'
    if state == 'box' and 'Рюкзак ('+nick+')\n\nПрочее' in messag and fromChat == gameId:
        baglines = messag.split('\n')
        for x in range(len(baglines)):
            if '🎁 Награда (36-40)' in baglines[x]:
                state = 'open'
                fin = ''
                while 'отсутствует в рюкзаке' not in fin and state == 'open':
                    await asyncio.sleep(1.5)
                    await client.send_message(game,'/use_DangeRewardII')
                    await asyncio.sleep(1)
                    m = await client.get_messages(game, limit=1)
                    fin = m[0].message
                    if 'отсутствует в рюкзаке' not in fin:
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        m = await client.get_messages(game, limit=1)
                        fin = m[0].message
                state = 'none'
                await asyncio.sleep(1)
                await client.send_message(game,'/other')
            elif '🎁 Награда (41-45)' in baglines[x]:
                state = 'open'
                fin = ''
                while 'отсутствует в рюкзаке' not in fin and state == 'open':
                    await asyncio.sleep(1.5)
                    await client.send_message(game,'/use_DangeRewardIII')
                    await asyncio.sleep(1)
                    m = await client.get_messages(game, limit=1)
                    fin = m[0].message
                    if 'отсутствует в рюкзаке' not in fin:
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        m = await client.get_messages(game, limit=1)
                        fin = m[0].message
                state = 'none'
                await asyncio.sleep(1)
                await client.send_message(game,'/other')
            elif 'Награда (46-50)' in baglines[x]:
                state = 'open'
                fin = ''
                while 'отсутствует в рюкзаке' not in fin and state == 'open':
                    await asyncio.sleep(1.5)
                    await client.send_message(game,'/use_DangeRewardIV')
                    m = await client.get_messages(game,limit=1)
                    fin = m[0].message
                    if 'отсутствует в рюкзаке' not in fin:
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        m= await client.get_messages(game,limit=1)
                        fin = m[0].message
                state = 'none'
                await asyncio.sleep(1)
                await client.send_message(game,'/other')
            elif 'Коробка ресурсов' in baglines[x]:
                fin = ''
                state = 'open'
                while 'отсутствует в рюкзаке' not in fin and state == 'open':
                    await asyncio.sleep(1.5)
                    await client.send_message(game,'/use_ResourcesBoxV')
                    await asyncio.sleep(1)
                    m = await client.get_messages(game,limit=1)
                    fin = m[0].message
                    if 'отсутствует в рюкзаке' not in fin:
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        m = await client.get_messages(game,limit=1)
                        fin = m[0].message
                state = 'none'
                await asyncio.sleep(1)
                await client.send_message(game,'/other')
            elif baglines[x].startswith('🗳 Коробка оружия'):
                fin = ''
                state = 'open'
                while 'отсутствует в рюкзаке' not in fin and state == 'open':
                    await asyncio.sleep(1.5)
                    await client.send_message(game,'/use_WeaponBoxIV')
                    await asyncio.sleep(1)
                    m = await client.get_messages(game, limit=1)
                    fin = m[0].message
                    if 'отсутствует в рюкзаке' not in fin:
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        m = await client.get_messages(game, limit=1)
                        fin = m[0].message
                state = 'none'
                await asyncio.sleep(1)
                await client.send_message(game,'/other')
            elif ('Коробка брони') in baglines[x] and state == 'open':
                fin = ''
                state = 'open'
                while 'отсутствует в рюкзаке' not in fin:
                    await asyncio.sleep(1.5)
                    await client.send_message(game,'/use_ClothesBoxIV')
                    await asyncio.sleep(1)
                    m = await client.get_messages(game, limit=1)
                    fin = m[0].message
                    if 'отсутствует в рюкзаке' not in fin:
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        m = await client.get_messages(game, limit=1)
                        fin = m[0].message
                state = 'none'
                await asyncio.sleep(1)
                await client.send_message(game,'/other')
    if messag.startswith('📰 Персонаж\n\n📟ID: '+str(me.id)) and fromChat == gameId:
        personaj = messag.split('\n')
        nick = personaj[3].split('Ник: ')[1].split(' /a')[0]
        prof = personaj[5].split('Класс: ')[1]
        energy = int(personaj[10].split('🔋Энергия: ')[1].split('/')[0])
    # print(nick,prof,energy)
    if 'Вы будете перенаправлены на официальный сайт нашего проекта' in messag and (fromChat == gameId or fromChat == me.id):
        entities = event.message.entities
        for ent in entities:
            if isinstance(ent,MessageEntityTextUrl):
                if "captcha.metro-wars.online/?id=" in ent.url:
                    sleep(randint(3,6))
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
                    try:
                        r = requests.get(ent.url,headers=headers)
                    except:
                        print('Капча пройдена')
                        sleep(randint(2,5))
                        await client.send_message(game,'/start')
    if '🚸 Статус: ' in messag and fromChat == gameId:
        if '❤️' in messag.split('\n')[0]:
            imhere = messag.split('\n')[3]
        else:
            imhere = messag.split('\n')[0]
    if messag.startswith('.imhere'):
        imhere = messag.split('.imhere ')[1]
    if messag == '.pl on' and sender == me and fromChat == me.id:
        PL = True
    elif messag == '.pl off' and sender == me and fromChat == me.id:
        PL = False
    if messag == '.autorun on' and PL == True and chatControl == fromChat:
        AutoRun = True
        await event.message.reply('Автозапуск включен')
    if messag == '.autorun off' and PL == True and chatControl == fromChat:
        AutoRun = False
        await event.message.reply('Автозапуск выключен')
    if messag.startswith('.leader ') and PL == True:
        swapToLeader = messag.split('leader ')[1]
        leaderChanged = False
        while leaderChanged == False:
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'🗣 Управление')
            await asyncio.sleep(0.5)
            await client.send_message(game,'👑 Лидерство')
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            buttonsDir = m[0].reply_markup
            for r in range(len(buttonsDir.rows)):
                buttonsInRow = buttonsDir.rows[r].buttons
                for b in range(len(buttonsInRow)):
                    if swapToLeader in buttonsInRow[b].text:
                        await m[0].click(text=buttonsInRow[b].text)
                        await asyncio.sleep(0.5)
                        m = await client.get_messages(game, limit=2)
                        if 'Предложение о передаче лидера группы отправлено' in m[1].message:
                            leaderChanged = True
                            PL = False
                            await event.message.reply('Принимай лидерку')
    if messag.startswith('.dg') and sender == me and fromChat == me.id and state == 'none':
        state = messag.split('.')[1]
    if (messag.startswith('🎁 Награда ') or messag.startswith('🗳 Коробка ')) and fromChat == gameId:
        await asyncio.sleep(1)
        await event.message.click(0)
    if messag == '.get' and fromChat == me.id:
        if AutoGet == True:
            AutoGet = False
            await client.send_message(me, 'Автополучение выключено')
        else:
            AutoGet = True
            await client.send_message(me, 'Автополучение включено')
    if messag.startswith( '📥 Получите предметы:') and fromChat == gameId and AutoGet == True:
        await asyncio.sleep(1)
        await event.message.click(0)
    if PL == True and 'хочет вступить в группу' in messag and fromChat == gameId:
        await asyncio.sleep(random.randint(1,3))
        await event.message.click(0)
    if PL == False and 'Предложение о передаче лидера группы' in messag and fromChat == gameId:
        await asyncio.sleep(random.randint(1,3))
        await event.message.click(0)
        PL = True
    if messag == '.lock' and PL == True:
        await client.send_message(game,'/group')
        await asyncio.sleep(0.5)
        await client.send_message(game,'🗣 Управление')
        await asyncio.sleep(0.5)
        await client.send_message(game,'🏃 Движение')
        await asyncio.sleep(0.5)
        await client.send_message(game,'💢 Включить захват')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=2)
        if m[0].message.startswith('❗️Указанные игроки находятся не рядом'):
            await event.message.reply(m[0].message)
        elif m[0].message == 'Неизвестная команда':
            await event.message.reply('Ошибка, повтори еще раз')
        elif 'Захват группы включен' in m[1].message:
            await asyncio.sleep(0.5)
            await event.message.reply('Захват выполнен')
        await asyncio.sleep(1)
        await client.send_message(game,'/buttons')
    if ('...вы отправляетесь на заброшенную территорию' in messag or '...переход в следующую комнату' in messag) and fromChat == gameId and state.startswith('dg'):
        almostRun = False
        stepBack = 0
        trap_cd = False
        rico_cd = False
        knockback_cd = False
        needsReload = False
        await asyncio.sleep(10)
        m = await client.get_messages(game, limit=1)
        if '[B]' in m[0].message:
            await client.send_message(game,'🏃 Движение')
            await asyncio.sleep(2)
            await client.send_message(game,'↕️ По направлению')
            await asyncio.sleep(2)
            await client.send_message(game,'⬇')
        else:
            isAutoFightButton = m[0].reply_markup
            if len(isAutoFightButton.rows)>1:
                if '[B]' not in messag and isAutoFightButton.rows[3].buttons[0].text.startswith('♻️ Автобой'):
                    await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
    elif weapon in messag and 'Выберите цель' not in messag and fromChat == gameId and state.startswith('dg'):
        m = await client.get_messages(game, limit=1)
        isAutoFightButton = m[0].reply_markup
        if len(isAutoFightButton.rows)>1:
            if '[B]' not in messag and isAutoFightButton.rows[3].buttons[0].text.startswith('♻️ Автобой'):
                await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
            elif '[B]' in messag and isAutoFightButton.rows[3].buttons[0].text.startswith('♻️ Автобой') and AutoFight == True:
                await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
            elif '[B]' in messag and isAutoFightButton.rows[3].buttons[0].text.startswith('♻️ Автобой') and AutoFight == False:
                if '⏱ Доступно - ⇴ Рикошет' in messag:
                    rico_cd = False
                if '⏱ Доступно - 🖲 Ловушка' in messag:
                    trap_cd = False
                if '⏱ Доступно - 🔊 Отброс' in messag:
                    knockback_cd = False
                if messag.split(weapon)[1].split('/')[0] == '0':
                    needsReload = True
                if trap_cd == False:
                    await asyncio.sleep(3)
                    await client.send_message(game,'🌀 Умения')
                    await asyncio.sleep(2)
                    await client.send_message(game,'🖲 Ловушка')
                    await asyncio.sleep(2)
                    await client.send_message(game,'⏹ К объекту')
                    await asyncio.sleep(1)
                    target = await client.get_messages(game, limit=1)
                    await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                    await asyncio.sleep(2)
                    await client.send_message(game,'✅ Подтвердить')
                    trap_cd = True
                elif needsReload == True:
                    await asyncio.sleep(3)
                    await client.send_message(game,'🔄 Перезарядка')
                    needsReload = False
                elif rico_cd == False:
                    await asyncio.sleep(3)
                    await client.send_message(game,'🌀 Умения')
                    await asyncio.sleep(2)
                    await client.send_message(game,'⇴ Рикошет')
                    await asyncio.sleep(1)
                    target = await client.get_messages(game, limit=1)
                    await asyncio.sleep(2)
                    await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                    rico_cd = True
                elif knockback_cd == False:
                    await asyncio.sleep(3)
                    await client.send_message(game,'🌀 Умения')
                    await asyncio.sleep(2)
                    await client.send_message(game,'🔊 Отброс')
                    await asyncio.sleep(2)
                    await client.send_message(game,'⏹ К объекту')
                    await asyncio.sleep(1)
                    target = await client.get_messages(game, limit=1)
                    await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                    await asyncio.sleep(2)
                    await client.send_message(game,'✅ Подтвердить')
                    knockback_cd = True
                else:
                    await asyncio.sleep(3)
                    await client.send_message(game,'⚔️ Атака')
                    await asyncio.sleep(1)
                    target = await client.get_messages(game, limit=1)
                    await asyncio.sleep(2)
                    await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
    # <============================================================================================BOSS
    if messag.startswith('.boss') and sender == me and fromChat == me.id and state == 'none':
        state = 'boss'
        await client.send_message(me, 'Режим Боссы включен')
    if messag.startswith('❕На вас нападает ') and fromChat == gameId and state == 'boss':
        stepBack = 0
        almostRun = False
        trap_cd = False
        rico_cd = False
        knockback_cd = False
        await asyncio.sleep(7)
        if 'Арахна' in messag:
            await client.send_message(game,'🏃 Движение')
            await asyncio.sleep(2)
            await client.send_message(game,'⌛️ Переждать')
            stepBack = stepBack + 1
        else:
            await client.send_message(game,'🏃 Движение')
            await asyncio.sleep(2)
            await client.send_message(game,'↕️ По направлению')
            await asyncio.sleep(2)
            await client.send_message(game,'↘')
            stepBack = 4
    elif weapon in messag and 'Выберите цель' not in messag and fromChat == gameId and state == 'boss':
        if stepBack == 1:
            await asyncio.sleep(2)
            await client.send_message(game,'🏃 Движение')
            await asyncio.sleep(2)
            await client.send_message(game,'↕️ По направлению')
            await asyncio.sleep(2)
            await client.send_message(game,'➡')
            stepBack = stepBack + 1
        elif stepBack == 2:
            await asyncio.sleep(2)
            await client.send_message(game,'🏃 Движение')
            await asyncio.sleep(2)
            await client.send_message(game,'↕️ По направлению')
            await asyncio.sleep(2)
            await client.send_message(game,'⬇')
            stepBack = stepBack + 1
        elif stepBack == 3:
            await asyncio.sleep(3)
            await client.send_message(game,'⚔️ Атака')
            await asyncio.sleep(1)
            target = await client.get_messages(game, limit=1)
            await asyncio.sleep(2)
            await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
            stepBack = 4
        elif stepBack == 4:
            if '⏱ Доступно - ⇴ Рикошет' in messag:
                rico_cd = False
            if '⏱ Доступно - 🖲 Ловушка' in messag:
                trap_cd = False
            if '⏱ Доступно - 🔊 Отброс' in messag:
                knockback_cd = False
            if trap_cd == False:
                await asyncio.sleep(3)
                await client.send_message(game,'🌀 Умения')
                await asyncio.sleep(2)
                await client.send_message(game,'🖲 Ловушка')
                await asyncio.sleep(2)
                await client.send_message(game,'⏹ К объекту')
                await asyncio.sleep(1)
                target = await client.get_messages(game, limit=1)
                await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                await asyncio.sleep(2)
                await client.send_message(game,'✅ Подтвердить')
                trap_cd = True
            elif '0/3]' in messag.split(weapon)[1]:
                await asyncio.sleep(3)
                await client.send_message(game,'🔄 Перезарядка')
            elif rico_cd == False:
                await asyncio.sleep(3)
                await client.send_message(game,'🌀 Умения')
                await asyncio.sleep(2)
                await client.send_message(game,'⇴ Рикошет')
                await asyncio.sleep(1)
                target = await client.get_messages(game, limit=1)
                await asyncio.sleep(2)
                await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                rico_cd = True
            elif knockback_cd == False:
                await asyncio.sleep(3)
                await client.send_message(game,'🌀 Умения')
                await asyncio.sleep(2)
                await client.send_message(game,'🔊 Отброс')
                await asyncio.sleep(2)
                await client.send_message(game,'⏹ К объекту')
                await asyncio.sleep(1)
                target = await client.get_messages(game, limit=1)
                await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                await asyncio.sleep(2)
                await client.send_message(game,'✅ Подтвердить')
                knockback_cd = True
            else:
                await asyncio.sleep(3)
                await client.send_message(game,'⚔️ Атака')
                await asyncio.sleep(1)
                target = await client.get_messages(game, limit=1)
                await asyncio.sleep(2)
                await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)

    # <============================================================================================M2
    if messag.startswith('.m2') and sender == me and fromChat == me.id and state == 'none':
        state = 'm2'
        await client.send_message(me, 'Режим M2 включен')
    if ('Вы нападаете на' in messag or 'На вас нападают:' in messag) and fromChat == gameId and state == 'm2':
        m2Fights = m2Fights + 1
        targets = messag.split('Вы нападаете на\n\n')[1].split('\n\nожидайте')[0]
        babySpl = targets.split('\n')
        for baby in range(len(babySpl)):
            m2Targets = m2Targets + 1
            if 'Чёрный Детёныш' in babySpl[baby]:
                m2Babies = m2Babies + 1
        almostRun = False
        stepBack = 0
        trap_cd = False
        rico_cd = False
        knockback_cd = False
        needsReload = False
        await asyncio.sleep(5)
        m = await client.get_messages(game, limit=1)
        if AutoFight == True:
            isAutoFightButton = m[0].reply_markup
            if len(isAutoFightButton.rows)>1:
                if isAutoFightButton.rows[3].buttons[0].text.startswith('♻️ Автобой'):
                    await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
        else:
            await client.send_message(game,'🏃 Движение')
            await asyncio.sleep(2)
            await client.send_message(game,'↕️ По направлению')
            await asyncio.sleep(2)
            await client.send_message(game,'⬅')
            stepBack = 2
    elif weapon in messag and 'Выберите цель' not in messag and fromChat == gameId and state.startswith('m2'):
        m = await client.get_messages(game, limit=1)
        isAutoFightButton = m[0].reply_markup
        if len(isAutoFightButton.rows)>1:
            if AutoFight == True and isAutoFightButton.rows[3].buttons[0].text.startswith('♻️ Автобой'):
                await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
            elif AutoFight == False and isAutoFightButton.rows[3].buttons[0].text.startswith('♻️ Автобой'):
                if stepBack == 1:
                    await asyncio.sleep(3)
                    await client.send_message(game,'🏃 Движение')
                    await asyncio.sleep(2)
                    await client.send_message(game,'↕️ По направлению')
                    await asyncio.sleep(2)
                    await client.send_message(game,'⬅')
                    stepBack = 2
                elif stepBack == 2:
                    if '⏱ Доступно - ⇴ Рикошет' in messag:
                        rico_cd = False
                    if '⏱ Доступно - 🖲 Ловушка' in messag:
                        trap_cd = False
                    if '⏱ Доступно - 🔊 Отброс' in messag:
                        knockback_cd = False
                    if messag.split(weapon)[1].split('/')[0] == '0':
                        needsReload = True
                    if trap_cd == False:
                        await asyncio.sleep(3)
                        await client.send_message(game,'🌀 Умения')
                        await asyncio.sleep(2)
                        await client.send_message(game,'🖲 Ловушка')
                        await asyncio.sleep(1)
                        await client.send_message(game,'⏹ К объекту')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                        await asyncio.sleep(2)
                        await client.send_message(game,'✅ Подтвердить')
                        trap_cd = True
                    elif needsReload == True:
                        await asyncio.sleep(3)
                        await client.send_message(game,'🔄 Перезарядка')
                        needsReload = False
                    elif rico_cd == False:
                        await asyncio.sleep(3)
                        await client.send_message(game,'🌀 Умения')
                        await asyncio.sleep(2)
                        await client.send_message(game,'⇴ Рикошет')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                        rico_cd = True
                    elif knockback_cd == False:
                        await asyncio.sleep(3)
                        await client.send_message(game,'🌀 Умения')
                        await asyncio.sleep(2)
                        await client.send_message(game,'🔊 Отброс')
                        await asyncio.sleep(1)
                        await client.send_message(game,'⏹ К объекту')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                        await asyncio.sleep(2)
                        await client.send_message(game,'✅ Подтвердить')
                        knockback_cd = True
                    else:
                        await asyncio.sleep(3)
                        await client.send_message(game,'⚔️ Атака')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await asyncio.sleep(2)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)

    # <============================================================================================M2
    if messag == '.farm' and sender == me and fromChat == me.id and state == 'none':
        state = 'farm'
        await client.send_message(me, 'Режим FARM включен')
    if ('Вы нападаете на' in messag or 'На вас нападают:' in messag) and fromChat == gameId and state == 'farm':
        if 'На вас нападают' in messag:
            await asyncio.sleep(2)
            await client.send_message(game,'⚔️ Драться')
        almostRun = False
        stepBack = 0
        trap_cd = False
        rico_cd = False
        knockback_cd = False
        needsReload = False
        await asyncio.sleep(5)
        m = await client.get_messages(game, limit=1)
        if AutoFight == True:
            isAutoFightButton = m[0].reply_markup
            if len(isAutoFightButton.rows)>1:
                if isAutoFightButton.rows[3].buttons[0].text.startswith('♻️ Автобой'):
                    await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
        else:
            await client.send_message(game,'🏃 Движение')
            await asyncio.sleep(2)
            await client.send_message(game,'↕️ По направлению')
            await asyncio.sleep(2)
            await client.send_message(game,'⬅')
            stepBack = 2
    elif weapon in messag and 'Выберите цель' not in messag and fromChat == gameId and state.startswith('m2'):
        m = await client.get_messages(game, limit=1)
        isAutoFightButton = m[0].reply_markup
        if len(isAutoFightButton.rows)>1:
            if AutoFight == True and isAutoFightButton.rows[3].buttons[0].text.startswith('♻️ Автобой'):
                await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
            elif AutoFight == False and isAutoFightButton.rows[3].buttons[0].text.startswith('♻️ Автобой'):
                if stepBack == 1:
                    await asyncio.sleep(3)
                    await client.send_message(game,'🏃 Движение')
                    await asyncio.sleep(2)
                    await client.send_message(game,'↕️ По направлению')
                    await asyncio.sleep(2)
                    await client.send_message(game,'⬅')
                    stepBack = 2
                elif stepBack == 2:
                    if '⏱ Доступно - ⇴ Рикошет' in messag:
                        rico_cd = False
                    if '⏱ Доступно - 🖲 Ловушка' in messag:
                        trap_cd = False
                    if '⏱ Доступно - 🔊 Отброс' in messag:
                        knockback_cd = False
                    if messag.split(weapon)[1].split('/')[0] == '0':
                        needsReload = True
                    if trap_cd == False:
                        await asyncio.sleep(3)
                        await client.send_message(game,'🌀 Умения')
                        await asyncio.sleep(2)
                        await client.send_message(game,'🖲 Ловушка')
                        await asyncio.sleep(1)
                        await client.send_message(game,'⏹ К объекту')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                        await asyncio.sleep(2)
                        await client.send_message(game,'✅ Подтвердить')
                        trap_cd = True
                    elif needsReload == True:
                        await asyncio.sleep(3)
                        await client.send_message(game,'🔄 Перезарядка')
                        needsReload = False
                    elif rico_cd == False:
                        await asyncio.sleep(3)
                        await client.send_message(game,'🌀 Умения')
                        await asyncio.sleep(2)
                        await client.send_message(game,'⇴ Рикошет')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                        rico_cd = True
                    elif knockback_cd == False:
                        await asyncio.sleep(3)
                        await client.send_message(game,'🌀 Умения')
                        await asyncio.sleep(2)
                        await client.send_message(game,'🔊 Отброс')
                        await asyncio.sleep(1)
                        await client.send_message(game,'⏹ К объекту')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                        await asyncio.sleep(2)
                        await client.send_message(game,'✅ Подтвердить')
                        knockback_cd = True
                    else:
                        await asyncio.sleep(3)
                        await client.send_message(game,'⚔️ Атака')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await asyncio.sleep(2)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)

    # <============================================================================================PARTY
    if 'Захват группы отключен' in messag and fromChat == gameId and PL == True and state != 'none':
        toLockParty = True
    if 'Захват группы включен' in messag and fromChat == gameId and PL == True and state != 'none':
        toLockParty = False
    if messag == 'Ты полноценно отдохнул!' and fromChat == gameId and PL == True and notEnoughNRG == True and (state == 'boss' or state.startswith('dg') or state == 'm2') and AutoRun == True:
        notEnoughNRG = False
        if state == 'dg 36-40':
            run = '🥀 Белорусский вокзал (36-40)'
        elif state == 'dg 41-45':
            run = '🥀 Аптекарский огород (41-45)'
        elif state == 'dg 46-50':
            run = '🥀 Площадь трёх вокзалов (46-50)'
        elif state == 'boss':
            run = '🦪 Использовать приманку'
        elif state == 'm2' or state == 'farm':
            run = '👾 Поиск монстров'
            if toLockParty == True and state == 'm2':
                isLocked = False
                await client.send_message(game,'/group')
                await asyncio.sleep(0.5)
                await client.send_message(game,'🗣 Управление')
                await asyncio.sleep(0.5)
                await client.send_message(game,'🏃 Движение')
                await asyncio.sleep(0.5)
                await client.send_message(game,'💢 Включить захват')
                while isLocked == False:
                    await asyncio.sleep(0.5)
                    m = await client.get_messages(game, limit=2)
                    if m[0].message.startswith('❗️Указанные игроки находятся не рядом'):
                        isLocked = True
                        await client.send_message(chatControl,m[0].message)
                    elif 'Захват группы включен' in m[1].message:
                        isLocked = True
                        toLockParty = False
                        await asyncio.sleep(0.5)
                        await client.send_message(game,'/buttons')
                        await asyncio.sleep(1)
                        await client.send_message(game,run)
        if state.startswith('dg'):
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'👥 Состав')
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            splitGroup = m[0].message.split('[1')[1].split('\n')
            plToAdr = ''
            for x in range(len(splitGroup)):
                if '[👑] ' in splitGroup[x]:
                    plToAdr = plToAdr + splitGroup[x].split('[👑] ')[1].split(' (')[0] + ' '
                else:
                    plToAdr = plToAdr + splitGroup[x].split('] ')[1].split(' (')[0] + ' '
            if plToAdr != '':
                await client.send_message(chatControl,'.tea '+plToAdr)
            await asyncio.sleep(0.5)
            await client.send_message(game,'/buttons')
            await asyncio.sleep(5)
        await client.send_message(game,run)
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'Выберите сложность ' in m[0].message:
            await m[0].click(hardMode)
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            await m[0].click(text='✅ Подтвердить')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'Монстров нет' in m[0].message:
            await client.send_message(game,'/flashlight')
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            await m[0].click(0)
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            if 'Запас прочности слишком мал' in m[0].message:
                await m[0].click(1)
                await asyncio.sleep(1)
                await client.send_message(game,'🎒 Рюкзак')
                await asyncio.sleep(1)
                m = await client.get_messages(game, limit=1)
                bSpl = m[0].message.split('\n')
                flToWear = ''
                for b in range(len(bSpl)):
                    if bSpl[b].startswith('🔦 Фонарик ﴾100'):
                        flToWear = b+1
                        break
                await client.send_message(game,bSpl[flToWear])
                await asyncio.sleep(1)
                await client.send_message(game,'/flashlight')
                await asyncio.sleep(1)
                m = await client.get_messages(game, limit=1)
                await m[0].click(1)
                await asyncio.sleep(1)
                await m[0].click(0)
                await asyncio.sleep(2)
            await client.send_message(game,'👾 Поиск монстров')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'Недостаточно энергии' in m[0].message:
            await client.send_message(chatControl,'Недостаточно энергии, ждем')
            notEnoughNRG = True
        elif 'отсутствует в рюкзаке' in m[0].message:
            await client.send_message(chatControl,m[0].message+'\n\n.leader __NICKNAME__, чтоб сменить лидера')
        elif 'Необходимо выполнить захват' in m[0].message:
            isLocked = False
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'🗣 Управление')
            await asyncio.sleep(0.5)
            await client.send_message(game,'🏃 Движение')
            await asyncio.sleep(0.5)
            await client.send_message(game,'💢 Включить захват')
            while isLocked == False:
                await asyncio.sleep(0.5)
                m = await client.get_messages(game, limit=2)
                if m[0].message.startswith('❗️Указанные игроки находятся не рядом'):
                    isLocked = True
                    await client.send_message(chatControl,m[0].message)
                elif 'Захват группы включен' in m[1].message:
                    isLocked = True
                    await asyncio.sleep(0.5)
                    await client.send_message(game,'/buttons')
                    await asyncio.sleep(1)
                    await client.send_message(game,run)
    if (state == 'boss' or state.startswith('dg') or state == 'm2' or state == 'farm') and 'Бой выигран' in messag and fromChat == gameId and PL == True and AutoRun == True:
        if 'пропуска Д-6' in messag:
            lootSpl = messag.split('\n')
            for l in range(len(lootSpl)):
                if 'пропуска Д-6' in lootSpl[l]:
                    await client.send_message(chatControl,'Получена '+lootSpl[l])
                    m2Tickets = m2Tickets + 1
                    if 'ч.1' in lootSpl[l]:
                        m2Ticket1 = m2Ticket1 + 1
                    elif 'ч.2' in lootSpl[l]:
                        m2Ticket2 = m2Ticket2 + 1
                    elif 'ч.3' in lootSpl[l]:
                        m2Ticket3 = m2Ticket3 + 1
        if state == 'm2' or state == 'farm':
            await asyncio.sleep(2)
        else:
            await asyncio.sleep(random.randint(5,10))
        if state == 'farm':
            await client.send_message(game,'/h')
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            spl = m[0].message.split('\n')[0].split(' 🔋')[0]
            heartEmoji = '❤️'
            if '❤️' in spl:
                heartEmoji = '❤️'
            elif '💛' in spl:
                heartEmoji = '💛'
            elif '❣️' in spl:
                heartEmoji = '❣️'
            pHPm = re.sub('\D', '', spl.split('/')[1])
            pHPc = re.sub('\D', '', spl.split(heartEmoji)[1].split('/')[0])
            myHP = math.ceil((int(pHPc)/int(pHPm))*100)
            if myHP < 55:
                await asyncio.sleep(1)
                await m[0].click(0)
                await asyncio.sleep(1)
                m = await client.get_messages(game, limit=1)
                await m[0].click(0)
                await asyncio.sleep(1)
                m = await client.get_messages(game, limit=1)
                await m[0].click(1)
            if heartEmoji == '❣️':
                await asyncio.sleep(1)
                adrText = ''
                m = await client.get_messages(game, limit=1)
                buttonsDir = m[0].reply_markup
                for r in range(len(buttonsDir.rows)):
                    buttonsInRow = buttonsDir.rows[r].buttons
                    for b in range(len(buttonsInRow)):
                        if 'Адреналин' in buttonsInRow[b].text:
                            adrText = buttonsInRow[b].text
                if adrText != '':
                    await m[0].click(text=adrText)
                    await asyncio.sleep(0.5)
                    m = await client.get_messages(game,limit=1)
                    buttonsDir = m[0].reply_markup
                    for r in range(len(buttonsDir.rows)):
                        buttonsInRow = buttonsDir.rows[r].buttons
                        for b in range(len(buttonsInRow)):
                            partStatus = buttonsInRow[b].text
                            if 'Назад' not in partStatus and int(re.findall('[0-9]+',partStatus)[0]) < 31:
                                await m[0].click(text=partStatus)
                                await asyncio.sleep(0.8)
        else:
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'👥 Состав')
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            splitGroup = m[0].message.split('\n')
            plToAdr = ''
            for x in range(len(splitGroup)):
                if '❣️' in splitGroup[x]:
                    if '[👑] ' in splitGroup[x]:
                        plToAdr = plToAdr + splitGroup[x].split('[👑] ')[1].split(' (❣️')[0] + ' '
                    else:
                        plToAdr = plToAdr + splitGroup[x].split('] ')[1].split(' (❣️')[0] + ' '
            if plToAdr != '':
                await client.send_message(chatControl,'.adr '+plToAdr)
            await asyncio.sleep(0.5)
            await client.send_message(game,'/buttons')
            if plToAdr != '':
                await asyncio.sleep(random.randint(10,20))
            elif nick in plToAdr:
                await asyncio.sleep(random.randint(1,5))
                await client.send_message(game,'/h')
                await asyncio.sleep(0.5)
                adrText = ''
                m = await client.get_messages(game, limit=1)
                buttonsDir = m[0].reply_markup
                for r in range(len(buttonsDir.rows)):
                    buttonsInRow = buttonsDir.rows[r].buttons
                    for b in range(len(buttonsInRow)):
                        if 'Адреналин' in buttonsInRow[b].text:
                            adrText = buttonsInRow[b].text
                if adrText != '':
                    await m[0].click(text=adrText)
                    await asyncio.sleep(1)
                    m = await client.get_messages(game,limit=1)
                    buttonsDir = m[0].reply_markup
                    for r in range(len(buttonsDir.rows)):
                        buttonsInRow = buttonsDir.rows[r].buttons
                        for b in range(len(buttonsInRow)):
                            partStatus = buttonsInRow.text
                            if 'Назад' not in partStatus and int(re.findall('[0-9]+',partStatus)[0]) < 31:
                                await m[0].click(text=partStatus)
                                await asyncio.sleep(1)
            else:
                await asyncio.sleep(3)
        await asyncio.sleep(1)
        if state == 'dg 36-40':
            run = '🥀 Белорусский вокзал (36-40)'
        elif state == 'dg 41-45':
            run = '🥀 Аптекарский огород (41-45)'
        elif state == 'dg 46-50':
            run = '🥀 Площадь трёх вокзалов (46-50)'
        elif state == 'boss':
            run = '🦪 Использовать приманку'
        elif state == 'm2' or state == 'farm':
            run = '👾 Поиск монстров'
            if toLockParty == True and state == 'm2':
                isLocked = False
                await client.send_message(game,'/group')
                await asyncio.sleep(0.5)
                await client.send_message(game,'🗣 Управление')
                await asyncio.sleep(0.5)
                await client.send_message(game,'🏃 Движение')
                await asyncio.sleep(0.5)
                await client.send_message(game,'💢 Включить захват')
                while isLocked == False:
                    await asyncio.sleep(0.5)
                    m = await client.get_messages(game, limit=2)
                    if m[0].message.startswith('❗️Указанные игроки находятся не рядом'):
                        isLocked = True
                        await client.send_message(chatControl,m[0].message)
                    elif 'Захват группы включен' in m[1].message:
                        isLocked = True
                        toLockParty = False
                        await asyncio.sleep(0.5)
                        await client.send_message(game,'/buttons')
                        await asyncio.sleep(1)
                        await client.send_message(game,run)
        await client.send_message(game,run)
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'Выберите сложность ' in m[0].message:
            await m[0].click(hardMode)
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            await m[0].click(text='✅ Подтвердить')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'Монстров нет' in m[0].message:
            await client.send_message(game,'/flashlight')
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            await m[0].click(0)
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            if 'Запас прочности слишком мал' in m[0].message:
                await m[0].click(1)
                await asyncio.sleep(1)
                await client.send_message(game,'🎒 Рюкзак')
                await asyncio.sleep(1)
                m = await client.get_messages(game, limit=1)
                bSpl = m[0].message.split('\n')
                flToWear = ''
                for b in range(len(bSpl)):
                    if bSpl[b].startswith('🔦 Фонарик ﴾100'):
                        flToWear = b+1
                        break
                await client.send_message(game,bSpl[flToWear])
                await asyncio.sleep(1)
                await client.send_message(game,'/flashlight')
                await asyncio.sleep(1)
                m = await client.get_messages(game, limit=1)
                await m[0].click(1)
                await asyncio.sleep(1)
                await m[0].click(0)
                await asyncio.sleep(2)
            await client.send_message(game,'👾 Поиск монстров')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'Недостаточно энергии' in m[0].message:
            await client.send_message(chatControl,'Недостаточно энергии, ждем')
            notEnoughNRG = True
        elif 'отсутствует в рюкзаке' in m[0].message:
            await client.send_message(chatControl,m[0].message+'\n\n.leader __NICKNAME__, чтоб сменить лидера')
        elif 'Необходимо выполнить захват' in m[0].message:
            isLocked = False
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'🗣 Управление')
            await asyncio.sleep(0.5)
            await client.send_message(game,'🏃 Движение')
            await asyncio.sleep(0.5)
            await client.send_message(game,'💢 Включить захват')
            while isLocked == False:
                await asyncio.sleep(0.5)
                m = await client.get_messages(game, limit=2)
                if m[0].message.startswith('❗️Указанные игроки находятся не рядом'):
                    isLocked = True
                    await client.send_message(chatControl,m[0].message)
                elif 'Захват группы включен' in m[1].message:
                    isLocked = True
                    await asyncio.sleep(0.5)
                    await client.send_message(game,'/buttons')
                    await asyncio.sleep(1)
                    await client.send_message(game,run)
    if messag == '.run' and almostRun == False and PL == True and chatControl == fromChat:
        await client.send_message(game,'/buttons')
        almostRun = True
        await asyncio.sleep(1)
        if state == 'dg 36-40':
            run = '🥀 Белорусский вокзал (36-40)'
        elif state == 'dg 41-45':
            run = '🥀 Аптекарский огород (41-45)'
        elif state == 'dg 46-50':
            run = '🥀 Площадь трёх вокзалов (46-50)'
        elif state == 'boss':
            run = '🦪 Использовать приманку'
        elif state == 'm2' or state == 'farm':
            run = '👾 Поиск монстров'
            if toLockParty == True and state == 'm2':
                isLocked = False
                await client.send_message(game,'/group')
                await asyncio.sleep(0.5)
                await client.send_message(game,'🗣 Управление')
                await asyncio.sleep(0.5)
                await client.send_message(game,'🏃 Движение')
                await asyncio.sleep(0.5)
                await client.send_message(game,'💢 Включить захват')
                while isLocked == False:
                    await asyncio.sleep(0.5)
                    m = await client.get_messages(game, limit=2)
                    if m[0].message.startswith('❗️Указанные игроки находятся не рядом'):
                        isLocked = True
                        await client.send_message(chatControl,m[0].message)
                    elif 'Захват группы включен' in m[1].message:
                        isLocked = True
                        toLockParty = False
                        await asyncio.sleep(0.5)
                        await client.send_message(game,'/buttons')
                        await asyncio.sleep(1)
                        await client.send_message(game,run)
        if state.startswith('dg'):
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'👥 Состав')
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            splitGroup = m[0].message.split('[1')[1].split('\n')
            plToAdr = ''
            for x in range(len(splitGroup)):
                if '[👑] ' in splitGroup[x]:
                    plToAdr = plToAdr + splitGroup[x].split('[👑] ')[1].split(' (')[0] + ' '
                else:
                    plToAdr = plToAdr + splitGroup[x].split('] ')[1].split(' (')[0] + ' '
            if plToAdr != '':
                await client.send_message(chatControl,'.tea '+plToAdr)
            await asyncio.sleep(0.5)
            await client.send_message(game,'/buttons')
            await asyncio.sleep(5)
        await client.send_message(game,run)
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'Выберите сложность ' in m[0].message:
            await m[0].click(hardMode)
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            await m[0].click(text='✅ Подтвердить')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'Монстров нет' in m[0].message:
            await client.send_message(game,'/flashlight')
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            await m[0].click(0)
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            if 'Запас прочности слишком мал' in m[0].message:
                await m[0].click(1)
                await asyncio.sleep(1)
                await client.send_message(game,'🎒 Рюкзак')
                await asyncio.sleep(1)
                m = await client.get_messages(game, limit=1)
                bSpl = m[0].message.split('\n')
                flToWear = ''
                for b in range(len(bSpl)):
                    if bSpl[b].startswith('🔦 Фонарик ﴾100'):
                        flToWear = b+1
                        break
                await client.send_message(game,bSpl[flToWear])
                await asyncio.sleep(1)
                await client.send_message(game,'/flashlight')
                await asyncio.sleep(1)
                m = await client.get_messages(game, limit=1)
                await m[0].click(1)
                await asyncio.sleep(1)
                await m[0].click(0)
                await asyncio.sleep(2)
            await client.send_message(game,'👾 Поиск монстров')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'Недостаточно энергии' in m[0].message:
            almostRun = False
            await event.message.reply('Недостаточно энергии, ждем')
            notEnoughNRG = True
        elif 'отсутствует в рюкзаке' in m[0].message:
            almostRun = False
            await event.message.reply(m[0].message+'\n\n.leader __NICKNAME__, чтоб сменить лидера')
        elif 'Необходимо выполнить захват' in m[0].message:
            isLocked = False
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'🗣 Управление')
            await asyncio.sleep(0.5)
            await client.send_message(game,'🏃 Движение')
            await asyncio.sleep(0.5)
            await client.send_message(game,'💢 Включить захват')
            while isLocked == False:
                await asyncio.sleep(0.8)
                m = await client.get_messages(game, limit=2)
                if m[0].message.startswith('❗️Указанные игроки находятся не рядом'):
                    isLocked = True
                    almostRun = False
                    await event.message.reply(m[0].message)
                elif 'Захват группы включен' in m[1].message:
                    isLocked = True
                    await asyncio.sleep(0.5)
                    await client.send_message(game,'/buttons')
                    await asyncio.sleep(1)
                    await client.send_message(game,run)
    # <==============================================================================================GO
    if messag.startswith('.go') and sender == me and fromChat == me.id and state == 'none':
        if imhere == '':
            await client.send_message(me, 'Идет получение изначального местоположения, ожидай...\nЭто разовое действие после запуска скрипта, далее местоположение будет обновляться само.')
            await client.send_message(game,'/fraction')
            await asyncio.sleep(1)
            await client.send_message(game,'📃 Состав')
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=2)
            # print(event)
            # print(m[0].message)
            for s in range(len(m)):
                sostavArr = m[s].message.split('\n')
                for i in range(len(sostavArr)):
                    if nick in sostavArr[i]:
                        # print(sostavArr[i])
                        imhere = sostavArr[i].split(' 🗺')[1].split(' ☑️')[0].split(' ✅')[0]
                        break
            await asyncio.sleep(random.randint(1,3))
            await client.send_message(game,'⬅️ Назад')
        if imhere != '':
            if messag == '.go':
                listing = 'Выбери номер станции, куда ты хочешь отправиться\nCейчас ты находишься тут: **'+imhere+'**\n'
                for x in range(len(stationNames)):
                    if x == 0: listing += '\n**🟩🟩🟩🟩ЗЕЛЕНАЯ🟩🟩🟩🟩**\n'
                    elif x == 6: listing += '\n**⬜️⬜️⬜️⬜️СЕРАЯ⬜️⬜️⬜️⬜️**\n'
                    elif x == 12: listing += '\n**🧩🧩🧩🧩САЛАТОВАЯ🧩🧩🧩🧩**\n'
                    elif x == 16: listing += '\n**🟧🟧🟧🟧ОРАНЖЕВАЯ🟧🟧🟧🟧**\n'
                    elif x == 22: listing += '\n**🟥🟥🟥🟥КРАСНАЯ🟥🟥🟥🟥**\n'
                    elif x == 30: listing += '\n**🟦🟦🟦🟦СИНЯЯ🟦🟦🟦🟦**\n'
                    elif x == 35: listing += '\n**🟪🟪🟪🟪ФИОЛЕТОВАЯ🟪🟪🟪🟪**\n'
                    elif x == 40: listing += '\n**🟨🟨🟨🟨ЖЕЛТАЯ🟨🟨🟨🟨**\n'
                    elif x == 42: listing += '\n**🗳🗳🗳🗳ГОЛУБАЯ🗳🗳🗳🗳**\n'
                    elif x == 46: listing += '\n**🟫🟫🟫🟫КОЛЬЦЕВАЯ🟫🟫🟫🟫**\n'
                    listing += str(x) + '. ' + stationNames[x]+' — `.go '+str(x)+'`\n'
                await client.send_message(me, listing)
            else:
                destination = int(messag.split('.go ')[1])
                # startPoint = stationNames.index(imhere)
                gpsTrack = gps(imhere,destination)
                # print(gpsTrack)
                waypointMsg = 'Направляемся из **'+imhere+'** на станцию **'+stationNames[destination]+'**\n\nМаршрут:\n'
                nrgRaw = gpsTrack["nrg"]
                nrgLeft = nrgRaw % 5
                nrg = nrgRaw - nrgLeft
                pathStr = ''
                for p in range(len(gpsTrack["path"])):
                    path_type = ''
                    if p in range(len(gpsTrack["pathType"])):
                        if gpsTrack["pathType"][p] == 1:
                            path_type = '[🚥 Переход] '
                        else:
                            path_type = '[🍙 Туннель] '
                    pathStr += stationNames[gpsTrack["path"][p]] + '\n'+path_type
                waypointMsg += pathStr+'\n\nТрата энергии: '+str(nrg)
                await client.send_message(me, waypointMsg)
                state = 'walking'
                if '-' in imhere:
                    print('two stations')
                else:
                    for i in range(len(gpsTrack['path'])):
                        nextStation = gpsTrack['path'][i]
                        nxStName = stationNames[nextStation]
                        if nxStName == imhere:
                            continue
                        else:
                            #print(imhere)
                            #print(nxStName)
                            await client.send_message(game, '🏃 Покинуть станцию')
                            await asyncio.sleep(random.randint(1,2))
                            if gpsTrack['pathType'][i-1] > 5:
                                await client.send_message(game, '🍙 Туннель')
                            else:
                                await client.send_message(game, '🚥 Переход')
                            await asyncio.sleep(random.randint(1,2))
                            m = await client.get_messages(game, limit=1)
                            buttonsDir = m[0].reply_markup
                            for r in range(len(buttonsDir.rows)):
                                buttonsInRow = buttonsDir.rows[r].buttons
                                for b in range(len(buttonsInRow)):
                                    if stationNames[nextStation] in buttonsInRow[b].text:
                                        await asyncio.sleep(random.randint(1,2))
                                        await m[0].click(text=buttonsInRow[b].text)
                                        await asyncio.sleep(random.randint(1,2))
                            m = await client.get_messages(game, limit=1)
                            while (nxStName+'\n\n🚸 Статус: ') not in m[0].message:
                                if 'Станция отправления:' in m[0].message:
                                    await client.send_message(game, '➡️ Вперёд на '+nxStName)
                                await asyncio.sleep(random.randint(1,2))
                                m = await client.get_messages(game, limit=1)
                    await client.send_message(me, 'Ты дошел до конечной локации')
                    state = 'none'
        else:
            await client.send_message(me, 'Ты не найден в составе фракции')
    if messag.startswith('.stop') and sender == me and fromChat == me.id and state != 'none':
        if state == 'm2':
            txt = ('**Проведено боёв в М2:** '+str(m2Fights)
                   + '\n**Найдено Чёрных Детёнышей:** '+str(m2Babies)+' из '+str(m2Targets)+' мобов __('+str("{:0.2f}".format((m2Babies/m2Targets)*100))+'%)__'
                   +'\n**Получено частей пропуска Д-6:** '+str(m2Tickets)+' __('+str("{:0.2f}".format((m2Tickets/m2Babies)*100))+'%)__')
            await event.message.reply(txt)
            m2Fights = 0
            m2Babies = 0
            m2Targets = 0
            m2Tickets = 0
        state = 'none'
        await client.send_message(me, 'Бот запущен')

client.start()
me = client.get_me()
client.send_message(me, 'Бот запущен')
client.send_message(game, '/character')
client.run_until_disconnected()