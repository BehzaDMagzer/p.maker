#!/usr/bin/python2
#Created by BEHZAD KHALIFEH
from sys import platform,exit
import os
import rlcompleter
import time
try:
        from colorama import init,Style,Back,Fore
except:
        os.system('pip install colorama')
        from colorama import init,Style,Back,Fore
init(autoreset=True)
print
ls_name=['First Name -> ','Last Name -> ','Age -> ','Birthday -> ','Mom Name -> ','Dad Name -> ','Phone Number -> ','Friend -> '
         ,'City -> ','Country -> ','Name Girl Friend -> ','Favorite Thing -> ','Favorite Sport -> ']
print Back.GREEN+"                                                      "
banner="""__________    _____          __                       
\\______   \\  /     \\ _____  |  | __ ___________       
 |     ___/ /  \\ /  \\\\__  \\ |  |/ // __ \\_  __ \\      
 |    |    /    Y    \\/ __ \\|    <\\  ___/|  | \\/      
 |____| /\\ \\____|__  (____  /__|_ \\\\___  >__|         
        \\/         \\/     \\/     \\/    \\/             """
print Fore.BLACK+Back.WHITE+banner 
print Back.RED+"                                                      \n"
print Fore.CYAN+Back.WHITE+"Created by BEHZAD KHALIFEH"
ls_value=[]
first_name=''
last_name=''
girl_name=''
zero=0
print
while len(ls_name)>zero:
        try:
                get=raw_input(ls_name[zero])
                if get=='exit':
                        print
                        exit()        
                if zero==0 and get!='':
                	first_name=get
	        elif zero==1 and get!='':
                        last_name=get
                print
                if get!='':
                        ls_value.append(get.lower())
                zero+=1
        except KeyboardInterrupt:
                print
                exit()
passwords=[]
zero=0
one=1
try:
    while len(ls_value)>zero:
        passwords.append(ls_value[zero].lower())
    	passwords.append(ls_value[zero].upper())
    	passwords.append(ls_value[zero].capitalize())
    	passwords.append(ls_value[zero]*2)
    	passwords.append(ls_value[zero]*3)
    	passwords.append(ls_value[zero]*4)
    	passwords.append(ls_value[zero][::-1])
    	passwords.append('mylove'+ls_value[zero])
    	passwords.append('mylife'+ls_value[zero])
    	passwords.append('mymom'+ls_value[zero])
    	passwords.append('mydad'+ls_value[zero])
    	passwords.append('myfreind'+ls_value[zero])
    	passwords.append(ls_value[zero]+'love')
    	passwords.append('ilove'+ls_value[zero])
        for i in range(0,10000):
       	    passwords.append(ls_value[zero]+str(i))
    	for j in range(0,10000):
            passwords.append(str(j)+ls_value[zero])
    	for x in range(0,10000):
            passwords.append(str(x)+ls_value[zero]+str(x))
	zero+=1		
    zero=1
    while len(ls_value)>zero:
	passwords.append(first_name+ls_value[zero])
	passwords.append(ls_value[zero]+first_name)
	passwords.append(ls_value[zero]+first_name+ls_value[zero])
	passwords.append(first_name+ls_value[zero]+first_name)
	zero+=1
    zero=0
    while len(ls_value)>zero:
	passwords.append(last_name+ls_value[zero])
	passwords.append(ls_value[zero]+last_name)
	passwords.append(ls_value[zero]+last_name+ls_value[zero])
	passwords.append(last_name+ls_value[zero]+last_name)
	zero+=1
    for y in range(0,10000):
        passwords.append(str(y))
    passwords.append('qwertyuiop')	
    passwords.append('qwertyuiop'.upper())
    passwords.append('asdfghjkl')	
    passwords.append('asdfghjkl'.upper())
    passwords.append('zxcvbnm')	
    passwords.append('zxcvbnm'.upper())
    passwords.append('qwertyuiopasdfghjklzxcvbnm')	
    passwords.append('qwertyuiopasdfghjklzxcvbnm'.upper())
    passwords.append('qazxswedcvfrtgbnhyujmkliop')
    passwords.append('qazxswedcvfrtgbnhyujmkliop'.upper())
    passwords.append('12345')
    passwords.append('123456')
    passwords.append('1234567')
    passwords.append('12345678')
    passwords.append('123456789')
    passwords.append('1234567890')
    passwords.append('09')
    passwords.append('098')
    passwords.append('0987')
    passwords.append('09876')
    passwords.append('098765')
    passwords.append('0987654')
    passwords.append('09876543')
    passwords.append('098765432')
    passwords.append('0987654321')
    passwords.append(first_name+girl_name+first_name)
    passwords.append(girl_name+first_name+girl_name)
    print Back.BLUE+"Number Of Password => "+Back.RED+str(len(passwords))
    if platform[0:-2]=='win':
        f=open('.\\Password_List.txt','w')
    else:
        f=open('./Password_List.txt','w')
    for r in passwords:
        f.write(r+'\n')
    f.close()
    time.sleep(10000)
except KeyboardInterrupt:
    exit()
