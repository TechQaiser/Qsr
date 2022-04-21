import os, sys, platform
os.system('git pull')
os.system('termux-setup-storage')
try:

    import requests

except:

    os.system('pip install requests')


from Qsr import qsbuy

qsbuy()

