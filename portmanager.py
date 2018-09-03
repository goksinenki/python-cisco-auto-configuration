#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A script to ssh into a cisco device, set the terminal length
# such that paging is turned off, then run commands.
# the results go into 'resp', then are displayed.
# Tweak to your hearts content!

import cmd
import paramiko
import time
import socket
import sys
import re
import subprocess
import commands
import smtplib
import os
import time
from termcolor import colored
from os import system
import subprocess
import commands
import smtplib
import string
import csv
from email.mime.text import MIMEText
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate

## Text menu in Python
buff = ''
resp = ''
os.system('clear')
os.system('figlet "PORT MANAGER"')
def print_menu():       ## Your menu design here
    print 30 * "-" , "PORT MANAGER MENU" , 30 * "-"
    print (colored('1. Switch Listesi (İzin Verilen)', 'blue','on_white'))
    print (colored('2. Boş Port Bulma', 'blue','on_white'))
    print (colored('3. Port Vlan Değiştirme', 'blue','on_white'))
    print (colored('4. Exit - ÇIKIŞ', 'blue','on_white'))
    print 67 * "-"

loop=True

while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Seçim Yapın [1-4]: ")

    if choice==1:
       my_file = open("ipler.txt", "rb")
       for line in my_file:
           l = [i.strip() for i in line.split(',')]
           Hostname = l[0]
           switchip = l[1]
           print (Hostname,switchip)
       my_file.close()
        ## You can add your code or functions here
    elif choice==2:
        my_file = open("ipler.txt", "rb")
        for line in my_file:
            l = [i.strip() for i in line.split(',')]
            Hostname = l[0]
            switchip = l[1]
        IP = raw_input("Switch IP Addresi Girin (örnek 192.168.x.x): ")
        ## You can add your code or functions here
        with open("ipler.txt") as fp:
            mesaj = MIMEText(fp.read())
            mesaj = str(mesaj)
            if IP in mesaj:
                  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
                  ssh = paramiko.SSHClient()
                  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                  ssh.connect(IP, username='sshusername', password='sshpassword')
                  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                  chan = ssh.invoke_shell()
                  chan.settimeout(20)
                  chan.send('en\n')
                  # enablepassword!
                  chan.send('enablepassword\n')
                  # komutcalistir!
                  chan.send('terminal length 0\n')
                  time.sleep(0.5)
                  chan.send('show int | i proto.*notconnect|proto.*administratively down|Last in.* [6-9]w|Last in.*[0-9][0-9]w|[0-9]y|disabled|Last input never, output never, output hang never | e output\n')
                  time.sleep(3)
                  #while buff.find('OK') < 0:
                  resp = chan.recv(999999)
                  result = resp
                  print (colored('BOŞ PORT LİSTESİ \r\n', 'white','on_red') + result)
                  ssh.close()
            else:
                  print (colored('Belirtilen switch yönetiminiz için izinli değil!', 'white','on_red'))
    elif choice==3:
        kimlik = raw_input("Kullanıcı Adınızı Girin (örnek: D_xxx)): ")
        IP = raw_input("Switch IP Addresi Girin (örnek: 192.168.x.x): ")
        switchint = raw_input("Switch Port Numarası Girin (örnek: Gi2/0/1): ")
        vlanid = raw_input("Vlan ID Girin (örnek: 10 // (NAC için 15 girin)): ")
        with open("ipler.txt") as fp:
                mesaj = MIMEText(fp.read())
                mesaj = str(mesaj)
                if IP in mesaj:
                      if vlanid == "14":
                          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
                          ssh = paramiko.SSHClient()
                          ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                          ssh.connect(IP, username='sshusername', password='sshpassword')
                          ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                          chan = ssh.invoke_shell()
                          chan.settimeout(20)
                          chan.send('en\n')
                          # enablepassword!
                          chan.send('enablepassword\n')
                          # komutcalistir!
                          chan.send('sh run int %s\n'%(switchint))
                          time.sleep(1)
                          resp = chan.recv(999999)
                          eskiconfig = resp
                          chan.send('conf t\n')
                          time.sleep(0.5)
                          chan.send('defa int %s\n'%(switchint))
                          time.sleep(1)
                          chan.send('int %s\n'%(switchint))
                          time.sleep(1)
                          chan.send('switchport access vlan id\n')
                          time.sleep(0.5)
                          chan.send('switchport mode access\n')
                          time.sleep(0.5)
                          chan.send('ip access-group ACL-ALLOW in\n')
                          time.sleep(0.5)
                          chan.send('authentication event fail action next-method\n')
                          time.sleep(0.5)
                          chan.send('authentication event server dead action reinitialize vlan id\n')
                          time.sleep(0.5)
                          chan.send('authentication event server alive action reinitialize\n')
                          time.sleep(0.5)
                          chan.send('authentication host-mode multi-auth\n')
                          time.sleep(0.5)
                          chan.send('authentication open\n')
                          time.sleep(0.5)
                          chan.send('authentication order dot1x mab\n')
                          time.sleep(0.5)
                          chan.send('authentication priority dot1x mab\n')
                          time.sleep(0.5)
                          chan.send('authentication port-control auto\n')
                          time.sleep(0.5)
                          chan.send('authentication violation restrict\n')
                          time.sleep(0.5)
                          chan.send('mab\n')
                          time.sleep(0.5)
                          chan.send('dot1x pae authenticator\n')
                          time.sleep(0.5)
                          chan.send('dot1x timeout tx-period 10\n')
                          time.sleep(0.5)
                          chan.send('spanning-tree portfast\n')
                          time.sleep(0.5)
                          chan.send('shut\n')
                          time.sleep(1)
                          chan.send('no shut\n')
                          time.sleep(1)
                          chan.send('do wr')
                          time.sleep(1)
                          buff = ''
                          while buff.find('OK') < 0:
                              resp = chan.recv(9999)
                              buff += resp
                              print (colored('Vlan Değişikliği Yapıldı', 'white','on_red'))
                              break
                          ssh.close()
                          ths = open('islem_logu.txt', 'w')
                          ths.write('Switch IP:%s\r\nEski Konfig\r\n %s\r\n Yeni Konfig\r\n port vlan %s yapıldı\r\n İşlemi Yapan:%s\n'%(IP,eskiconfig,vlanid,kimlik))
                          ths.close()
                          filePath = r'islem_logu.txt'

                          def sendEmail(TO = "admin1@company.local",
                                        CC = "admin1@company.local",
                                        FROM="portmanager@company.local"):
                              HOST = "mailserver.company.local"

                              msg = MIMEMultipart()
                              msg["From"] = FROM
                              msg["To"] = TO
                              msg["Cc"] = CC
                              msg["Subject"] = " vlan port degisikligi yapildi!".decode('unicode_escape').decode("utf-8")
                              msg['Date']    = formatdate(localtime=True)

                              # attach a file
                              part = MIMEBase('application', "octet-stream")
                              part.set_payload( open(filePath,"rb").read() )
                              Encoders.encode_base64(part)
                              part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filePath))
                              msg.attach(part)

                              server = smtplib.SMTP(HOST)
                              # server.login(username, password)  # optional

                              try:
                                  failed = server.sendmail(FROM, TO, msg.as_string())
                                  server.close()
                              except Exception, e:
                                  errorMsg = "Unable to send email. Error: %s" % str(e)

                          if __name__ == "__main__":
                              sendEmail()
                      else:
                          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
                          ssh = paramiko.SSHClient()
                          ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                          ssh.connect(IP, username='sshusername', password='sshpassword')
                          ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                          chan = ssh.invoke_shell()
                          chan.settimeout(20)
                          chan.send('en\n')
                          # enablepassword!
                          chan.send('enablepassword\n')
                          # komutcalistir!
                          chan.send('sh run int %s\n'%(switchint))
                          time.sleep(1)
                          resp = chan.recv(999999)
                          eskiconfig = resp
                          chan.send('conf t\n')
                          time.sleep(0.5)
                          chan.send('defa int %s\n'%(switchint))
                          time.sleep(1)
                          chan.send('int %s\n'%(switchint))
                          time.sleep(1)
                          chan.send('switchport mode access\n')
                          time.sleep(0.5)
                          chan.send('switchport access vlan %s\n'%(vlanid))
                          time.sleep(0.5)
                          chan.send('shut\n')
                          time.sleep(1)
                          chan.send('no shut\n')
                          time.sleep(1)
                          chan.send('do wr')
                          time.sleep(1)
                          buff = ''
                          while buff.find('OK') < 0:
                              resp = chan.recv(9999)
                              buff += resp
                              print (colored('Vlan Değişikliği Yapıldı', 'white','on_red'))
                              break
                          ssh.close()
                          ths = open('islem_logu.txt', 'w')
                          ths.write('Switch IP:%s\r\nEski Konfig\r\n %s\r\n Yeni Konfig\r\n port vlan %s yapıldı\r\n İşlemi Yapan:%s\n'%(IP,eskiconfig,vlanid,kimlik))
                          ths.close()
                          filePath = r'islem_logu.txt'
                          def sendEmail(TO = "admin1@company.com",
                                        CC = "admin2@company.com",
                                        FROM="portmanager@company.com"):
                              HOST = "mailserver.company.local"

                              msg = MIMEMultipart()
                              msg["From"] = FROM
                              msg["To"] = TO
                              msg["Cc"] = CC
                              msg["Subject"] = "vlan port degisikligi yapildi!".decode('unicode_escape').decode("utf-8")
                              msg['Date']    = formatdate(localtime=True)

                              # attach a file
                              part = MIMEBase('application', "octet-stream")
                              part.set_payload( open(filePath,"rb").read() )
                              Encoders.encode_base64(part)
                              part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filePath))
                              msg.attach(part)

                              server = smtplib.SMTP(HOST)
                              # server.login(username, password)  # optional

                              try:
                                  failed = server.sendmail(FROM, TO, msg.as_string())
                                  server.close()
                              except Exception, e:
                                  errorMsg = "Unable to send email. Error: %s" % str(e)

                          if __name__ == "__main__":
                              sendEmail()
                else:
                      print (colored('Belirtilen switch yönetiminiz için izinli değil!', 'white','on_red'))
    elif choice==4:
        print "ÇIKIŞ YAPILDI - PENCEREYİ KAPATABİLİRSİNİZ!"
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Yanlış seçim yapıldı. Tekrar deneyin..")
