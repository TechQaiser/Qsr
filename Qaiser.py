import os, sys, platform

try:

    import requests

except:

    os.system('pip install requests')


from Qsr import qsbuy

qsbuy()

