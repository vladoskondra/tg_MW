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
from script.config import game_cfg
from script.modules.gps.gpsGo import gps, station_Names
import re
from operator import itemgetter, attrgetter

api_id = 4889182
api_hash = "38ea074a004c2927bddf31c96f9c03e0"
game = game_cfg()[0]
gameId = game_cfg()[1]
client = TelegramClient('MW_bot', api_id, api_hash)
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
weapon = '๐ง[๐โ๐จ]MM TAC-50 ะกะปะฐะฒั โข (๐ธ+8) ๐ฆ[๐โ๐จ]['
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
        if 'ะัะตะดะผะตั ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' in m[0].message:
            await asyncio.sleep(1)
            await client.send_message(game,'/use_Food21')
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            if 'ะัะตะดะผะตั ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' in m[0].message:
                teaUse = False
        await asyncio.sleep(1)
        m = await client.get_messages(game, limit=1)
        if teaUse == True and 'ะัะตะดะผะตั ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in m[0].message and 'ัะฐะน' in m[0].message and 'ัะฒะตะปะธัะธะฒะฐะตั ัะฐัะฐะบัะตัะธััะธะบะธ ะฟะตััะพะฝะฐะถะฐ' in m[0].message:
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
                if 'ะะดัะตะฝะฐะปะธะฝ' in buttonsInRow[b].text:
                    adrText = buttonsInRow[b].text
        if adrText == '':
            event.message.reply('ะฃ ะผะตะฝั ะทะฐะบะพะฝัะธะปัั ะะดัะตะฝะฐะปะธะฝ')
        else:
            await m[0].click(text=adrText)
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            buttonsDir = m[0].reply_markup
            for r in range(len(buttonsDir.rows)):
                buttonsInRow = buttonsDir.rows[r].buttons
                for b in range(len(buttonsInRow)):
                    partStatus = buttonsInRow[b].text
                    if 'ะะฐะทะฐะด' not in partStatus and int(re.findall('[0-9]+', partStatus)[0]) < 31:
                        await m[0].click(text=partStatus)
                        await asyncio.sleep(0.8)
    if messag.startswith('.hardmode') and fromChat == me.id:
        hardMode = int(messag.split(' ')[1]) -1
    if messag.startswith('.auto') and fromChat == me.id:
        if AutoFight == False:
            AutoFight = True
            await client.send_message(me, 'ะ?ะตะถะธะผ ะะฒัะพะฑะพะน ะฒะบะปััะตะฝ')
        else:
            AutoFight = False
            await client.send_message(me, 'ะ?ะตะถะธะผ ะะฒัะพะฑะพะน ะฒัะบะปััะตะฝ')
    if messag.startswith('.broke') and fromChat == me.id and state == 'none':
        state = 'broke'
        mod = int(messag.split(' ')[1]) - 1
        await client.send_message(game,'๐ค ะัะฑัะฐัั ะฟัะตะดะผะตั')
        await asyncio.sleep(1)
        m = await client.get_messages(game, limit=1)
        await m[0].click(mod)
    if 'ะะพะฑะฐะฒััะต ะฟัะตะดะผะตั' in messag and fromChat == gameId and state == 'broke':
        await asyncio.sleep(1.5)
        m = await client.get_messages(game, limit=1)
        await m[0].click(0)
        await asyncio.sleep(1.5)
        m = await client.get_messages(game, limit=1)
        fin = m[0].message
        while 'ะะพัััะฟะฝะฐั' not in fin and 'ะะตะดะพััะฐัะพัะฝะพ ััะตะดััะฒ' not in fin and state == 'broke':
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
            txt = ('**ะัะพะฒะตะดะตะฝะพ ะฑะพัะฒ ะฒ ะ2:** '+str(m2Fights)
                   + '\n**ะะฐะนะดะตะฝะพ ะงััะฝัั ะะตััะฝััะตะน:** '+str(m2Babies)+' ะธะท '+str(m2Targets)+' ะผะพะฑะพะฒ __('+str("{:0.2f}".format((m2Babies/m2Targets)*100))+'%)__'
                   +'\n**ะะพะปััะตะฝะพ ัะฐััะตะน ะฟัะพะฟััะบะฐ ะ-6:** '+str(m2Tickets)+' __('+str("{:0.2f}".format((m2Tickets/m2Babies)*100))+'%)__'
                   +'\n\n๐ณ๐ตั.1 ะฟัะพะฟััะบะฐ ะ-6 โ'+str(m2Ticket1)+'\n๐ณ๐ตั.2 ะฟัะพะฟััะบะฐ ะ-6 โ'+str(m2Ticket2)+'\n๐ณ๐ตั.3 ะฟัะพะฟััะบะฐ ะ-6 โ'+str(m2Ticket3))
            await event.message.reply(txt)
    if messag.startswith('.synt ') and fromChat == me.id and state == 'none':
        state = 'synt'
        mod = int(messag.split(' ')[1])
        print(mod)
        await client.send_message(game,'๐ค ะัะฑัะฐัั ะฟัะตะดะผะตั')
    if 'ะะพะฑะฐะฒััะต ะฟะตัะฒัะน ะผะพะดัะปั' in messag and fromChat == gameId and state == 'synt' and mod > 0:
        print(mod)
        await asyncio.sleep(1)
        m = await client.get_messages(game, limit=1)
        await m[0].click(mod-1)
        await asyncio.sleep(1)
        m = await client.get_messages(game, limit=1)
        fin = m[0].message
        if 'ะะพัััะฟะฝัะต ะดะปั ัะธะฝัะตะทะฐ ะผะพะดัะปะธ ะพััััััะฒััั' not in fin:
            m = await client.get_messages(game, limit=1)
            await asyncio.sleep(1)
            await m[0].click(0)
            m = await client.get_messages(game, limit=1)
            await asyncio.sleep(1)
            await m[0].click(0)
            m = await client.get_messages(game, limit=1)
            await asyncio.sleep(1)
            await client.send_message(game,'๐ค ะัะฑัะฐัั ะฟัะตะดะผะตั')
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
            while 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin and 'ะ?ัะบะทะฐะบ ะฟะตัะตะฟะพะปะฝะตะฝ' not in fin and state == 'open':
                await asyncio.sleep(1.5)
                await client.send_message(game,'/use_ClothesBoxIV')
                await asyncio.sleep(1)
                m = await client.get_messages(game, limit=1)
                fin = m[0].message
                if 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin:
                    await asyncio.sleep(1)
                    await event.message.click(0)
                    await asyncio.sleep(1)
                    await event.message.click(0)
                    m = await client.get_messages(game, limit=1)
                    fin = m[0].message
            state = 'none'
    if state == 'box' and 'ะ?ัะบะทะฐะบ ('+nick+')\n\nะัะพัะตะต' in messag and fromChat == gameId:
        baglines = messag.split('\n')
        for x in range(len(baglines)):
            if '๐ ะะฐะณัะฐะดะฐ (36-40)' in baglines[x]:
                state = 'open'
                fin = ''
                while 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin and state == 'open':
                    await asyncio.sleep(1.5)
                    await client.send_message(game,'/use_DangeRewardII')
                    await asyncio.sleep(1)
                    m = await client.get_messages(game, limit=1)
                    fin = m[0].message
                    if 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin:
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        m = await client.get_messages(game, limit=1)
                        fin = m[0].message
                state = 'none'
                await asyncio.sleep(1)
                await client.send_message(game,'/other')
            elif '๐ ะะฐะณัะฐะดะฐ (41-45)' in baglines[x]:
                state = 'open'
                fin = ''
                while 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin and state == 'open':
                    await asyncio.sleep(1.5)
                    await client.send_message(game,'/use_DangeRewardIII')
                    await asyncio.sleep(1)
                    m = await client.get_messages(game, limit=1)
                    fin = m[0].message
                    if 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin:
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        m = await client.get_messages(game, limit=1)
                        fin = m[0].message
                state = 'none'
                await asyncio.sleep(1)
                await client.send_message(game,'/other')
            elif 'ะะฐะณัะฐะดะฐ (46-50)' in baglines[x]:
                state = 'open'
                fin = ''
                while 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin and state == 'open':
                    await asyncio.sleep(1.5)
                    await client.send_message(game,'/use_DangeRewardIV')
                    m = await client.get_messages(game,limit=1)
                    fin = m[0].message
                    if 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin:
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        m= await client.get_messages(game,limit=1)
                        fin = m[0].message
                state = 'none'
                await asyncio.sleep(1)
                await client.send_message(game,'/other')
            elif 'ะะพัะพะฑะบะฐ ัะตััััะพะฒ' in baglines[x]:
                fin = ''
                state = 'open'
                while 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin and state == 'open':
                    await asyncio.sleep(1.5)
                    await client.send_message(game,'/use_ResourcesBoxV')
                    await asyncio.sleep(1)
                    m = await client.get_messages(game,limit=1)
                    fin = m[0].message
                    if 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin:
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        m = await client.get_messages(game,limit=1)
                        fin = m[0].message
                state = 'none'
                await asyncio.sleep(1)
                await client.send_message(game,'/other')
            elif baglines[x].startswith('๐ณ ะะพัะพะฑะบะฐ ะพััะถะธั'):
                fin = ''
                state = 'open'
                while 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin and state == 'open':
                    await asyncio.sleep(1.5)
                    await client.send_message(game,'/use_WeaponBoxIV')
                    await asyncio.sleep(1)
                    m = await client.get_messages(game, limit=1)
                    fin = m[0].message
                    if 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin:
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        m = await client.get_messages(game, limit=1)
                        fin = m[0].message
                state = 'none'
                await asyncio.sleep(1)
                await client.send_message(game,'/other')
            elif ('ะะพัะพะฑะบะฐ ะฑัะพะฝะธ') in baglines[x] and state == 'open':
                fin = ''
                state = 'open'
                while 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin:
                    await asyncio.sleep(1.5)
                    await client.send_message(game,'/use_ClothesBoxIV')
                    await asyncio.sleep(1)
                    m = await client.get_messages(game, limit=1)
                    fin = m[0].message
                    if 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' not in fin:
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        await asyncio.sleep(1)
                        await event.message.click(0)
                        m = await client.get_messages(game, limit=1)
                        fin = m[0].message
                state = 'none'
                await asyncio.sleep(1)
                await client.send_message(game,'/other')
    if messag.startswith('๐ฐ ะะตััะพะฝะฐะถ\n\n๐ID: '+str(me.id)) and fromChat == gameId:
        personaj = messag.split('\n')
        nick = personaj[3].split('ะะธะบ: ')[1].split(' /a')[0]
        prof = personaj[5].split('ะะปะฐัั: ')[1]
        energy = int(personaj[10].split('๐ะญะฝะตัะณะธั: ')[1].split('/')[0])
    # print(nick,prof,energy)
    if 'ะั ะฑัะดะตัะต ะฟะตัะตะฝะฐะฟัะฐะฒะปะตะฝั ะฝะฐ ะพัะธัะธะฐะปัะฝัะน ัะฐะนั ะฝะฐัะตะณะพ ะฟัะพะตะบัะฐ' in messag and (fromChat == gameId or fromChat == me.id):
        entities = event.message.entities
        for ent in entities:
            if isinstance(ent, MessageEntityTextUrl):
                if "captcha.metro-wars.online/?id=" in ent.url:
                    sleep(randint(3, 6))
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
                    try:
                        r = requests.get(ent.url, headers=headers)
                    except:
                        print('ะะฐะฟัะฐ ะฟัะพะนะดะตะฝะฐ')
                        sleep(randint(2, 5))
                        await client.send_message(game, '/start')
    if '๐ธ ะกัะฐััั: ' in messag and fromChat == gameId:
        if 'โค๏ธ' in messag.split('\n')[0]:
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
        await event.message.reply('ะะฒัะพะทะฐะฟััะบ ะฒะบะปััะตะฝ')
    if messag == '.autorun off' and PL == True and chatControl == fromChat:
        AutoRun = False
        await event.message.reply('ะะฒัะพะทะฐะฟััะบ ะฒัะบะปััะตะฝ')
    if messag.startswith('.leader ') and PL == True:
        swapToLeader = messag.split('leader ')[1]
        leaderChanged = False
        while leaderChanged == False:
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ฃ ะฃะฟัะฐะฒะปะตะฝะธะต')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ ะะธะดะตัััะฒะพ')
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
                        if 'ะัะตะดะปะพะถะตะฝะธะต ะพ ะฟะตัะตะดะฐัะต ะปะธะดะตัะฐ ะณััะฟะฟั ะพัะฟัะฐะฒะปะตะฝะพ' in m[1].message:
                            leaderChanged = True
                            PL = False
                            await event.message.reply('ะัะธะฝะธะผะฐะน ะปะธะดะตัะบั')
    if messag.startswith('.dg') and sender == me and fromChat == me.id and state == 'none':
        state = messag.split('.')[1]
    if (messag.startswith('๐ ะะฐะณัะฐะดะฐ ') or messag.startswith('๐ณ ะะพัะพะฑะบะฐ ')) and fromChat == gameId:
        await asyncio.sleep(1)
        await event.message.click(0)
    if messag == '.get' and fromChat == me.id:
        if AutoGet == True:
            AutoGet = False
            await client.send_message(me, 'ะะฒัะพะฟะพะปััะตะฝะธะต ะฒัะบะปััะตะฝะพ')
        else:
            AutoGet = True
            await client.send_message(me, 'ะะฒัะพะฟะพะปััะตะฝะธะต ะฒะบะปััะตะฝะพ')
    if messag.startswith( '๐ฅ ะะพะปััะธัะต ะฟัะตะดะผะตัั:') and fromChat == gameId and AutoGet == True:
        await asyncio.sleep(1)
        await event.message.click(0)
    if PL == True and 'ัะพัะตั ะฒัััะฟะธัั ะฒ ะณััะฟะฟั' in messag and fromChat == gameId:
        await asyncio.sleep(random.randint(1,3))
        await event.message.click(0)
    if PL == False and 'ะัะตะดะปะพะถะตะฝะธะต ะพ ะฟะตัะตะดะฐัะต ะปะธะดะตัะฐ ะณััะฟะฟั' in messag and fromChat == gameId:
        await asyncio.sleep(random.randint(1,3))
        await event.message.click(0)
        PL = True
    if messag == '.lock' and PL == True:
        await client.send_message(game,'/group')
        await asyncio.sleep(0.5)
        await client.send_message(game,'๐ฃ ะฃะฟัะฐะฒะปะตะฝะธะต')
        await asyncio.sleep(0.5)
        await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
        await asyncio.sleep(0.5)
        await client.send_message(game,'๐ข ะะบะปััะธัั ะทะฐัะฒะฐั')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=2)
        if m[0].message.startswith('โ๏ธะฃะบะฐะทะฐะฝะฝัะต ะธะณัะพะบะธ ะฝะฐัะพะดัััั ะฝะต ััะดะพะผ'):
            await event.message.reply(m[0].message)
        elif m[0].message == 'ะะตะธะทะฒะตััะฝะฐั ะบะพะผะฐะฝะดะฐ':
            await event.message.reply('ะัะธะฑะบะฐ, ะฟะพะฒัะพัะธ ะตัะต ัะฐะท')
        elif 'ะะฐัะฒะฐั ะณััะฟะฟั ะฒะบะปััะตะฝ' in m[1].message:
            await asyncio.sleep(0.5)
            await event.message.reply('ะะฐัะฒะฐั ะฒัะฟะพะปะฝะตะฝ')
        await asyncio.sleep(1)
        await client.send_message(game,'/buttons')
    if ('...ะฒั ะพัะฟัะฐะฒะปัะตัะตัั ะฝะฐ ะทะฐะฑัะพัะตะฝะฝัั ัะตััะธัะพัะธั' in messag or '...ะฟะตัะตัะพะด ะฒ ัะปะตะดััััั ะบะพะผะฝะฐัั' in messag) and fromChat == gameId and state.startswith('dg'):
        almostRun = False
        stepBack = 0
        trap_cd = False
        rico_cd = False
        knockback_cd = False
        needsReload = False
        await asyncio.sleep(10)
        m = await client.get_messages(game, limit=1)
        if '[B]' in m[0].message:
            await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
            await asyncio.sleep(2)
            await client.send_message(game,'โ๏ธ ะะพ ะฝะฐะฟัะฐะฒะปะตะฝะธั')
            await asyncio.sleep(2)
            await client.send_message(game,'โฌ')
        else:
            isAutoFightButton = m[0].reply_markup
            if len(isAutoFightButton.rows)>1:
                if '[B]' not in messag and isAutoFightButton.rows[3].buttons[0].text.startswith('โป๏ธ ะะฒัะพะฑะพะน'):
                    await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
    elif weapon in messag and 'ะัะฑะตัะธัะต ัะตะปั' not in messag and fromChat == gameId and state.startswith('dg'):
        m = await client.get_messages(game, limit=1)
        isAutoFightButton = m[0].reply_markup
        if len(isAutoFightButton.rows)>1:
            if '[B]' not in messag and isAutoFightButton.rows[3].buttons[0].text.startswith('โป๏ธ ะะฒัะพะฑะพะน'):
                await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
            elif '[B]' in messag and isAutoFightButton.rows[3].buttons[0].text.startswith('โป๏ธ ะะฒัะพะฑะพะน') and AutoFight == True:
                await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
            elif '[B]' in messag and isAutoFightButton.rows[3].buttons[0].text.startswith('โป๏ธ ะะฒัะพะฑะพะน') and AutoFight == False:
                if 'โฑ ะะพัััะฟะฝะพ - โด ะ?ะธะบะพัะตั' in messag:
                    rico_cd = False
                if 'โฑ ะะพัััะฟะฝะพ - ๐ฒ ะะพะฒััะบะฐ' in messag:
                    trap_cd = False
                if 'โฑ ะะพัััะฟะฝะพ - ๐ ะัะฑัะพั' in messag:
                    knockback_cd = False
                if messag.split(weapon)[1].split('/')[0] == '0':
                    needsReload = True
                if trap_cd == False:
                    await asyncio.sleep(3)
                    await client.send_message(game,'๐ ะฃะผะตะฝะธั')
                    await asyncio.sleep(2)
                    await client.send_message(game,'๐ฒ ะะพะฒััะบะฐ')
                    await asyncio.sleep(2)
                    await client.send_message(game,'โน ะ ะพะฑัะตะบัั')
                    await asyncio.sleep(1)
                    target = await client.get_messages(game, limit=1)
                    await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                    await asyncio.sleep(2)
                    await client.send_message(game,'โ ะะพะดัะฒะตัะดะธัั')
                    trap_cd = True
                elif needsReload == True:
                    await asyncio.sleep(3)
                    await client.send_message(game,'๐ ะะตัะตะทะฐััะดะบะฐ')
                    needsReload = False
                elif rico_cd == False:
                    await asyncio.sleep(3)
                    await client.send_message(game,'๐ ะฃะผะตะฝะธั')
                    await asyncio.sleep(2)
                    await client.send_message(game,'โด ะ?ะธะบะพัะตั')
                    await asyncio.sleep(1)
                    target = await client.get_messages(game, limit=1)
                    await asyncio.sleep(2)
                    await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                    rico_cd = True
                elif knockback_cd == False:
                    await asyncio.sleep(3)
                    await client.send_message(game,'๐ ะฃะผะตะฝะธั')
                    await asyncio.sleep(2)
                    await client.send_message(game,'๐ ะัะฑัะพั')
                    await asyncio.sleep(2)
                    await client.send_message(game,'โน ะ ะพะฑัะตะบัั')
                    await asyncio.sleep(1)
                    target = await client.get_messages(game, limit=1)
                    await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                    await asyncio.sleep(2)
                    await client.send_message(game,'โ ะะพะดัะฒะตัะดะธัั')
                    knockback_cd = True
                else:
                    await asyncio.sleep(3)
                    await client.send_message(game,'โ๏ธ ะัะฐะบะฐ')
                    await asyncio.sleep(1)
                    target = await client.get_messages(game, limit=1)
                    await asyncio.sleep(2)
                    await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
    # <============================================================================================BOSS
    if messag.startswith('.boss') and sender == me and fromChat == me.id and state == 'none':
        state = 'boss'
        await client.send_message(me, 'ะ?ะตะถะธะผ ะะพััั ะฒะบะปััะตะฝ')
    if messag.startswith('โะะฐ ะฒะฐั ะฝะฐะฟะฐะดะฐะตั ') and fromChat == gameId and state == 'boss':
        stepBack = 0
        almostRun = False
        trap_cd = False
        rico_cd = False
        knockback_cd = False
        await asyncio.sleep(7)
        if 'ะัะฐัะฝะฐ' in messag:
            await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
            await asyncio.sleep(2)
            await client.send_message(game,'โ๏ธ ะะตัะตะถะดะฐัั')
            stepBack = stepBack + 1
        else:
            await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
            await asyncio.sleep(2)
            await client.send_message(game,'โ๏ธ ะะพ ะฝะฐะฟัะฐะฒะปะตะฝะธั')
            await asyncio.sleep(2)
            await client.send_message(game,'โ')
            stepBack = 4
    elif weapon in messag and 'ะัะฑะตัะธัะต ัะตะปั' not in messag and fromChat == gameId and state == 'boss':
        if stepBack == 1:
            await asyncio.sleep(2)
            await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
            await asyncio.sleep(2)
            await client.send_message(game,'โ๏ธ ะะพ ะฝะฐะฟัะฐะฒะปะตะฝะธั')
            await asyncio.sleep(2)
            await client.send_message(game,'โก')
            stepBack = stepBack + 1
        elif stepBack == 2:
            await asyncio.sleep(2)
            await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
            await asyncio.sleep(2)
            await client.send_message(game,'โ๏ธ ะะพ ะฝะฐะฟัะฐะฒะปะตะฝะธั')
            await asyncio.sleep(2)
            await client.send_message(game,'โฌ')
            stepBack = stepBack + 1
        elif stepBack == 3:
            await asyncio.sleep(3)
            await client.send_message(game,'โ๏ธ ะัะฐะบะฐ')
            await asyncio.sleep(1)
            target = await client.get_messages(game, limit=1)
            await asyncio.sleep(2)
            await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
            stepBack = 4
        elif stepBack == 4:
            if 'โฑ ะะพัััะฟะฝะพ - โด ะ?ะธะบะพัะตั' in messag:
                rico_cd = False
            if 'โฑ ะะพัััะฟะฝะพ - ๐ฒ ะะพะฒััะบะฐ' in messag:
                trap_cd = False
            if 'โฑ ะะพัััะฟะฝะพ - ๐ ะัะฑัะพั' in messag:
                knockback_cd = False
            if trap_cd == False:
                await asyncio.sleep(3)
                await client.send_message(game,'๐ ะฃะผะตะฝะธั')
                await asyncio.sleep(2)
                await client.send_message(game,'๐ฒ ะะพะฒััะบะฐ')
                await asyncio.sleep(2)
                await client.send_message(game,'โน ะ ะพะฑัะตะบัั')
                await asyncio.sleep(1)
                target = await client.get_messages(game, limit=1)
                await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                await asyncio.sleep(2)
                await client.send_message(game,'โ ะะพะดัะฒะตัะดะธัั')
                trap_cd = True
            elif '0/3]' in messag.split(weapon)[1]:
                await asyncio.sleep(3)
                await client.send_message(game,'๐ ะะตัะตะทะฐััะดะบะฐ')
            elif rico_cd == False:
                await asyncio.sleep(3)
                await client.send_message(game,'๐ ะฃะผะตะฝะธั')
                await asyncio.sleep(2)
                await client.send_message(game,'โด ะ?ะธะบะพัะตั')
                await asyncio.sleep(1)
                target = await client.get_messages(game, limit=1)
                await asyncio.sleep(2)
                await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                rico_cd = True
            elif knockback_cd == False:
                await asyncio.sleep(3)
                await client.send_message(game,'๐ ะฃะผะตะฝะธั')
                await asyncio.sleep(2)
                await client.send_message(game,'๐ ะัะฑัะพั')
                await asyncio.sleep(2)
                await client.send_message(game,'โน ะ ะพะฑัะตะบัั')
                await asyncio.sleep(1)
                target = await client.get_messages(game, limit=1)
                await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                await asyncio.sleep(2)
                await client.send_message(game,'โ ะะพะดัะฒะตัะดะธัั')
                knockback_cd = True
            else:
                await asyncio.sleep(3)
                await client.send_message(game,'โ๏ธ ะัะฐะบะฐ')
                await asyncio.sleep(1)
                target = await client.get_messages(game, limit=1)
                await asyncio.sleep(2)
                await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)

    # <============================================================================================M2
    if messag.startswith('.m2') and sender == me and fromChat == me.id and state == 'none':
        state = 'm2'
        await client.send_message(me, 'ะ?ะตะถะธะผ M2 ะฒะบะปััะตะฝ')
    if ('ะั ะฝะฐะฟะฐะดะฐะตัะต ะฝะฐ' in messag or 'ะะฐ ะฒะฐั ะฝะฐะฟะฐะดะฐัั:' in messag) and fromChat == gameId and state == 'm2':
        m2Fights = m2Fights + 1
        targets = messag.split('ะั ะฝะฐะฟะฐะดะฐะตัะต ะฝะฐ\n\n')[1].split('\n\nะพะถะธะดะฐะนัะต')[0]
        babySpl = targets.split('\n')
        for baby in range(len(babySpl)):
            m2Targets = m2Targets + 1
            if 'ะงััะฝัะน ะะตััะฝัั' in babySpl[baby]:
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
                if isAutoFightButton.rows[3].buttons[0].text.startswith('โป๏ธ ะะฒัะพะฑะพะน'):
                    await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
        else:
            await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
            await asyncio.sleep(2)
            await client.send_message(game,'โ๏ธ ะะพ ะฝะฐะฟัะฐะฒะปะตะฝะธั')
            await asyncio.sleep(2)
            await client.send_message(game,'โฌ')
            stepBack = 2
    elif weapon in messag and 'ะัะฑะตัะธัะต ัะตะปั' not in messag and fromChat == gameId and state.startswith('m2'):
        m = await client.get_messages(game, limit=1)
        isAutoFightButton = m[0].reply_markup
        if len(isAutoFightButton.rows)>1:
            if AutoFight == True and isAutoFightButton.rows[3].buttons[0].text.startswith('โป๏ธ ะะฒัะพะฑะพะน'):
                await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
            elif AutoFight == False and isAutoFightButton.rows[3].buttons[0].text.startswith('โป๏ธ ะะฒัะพะฑะพะน'):
                if stepBack == 1:
                    await asyncio.sleep(3)
                    await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
                    await asyncio.sleep(2)
                    await client.send_message(game,'โ๏ธ ะะพ ะฝะฐะฟัะฐะฒะปะตะฝะธั')
                    await asyncio.sleep(2)
                    await client.send_message(game,'โฌ')
                    stepBack = 2
                elif stepBack == 2:
                    if 'โฑ ะะพัััะฟะฝะพ - โด ะ?ะธะบะพัะตั' in messag:
                        rico_cd = False
                    if 'โฑ ะะพัััะฟะฝะพ - ๐ฒ ะะพะฒััะบะฐ' in messag:
                        trap_cd = False
                    if 'โฑ ะะพัััะฟะฝะพ - ๐ ะัะฑัะพั' in messag:
                        knockback_cd = False
                    if messag.split(weapon)[1].split('/')[0] == '0':
                        needsReload = True
                    if trap_cd == False:
                        await asyncio.sleep(3)
                        await client.send_message(game,'๐ ะฃะผะตะฝะธั')
                        await asyncio.sleep(2)
                        await client.send_message(game,'๐ฒ ะะพะฒััะบะฐ')
                        await asyncio.sleep(1)
                        await client.send_message(game,'โน ะ ะพะฑัะตะบัั')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                        await asyncio.sleep(2)
                        await client.send_message(game,'โ ะะพะดัะฒะตัะดะธัั')
                        trap_cd = True
                    elif needsReload == True:
                        await asyncio.sleep(3)
                        await client.send_message(game,'๐ ะะตัะตะทะฐััะดะบะฐ')
                        needsReload = False
                    elif rico_cd == False:
                        await asyncio.sleep(3)
                        await client.send_message(game,'๐ ะฃะผะตะฝะธั')
                        await asyncio.sleep(2)
                        await client.send_message(game,'โด ะ?ะธะบะพัะตั')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                        rico_cd = True
                    elif knockback_cd == False:
                        await asyncio.sleep(3)
                        await client.send_message(game,'๐ ะฃะผะตะฝะธั')
                        await asyncio.sleep(2)
                        await client.send_message(game,'๐ ะัะฑัะพั')
                        await asyncio.sleep(1)
                        await client.send_message(game,'โน ะ ะพะฑัะตะบัั')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                        await asyncio.sleep(2)
                        await client.send_message(game,'โ ะะพะดัะฒะตัะดะธัั')
                        knockback_cd = True
                    else:
                        await asyncio.sleep(3)
                        await client.send_message(game,'โ๏ธ ะัะฐะบะฐ')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await asyncio.sleep(2)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)

    # <============================================================================================M2
    if messag == '.farm' and sender == me and fromChat == me.id and state == 'none':
        state = 'farm'
        await client.send_message(me, 'ะ?ะตะถะธะผ FARM ะฒะบะปััะตะฝ')
    if ('ะั ะฝะฐะฟะฐะดะฐะตัะต ะฝะฐ' in messag or 'ะะฐ ะฒะฐั ะฝะฐะฟะฐะดะฐัั:' in messag) and fromChat == gameId and state == 'farm':
        if 'ะะฐ ะฒะฐั ะฝะฐะฟะฐะดะฐัั' in messag:
            await asyncio.sleep(2)
            await client.send_message(game,'โ๏ธ ะัะฐัััั')
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
                if isAutoFightButton.rows[3].buttons[0].text.startswith('โป๏ธ ะะฒัะพะฑะพะน'):
                    await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
        else:
            await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
            await asyncio.sleep(2)
            await client.send_message(game,'โ๏ธ ะะพ ะฝะฐะฟัะฐะฒะปะตะฝะธั')
            await asyncio.sleep(2)
            await client.send_message(game,'โฌ')
            stepBack = 2
    elif weapon in messag and 'ะัะฑะตัะธัะต ัะตะปั' not in messag and fromChat == gameId and state.startswith('m2'):
        m = await client.get_messages(game, limit=1)
        isAutoFightButton = m[0].reply_markup
        if len(isAutoFightButton.rows)>1:
            if AutoFight == True and isAutoFightButton.rows[3].buttons[0].text.startswith('โป๏ธ ะะฒัะพะฑะพะน'):
                await client.send_message(game,isAutoFightButton.rows[3].buttons[0].text)
            elif AutoFight == False and isAutoFightButton.rows[3].buttons[0].text.startswith('โป๏ธ ะะฒัะพะฑะพะน'):
                if stepBack == 1:
                    await asyncio.sleep(3)
                    await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
                    await asyncio.sleep(2)
                    await client.send_message(game,'โ๏ธ ะะพ ะฝะฐะฟัะฐะฒะปะตะฝะธั')
                    await asyncio.sleep(2)
                    await client.send_message(game,'โฌ')
                    stepBack = 2
                elif stepBack == 2:
                    if 'โฑ ะะพัััะฟะฝะพ - โด ะ?ะธะบะพัะตั' in messag:
                        rico_cd = False
                    if 'โฑ ะะพัััะฟะฝะพ - ๐ฒ ะะพะฒััะบะฐ' in messag:
                        trap_cd = False
                    if 'โฑ ะะพัััะฟะฝะพ - ๐ ะัะฑัะพั' in messag:
                        knockback_cd = False
                    if messag.split(weapon)[1].split('/')[0] == '0':
                        needsReload = True
                    if trap_cd == False:
                        await asyncio.sleep(3)
                        await client.send_message(game,'๐ ะฃะผะตะฝะธั')
                        await asyncio.sleep(2)
                        await client.send_message(game,'๐ฒ ะะพะฒััะบะฐ')
                        await asyncio.sleep(1)
                        await client.send_message(game,'โน ะ ะพะฑัะตะบัั')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                        await asyncio.sleep(2)
                        await client.send_message(game,'โ ะะพะดัะฒะตัะดะธัั')
                        trap_cd = True
                    elif needsReload == True:
                        await asyncio.sleep(3)
                        await client.send_message(game,'๐ ะะตัะตะทะฐััะดะบะฐ')
                        needsReload = False
                    elif rico_cd == False:
                        await asyncio.sleep(3)
                        await client.send_message(game,'๐ ะฃะผะตะฝะธั')
                        await asyncio.sleep(2)
                        await client.send_message(game,'โด ะ?ะธะบะพัะตั')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                        rico_cd = True
                    elif knockback_cd == False:
                        await asyncio.sleep(3)
                        await client.send_message(game,'๐ ะฃะผะตะฝะธั')
                        await asyncio.sleep(2)
                        await client.send_message(game,'๐ ะัะฑัะพั')
                        await asyncio.sleep(1)
                        await client.send_message(game,'โน ะ ะพะฑัะตะบัั')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)
                        await asyncio.sleep(2)
                        await client.send_message(game,'โ ะะพะดัะฒะตัะดะธัั')
                        knockback_cd = True
                    else:
                        await asyncio.sleep(3)
                        await client.send_message(game,'โ๏ธ ะัะฐะบะฐ')
                        await asyncio.sleep(1)
                        target = await client.get_messages(game, limit=1)
                        await asyncio.sleep(2)
                        await client.send_message(game,target[0].reply_markup.rows[0].buttons[0].text)

    # <============================================================================================PARTY
    if 'ะะฐัะฒะฐั ะณััะฟะฟั ะพัะบะปััะตะฝ' in messag and fromChat == gameId and PL == True and state != 'none':
        toLockParty = True
    if 'ะะฐัะฒะฐั ะณััะฟะฟั ะฒะบะปััะตะฝ' in messag and fromChat == gameId and PL == True and state != 'none':
        toLockParty = False
    if messag == 'ะขั ะฟะพะปะฝะพัะตะฝะฝะพ ะพัะดะพัะฝัะป!' and fromChat == gameId and PL == True and notEnoughNRG == True and (state == 'boss' or state.startswith('dg') or state == 'm2') and AutoRun == True:
        notEnoughNRG = False
        if state == 'dg 36-40':
            run = '๐ฅ ะะตะปะพััััะบะธะน ะฒะพะบะทะฐะป (36-40)'
        elif state == 'dg 41-45':
            run = '๐ฅ ะะฟัะตะบะฐััะบะธะน ะพะณะพัะพะด (41-45)'
        elif state == 'dg 46-50':
            run = '๐ฅ ะะปะพัะฐะดั ัััั ะฒะพะบะทะฐะปะพะฒ (46-50)'
        elif state == 'boss':
            run = '๐ฆช ะัะฟะพะปัะทะพะฒะฐัั ะฟัะธะผะฐะฝะบั'
        elif state == 'm2' or state == 'farm':
            run = '๐พ ะะพะธัะบ ะผะพะฝัััะพะฒ'
            if toLockParty == True and state == 'm2':
                isLocked = False
                await client.send_message(game,'/group')
                await asyncio.sleep(0.5)
                await client.send_message(game,'๐ฃ ะฃะฟัะฐะฒะปะตะฝะธะต')
                await asyncio.sleep(0.5)
                await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
                await asyncio.sleep(0.5)
                await client.send_message(game,'๐ข ะะบะปััะธัั ะทะฐัะฒะฐั')
                while isLocked == False:
                    await asyncio.sleep(0.5)
                    m = await client.get_messages(game, limit=2)
                    if m[0].message.startswith('โ๏ธะฃะบะฐะทะฐะฝะฝัะต ะธะณัะพะบะธ ะฝะฐัะพะดัััั ะฝะต ััะดะพะผ'):
                        isLocked = True
                        await client.send_message(chatControl,m[0].message)
                    elif 'ะะฐัะฒะฐั ะณััะฟะฟั ะฒะบะปััะตะฝ' in m[1].message:
                        isLocked = True
                        toLockParty = False
                        await asyncio.sleep(0.5)
                        await client.send_message(game,'/buttons')
                        await asyncio.sleep(1)
                        await client.send_message(game,run)
        if state.startswith('dg'):
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ฅ ะกะพััะฐะฒ')
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            splitGroup = m[0].message.split('[1')[1].split('\n')
            plToAdr = ''
            for x in range(len(splitGroup)):
                if '[๐] ' in splitGroup[x]:
                    plToAdr = plToAdr + splitGroup[x].split('[๐] ')[1].split(' (')[0] + ' '
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
        if 'ะัะฑะตัะธัะต ัะปะพะถะฝะพััั ' in m[0].message:
            await m[0].click(hardMode)
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            await m[0].click(text='โ ะะพะดัะฒะตัะดะธัั')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'ะะพะฝัััะพะฒ ะฝะตั' in m[0].message:
            await client.send_message(game,'/flashlight')
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            await m[0].click(0)
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            if 'ะะฐะฟะฐั ะฟัะพัะฝะพััะธ ัะปะธัะบะพะผ ะผะฐะป' in m[0].message:
                await m[0].click(1)
                await asyncio.sleep(1)
                await client.send_message(game,'๐ ะ?ัะบะทะฐะบ')
                await asyncio.sleep(1)
                m = await client.get_messages(game, limit=1)
                bSpl = m[0].message.split('\n')
                flToWear = ''
                for b in range(len(bSpl)):
                    if bSpl[b].startswith('๐ฆ ะคะพะฝะฐัะธะบ ๏ดพ100'):
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
            await client.send_message(game,'๐พ ะะพะธัะบ ะผะพะฝัััะพะฒ')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'ะะตะดะพััะฐัะพัะฝะพ ัะฝะตัะณะธะธ' in m[0].message:
            await client.send_message(chatControl,'ะะตะดะพััะฐัะพัะฝะพ ัะฝะตัะณะธะธ, ะถะดะตะผ')
            notEnoughNRG = True
        elif 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' in m[0].message:
            await client.send_message(chatControl,m[0].message+'\n\n.leader __NICKNAME__, ััะพะฑ ัะผะตะฝะธัั ะปะธะดะตัะฐ')
        elif 'ะะตะพะฑัะพะดะธะผะพ ะฒัะฟะพะปะฝะธัั ะทะฐัะฒะฐั' in m[0].message:
            isLocked = False
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ฃ ะฃะฟัะฐะฒะปะตะฝะธะต')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ข ะะบะปััะธัั ะทะฐัะฒะฐั')
            while isLocked == False:
                await asyncio.sleep(0.5)
                m = await client.get_messages(game, limit=2)
                if m[0].message.startswith('โ๏ธะฃะบะฐะทะฐะฝะฝัะต ะธะณัะพะบะธ ะฝะฐัะพะดัััั ะฝะต ััะดะพะผ'):
                    isLocked = True
                    await client.send_message(chatControl,m[0].message)
                elif 'ะะฐัะฒะฐั ะณััะฟะฟั ะฒะบะปััะตะฝ' in m[1].message:
                    isLocked = True
                    await asyncio.sleep(0.5)
                    await client.send_message(game,'/buttons')
                    await asyncio.sleep(1)
                    await client.send_message(game,run)
    if (state == 'boss' or state.startswith('dg') or state == 'm2' or state == 'farm') and 'ะะพะน ะฒัะธะณัะฐะฝ' in messag and fromChat == gameId and PL == True and AutoRun == True:
        if 'ะฟัะพะฟััะบะฐ ะ-6' in messag:
            lootSpl = messag.split('\n')
            for l in range(len(lootSpl)):
                if 'ะฟัะพะฟััะบะฐ ะ-6' in lootSpl[l]:
                    await client.send_message(chatControl,'ะะพะปััะตะฝะฐ '+lootSpl[l])
                    m2Tickets = m2Tickets + 1
                    if 'ั.1' in lootSpl[l]:
                        m2Ticket1 = m2Ticket1 + 1
                    elif 'ั.2' in lootSpl[l]:
                        m2Ticket2 = m2Ticket2 + 1
                    elif 'ั.3' in lootSpl[l]:
                        m2Ticket3 = m2Ticket3 + 1
        if state == 'm2' or state == 'farm':
            await asyncio.sleep(2)
        else:
            await asyncio.sleep(random.randint(5,10))
        if state == 'farm':
            await client.send_message(game,'/h')
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            spl = m[0].message.split('\n')[0].split(' ๐')[0]
            heartEmoji = 'โค๏ธ'
            if 'โค๏ธ' in spl:
                heartEmoji = 'โค๏ธ'
            elif '๐' in spl:
                heartEmoji = '๐'
            elif 'โฃ๏ธ' in spl:
                heartEmoji = 'โฃ๏ธ'
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
            if heartEmoji == 'โฃ๏ธ':
                await asyncio.sleep(1)
                adrText = ''
                m = await client.get_messages(game, limit=1)
                buttonsDir = m[0].reply_markup
                for r in range(len(buttonsDir.rows)):
                    buttonsInRow = buttonsDir.rows[r].buttons
                    for b in range(len(buttonsInRow)):
                        if 'ะะดัะตะฝะฐะปะธะฝ' in buttonsInRow[b].text:
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
                            if 'ะะฐะทะฐะด' not in partStatus and int(re.findall('[0-9]+',partStatus)[0]) < 31:
                                await m[0].click(text=partStatus)
                                await asyncio.sleep(0.8)
        else:
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ฅ ะกะพััะฐะฒ')
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            splitGroup = m[0].message.split('\n')
            plToAdr = ''
            for x in range(len(splitGroup)):
                if 'โฃ๏ธ' in splitGroup[x]:
                    if '[๐] ' in splitGroup[x]:
                        plToAdr = plToAdr + splitGroup[x].split('[๐] ')[1].split(' (โฃ๏ธ')[0] + ' '
                    else:
                        plToAdr = plToAdr + splitGroup[x].split('] ')[1].split(' (โฃ๏ธ')[0] + ' '
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
                        if 'ะะดัะตะฝะฐะปะธะฝ' in buttonsInRow[b].text:
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
                            if 'ะะฐะทะฐะด' not in partStatus and int(re.findall('[0-9]+',partStatus)[0]) < 31:
                                await m[0].click(text=partStatus)
                                await asyncio.sleep(1)
            else:
                await asyncio.sleep(3)
        await asyncio.sleep(1)
        if state == 'dg 36-40':
            run = '๐ฅ ะะตะปะพััััะบะธะน ะฒะพะบะทะฐะป (36-40)'
        elif state == 'dg 41-45':
            run = '๐ฅ ะะฟัะตะบะฐััะบะธะน ะพะณะพัะพะด (41-45)'
        elif state == 'dg 46-50':
            run = '๐ฅ ะะปะพัะฐะดั ัััั ะฒะพะบะทะฐะปะพะฒ (46-50)'
        elif state == 'boss':
            run = '๐ฆช ะัะฟะพะปัะทะพะฒะฐัั ะฟัะธะผะฐะฝะบั'
        elif state == 'm2' or state == 'farm':
            run = '๐พ ะะพะธัะบ ะผะพะฝัััะพะฒ'
            if toLockParty == True and state == 'm2':
                isLocked = False
                await client.send_message(game,'/group')
                await asyncio.sleep(0.5)
                await client.send_message(game,'๐ฃ ะฃะฟัะฐะฒะปะตะฝะธะต')
                await asyncio.sleep(0.5)
                await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
                await asyncio.sleep(0.5)
                await client.send_message(game,'๐ข ะะบะปััะธัั ะทะฐัะฒะฐั')
                while isLocked == False:
                    await asyncio.sleep(0.5)
                    m = await client.get_messages(game, limit=2)
                    if m[0].message.startswith('โ๏ธะฃะบะฐะทะฐะฝะฝัะต ะธะณัะพะบะธ ะฝะฐัะพะดัััั ะฝะต ััะดะพะผ'):
                        isLocked = True
                        await client.send_message(chatControl,m[0].message)
                    elif 'ะะฐัะฒะฐั ะณััะฟะฟั ะฒะบะปััะตะฝ' in m[1].message:
                        isLocked = True
                        toLockParty = False
                        await asyncio.sleep(0.5)
                        await client.send_message(game,'/buttons')
                        await asyncio.sleep(1)
                        await client.send_message(game,run)
        await client.send_message(game,run)
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'ะัะฑะตัะธัะต ัะปะพะถะฝะพััั ' in m[0].message:
            await m[0].click(hardMode)
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            await m[0].click(text='โ ะะพะดัะฒะตัะดะธัั')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'ะะพะฝัััะพะฒ ะฝะตั' in m[0].message:
            await client.send_message(game,'/flashlight')
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            await m[0].click(0)
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            if 'ะะฐะฟะฐั ะฟัะพัะฝะพััะธ ัะปะธัะบะพะผ ะผะฐะป' in m[0].message:
                await m[0].click(1)
                await asyncio.sleep(1)
                await client.send_message(game,'๐ ะ?ัะบะทะฐะบ')
                await asyncio.sleep(1)
                m = await client.get_messages(game, limit=1)
                bSpl = m[0].message.split('\n')
                flToWear = ''
                for b in range(len(bSpl)):
                    if bSpl[b].startswith('๐ฆ ะคะพะฝะฐัะธะบ ๏ดพ100'):
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
            await client.send_message(game,'๐พ ะะพะธัะบ ะผะพะฝัััะพะฒ')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'ะะตะดะพััะฐัะพัะฝะพ ัะฝะตัะณะธะธ' in m[0].message:
            await client.send_message(chatControl,'ะะตะดะพััะฐัะพัะฝะพ ัะฝะตัะณะธะธ, ะถะดะตะผ')
            notEnoughNRG = True
        elif 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' in m[0].message:
            await client.send_message(chatControl,m[0].message+'\n\n.leader __NICKNAME__, ััะพะฑ ัะผะตะฝะธัั ะปะธะดะตัะฐ')
        elif 'ะะตะพะฑัะพะดะธะผะพ ะฒัะฟะพะปะฝะธัั ะทะฐัะฒะฐั' in m[0].message:
            isLocked = False
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ฃ ะฃะฟัะฐะฒะปะตะฝะธะต')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ข ะะบะปััะธัั ะทะฐัะฒะฐั')
            while isLocked == False:
                await asyncio.sleep(0.5)
                m = await client.get_messages(game, limit=2)
                if m[0].message.startswith('โ๏ธะฃะบะฐะทะฐะฝะฝัะต ะธะณัะพะบะธ ะฝะฐัะพะดัััั ะฝะต ััะดะพะผ'):
                    isLocked = True
                    await client.send_message(chatControl,m[0].message)
                elif 'ะะฐัะฒะฐั ะณััะฟะฟั ะฒะบะปััะตะฝ' in m[1].message:
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
            run = '๐ฅ ะะตะปะพััััะบะธะน ะฒะพะบะทะฐะป (36-40)'
        elif state == 'dg 41-45':
            run = '๐ฅ ะะฟัะตะบะฐััะบะธะน ะพะณะพัะพะด (41-45)'
        elif state == 'dg 46-50':
            run = '๐ฅ ะะปะพัะฐะดั ัััั ะฒะพะบะทะฐะปะพะฒ (46-50)'
        elif state == 'boss':
            run = '๐ฆช ะัะฟะพะปัะทะพะฒะฐัั ะฟัะธะผะฐะฝะบั'
        elif state == 'm2' or state == 'farm':
            run = '๐พ ะะพะธัะบ ะผะพะฝัััะพะฒ'
            if toLockParty == True and state == 'm2':
                isLocked = False
                await client.send_message(game,'/group')
                await asyncio.sleep(0.5)
                await client.send_message(game,'๐ฃ ะฃะฟัะฐะฒะปะตะฝะธะต')
                await asyncio.sleep(0.5)
                await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
                await asyncio.sleep(0.5)
                await client.send_message(game,'๐ข ะะบะปััะธัั ะทะฐัะฒะฐั')
                while isLocked == False:
                    await asyncio.sleep(0.5)
                    m = await client.get_messages(game, limit=2)
                    if m[0].message.startswith('โ๏ธะฃะบะฐะทะฐะฝะฝัะต ะธะณัะพะบะธ ะฝะฐัะพะดัััั ะฝะต ััะดะพะผ'):
                        isLocked = True
                        await client.send_message(chatControl,m[0].message)
                    elif 'ะะฐัะฒะฐั ะณััะฟะฟั ะฒะบะปััะตะฝ' in m[1].message:
                        isLocked = True
                        toLockParty = False
                        await asyncio.sleep(0.5)
                        await client.send_message(game,'/buttons')
                        await asyncio.sleep(1)
                        await client.send_message(game,run)
        if state.startswith('dg'):
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ฅ ะกะพััะฐะฒ')
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            splitGroup = m[0].message.split('[1')[1].split('\n')
            plToAdr = ''
            for x in range(len(splitGroup)):
                if '[๐] ' in splitGroup[x]:
                    plToAdr = plToAdr + splitGroup[x].split('[๐] ')[1].split(' (')[0] + ' '
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
        if 'ะัะฑะตัะธัะต ัะปะพะถะฝะพััั ' in m[0].message:
            await m[0].click(hardMode)
            await asyncio.sleep(0.5)
            m = await client.get_messages(game, limit=1)
            await m[0].click(text='โ ะะพะดัะฒะตัะดะธัั')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'ะะพะฝัััะพะฒ ะฝะตั' in m[0].message:
            await client.send_message(game,'/flashlight')
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            await m[0].click(0)
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=1)
            if 'ะะฐะฟะฐั ะฟัะพัะฝะพััะธ ัะปะธัะบะพะผ ะผะฐะป' in m[0].message:
                await m[0].click(1)
                await asyncio.sleep(1)
                await client.send_message(game,'๐ ะ?ัะบะทะฐะบ')
                await asyncio.sleep(1)
                m = await client.get_messages(game, limit=1)
                bSpl = m[0].message.split('\n')
                flToWear = ''
                for b in range(len(bSpl)):
                    if bSpl[b].startswith('๐ฆ ะคะพะฝะฐัะธะบ ๏ดพ100'):
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
            await client.send_message(game,'๐พ ะะพะธัะบ ะผะพะฝัััะพะฒ')
        await asyncio.sleep(0.5)
        m = await client.get_messages(game, limit=1)
        if 'ะะตะดะพััะฐัะพัะฝะพ ัะฝะตัะณะธะธ' in m[0].message:
            almostRun = False
            await event.message.reply('ะะตะดะพััะฐัะพัะฝะพ ัะฝะตัะณะธะธ, ะถะดะตะผ')
            notEnoughNRG = True
        elif 'ะพััััััะฒัะตั ะฒ ััะบะทะฐะบะต' in m[0].message:
            almostRun = False
            await event.message.reply(m[0].message+'\n\n.leader __NICKNAME__, ััะพะฑ ัะผะตะฝะธัั ะปะธะดะตัะฐ')
        elif 'ะะตะพะฑัะพะดะธะผะพ ะฒัะฟะพะปะฝะธัั ะทะฐัะฒะฐั' in m[0].message:
            isLocked = False
            await client.send_message(game,'/group')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ฃ ะฃะฟัะฐะฒะปะตะฝะธะต')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ ะะฒะธะถะตะฝะธะต')
            await asyncio.sleep(0.5)
            await client.send_message(game,'๐ข ะะบะปััะธัั ะทะฐัะฒะฐั')
            while isLocked == False:
                await asyncio.sleep(0.8)
                m = await client.get_messages(game, limit=2)
                if m[0].message.startswith('โ๏ธะฃะบะฐะทะฐะฝะฝัะต ะธะณัะพะบะธ ะฝะฐัะพะดัััั ะฝะต ััะดะพะผ'):
                    isLocked = True
                    almostRun = False
                    await event.message.reply(m[0].message)
                elif 'ะะฐัะฒะฐั ะณััะฟะฟั ะฒะบะปััะตะฝ' in m[1].message:
                    isLocked = True
                    await asyncio.sleep(0.5)
                    await client.send_message(game,'/buttons')
                    await asyncio.sleep(1)
                    await client.send_message(game,run)
    # <==============================================================================================GO
    if messag.startswith('.go') and sender == me and fromChat == me.id and state == 'none':
        if imhere == '':
            await client.send_message(me, 'ะะดะตั ะฟะพะปััะตะฝะธะต ะธะทะฝะฐัะฐะปัะฝะพะณะพ ะผะตััะพะฟะพะปะพะถะตะฝะธั, ะพะถะธะดะฐะน...\nะญัะพ ัะฐะทะพะฒะพะต ะดะตะนััะฒะธะต ะฟะพัะปะต ะทะฐะฟััะบะฐ ัะบัะธะฟัะฐ, ะดะฐะปะตะต ะผะตััะพะฟะพะปะพะถะตะฝะธะต ะฑัะดะตั ะพะฑะฝะพะฒะปััััั ัะฐะผะพ.')
            await client.send_message(game,'/fraction')
            await asyncio.sleep(1)
            await client.send_message(game,'๐ ะกะพััะฐะฒ')
            await asyncio.sleep(1)
            m = await client.get_messages(game, limit=2)
            # print(event)
            # print(m[0].message)
            for s in range(len(m)):
                sostavArr = m[s].message.split('\n')
                for i in range(len(sostavArr)):
                    if nick in sostavArr[i]:
                        # print(sostavArr[i])
                        imhere = sostavArr[i].split(' ๐บ')[1].split(' โ๏ธ')[0].split(' โ')[0]
                        break
            await asyncio.sleep(random.randint(1,3))
            await client.send_message(game,'โฌ๏ธ ะะฐะทะฐะด')
        if imhere != '':
            if messag == '.go':
                listing = 'ะัะฑะตัะธ ะฝะพะผะตั ััะฐะฝัะธะธ, ะบัะดะฐ ัั ัะพัะตัั ะพัะฟัะฐะฒะธัััั\nCะตะนัะฐั ัั ะฝะฐัะพะดะธัััั ััั: **'+imhere+'**\n'
                for x in range(len(stationNames)):
                    if x == 0: listing += '\n**๐ฉ๐ฉ๐ฉ๐ฉะะะะะะะฏ๐ฉ๐ฉ๐ฉ๐ฉ**\n'
                    elif x == 6: listing += '\n**โฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธะกะะ?ะะฏโฌ๏ธโฌ๏ธโฌ๏ธโฌ๏ธ**\n'
                    elif x == 12: listing += '\n**๐งฉ๐งฉ๐งฉ๐งฉะกะะะะขะะะะฏ๐งฉ๐งฉ๐งฉ๐งฉ**\n'
                    elif x == 16: listing += '\n**๐ง๐ง๐ง๐งะะ?ะะะะะะะฏ๐ง๐ง๐ง๐ง**\n'
                    elif x == 22: listing += '\n**๐ฅ๐ฅ๐ฅ๐ฅะะ?ะะกะะะฏ๐ฅ๐ฅ๐ฅ๐ฅ**\n'
                    elif x == 30: listing += '\n**๐ฆ๐ฆ๐ฆ๐ฆะกะะะฏะฏ๐ฆ๐ฆ๐ฆ๐ฆ**\n'
                    elif x == 35: listing += '\n**๐ช๐ช๐ช๐ชะคะะะะะขะะะะฏ๐ช๐ช๐ช๐ช**\n'
                    elif x == 40: listing += '\n**๐จ๐จ๐จ๐จะะะะขะะฏ๐จ๐จ๐จ๐จ**\n'
                    elif x == 42: listing += '\n**๐ณ๐ณ๐ณ๐ณะะะะฃะะะฏ๐ณ๐ณ๐ณ๐ณ**\n'
                    elif x == 46: listing += '\n**๐ซ๐ซ๐ซ๐ซะะะะฌะฆะะะะฏ๐ซ๐ซ๐ซ๐ซ**\n'
                    listing += str(x) + '. ' + stationNames[x]+' โ `.go '+str(x)+'`\n'
                await client.send_message(me, listing)
            else:
                destination = int(messag.split('.go ')[1])
                # startPoint = stationNames.index(imhere)
                gpsTrack = gps(imhere,destination)
                # print(gpsTrack)
                waypointMsg = 'ะะฐะฟัะฐะฒะปัะตะผัั ะธะท **'+imhere+'** ะฝะฐ ััะฐะฝัะธั **'+stationNames[destination]+'**\n\nะะฐััััั:\n'
                nrgRaw = gpsTrack["nrg"]
                nrgLeft = nrgRaw % 5
                nrg = nrgRaw - nrgLeft
                pathStr = ''
                for p in range(len(gpsTrack["path"])):
                    path_type = ''
                    if p in range(len(gpsTrack["pathType"])):
                        if gpsTrack["pathType"][p] == 1:
                            path_type = '[๐ฅ ะะตัะตัะพะด] '
                        else:
                            path_type = '[๐ ะขัะฝะฝะตะปั] '
                    pathStr += stationNames[gpsTrack["path"][p]] + '\n'+path_type
                waypointMsg += pathStr+'\n\nะขัะฐัะฐ ัะฝะตัะณะธะธ: '+str(nrg)
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
                            await client.send_message(game, '๐ ะะพะบะธะฝััั ััะฐะฝัะธั')
                            await asyncio.sleep(random.randint(1,2))
                            if gpsTrack['pathType'][i-1] > 5:
                                await client.send_message(game, '๐ ะขัะฝะฝะตะปั')
                            else:
                                await client.send_message(game, '๐ฅ ะะตัะตัะพะด')
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
                            while (nxStName+'\n\n๐ธ ะกัะฐััั: ') not in m[0].message:
                                if 'ะกัะฐะฝัะธั ะพัะฟัะฐะฒะปะตะฝะธั:' in m[0].message:
                                    await client.send_message(game, 'โก๏ธ ะะฟะตััะด ะฝะฐ '+nxStName)
                                await asyncio.sleep(random.randint(1,2))
                                m = await client.get_messages(game, limit=1)
                    await client.send_message(me, 'ะขั ะดะพัะตะป ะดะพ ะบะพะฝะตัะฝะพะน ะปะพะบะฐัะธะธ')
                    state = 'none'
        else:
            await client.send_message(me, 'ะขั ะฝะต ะฝะฐะนะดะตะฝ ะฒ ัะพััะฐะฒะต ััะฐะบัะธะธ')
    if messag.startswith('.stop') and sender == me and fromChat == me.id and state != 'none':
        if state == 'm2':
            txt = ('**ะัะพะฒะตะดะตะฝะพ ะฑะพัะฒ ะฒ ะ2:** '+str(m2Fights)
                   + '\n**ะะฐะนะดะตะฝะพ ะงััะฝัั ะะตััะฝััะตะน:** '+str(m2Babies)+' ะธะท '+str(m2Targets)+' ะผะพะฑะพะฒ __('+str("{:0.2f}".format((m2Babies/m2Targets)*100))+'%)__'
                   +'\n**ะะพะปััะตะฝะพ ัะฐััะตะน ะฟัะพะฟััะบะฐ ะ-6:** '+str(m2Tickets)+' __('+str("{:0.2f}".format((m2Tickets/m2Babies)*100))+'%)__')
            await event.message.reply(txt)
            m2Fights = 0
            m2Babies = 0
            m2Targets = 0
            m2Tickets = 0
        state = 'none'
        await client.send_message(me, 'ะะพั ะทะฐะฟััะตะฝ')

client.start()
me = client.get_me()
client.send_message(me, 'ะะพั ะทะฐะฟััะตะฝ')
client.send_message(game, '/character')
client.run_until_disconnected()