import os

import random
import urllib
from email import message
from io import BytesIO
from random import choice
from aiofile import author_info
import time
import requests
from BotAmino import BotAmino
from click import command
from importlib_metadata import suppress
from requests import request
from urllib.request import urlopen # To load URL's.



client = BotAmino(email="ui8w5y6@esiix.com", password="spam123")
client.prefix = "!"


def tradlist(sub):
    sublist = []
    for elem in sub:
        try:
            sublist.append(client.get_from_code(f"http://aminoapps.com/u/{elem}").objectId)
            continue
        except Exception:
            pass
        sublist.append(elem)
    return sublist


whitefile = 'whitelist.txt'
whitelist = []
try:
    with open(whitefile, 'r') as file:
        for whitelistmember in file.readlines():
            whitelist.append(whitelistmember.strip())
except FileNotFoundError:
    a = open(whitefile, "w")
    a.close()


whitelist = tradlist(whitelist)


def upload(url):
    link = requests.get(url)
    result = BytesIO(link.content)
    return result

def is_it_me(data):
    return data.authorId in ('f74b68b3-22f7-46c2-99f5-1b6a6ab7c68d','userId')

#This code will be executed if is_it_me return True
@client.on_message(is_it_me)
def dueño(data):
    print(data.author, data.message)

@client.command()
def hola(data):
    data.subClient.send_message(data.chatId, message="Hola, bebe")

@client.on_message()
def text_message(data):
 # print(data.message)
  content=data.message
  if "aminoapps.com/c" in content or "aminoapps.com/p" in content:
    info = client.get_from_code(content)
    comid = info.path[1:info.path.index("/")]
    if comid != f'{data.comId}':
           data.subClient.send_message(data.chatId, "NO ENVIES LINKS DE OTRAS COMUNIDADES")
           data.subClient.delete_message(chatId=data.chatId,messageId=data.messageId,asStaff=True, reason='link externo compartido')
           data.subClient.warn(userId=data.authorId,reason="Compartio links de otras comunidades")


@client.command()
def privado (data):
    data.subClient.start_chat(message="Hola, soy Irene", userId=data.authorId)
    data.subClient.send_message(data.chatId, "Listo, ya te abri privado")

@client.command()
def idusuario(data):
    data.subClient.send_message(data.chatId, message=f"""a
[Cb]Nombre: 
[C]{data.author}
[Cb]UserId: 
[c]{data.authorId}""")

@client.command()
def Irene (data):
    test = choice(["No, no quiero.", "SI!", "talvez", "claro", "nunca", "No lo recuerdo, creo que si.", "Pero que tipo de cosas le preguntas a un bot, tontito. .///."])
    data.subClient.send_message(data.chatId, test)

@client.command("comentame")
def comment_profile(data):
    data.subClient.comment(message=data.message, userId=data.authorId)
    data.subClient.send_message(data.chatId, f"Listo, ya comenté. {data.author}")

