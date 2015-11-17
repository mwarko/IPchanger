import sys
import os
import tkinter
from tkinter.messagebox import *
from tkinter import *

fenetre = tkinter.Tk()
fenetre.title("IPchange by Marc-Antoine FOURNIER")

interface = "laptop"


def exxit():
	if askyesno('Quitter ?', 'Fernando, t\'es sûr de vouloir quitter ce superbe UI ?') :
		sys.exit()
	else :
		pass

def ipoffice():
	os.system("netsh int ip set address " + interface + " static 192.168.42.10 255.255.255.0 192.168.42.1 0")
	os.system("netsh int ip add address name=" + interface + " 192.168.43.10 255.255.255.0 192.168.43.1 0")
	os.system("ipconfig /all")


def dhcp():
	os.system("netsh int ip set address " + interface + " dhcp")
	os.system("netsh int ip set dns " + interface + " dhcp")
	os.system("ipconfig /all")

def ipconfig():
	os.system("ipconfig /all")

def cmd():
	os.system("start cmd.exe")
	os.system("c:")

def pinggoogle():
	os.system("ping 8.8.8.8")


btn_ipoffice = tkinter.Button(fenetre, text = "IPOFFICE", command=ipoffice)
btn_dhcp = tkinter.Button(fenetre, text="DHCP", command=dhcp)
btn_pingwantest = tkinter.Button(fenetre, text="PING GOOGLE", command=pinggoogle)
btn_ipconf = tkinter.Button(fenetre, text="IPCONFIG", command=ipconfig)
btn_cmd = tkinter.Button(fenetre, text="CMD", command=cmd)
btn_quit = tkinter.Button(fenetre, text="EXIT", command=exxit)

btn_ipoffice.pack()
btn_dhcp.pack()
btn_pingwantest.pack()
btn_ipconf.pack()
btn_cmd.pack()
btn_quit.pack()
fenetre.mainloop()