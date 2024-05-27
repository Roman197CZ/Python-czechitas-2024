import requests
ico = input("Zadejte IČO hledaného subjektu ve formátu 12345678: ")
response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
data = response.json()
print (data["obchodniJmeno"])
print (data["sidlo"]['textovaAdresa'])

name = input("Zadejte název hledaného subjektu: ")
headers = {           
    "Content-Type": "application/json",
    }
data = '{"obchodniJmeno": '+ '"'+name +'"}'
data = data.encode("utf-8")
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)
vysl = res.json()
print ("Nalezeno subjektů:",vysl["pocetCelkem"])

for subjekt in vysl["ekonomickeSubjekty"]:
    print(subjekt["obchodniJmeno"]+", "+subjekt["ico"])