@client.command("comentale")
def comment_profile(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
       data.subClient.comment(message=data.message, userId=str(user))
       data.subClient.send_message(data.chatId, f"Listo, ya le comenté")

@client.command(name="banamex")
def banamex(data):
    url = data.message
    print("url:", url)
    id=client.get_from_code(url).objectId
    data.subClient.get_user_info(id)
    data.subClient.ban(id, "Estaba haciendo spam")
    data.subClient.send_message(data.chatId, "Ya lo fune")



@client.command(name="global")
def glob(data):
    url = data.message
    print("url:", url)
    id=client.get_from_code(url).objectId
    data.subClient.get_user_info(id)
    AID=client.get_user_info(userId=str(id)).aminoId
    data.subClient.send_message(data.chatId,message="https://aminoapps.com/u/"+str(AID))



@client.command()
def sigueme(data):
    data.subClient.follow_user(data.authorId)
    data.subClient.send_message(data.chatId, f"Te sigo {data.author}")

@client.command()
def nomesigas(data):
    data.subClient.unfollow_user(data.authorId)
    data.subClient.send_message(data.chatId, f"Ya no te sigo {data.author}")


    ###data.subClient.set_welcome_message

@client.command()
def wall(data):
    data.subClient.set_welcome_message(data.message)
    data.subClient.send_message(data.chatId,"Updated wall message!", replyTo=data.messageId)

@client.on_all()
def on_menssage (data):
    data.subClient.check_new_member()
    data.subClient.welcome_new_member(message=data.message, userId=data.authorId)

@client.on_member_join_chat()
def say_hello(data):
    l = data.subClient.get_user_info(data.authorId).icon
    level = data.subClient.get_member_level(data.authorId)
    req = requests.get(l).content
    with open('giga.jpeg', 'wb') as file:
        file.write(req)
    with open('giga.jpeg', 'rb') as file:
        data.subClient.send_message(data.chatId, f"""
[c]𝗪𝗘𝗟𝗖𝗢𝗠𝗘 <$@{data.author}$>,
[C]
[C]
[C]╭╭╌💮 〕﹟𝗕𝗢𝗧 𝗗𝗘 𝗝𝗢𝗡  ↓↓︕ ╌╮╮
[C]╰╰▻ ❪﹟𝐔𝐧 𝐛𝐮𝐞𝐧 𝐚𝐦𝐢𝐠𝐨  ❫ 💮﹞ ︵ . ╯
[C]☆  /  /  ★  ᨓ  ¡¡  +  ♡̶  𓂃 ###  !! `
[C]︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿
[C]                𝐖3𝗟𝗖𝐎𝕸𝗘      𝖴𝖲𝖴𝖠𝖱𝖨𝖮
[C]!! ⸺ 𝗟𝗲𝗮 𝗹𝗮𝘀 𝗿𝗲𝗴𝗹𝗮𝘀 para evitar lle
[C]          varse el ban. Esperemos que
[C]          su                                             !!
[C]          𝗲𝘀𝘁𝗮𝗻𝗰𝗶𝗮 en éste chat sea de
[C]          𝗼𝗿𝗼.                            ¡Disfrute!
[C]︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿ . ︿""",mentionUserIds=data.authorId ,embedImage=file, embedTitle=f'{data.author}', embedContent=f'Level: {level}, una nueva personita')


@client.command()
def limpiar(data : str, nt = 1):
    level = data.subClient.get_member_level(data.authorId)
    for _ in range(int(nt)):
        if level < 3:
           data.subClient.kick(chatId=data.chatId, userId=data.authorId, allowRejoin=False)

@client.command("comentame")
def comment_profile(data):
    data.subClient.comment(message=data.message, userId=data.authorId)
    data.subClient.send_message(data.chatId, f"Listo, ya comenté. {data.author}")


@client.command()
def joinall(data):
    data.subClient.join_all_chat()
    data.subClient.send_message(data.chatId, "Unido a todos los chats")

@client.command("On")
def random_action(data):
    data.subClient.send_message(data.chatId, "Hola, estoy activada!^^")

@client.command("Testeo")
def test(data):
    data.subClient.send_message(data.chatId, f"Hola {data.author}")

@client.command("iconuser")
def iconuser(data):
    id=client.get_from_code(data.message).objectId
    image = data.subClient.get_user_info(id).icon
    filename = image.split("/")[-1]
    filetype = image.split(".")[-1]
    if filetype != "gif":
        filetype = "image"
        urllib.request.urlretrieve(image, filename)
        with open(filename, 'rb') as fp:
            with suppress(Exception):
                data.subClient.send_message(data.chatId, file=fp, fileType=filetype)
                os.remove(filename)

@client.command("icon")
def icon(args):
    info = args.subClient.get_message_info(chatId = args.chatId, messageId = args.messageId)
    reply_message = info.json['extensions']
    if reply_message:
        image = info.json['extensions']['replyMessage']['mediaValue']
    filename = image.split("/")[-1]
    filetype = image.split(".")[-1]
    if filetype != "gif":
        filetype = "image"
    urllib.request.urlretrieve(image, filename)
    with open(filename, 'rb') as image:
        for i in range(1,3):
            try:
                args.subClient.edit_profile(icon=image)
            except Exception:
                    args.subClient.send_message(args.chatId, message="ready",replyTo=args.messageId)


@client.command("icon")
def icon(args):
    info = args.subClient.get_message_info(chatId = args.chatId, messageId = args.messageId)
    reply_message = info.json['extensions']
    if reply_message:
        image = info.json['extensions']['replyMessage']['mediaValue']
    filename = image.split("/")[-1]
    filetype = image.split(".")[-1]
    if filetype != "gif":
        filetype = "image"
    urllib.request.urlretrieve(image, filename)
    with open(filename, 'rb') as image:
        for i in range(1,3):
            try:
                args.subClient.edit_profile(icon=image)
            except Exception:
                    args.subClient.send_message(args.chatId, message="ready",replyTo=args.messageId)

@client.command("icon")
def icon(args):
    if client.check(args, 'staff'):
        info = args.subClient.get_message_info(chatId = args.chatId, messageId = args.messageId)
        reply_message = info.json['extensions']
        if reply_message:
            image = info.json['extensions']['replyMessage']['mediaValue']
        filename = image.split("/")[-1]
        filetype = image.split(".")[-1]
        if filetype != "gif":
            filetype = "image"
        urllib.request.urlretrieve(image, filename)
        with open(filename, 'rb') as image:
            for i in range(1,3):
                try:
                    args.subClient.edit_profile(icon=image)
                except Exception:
                        args.subClient.send_message(args.chatId, message="ready",replyTo=args.messageId)

 

@client.on_all()
def on_message(data):
    content = str(data.message).split()
    mtype = data.info.message.type

    if (mtype == 100) | (mtype == 107) | (mtype == 110) | (mtype == 108) | (mtype == 111) | (mtype == 111)| (mtype == 109) :
        if mtype == 100 and not content:
            pass
        if client.check(data,'staff', 'bot'):
            pass
        else:
            data.subClient.kick(chatId=data.chatId, userId=data.authorId, allowRejoin=False)
            try:
                data.subClient.ban(data.authorId, f"""[C]╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾
[c]Tipo de mensaje {mtype} 
[c]Detectado! Nickname: {data.author} 
[c]userId: {data.authorId} 
[c]messageId: {data.messageId}.
[C]╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾╼╾""")
            except Exception:
                pass


@client.command("global")
def globall(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
       AID=client.get_user_info(userId=str(user)).aminoId
       data.subClient.send_message(data.chatId,message="https://aminoapps.com/u/"+str(AID))


@client.command(name="busqueda")
def busqueda(data):
    data.subClient.send_message(data.chatId,message="iniciando busqueda")
    users_count = data.subClient.get_online_users(size=1).userProfileCount
    users_count = users_count - (users_count % 100 - 1)
    for i in range(0, users_count, 100):
        users = data.subClient.get_online_users(start=i, size=100).profile
        for nickname, uid, content in zip(users.nickname, users.userId, users.content):
            if content is None: continue
                
            if '_(.a={}{}{}' in content:
                data.subClient.send_message(data.chatId,message=f"se encontro a {nickname}")
                data.subClient.ban(userId=uid, reason='usuario con biografia crash')
                data.subClient.send_message(data.chatId,message=f"{nickname} a sido baneado")
                print(f'Baneado {nickname}...')
            time.sleep(10)

@client.command(name="busquedatodos")
def todos(data):
    data.subClient.send_message(data.chatId,message="iniciando busqueda")
    users_count = 9901 if data.com_info.usersCount > 10000 else data.com_info.usersCount - (data.com_info.usersCount % 100 - 1)
    for i in range(0, users_count, 100):
        users = data.sub.Client.get_all_users(start=i, size=100).profile
        for nickname, uid, content in zip(users.nickname, users.userId, users.content):
            if content is None: continue
            if '_(.a={}{}{}' in content:
                data.subClient.send_message(data.chatId,message=f"se encontro a {nickname}")
                data.subClient.ban(userId=uid, reason='usuario con biografia crash')
                data.subClient.send_message(data.chatId,message=f"{nickname} a sido baneado")
                print(f'Baneado {nickname}...')
            time.sleep(5)


@client.command()
def patear(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("patear.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif")
            time.sleep(1)
            data.subClient.send_message(chatId=data.chatId,message=f"{data.author} a pateado a "+ str(n)+ "en la bombacha")



@client.command()
def unete(data):
    url = data.message
    print("url:", url)
    id=client.get_from_code(url).objectId
    data.subClient.join_chat(chatId= id)
    data.subClient.send_message(data.chatId, message = "Listo, me uni al chat")

#@client.command(name="global")
def glob(data):
    url = data.message
    print("url:", url)
    id=client.get_from_code(url).objectId
    data.subClient.get_user_info(id)
    AID=client.get_user_info(userId=str(id)).aminoId
    data.subClient.send_message(data.chatId,message="https://aminoapps.com/u/"+str(AID))




@client.command()
def cumear(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("cumear.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif")
            time.sleep(1)
            data.subClient.send_message(chatId=data.chatId,message=f"{data.author} se a venidido encima de"+ str(n))

@client.command()
def besar (data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("besar.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif")
            time.sleep(1)
            data.subClient.send_message(chatId=data.chatId,message=f"{data.author} a besado a "+ str(n))

@client.command()
def abrazar (data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("abrazo.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif")
            time.sleep(1)
            data.subClient.send_message(chatId=data.chatId,message=f"{data.author} a comenzado a abrazar a "+ str(n))

@client.command()
def putazo (data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("putazo.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif")
            time.sleep(1)
            data.subClient.send_message(chatId=data.chatId,message=f"{data.author} le dio un putazo a "+ str(n))

@client.command()
def patpat (data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("patpat.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif")
            time.sleep(1)
            data.subClient.send_message(chatId=data.chatId,message=f"{data.author} le da un pat pat a "+ str(n))

@client.command()
def gey (data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("gey.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif")
            time.sleep(1)
            data.subClient.send_message(chatId=data.chatId,message=f"{data.author} confirmo que  "+ str(n)+ " es tremendo sauuuu")

@client.command()
def matrimonio (data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        n =data.subClient.get_user_info(str(user)).nickname
        with open("matrimonio.gif","rb") as fp:
            data.subClient.send_message(data.chatId,file=fp, fileType="gif")
            time.sleep(1)
            data.subClient.send_message(chatId=data.chatId,message=f"{data.author} te a pedido matrimonio  "+ str(n)+ " ¿aceptas?")



@client.command()
def ayuda (data):
    data.subClient.send_message(chatId=data.chatId, message= f"""
[c]⌈                          ⌉
[c]
[uc]⁽ ↳ ♡'  𝗁ᥱ̅𝗒 𝗎. 𝗌𝖾𝗋 ⸺ 𝘄𝗲𝗹.𝖼᥆̅𝗆𝖾 ⭏ ¡ 💭̷ ! 
[c]﹫𝖨𝗋ᥱ̅𝗇𝖾'𝗌 𝖼. ᥆̅𝗆𝗆͟𝖺͟𝗇𝖽𝗌 ꜝ ﹝𔘓﹞⸺ 𝗎. 𝗌ᥱ̅ 𝗂𝗍 ˿
[c]
[c]⏝ .⏝ . ⏝ . ⏝ . ⏝. ⏝ . ⏝ . ⏝
[c]
[c]¡Hola usuario! Soy Irene, un bot creado
[c]por﹫𝗝𝗼𝗻. A  continuación dejo mi lista
[c]de comandos, recuerda que el prefijo
[c]de uso es " ! "
[c]───────────────────
[c]!sigueme !privado  !global  !comentame
[c]!comentale  !iconuser !idusuario !Irene
[c]!abrazar !besar !cumear !patear !putazo
[c]!gey !matrimonio !patpat
[c]───────────────────
[c]
[cu]⁽  ↳ 𝖽᥆̅𝗇'𝗍 𝗮𝗯𝘂.𝗌ᥱ̅! ⸺ 𝖻𝗒𝖾 𝖻𝗒𝖾 𝗌. 𝗐𝖾𝖾𝗍𝗂𝖾﹕
[c]
[c]⌊                          ⌋

""",embedTitle=f"{data.author}",embedImage=upload(data.info.message.author.icon))


@client.command()
def prank(data, amt : int , nt = 1):
    print(data.comId)
    print(data.authorId)
    print(data.chatId)
    amt , nt =int(amt) , int(nt)
    for _ in range(nt):
        try:
            data.subClient.send_message(ctahId= data.chatId, coins=amt, transactionId= "7bdd69c4-71ae-47b4-899d-413368743f83")
        except:
            pass
          
@client.command()
def amor (data):
        msg = data.message + " null null "
        msg = msg.split(" ")
        msg[2] = msg[1]
        msg[1] = msg[0]
        try:
            data.subClient.send_message(data.chatId, message=f"[c]La posiblidad de amor entre {msg[1]} y {msg[2]} es de {random.randint(0,100)}%",replyTo=data.messageId)
        except:
            pass

@client.command("userid")
def userid(data):
    data.subClient.get_user_info(data.authorId).reputation
    data.subClient.send_message(data.chatId, message=f"""
[C]Nickname: {data.author}
[C]UserId: {data.authorId}""")


print("El bot inicio")
client.launch()
