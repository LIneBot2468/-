# -*- coding: utf-8 -*-
from Linephu.linepy import *
#from thrift import*
from datetime import datetime
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
import timeit

botStart = time.time()
cl = LINE("joson01@outlook.com","wwe71411")
k1 = LINE("joson02@outlook.com","wwe71411")
k2 = LINE("o7002588@nwytg.net","wwe71411")
k3 = LINE("cuz58430@cndps.com","wwe71411")
k4 = LINE("agn63515@cndps.com","wwe71411")
#======追加==========#

kick1 = LINE("joson0123@outlook.com","wwe71411")
kick2 = LINE("omu64244@cndps.com","wwe71411")
kick3 = LINE("eyw32128@cndps.com","wwe71411")
kick4 = LINE("jbx73299@cndps.com","wwe71411")
kick5 = LINE("xqa47032@cndps.com","wwe71411")
print ("[ Login ]Login successful")
clMID = cl.profile.mid
k1MID = k1.profile.mid
k2MID = k2.profile.mid
k3MID = k3.profile.mid
k4MID = k4.profile.mid
kick1MID = kick1.profile.mid
kick2MID = kick2.profile.mid
kick3MID = kick3.profile.mid
kick4MID = kick4.profile.mid
kick5MID = kick5.profile.mid

Bots = [clMID,k1MID,k2MID,k3MID,k4MID]
botkick = [kick1MID,kick2MID,kick3MID,kick4MID,kick5MID]
botKIC = botkick + Bots
gom = ['u4b9e74efaa8bb22757fa4499deddf06f','u2888443d25562a0d5a0c7fc2e5e4fe18']
oepoll = OEPoll(cl)

