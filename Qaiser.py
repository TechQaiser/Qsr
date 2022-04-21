import os, sys, platform
os.system('git pull')
os.system('termux-setup-storage')
try:

    import requests

except:

    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/2734614926615884/')

from Qsr import qsbuy

qsbuy()

