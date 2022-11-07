from glob import glob
import os;
import sqlite3;
import time;
import requests;
import subprocess;
import threading;
import schedule;
_db_address = '/etc/x-ui/x-ui.db'
_max_allowed_connections = 1
_checkCycle = 5 #seconds
_telegrambot_token = '5758012062:AAE8BArx_BlgbY5zsrpEzrOvmUKxw3FaYcs'
_telegram_chat_id = '763234354' # you can get this in @cid_bot bot.
_sv_addr = 'TEST SV'
def getUsers():
    conn = sqlite3.connect(_db_address)
    cursor = conn.execute(f"select id,remark,port from inbounds where id > 0");
    users_list = [];
    for c in cursor:
        users_list.append({'name':c[1],'port':c[2]})
    conn.close();
    return users_list

def disableAccount(user_port):
    conn = sqlite3.connect(_db_address) 
    conn.execute(f"update inbounds set enable = 0 where port={user_port}");
    conn.commit()
    conn.close();
    time.sleep(2)
    os.popen("x-ui restart")
    time.sleep(3)
    
def checkNewUsers():
    conn = sqlite3.connect(_db_address)
    cursor = conn.execute(f"select count(*) from inbounds WHERE id > {_user_last_id}");
    new_counts = cursor.fetchone()[0];
    conn.close();
    if new_counts > 0:
        init()

def fireUP():
    users_list = getUsers();
    for user in users_list:
        checker = AccessChecker(user)
        checker.run()
class AccessChecker():
    def __init__(self, user):
        self.user = user;
    def run(self):
        time.sleep(5)
        print(f"checking {self.user['name']}")
        user_remark = self.user['name'];
        user_port = self.user['port'];
        netstate_data =  os.popen("netstat -np 2>/dev/null | grep :"+str(user_port)+" | awk '{if($3!=0) print $5;}' | cut -d: -f1 | sort | uniq -c | sort -nr | head").read();
        netstate_data = str(netstate_data)
        connection_count =  len(netstate_data.split("\n")) - 1;
        if connection_count > _max_allowed_connections:
           print("c "+str(user_port) + "-"+ str(connection_count)+" - "+str(_max_allowed_connections))
           requests.get(f'https://api.telegram.org/bot{_telegrambot_token}/sendMessage?chat_id={_telegram_chat_id}&text={user_remark}%20locked%20{_sv_addr}')
           disableAccount(user_port=user_port)
           print(f"inbound with port {user_port} blocked")
while True:
    fireUP()
    time.sleep(_checkCycle)
