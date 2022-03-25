#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Sabiha
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2022


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

#Sa:Bi_Ha
##### LOGO #####
logo = """

              ██████████████
                ██████████
                  ██████
                    ███
⓿⸙๏๏⸙❮𝐌𝐒 SABIHA 𝐇𝐄𝐑𝐄 QUEEN 𝐎𝐅 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 ❯⸙๏๏⸙⓿
                    ███ 
                  ██████
                ██████████
              ██████████████

---------------------------------------------
\033[1;96m|-------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-----|
\033[1;96m|               QUEEN 𝐎𝐅 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊               |
\033[1;96m|This Tool is Only for Bangladesh FACEBOOK CLONER|
\033[1;96m|------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+------|

\033[1;91m [⚡\033[1;97mAuthor Name: SABIHA     ⚡\033[1;91m]
\033[1;91m [⚡\033[1;97mYutube Chnl: m.youtube.com/channel/UCELUcwsMUQrgKKvlO_WvVcw ⚡\033[1;91m]
\033[1;91m [⚡       \033[1;97mFrom: BANGLADESH      ⚡\033[1;91m]
\033[1;95m«-_-_-_-_-_-_-_-_-\033[1;91mJESMIN\033[1;95m-_-_-_-_-_-_-_-_-»
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
┏━━━•| 💚 |•━━━┓
🔶
🔷
◢▔▔▔◣
╔╝💀╚╗
╠☞𝐌𝐒 JESMIN ☜╣
╚╗𝐌𝐒 SABIHA╔╝
◥▂▂▂◤
🔷
🔶
●▬▬▬▬●
●▬▬▬●
┗━━•| 💙 |•━━┛
\033[1;95m«-_-_-_-_-_-_-_-_-\033[1;91mQUEEN 𝐎𝐅 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊\033[1;95m-_-_-_-_-_-_-_-_-»
\033[1;92mNote1: Enter Tool usernam and Password 
\033[1;92mNote2: This Tool is only for Bangladesh
\033[1;95m«-_-_-_-_-_-_-_-_-\033[1;91mQUEEN 𝐎𝐅 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊\033[1;95m-_-_-_-_-_-_-_-_-»
 """
CorrectUsername = "SABIHA QUEEN"
CorrectPassword = "JESMIN QUEEN"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m \x1b[1;91mTool Username \x1b[1;91m: \x1b[1;92m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m \x1b[1;91mTool Password \x1b[1;91m: \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #SABIHA
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;93mWrong Password"
            os.system('xdg-open https://.youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://youtube.com/channel/UCELUcwsMUQrgKKvlO_WvVcw')

