import struct,os,sys
os.system('git pull')
my_bit = struct.calcsize("P") * 8
os.system('rm -rf README*')
#----[UPDATE-RESET]----#
try:
    if sys.argv[1] == 'update' or 'upgrade':    os.remove('qsr.cpython-311.so')
    if sys.argv[1] == 'reset':    os.remove('qsr.cpython-311.so')
    if sys.argv[1] == 'help':    print(' +923197951814 contact admin for help ')
    if sys.argv[1] == 'module':
        os.system('chmod 777 *')
        os.remove('rm -rf b*')
        os.remove('rm -rf s*')
        os.system('curl -L https://github.com/TechQaiser/Qsr/blob/main/mod.7z?raw=true -o mod.7z')
    else:    exit('Non Define Keyword')
except:    pass
#-----------------------------------#

if my_bit == 64:
	if not os.path.isfile('soupsieve'):
		os.system('unzip mod.zip')
		os.system('rm -rf mod.zip')
	if os.path.isfile('qsr.cpython-311.so'):
		os.system('git pull')
		import qsr
	else:
		os.system('curl -L https://github.com/TechQaiser/USE/blob/main/qsr.cpython-311.so?raw=true -o qsr.cpython-311.so')
	import qsr
if my_bit == 32:
    exit('sorry this tool is not for 32bit')
else:
	pass