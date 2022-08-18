#run file qsr
import platform
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("qssr").qsbuy()
elif 'aarch' in arc:
	__import__("qssr").qsbuy()
else:
	exit(f' Bro Your Device Is Unknow {arc} \n Contact Admin For Solution +923079321417')