banOpen = codecs.open("ban.json","r","utf-8")
groupOpen = codecs.open("group.json","r","utf-8")
proOpen = codecs.open("pro.json","r","utf-8")
ban = json.load(banOpen)
gp = json.load(groupOpen)
pro = json.load(proOpen)
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def botJoin(to):
    G = cl.getGroup(to)
    G.preventedJoinByTicket = False
    cl.updateGroup(G)
    Ticket = cl.reissueGroupTicket(op.param1)
    k1.acceptGroupInvitationByTicket(to,Ticket)
    k2.acceptGroupInvitationByTicket(to,Ticket)
    k3.acceptGroupInvitationByTicket(to,Ticket)
    k4.acceptGroupInvitationByTicket(to,Ticket)
    G.preventedJoinByTicket = True
    cl.updateGroup(G)
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invaliod mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
            textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def backupData():
    try:
        backup = ban
        f = codecs.open('ban.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = gp
        f = codecs.open('group.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = pro
        f = codecs.open('pro.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)		
        return True
    except Exception as error:
        logError(error)
        return False
def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """╔═══════
╠➥簡易型防翻指令表
╠➥══[ 基本指令 ]═══
╠➥ Gc-剩餘票數
╠➥ /sp-速度
╠➥ speed-速度
╠➥ join-機器入群
╠➥ 機器退出-就 = 口 = 機器退出
╠➥ Godd @-新增群管
╠➥ Godl @-刪除群管
╠➥ gadd @-新增最高權限
╠➥ gdel @-刪除最高權限
╠➥ GM-查看本群管理者
╠➥ owners  -查看最高權限名單
╠➥ Banlist-黑單
╠➥ Adminlist-權限者清單"""
    return helpMessage
def helpmessagetag():
    helpMessageTag ="""╔═════════
╠✪ 簡易型防翻指令表 ✪
╠═══[ 基本指令 ]═══
╠➥ speed-速度
╠➥ join-機器入群
╠➥ 機器退出-機器終止防護
╠➥ Godd @-新增群管
╠➥ Godl @-刪除群管
╠➥ gadd @-新增最高權限
╠➥ gdel @-刪除最高權限
╠═══[ 網址開關 ]═══
╠➥ link on -群組網址開
╠➥ link off-群組網址關
╠═══[ 防翻指令 ]═══
╠➥kick/on-踢人保護開啟
╠➥kick/off-踢人保護關閉
╠➥inv/on-邀請保護開啟
╠➥inv/off-邀請保護關閉
╠➥qr/on-網址保護開啟
╠➥qr/off-網址保護關閉
╠➥pro on- 全體保護開起
╠➥pro off-全體保護關閉
╠═══[ 票券查詢 ]═══
╠➥ Gc mid-查看票券
╠➥ A (mid) (int)- 賦予票券
╠➥ 票券 -查詢票券ஜ
╠═══[ 黑單指令 ]═══
╠➥ ban -友資黑單
╠➥ Ban @-標註黑單
╠➥ ban:mid-MID新增黑單
╠➥ Unban-友資解除黑單
╠➥ Unban @-標註解除黑單
╠➥ Unban:mid-MID解除黑單
╠➥ banlist -黑名單列表
╠➥ clear ban -清空黑名單
╠═══[ 機器/群組 ]═══
╠➥ about-查看機器狀態
╠➥ ginfo-查看群組
╠➥ speed-速度
╠➥ test -查看機器死活
║    如果死了請私訊以下ID
║    »  speed.test#  «
╠➥ join-入防
╠➥ 機器退出-退防
╠➥ 群長-查看群長
╠═══[ 權限查詢 ]═══
╠➥ Adminlist-普通權限者
╠➥ owner-最高權限者
╠➥ GM-查看本群管理者
╠═〘 原創 by. 史萊姆 〙═
╚═〘 修改 by. 白朗 〙══"""
    return helpMessageTag
def helpn():
    helpN = """╔═══════
╠➥簡易型防翻指令表
╠➥══[ 基本指令 ]═══
╠➥ Gc-查詢自己剩餘票數
╠➥ Speed-速度
╠➥ GM-查看本群管理者
╚創作者為 羅莉喵🎵 修改者 by 白朗 """
    return helpN

wait = {
    "ban" : False,
    "unban" : False,
    "add" : False,
    "rapidFire":{},		
    "del" : False
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
msg_dict = {}
bl = [""]

if clMID not in ban["owners"]:
    ban["owners"].append(clMID)
if k1MID not in ban["owners"]:
    ban["owners"].append(k1MID)
if k2MID not in ban["owners"]:
    ban["owners"].append(k2MID)
if k3MID not in ban["owners"]:
    ban["owners"].append(k3MID)
if k4MID not in ban["owners"]:
    ban["owners"].append(k4MID)
if kick1MID not in ban["owners"]:
    ban["owners"].append(kick1MID)
if kick2MID not in ban["owners"]:
    ban["owners"].append(kick2MID)
if kick3MID not in ban["owners"]:
    ban["owners"].append(kick3MID)
if kick4MID not in ban["owners"]:
    ban["owners"].append(kick4MID)
if kick5MID not in ban["owners"]:
    ban["owners"].append(kick5MID)
if "u2888443d25562a0d5a0c7fc2e5e4fe18" not in ban["owners"]:
    ban["owners"].append("u2888443d25562a0d5a0c7fc2e5e4fe18")
def lineBot(op):
    try:	
        if op.type == 11:
            G = cl.getGroup(op.param1)
            if op.param1 in pro["qrprotect"]:
                if op.param2 in ban["owners"] or op.param2 in ban["admin"] :
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    if G.id in gp["s"] and op.param2 in gp["s"][G.id]:
                        pass	
                    else:						
                        bot =[cl,k1,k2,k3,k4,kick1,kick2,kick3,kick4,kick5]			
                        k123=random.choice(bot)			
                        gs = cl.getGroup(op.param1)
                        k123.sendMessage(op.param1,cl.getContact(op.param2).displayName + "網址保護中...不要動群組網址！")						
                        k123.kickoutFromGroup(op.param1,[op.param2])
                        gs.preventedJoinByTicket = False
                        gs.preventedJoinByTicket = True
                        k123.updateGroup(gs)
#def lineBot(op):
   # try:	
       # if op.type == 11:
          #  G = cl.getGroup(op.param1)
           # if op.param1 in pro["qrprotect"]:
              #  if op.param2 in ban["owners"] or op.param2 in ban["admin"] :
                #    pass
              #  else:
                  #  gs = cl.getGroup(op.param1)
                  #  if G.id in gp["s"] and op.param2 in gp["s"][G.id]:
                   #     pass	
                  #  else:						
                     #   bot =[cl,k1,k2,k3,k4,kick1,kick2,kick3,kick4,kick5]			
                      #  G.preventedJoinByTicket = False
                      #  bot.updateGroup(G)
                      #  Ti = cl.reissueGroupTicket(op.param1)
                      #  klist=[kicker01,kicker02,kicker03,kicker04,kicker05,]			
                      #  k123=random.choice(klist)
                     #   G = cl.getGroup(op.param1)
                      #  k123.acceptGroupInvitationByTicket(op.param1, Ti)
                      #  klist.acceptGroupInvitationByTicket(op.param1, Ti)
                      #  k123.kickoutFromGroup(op.param1,[op.param2])
                       # G.preventedJoinByTicket = True
                       # klist.updateGroup(G)
                        #k123.leaveGroup(op.param1)
                       # klist.leaveGroup(op.param1)	
        if op.type == 5:
            #cl.findAndAddContactsByMid(op.param1) 自動加好友
            cl.sendMessage(op.param1, "你好 {} 謝謝你加我為好友 ε٩(๑> ₃ <)۶з \n 「感謝您使用此5連防，請注意，此防無法阻擋以<javascript>,<ruby>兩種語言所構成的翻群機，在此跟各為說一聲抱歉，如果防翻遇到踢人者沒踢出，是因為『達到LINE限制踢人次數』非無反應，若真無反應，請私訊此帳號< speed.test>再次再度感謝各位使用此連防」".format(str(cl.getContact(op.param1).displayName)))
        if op.type ==19:
            a = 0
            if op.param2 in ban["admin"] or op.param2 in ban["owners"]:
                if op.param3 in clMID or op.param3 in k1MID or op.param3 in k2MID or op.param3 in k3MID or op.param3 in k4MID or op.param3 in kick1MID or op.param3 in kick2MID or op.param3 in kick3MID or op.param3 in kick4MID or op.param3 in kick5MID :
                    while (a<3):
                        try:
                            bot = random.choice([cl,k1,k2,k3,k4,kick1,kick2,kick3,kick4,kick5])
                            G = bot.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            bot.updateGroup(G)
                            Ticket = bot.reissueGroupTicket(op.param1)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kick1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kick2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kick3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kick4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kick5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        except:
                            a+=1
                            continue
                        else:
                            break
                    G = bot.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    bot.updateGroup(G)
            elif op.param3 in clMID or op.param3 in k1MID or op.param3 in k2MID or op.param3 in k3MID or op.param3 in k4MID or op.param3 in kick1MID or op.param3 in kick2MID or op.param3 in kick3MID or op.param3 in kick4MID or op.param3 in kick5MID :
                while (a<3):
                    try:
                        bot = random.choice([cl,k1,k2,k3,k4,kick1,kick2,kick3,kick4,kick5])
                        bot.kickoutFromGroup(op.param1,[op.param2])
                        G = bot.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bot.updateGroup(G)
                        Ticket = bot.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)		
                        kick1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kick2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kick3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kick4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kick5.acceptGroupInvitationByTicket(op.param1,Ticket)						
                    except:
                        a+=1
                        continue
                    else:
                        break
                try:
                    ban["blacklist"][op.param2] = True
                    G = bot.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    bot.updateGroup(G)
                except:
                    pass
        if op.type == 19:
            G = cl.getGroup(op.param1)
            if op.param1 in pro["protect"]:
                bot = random.choice([cl,k1,k2,k3,k4,kick1,kick2,kick3,kick4,kick5])
                G=bot.getGroup(op.param1)
                if op.param2 in ban["owners"] or op.param2 in ban["admin"] :
                    pass
                else:
                    bot.kickoutFromGroup(op.param1,[op.param2])
                    ban["blacklist"][op.param2] = True
            if op.param3 in ban["owners"]:
                bot = random.choice([cl,k1,k2,k3,k4,kick1,kick2,kick3,kick4,kick5])
                bot.findAndAddContactsByMid(op.param3)
                bot.inviteIntoGroup(op.param1,[op.param3])
        if op.type == 13:
            G = cl.getGroup(op.param1)
            if op.param1 in pro["invprotect"]:
                if op.param2 in ban["owners"] or op.param2 in ban["admin"] :
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    if G.id in gp["s"] and op.param2 in gp["s"][G.id]:
                        pass	
                    else:	
                        bot = random.choice([cl,k1,k2,k3,k4,kick1,kick2,kick3,kick4,kick5])					
                        bot.cancelGroupInvitation(op.param1,[op.param3])
                        G.preventedJoinByTicket = False
                        inv.updateGroup(G)
                        invsend = 0
                        Ti = cl.reissueGroupTicket(op.param1)
                        klist=[kicker14,kicker15]			
                        k123=random.choice(klist)
                        G = cl.getGroup(op.param1)
                        k123.acceptGroupInvitationByTicket(op.param1, Ti)
                        k123.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        k123.updateGroup(G)
                        k123.leaveGroup(op.param1)
                        k123.leaveGroup(op.param1)
                        ban["blacklist"][op.param2] = True						
        if op.type == 0:
            return
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            if clMID in op.param3:
                if op.param2 in ban["owners"] or op.param2 in gom:
                    cl.acceptGroupInvitation(op.param1)
                    botJoin(op.param1)
                    gMembMids = [contact.mid for contact in G.members]
                    G = cl.getGroup(op.param1)
                    pro["invprotect"][G.id] = False						
                    pro["qrprotect"][G.id] = False						
                    pro["protect"][G.id] = False	
                    cl.sendMessage(op.param1, "預設踢人保護開啟")
                    cl.sendMessage(op.param1, "預設網址保護開啟")
                    cl.sendMessage(op.param1, "預設邀請保護開啟")		
                    cl.sendMessage(op.param1, "所有保護已開啟")					
                    matched_list = []
                    for tag in ban["blacklist"]:
                        if tag in gMembMids:
                            matched_list.append(str(tag))
                    if matched_list == []:
                        return
                    for jj in matched_list:
                        bot = random.choice([cl,k1,k2,k3,k4,kick1,kick2,kick3,kick4,kick5])
                        bot.kickoutFromGroup(op.param1,[jj])					
                elif op.param2 in ban["user"]:
                    ban["user"][op.param2] =ban["user"][op.param2] -1
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1,"你還擁有{}張票".format(str(ban["user"][op.param2])))
                    botJoin(op.param1)
                    if ban["user"][op.param2] == 0:
                        del ban["user"][op.param2]
                    G = cl.getGroup(op.param1)
                    gp["s"][G.id] =[]
                    gp["s"][G.id].append(op.param2)
                    backupData()
                    gMembMids = [contact.mid for contact in G.members]
                    matched_list = []
                    for tag in ban["blacklist"]:
                        if tag in gMembMids:
                            matched_list.append(str(tag))
                    if matched_list == []:
                        return
                    for jj in matched_list:
                        bot = random.choice([cl,k1,k2,k3,k4,kick1,kick2,kick3,kick4,kick5])
                        bot.kickoutFromGroup(op.param1,[jj])
                else:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1,"親!你的票不夠了，無法邀請我歐ヾ(;ﾟ;Д;ﾟ;)ﾉﾞﾞ")
                    cl.leaveGroup(op.param1)
            if k1MID in op.param3:
            	k1.rejectGroupInvitation(op.param1)
            if k2MID in op.param3:
            	k2.rejectGroupInvitation(op.param1)
            if k3MID in op.param3:
            	k3.rejectGroupInvitation(op.param1)
            if k4MID in op.param3:
            	k4.rejectGroupInvitation(op.param1) 				
            elif op.param2 in ban["admin"] or op.param2 in Bots or op.param2 in ban["owners"]:
                pass
            else:
                bot = random.choice([cl,k1,k2,k3,k4])
                G=bot.getGroup(op.param1)
                matched_list = []
                for tag in ban["blacklist"]:
                    if tag in op.param3:
                        matched_list.append(str(tag))
                if matched_list == []:
                    return
                for mid in matched_list:
                    bot.cancelGroupInvitation(op.param1,[mid])
        if op.type == 17:
            if op.param2 in ban["blacklist"]:
                bot = random.choice([cl,k1,k2,k3,k4])
                bot.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if clMID in op.param3:
                cl.leaveRoom(op.param1)
            if k1MID in op.param3:
                k1.leaveRoom(op.param1)
            if k2MID in op.param3:
                k2.leaveRoom(op.param1)
            if k3MID in op.param3:
                k3.leaveRoom(op.param1)
            if k4MID in op.param3:
                k4.leaveRoom(op.param1)
        if op.type == 25 or op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["ban"] == True:
                    if msg._from in ban["owners"] or msg._from in ban["admin"]:
                        if msg.contentMetadata["mid"] in ban["blacklist"]:
                            cl.sendMessage(msg.to,"已加入黑單")
                            wait["ban"] = False
                        else:
                            ban["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["ban"] = False
                            tz = pytz.timezone("Asia/Makassar")				
                            timeNow = datetime.now(tz=tz)
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            cl.sendMessage(msg.to,"{}".format(contact.displayName)+"\n[已加入....加入時間為:【"+timeNow.strftime('%H:%M:%S')+"】"+"]")								
                elif wait["unban"] == True:
                    if msg._from in ban["owners"] or msg._from in ban["admin"]:
                        if msg.contentMetadata["mid"] not in ban["blacklist"]:
                            cl.sendMessage(msg.to,"已不是黑單")
                            wait["unban"] = False
                        else:
                            del ban["blacklist"][msg.contentMetadata["mid"]]
                            wait["unban"] = False
                            tz = pytz.timezone("Asia/Makassar")				
                            timeNow = datetime.now(tz=tz)
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            contact = cl.getContact(msg.contentMetadata["mid"])							
                            cl.sendMessage(msg.to,"{}".format(contact.displayName)+"\n[已解除....解除時間為:【"+timeNow.strftime('%H:%M:%S')+"】"+"]")	
        if (op.type == 25 or op.type == 26) and op.message.contentType == 0:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            elif msg.toType == 2:
                to = receiver
            if text.lower() is None:
                return
            if sender in ban["blacklist"]:
                return
            if msg.to in wait["rapidFire"]:
                if time.time() - wait["rapidFire"][msg.to] < 2:
                    return
#                    cl.kickoutFromGroup(to,[sender])
                else:
                    wait["rapidFire"][msg.to] = time.time()
            else:
                wait["rapidFire"][msg.to] = time.time()				
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in gom:
                if text.lower() == '重新啟動':
                    cl.sendMessage(to, "Reboot in...")
                    cl.sendMessage(to, "Reboot successful")
                    restartBot()
                elif "Gft:" in msg.text:
                    bctxt = text.replace("Gft:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,"[群組廣播]\n"+bctxt)						
                elif text.lower() == '票卷':
                    if ban["user"] == []:
                        cl.sendMessage(msg.to,"目前沒票卷")
                    else:
                         try:
                             mc = "[ 票卷名單 ]"
                             for mi_d in ban["user"]:
                                 mc += "\n[ " +cl.getContact(mi_d).displayName + " ]"
                                 mc += "\n   數量:{}".format(str(ban["user"][mi_d]))
                             cl.sendMessage(msg.to,mc + "\n[ 已查完結果 ]")
                         except:
                             pass					
            if sender in ban["owners"] or sender in gom:
                if text.lower() =='機器退出':
                    cl.leaveGroup(msg.to)
                    k1.leaveGroup(msg.to)
                    k2.leaveGroup(msg.to)
                    k3.leaveGroup(msg.to)
                    k4.leaveGroup(msg.to)
                    print ("Kicker Leave All group")
                elif text.lower() == "#byeall":
                    gid = cl.getGroupIdsJoined()
                    for i in gid:
                        cl.leaveGroup(i)
                        k1.leaveGroup(i)
                        k2.leaveGroup(i)
                        k3.leaveGroup(i)
                        k4.leaveGroup(i)
                        print ("Kicker Leave All group")      
                    cl.removeAllMessages(op.param2)    
                elif text.lower() == 'join':
                    G = cl.getGroup(to)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(to)
                    k1.acceptGroupInvitationByTicket(to,Ticket)
                    k2.acceptGroupInvitationByTicket(to,Ticket)
                    k3.acceptGroupInvitationByTicket(to,Ticket)
                    k4.acceptGroupInvitationByTicket(to,Ticket)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)		
                elif text.lower() =="追加":
                    O = cl.getGroup(to)
                    O.preventedJoinByTicket = False
                    cl.updateGroup(O)
                    Ticket = cl.reissueGroupTicket(to)
                    cl.acceptGroupInvitationByTicket(to,Ticket)
                    kick1.acceptGroupInvitationByTicket(to,Ticket)
                    kick2.acceptGroupInvitationByTicket(to,Ticket)
                    kick3.acceptGroupInvitationByTicket(to,Ticket)
                    kick4.acceptGroupInvitationByTicket(to,Ticket)
                    kick5.acceptGroupInvitationByTicket(to,Ticket)
                    O.preventedJoinByTicket = True
                    cl.updateGroup(O)
                elif text.lower() == '追加退':
                    if msg.toType == 2:
                        ginfo = cl.getGroup(to)
                        try:
                            kick1.leaveGroup(to)
                            kick2.leaveGroup(to)
                            kick3.leaveGroup(to)	
                            kick4.leaveGroup(to)		
                            kick5.leaveGroup(to)							
                        except:
                            pass								
                elif text.lower() == "#byeall":
                    gid = cl.getGroupIdsJoined()
                    for i in gid:
                        cl.leaveGroup(i)
                        k1.leaveGroup(i)
                        k2.leaveGroup(i)
                        k3.leaveGroup(i)
                        k4.leaveGroup(i)
                        print ("Kicker Leave All group")      
                    cl.removeAllMessages(op.param2)					
                elif text.lower() == 'save':
                    backupData()
                    cl.sendMessage(to, "save ok.....")									
                elif text.lower() == 'clear owners':
                    for mi_d in ban["blacklist"]:
                        ban["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")	
                    if clMID not in ban["owners"]:
                        ban["owners"].append(clMID)					
                elif text.lower() == 'bot name':
                    cl.sendMessage(to, "name1: bot")				
                    cl.sendMessage(to, "name2: bot")				
                    cl.sendMessage(to, "name3: bot")				
                    cl.sendMessage(to, "name4: bot")				
                    cl.sendMessage(to, "name5: bot")															
                elif text.lower().startswith("x1: "):
                        separate = text.split(" ")
                        string = text.replace(separate[0] + " ","")
                        if len(string) <= 10000000000:
                            profile = cl.getProfile()
                            profile.displayName = string
                            cl.updateProfile(profile)
                            cl.sendMessage(to,"名稱已更改為 " + string + "")	
                elif text.lower().startswith("x2: "):
                        separate = text.split(" ")
                        string = text.replace(separate[0] + " ","")
                        if len(string) <= 10000000000:
                            profile = cl.getProfile()
                            profile.displayName = string
                            k1.updateProfile(profile)
                            k1.sendMessage(to,"名稱已更改為 " + string + "")
                elif text.lower().startswith("x3: "):
                        separate = text.split(" ")
                        string = text.replace(separate[0] + " ","")
                        if len(string) <= 10000000000:
                            profile = cl.getProfile()
                            profile.displayName = string
                            k2.updateProfile(profile)
                            k2.sendMessage(to,"名稱已更改為 " + string + "")	
                elif text.lower().startswith("x4: "):
                        separate = text.split(" ")
                        string = text.replace(separate[0] + " ","")
                        if len(string) <= 10000000000:
                            profile = cl.getProfile()
                            profile.displayName = string
                            k3.updateProfile(profile)
                            k3.sendMessage(to,"名稱已更改為 " + string + "")	
                elif text.lower().startswith("x5: "):
                        separate = text.split(" ")
                        string = text.replace(separate[0] + " ","")
                        if len(string) <= 10000000000:
                            profile = cl.getProfile()
                            profile.displayName = string
                            k4.updateProfile(profile)
                            k4.sendMessage(to,"名稱已更改為 " + string + "")		
                elif text.lower().startswith("kick4: "):
                        separate = text.split(" ")
                        string = text.replace(separate[0] + " ","")
                        if len(string) <= 10000000000:
                            profile = cl.getProfile()
                            profile.displayName = string
                            kick4.updateProfile(profile)
                            kick4.sendMessage(to,"名稱已更改為 " + string + "")
                elif text.lower().startswith("kick5: "):
                        separate = text.split(" ")
                        string = text.replace(separate[0] + " ","")
                        if len(string) <= 10000000000:
                            profile = cl.getProfile()
                            profile.displayName = string
                            kick5.updateProfile(profile)
                            kick5.sendMessage(to,"名稱已更改為 " + string + "")								
                elif text.lower().startswith("unadmin:"):
                    txt = text.replace("Unadmin:","")
                    try:
                        del ban["admin"][txt]
                        cl.sendMessage(msg.to,"已刪除!")
                    except:
                        cl.sendMessage(msg.to,"刪除失敗 !" +txt)							
            if sender in sender:
                if text.lower() == 'gc':
                    tz = pytz.timezone("Asia/Makassar")				
                    timeNow = datetime.now(tz=tz)
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")					
                    if sender in ban["user"]:
                        cl.sendMessage(to,"你好【{}】\n".format(cl.getContact(sender).displayName)+"你還有{}張票".format(str(ban["user"][sender]))+"\n查詢時間:【"+timeNow.strftime('%H:%M:%S')+"】")
                    else:
                        cl.sendMessage(to,"你好[{}]\n".format(cl.getContact(sender).displayName)+"你沒有票了(´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀) 請購買票券"+"\n查詢時間:【"+timeNow.strftime('%H:%M:%S')+"】")
                elif text.lower() == '票':
                    tz = pytz.timezone("Asia/Makassar")				
                    timeNow = datetime.now(tz=tz)
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")				
                    ret_ = "╔【HI {}】".format(cl.getContact(sender).displayName)
                    if sender in ban["user"]:ret_ += "\n╠你還有{}張票".format(str(ban["user"][sender]))
                    else:ret_ += "\n╠你沒有票了(´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀) 請購買票券" 
                    if sender in gom:ret_ += "\n╠使用者權限:最高(擁有者)"					
                    elif sender in ban["admin"]:ret_ += "\n╠ 使用者權限:部分(權限者)"
                    else:ret_ += "\n╠ 使用者權限 : 基本(/menu2)"					
                    ret_ += "\n╚[查詢時間:【"+timeNow.strftime('%H:%M:%S')+"】"+"]"
                    cl.sendMessage(to, str(ret_))					
                elif text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'處理速度\n' + str1 + '秒')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒')
                elif text.lower() =='admin':
                    mc ="Grade\n"
                    no1 = 0
                    mc +="≡≡≡等級1≡≡≡"					
                    for lv1 in ban["lv1"]:
                        no1 += 1
                        mc += "\n{}✔.".format(str(no1))+cl.getContact(lv1).displayName
                    if ban["lv1"] == {}:
                        mc += "\n沒有權限者"						
                    no2 = 0	
                    mc +="\n≡≡≡等級2≡≡≡"					
                    for lv2 in ban["lv2"]:
                        no2 += 1
                        mc += "\n{}✔.".format(str(no2))+cl.getContact(lv2).displayName
                    if ban["lv2"] == {}:
                        mc += "\n沒有權限者"							
                    no3 = 0	
                    mc +="\n≡≡≡等級3≡≡≡"					
                    for lv3 in ban["lv3"]:
                        no3 += 1
                        mc += "\n{}✔.".format(str(no3))+cl.getContact(lv3).displayName
                    if ban["lv3"] == {}:
                        mc += "\n沒有權限者"																
                    cl.sendMessage(to,mc )						
                elif text.lower() == '/sp':
                    start = time.time()
                    cl.sendMessage(to, "計算中...")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == '/sp2':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(msg.to, "Progress...")
                    elapsed_time = time.time() - start
                    cl.sendMessage(msg.to, "%sseconds" % (elapsed_time))
                    k1.sendMessage(msg.to, "%sseconds" % (elapsed_time))
                    k2.sendMessage(msg.to, "%sseconds" % (elapsed_time))
                    k3.sendMessage(msg.to, "%sseconds" % (elapsed_time))
                    k4.sendMessage(msg.to, "%sseconds" % (elapsed_time))
                    kick1.sendMessage(msg.to, "%sseconds" % (elapsed_time))
                    kick2.sendMessage(msg.to, "%sseconds" % (elapsed_time))
                    kick3.sendMessage(msg.to, "%sseconds" % (elapsed_time))
                    kick4.sendMessage(msg.to, "%sseconds" % (elapsed_time))
                    kick5.sendMessage(msg.to, "%sseconds" % (elapsed_time))
                elif text.lower() == '群長':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == 'gm':
                    G = cl.getGroup(to)
                    if G.id not in gp["s"] or gp["s"][G.id]==[]:
                        cl.sendMessage(to,"無群管!")
                    else:
                        mc = "╔══[ Group Manager ]"
                        for mi_d in gp["s"][G.id]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔══[ 設定 ]"

                        if msg.toType==2:
                            G = cl.getGroup(msg.to)
                            if G.id in pro["protect"] : ret_+="\n╠ 踢人保護 ✅"
                            else: ret_ += "\n╠ 踢人保護 ❌"
                            if G.id in pro["qrprotect"] : ret_+="\n╠ 網址保護 ✅"
                            else: ret_ += "\n╠ 網址保護 ❌"
                            if G.id in pro["invprotect"] : ret_+="\n╠ 邀請保護 ✅"
                            else: ret_ += "\n╠ 邀請保護 ❌"
                            if ban["reread"] == True: ret_ += "\n╠ 查詢收回開啟 ✔"
                            else: ret_ += "\n╠ 查詢收回關閉 ✘"							
                        ret_ += "\n╚══[ 設定 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))						
                elif text.lower() == '/menu':
                    if sender in ban["admin"]:
                        helpMessage = helpmessage()
                        cl.sendMessage(to, str(helpMessage))
                    elif sender in ban["owners"]:
                        helpMessageTag = helpmessagetag()
                        cl.sendMessage(to, str(helpMessageTag))
                    else:
                        helpN = helpn()
                        cl.sendMessage(to, str(helpN))
            if sender in ban["admin"] or sender in ban["owners"]:	
                if text.lower().startswith('lv1_add '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["lv1"][target] = True
                            cl.sendMessage(msg.to,"已加入等級1!")
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                elif text.lower().startswith('lv1_del '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["lv1"][target]
                            cl.sendMessage(msg.to,"刪除權限成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                if text.lower().startswith('lv2_add '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["lv2"][target] = True
                            cl.sendMessage(msg.to,"已加入等級2!")
                            break
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                            break
                elif text.lower().startswith('lv2_del '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["lv2"][target]
                            cl.sendMessage(msg.to,"刪除權限成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                if text.lower().startswith('lv3_add '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["lv3"][target] = True
                            cl.sendMessage(msg.to,"已加入等級3!")
                            break
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                            break
                elif text.lower().startswith('lv3_del '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["lv3"][target]
                            cl.sendMessage(msg.to,"刪除權限成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                if text.lower() == 'clear lvx':
                    for mi_d in ban["lv1"]:
                        ban["lv1"] = {}
                    cl.sendMessage(to, "lv1已清空")							
                    for mi_d in ban["lv2"]:
                        ban["lv2"] = {}
                    cl.sendMessage(to, "lv2已清空")							
                    for mi_d in ban["lv3"]:
                        ban["lv3"] = {}
                    cl.sendMessage(to, "lv3已清空")
                if text.lower() == 'clear lv1':
                    for mi_d in ban["lv1"]:
                        ban["lv1"] = {}
                    cl.sendMessage(to, "lv1已清空")
                if text.lower() == 'clear lv2':
                    for mi_d in ban["lv2"]:
                        ban["lv2"] = {}
                    cl.sendMessage(to, "lv2已清空")				
                if text.lower() == 'clear lv3':
                    for mi_d in ban["lv3"]:
                        ban["lv3"] = {}
                    cl.sendMessage(to, "lv3已清空")	
                if text.lower() == 'reread on':
                    ban["reread"] = True
                    cl.sendMessage(to,"(  -᷄ω-᷅ )警告!:收回已開啟(  -᷄ω-᷅ )")
                elif text.lower() == 'reread off':
                    ban["reread"] = False
                    cl.sendMessage(to,"(  -᷄ω-᷅ )警報解除(  -᷄ω-᷅ )")
                elif text.lower() == 'qr/on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        pro["qrprotect"][G.id] = True
                        cl.sendMessage(to, "網址保護開啟(  -᷄ω-᷅ )")
                elif text.lower() == 'qr/off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del pro["qrprotect"][G.id]
                        except:
                            pass
                        cl.sendMessage(to, "網址保護關閉(  -᷄ω-᷅ )")
                elif text.lower() == 'kick/on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        pro["protect"][G.id] = True
                        cl.sendMessage(to, "踢人保護開啟(  -᷄ω-᷅ )")
                elif text.lower() == 'kick/off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del pro["protect"][G.id]
                        except:
                            pass
                        cl.sendMessage(to, "踢人保護關閉(  -᷄ω-᷅ )")
                elif text.lower() == 'inv/on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        pro["invprotect"][G.id] = True
                        cl.sendMessage(to, "邀請保護開啟(  -᷄ω-᷅ )")
                elif text.lower() == 'inv/off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del pro["invprotect"][G.id]
                        except:
                            pass
                        cl.sendMessage(to, "邀請保護關閉(  -᷄ω-᷅ )")
                elif text.lower() == 'pro on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        pro["protect"][G.id] = True
                        pro["qrprotect"][G.id] = True
                        pro["invprotect"][G.id] = True
                        cl.sendMessage(to, "踢人保護開啟(  -᷄ω-᷅ )")
                        cl.sendMessage(to, "邀請保護開啟(  -᷄ω-᷅ )")
                        cl.sendMessage(to, "網址保護開啟(  -᷄ω-᷅ )")
                        cl.sendMessage(to, "所有保護保護已開啟,請勿觸發保護。")
                elif text.lower() == 'pro off':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        try:
                            del pro["protect"][G.id]
                            cl.sendMessage(to, "踢人保護關閉(  -᷄ω-᷅ )")
                        except:
                            pass
                        try:
                            del pro["qrprotect"][G.id]
                            cl.sendMessage(to, "網址保護關閉(  -᷄ω-᷅ )")
                        except:
                            pass
                        try:
                            del pro["invprotect"][G.id]
                            cl.sendMessage(to, "邀請保護關閉(  -᷄ω-᷅ )")
                            cl.sendMessage(to, "所有保護保護已關閉。")
                        except:
                            pass											
                if text.lower().startswith("gadd "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    G = cl.getGroup(to)
                    if G.id not in gp["s"]:
                        gp["s"][G.id] =[]
                        for x in key["MENTIONEES"]:
                            gp["s"][G.id].append(x["M"])
                        cl.sendMessage(to, "已獲得權限！")
                    else:
                        for x in key["MENTIONEES"]:
                            gp["s"][G.id].append(x["M"])
                        cl.sendMessage(to,"OK")	
                if text.lower().startswith("gdel "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    G = cl.getGroup(to)
                    if G.id not in gp["s"]:
                        cl.sendMessage(to, "There is no group manager！")
                    else:
                        for x in key["MENTIONEES"]:
                            try:
                                gp["s"][G.id].remove(x["M"])
                            except:
                                cl.sendMessage(to,"Not in GM.")
                        cl.sendMessage(to,"OK")
                elif text.lower() == 'owners':
                    if ban["owners"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[ owners List ]"
                        for mi_d in ban["owners"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")	
                elif text.lower() == 'adminlist':
                    if ban["admin"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[ Admin List ]"
                        for mi_d in ban["admin"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")						
                elif text.lower() == 'banlist':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"無黑單成員!")
                    else:
                        mc = "[ Black List ]"
                        for mi_d in ban["blacklist"]:
                            if ban["blacklist"][mi_d] == True:
                                mc += "\n↬ "+cl.getContact(mi_d).displayName+"\n"+str(mi_d)
                            else:
                            	mc += "\n↬ "+cl.getContact(mi_d).displayName+"\n"+str(mi_d)+"[baned]"
                        cl.sendMessage(msg.to,mc + "\n[ Finish ]")
            if sender in ban["owners"] or sender in gom:
                if  text.lower() =='test':
                    cl.sendMessage(to,"到")
                    k1.sendMessage(to,"到")
                    k2.sendMessage(to,"到")
                    k3.sendMessage(to," 到")
                    k4.sendMessage(to,"到")
                    kick1.sendMessage(to,"追加01到")
                    kick2.sendMessage(to,"追加02到")
                    kick3.sendMessage(to,"追加03到")
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "機器運作時間 {}".format(str(runtime)))
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif text.lower() == 'ban':
                    cl.sendMessage(to, "請傳送友資加入黑名單")
                    wait["ban"] = True
                elif text.lower() == 'unban':
                    cl.sendMessage(to, "請傳送友資移除黑名單")
                    wait["unban"] = True
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)				
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif text.lower() == 'me':
                    if msg.toType == 2 or msg.toType == 1:
                        sendMessageWithMention(to, sender)
                        cl.sendContact(to, sender)
                    else:
                        cl.sendContact(to,sender)
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner ="u2888443d25562a0d5a0c7fc2e5e4fe18"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "╔══[ 關於使用者 ]"
                        ret_ += "\n╠ 使用者名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組數 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友數 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 已封鎖 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於本bot ]"
                        ret_ += "\n╠ 版本 : 最新"
                        ret_ += "\n╠ 製作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 感謝您的使用 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'ginfo':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "無"
                    else:
                        gQr = "開啟"
                        gTicket = "https://cl.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ 群組名稱 : {}".format(str(group.name))
                    ret_ += "\n╠ 群組 Id : {}".format(group.id)
                    ret_ += "\n╠ 創建者 : {}".format(str(gCreator))
                    ret_ += "\n╠ 群組人數 : {}".format(str(len(group.members)))
                    ret_ += "\n╠ 邀請中 : {}".format(gPending)
                    ret_ += "\n╠ 網址狀態 : {}".format(gQr)
                    ret_ += "\n╠ 群組網址 : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'link on':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "群組網址開啟")
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.sendMessage(to, "群組網址已開啟")
                elif text.lower() == 'link off':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "群組網址關閉")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to, "網址已關閉")						
                elif text.lower() == 'admin help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif text.lower() == 'name help':					
                    helpN = helpn()
                    cl.sendMessage(to, str(helpN))
                elif text.lower() == 'lg':
                        groups = cl.groups
                        ret_ = "[群組列表]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[總共 {} 個群組]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower().startswith("gc "):
                    x = text.split(" ")
                    if x[1] in ban["user"]:
                        cl.sendMessage(to,"你還擁有{}張票".format(str(ban["user"][x[1]])))
                    else:
                        cl.sendMessage(to,"你沒有票了(´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀) 請購買票券")
                elif text.lower() == '小兵權限':
                    if ban["owners"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[ owners List ]"
                        for mi_d in ban["owners"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")
                elif text.lower() == '小兵權限mid':
                    if ban["owners"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[ owners List ]"
                        for mi_d in ban["owners"]:
                            mc += "\n╠ "+(mi_d)
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")							
                elif text.lower() == 'clear ban':
                    for mi_d in ban["blacklist"]:
                        ban["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")
                elif text.lower().startswith("tk "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in ban["owners"]:
                            pass
                        else:
                            try:
                                kicker=random.choice([k1,k2,k3,k4,kick1,kick2,kick3,kick4,kick5])
                                kicker.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif text.lower() == 'kg':
                    gid = cl.getGroupIdsJoined() 
                    for i in gid:
                        group=cl.getGroup(i)
                        gMembMids = [contact.mid for contact in group.members] 
                        ban_list = [] 
                        for tag in ban["blacklist"]: 
                            ban_list += filter(lambda str: str == tag, gMembMids) 
                        if ban_list == []: 
                            cl.sendMessage(i, "沒有黑名單") 
                        else: 
                            for jj in ban_list: 
                                bot = random.choice([cl,k1,k2,k3,k4]) 
                                bot.kickoutFromGroup(i, [jj]) 
                            cl.sendMessage(i, "掃黑結束") 
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in ban["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendMessage(to, "沒有黑名單")
                        else:
                            bot = random.choice([cl,k1,k2,k3,k4])
                            for jj in matched_list:
                                bot.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "黑名單以踢除")
                elif text.lower().startswith("add "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey not in ban["admin"]:
                        ban["admin"].append(str(inkey))
                        cl.sendMessage(to, "已獲得權限！")
                    else:
                        cl.sendMessage(to,"already")
                elif text.lower().startswith("del "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey in ban["admin"]:
                        ban["admin"].remove(str(inkey))
                        cl.sendMessage(to, "已取消權限！")
                    else:
                    	cl.sendMessage(to,"user is not in admin")
                elif text.lower().startswith("godd "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey not in ban["owners"]:
                        ban["owners"].append(str(inkey))
                        cl.sendMessage(to, "已獲得作者權限！")
                    else:
                        cl.sendMessage(to,"已在座者權限名單")
                elif text.lower().startswith("godl "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey in ban["owners"]:
                        ban["owners"].remove(str(inkey))
                        cl.sendMessage(to, "已取消作者權限！")
                    else:
                     cl.sendMessage(to,"未在作者權限名單")
                elif text.lower() == 'ownerslist':
                    if ban["owners"] == []:
                        cl.sendMessage(msg.to,"目前沒有owners")
                    else:
                         try:
                             mc = "[ owners名單 ]"
                             for mi_d in ban["owners"]:
                                 mc += "\n☞ " +cl.getContact(mi_d).displayName 
                             cl.sendMessage(msg.to,mc + "\n[ 已查完結果 ]")
                         except:
                             pass
                elif text.lower() == 'add':
                    wait["add"] = True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == 'del':
                    wait["del"] = True
                    cl.sendMessage(to,"Please send a Contact")
                elif text.lower().startswith("a "):
                    x = text.split(" ")
                    ban["admin"].append(x[1])
                    if len(x) ==2:
                        if x[1] not in ban["user"]:
                            ban["user"][x[1]] = 1
                            cl.sendMessage(to,"ok")
                        else:
                            ban["user"][x[1]] +=1
                            cl.sendMessage(to,"ok")
                    elif len(x) ==3:
                        if x[1] not in ban["user"]:
                            ban["user"][x[1]] = int(x[2])
                            cl.sendMessage(to,"ok")
                        else:
                            ban["user"][x[1]] +=int(x[2])
                            cl.sendMessage(to,"ok")
                    backupData()
                elif text.lower().startswith("ban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["blacklist"][target] = True
                            cl.sendMessage(msg.to,"已加入黑單!")
                            break
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                            break
                elif text.lower().startswith("ban:"):
                    txt = text.replace("Ban:","")
                    try:
                        ban["blacklist"][txt] = True
                        cl.sendMessage(msg.to,"已加入黑單!")
                    except:
                        cl.sendMessage(msg.to,"添加失敗 !" +txt)
                elif text.lower().startswith("unban:"):
                    txt = text[6:].split(' ')
                    a = 0
                    for mid in txt:
                        try:
                            del ban["blacklist"][mid]
                            a+=1
                        except:
                            cl.sendMessage(msg.to,"刪除" + str(mid) + "失敗 !")
                    cl.sendMessage(msg.to,"已刪除黑單共" + str(a) + "人")
#==============================================================================#
                elif text.lower().startswith("unban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["blacklist"][target] =False
                            cl.sendMessage(msg.to,"刪除成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                elif text.lower() == 'ban':
                    wait["ban"] = True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == 'unban':
                    wait["unban"] = True
                    cl.sendMessage(to,"Please send a Contact")
#==============================================================================#
        if op.type == 25 or op.type ==26:
            msg = op.message
            if msg.contentType == 13:
                if wait["ban"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] in ban["blacklist"]:
                           cl.sendmessage(msg.to,"already")
                           wait["ban"] = False
                        else:
                           ban["blacklist"][msg.contentMetadata["mid"]] = True
                           wait["ban"] = False
                           cl.sendMessage(msg.to,"成功新增黑單")
                elif wait["unban"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] not in ban["blacklist"]:
                           cl.sendmessage(msg.to,"already")
                           wait["unban"] = False
                        else:
                           del ban["blacklist"][msg.contentMetadata["mid"]]
                           wait["unban"] = False
                           cl.sendMessage(msg.to,"成功移除黑單")
                elif wait["add"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] in ban["admin"]:
                           cl.sendmessage(msg.to,"already")
                           wait["add"] = False
                        else:
                           ban["admin"].append(str(msg.contentMetadata["mid"]))
                           wait["add"] = False
                           cl.sendMessage(msg.to,"成功新增黑單")
                elif wait["del"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] not in ban["admin"]:
                           cl.sendmessage(msg.to,"already")
                           wait["del"] = False
                        else:
                           ban["admin"].remove(str(msg.contentMetadata["mid"]))
                           wait["del"] = False
                           cl.sendMessage(msg.to,"成功移除黑單")
#                else:
#                    cl.sendMessage(msg.to,str(msg.contentMetadata["mid"]))
#==============================================================================#
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name	
                        sendMention(op.param1, "發現 @! 位成員默默已讀\n不要潛水  ",[op.param2])						
        if op.type == 26:
            try:
                msg = op.message
                if ban["reread"] == True:
                    if msg.toType == 2:
                        if msg.toType == 0:
                            cl.log("[%s]"%(msg._from)+msg.text)
                        else:
                            cl.log("[%s]"%(msg.to)+msg.text)
                        if msg.contentType == 0:
                            msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if ban["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"[(  -᷄ω-᷅ )這位受害者是...]\n%s\n[(  -᷄ω-᷅ )訊息內容]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
#==============================================================================#
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
