import os, sys, platform

try:

    import requests

except:

    os.system('pip install requests')

if not os.path.isfile('.agents.txt'):

    os.system('curl -L https://raw.githubusercontent.com/TechQaiser/ap/main/.agents.txt > .agents.txt')

    os.system('clear')

from Qsr import qsbuy

qsbuy()

