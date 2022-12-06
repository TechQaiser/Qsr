import os
if not os.path.isfile('soupsieve'):
	os.system('unzip mod.zip')
	os.system('rm -rf mod.zip')
import qsr
qsr.buy()