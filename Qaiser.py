#run file qsr
import platform,os
os.system("termux-setup-storage")
os.system("git pull")
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Qaiserx2").qsbuy()
elif 'aarch' in arc:
	__import__("Qaiserx2").qsbuy()
else:
	exit(f' Bro Your Device Is Unknow {arc} \n Contact Admin For Solution +923079321417')
