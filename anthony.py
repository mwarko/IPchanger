import sys
import os
import tkinter
from tkinter.messagebox import *
from tkinter import *

fenetre = tkinter.Tk()
fenetre.title("IPchange by Marc-Antoine FOURNIER")

last = "sweg"
interface = "eth"

def dock():
	global interface 
	interface = "dock"
	global last
	last = texte_last.get()
	lbl_range.configure(text="Choisissez le X dans 192.168.X." + last)


def laptop():
	global interface 
	interface = "laptop"
	global last 
	last = texte_last.get()
	lbl_range.configure(text="Choisissez le X dans 192.168.X." + last)

def exxit():
	if askyesno('Quitter ?', 'Voulez-vous quitter ce superbe UI ?') :
		sys.exit()
	else :
		pass

def change():
	gw = texte_gw.get()
	ran = texte_range.get()
	dns = texte_dns.get()
	os.system("netsh int ip set address " + interface + " static 192.168." + ran + "." + last + " 255.255.255.0 192.168." + ran + "." + gw + " 0")
	os.system("netsh int ip set dns " + interface + " static 192.168." + ran + "." + dns)
	os.system("netsh int ip add dns name=" + interface + " 8.8.8.8")
	os.system("ipconfig /all")

def add():
	gw = texte_gw.get()
	ran = texte_range.get()
	dns = texte_dns.get()
	os.system("netsh int ip add address name=" + interface + " 192.168." + ran + "." + last + " 255.255.255.0 192.168." + ran + "." + gw + " 0")
	os.system("netsh int ip add dns name=" + interface + " 192.168." + ran + "." + dns)
	os.system("ipconfig /all")


def dhcp():
	os.system("netsh int ip set address " + interface + " dhcp")
	os.system("netsh int ip set dns " + interface + " dhcp")
	os.system("ipconfig /all")

def ipconfig():
	os.system("ipconfig /all")

def cmd():
	os.system("start cmd.exe")

def pinggoogle():
	os.system("ping 8.8.8.8")


lbl_int = tkinter.Label(fenetre, text="Quelle interface vous choisissez ?")
btn_dock = tkinter.Button(fenetre, text="DOCK", command=dock)
btn_laptop = tkinter.Button(fenetre, text="LAPTOP", command=laptop)
lbl_range = tkinter.Label(fenetre, text="Choisissez le X dans 192.168.X." + last)
texte_range = tkinter.Entry(fenetre)
lbl_last = tkinter.Label(fenetre, text="Choissisez le Y dans 192.168." + ran + ".Y")
texte_last = tkinter.Entry(fenetre)
lbl_gw = tkinter.Label(fenetre, text="Choisissez la passerelle")
texte_gw = tkinter.Entry(fenetre)
lbl_dns = tkinter.Label(fenetre, text="Choisissez le DNS")
texte_dns = tkinter.Entry(fenetre)
btn_ok = tkinter.Button(fenetre, text = "RESET WITH", command=change)
btn_add = tkinter.Button(fenetre, text="ADD THIS", command=add)
btn_dhcp = tkinter.Button(fenetre, text="DHCP", command=dhcp)
btn_pingwantest = tkinter.Button(fenetre, text="PING GOOGLE", command=pinggoogle)
btn_ipconf = tkinter.Button(fenetre, text="IPCONFIG", command=ipconfig)
btn_cmd = tkinter.Button(fenetre, text="CMD", command=cmd)
btn_quit = tkinter.Button(fenetre, text="EXIT", command=exxit)

lbl_int.pack()
btn_dock.pack(fill=BOTH)
btn_laptop.pack(fill=BOTH)
lbl_range.pack()
texte_range.pack()
lbl_gw.pack()
texte_gw.pack()
lbl_dns.pack()
texte_dns.pack()
btn_ok.pack()
btn_add.pack()
btn_dhcp.pack()
btn_pingwantest.pack()
btn_ipconf.pack()
btn_cmd.pack()
btn_quit.pack()
fenetre.mainloop()