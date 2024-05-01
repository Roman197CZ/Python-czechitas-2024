# Implementace systému pro doručování pizzy
# Systém bude sledovat objednávky, včetně položek v objednávce
# (pizzy a nápoje), a  spravovat proces doručování.

class Item:
    def __init__(self,
                 name: str,
                 price: float):
        self.name = name
        self.price = price

    def __str__(self): # řetězcová reprezentace položky ve formátu: `<název>: <cena> Kč`
        return f"{self.name}: {self.price} Kč"

class Pizza(Item):
    def __init__(self, 
                  name: str, 
                  price: float, 
                  ingredients: dict): # slovník ingrediencí a jejich množství
        super().__init__ (name, price)
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, price_per_ingredient): # Přidává extra ingredienci do pizzy a aktualizuje její cenu.
        self.ingredients [ingredient] = quantity
        self.price += price_per_ingredient

    def __str__(self): # textový popis pizzy včetně ingrediencí a ceny
        return f"{self.name} - {self.ingredients}. Cena: {self.price} Kč"

class Drink(Item):
    def __init__(self,
                 name,
                 price,
                 volume): # objem nápoje v mililitrech
        super().__init__ (name, price)
        self.volume = volume
    
    def __str__(self): # popis nápoje, včetně jeho objemu a ceny
        return f"{self.name} - objem: {self.volume} ml. Cena: {self.price} Kč"
    
class Order: # Reprezentuje objednávku učiněnou zákazníkem. Měla by obsahovat 
             # jméno zákazníka, adresu doručení, seznam objednaných položek 
             # a stav objednávky (např. "Nová", "Doručeno")
    def __init__(self,
                 customer_name: str, # Jméno zákazníka
                 delivery_address: str, # Adresa doručení
                 items = list, # Seznam položek v objednávce
                 status = "Nová"): # Stav objednávky
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.items = items
        self.status = status
     
    def mark_delivered (self): # změní stav objednávky na "Doručeno"
        self.status = "Doručeno"
        return self.status
    
    def __str__(self): # vrací podrobné informace o objednávce, včetně jména zákazníka, 
                       # adresy, položek v objednávce a stavu objednávky¨
        seznam = "["
        sum_price = 0
        for i in self.items:
            seznam += str(i.name)+"("+ str(i.price)+" Kč), "
            sum_price += i.price
        seznam += "Celkem: "+str(sum_price)+"Kč] "
        if self.status == "Doručeno":
            return f"Objednávka pro: {self.customer_name} na adresu: {self.delivery_address} {seznam}byla doručena."

        return f"Objednávka pro: {self.customer_name} na adresu: {self.delivery_address} {seznam}je ve stavu: {self.status}."

class DeliveryPerson: # Reprezentuje doručovatele. Měla by obsahovat: 
             # jméno doručovatele, telefonní číslo, stav dostupnosti 
             # a aktuální objednávku, kterou doručuje (pokud nějakou má)
    def __init__(self,
                 name_dp: str, # Jméno doručovatele
                 phone_number: str): # Telefonní číslo doručovatele
                #  available = "True", # Dostupnost doručovatele
                #  current_order: Order): # Aktuální objednávka k doručení
        self.name_dp = name_dp
        self.phone_number = phone_number
        self.available = True
        self.current_order = Order("", "", [])
  
    def assign_order (self, order_x): # přiřadí objednávku doručovateli, pokud je dostupný.
                             # Stav objednávky by měl být aktualizován na "Na cestě"
        if self.available:
            self.current_order = order_x
            self.available = False
            self.current_order.status = "Na cestě"
        else:
            self.current_order.status = "na cestě"
            print(f"Objednávku {order_x.customer_name}, {order_x.delivery_address} nelze přidělit doručovateli {self.name_dp} ({self.phone_number}), protože právě doručuje objednávku {self.current_order.customer_name}, {self.current_order.delivery_address}", end = "")

    def complete_delivery (self): # označí objednávku jako doručenou a doručovatele znovu 
                                  # učiní dostupným pro nové objednávky
        self.current_order.mark_delivered()
        self.available = True

    def __str__(self): # vrací informace o doručovateli, včetně jeho stavu dostupnosti
        if not self.available:
            if self.current_order.status == "Na cestě":
                return f"Doručovatel {self.name_dp} ({self.phone_number}) doručuje objednávku pro: {self.current_order.customer_name}, {self.current_order.delivery_address} => je nedostupný."
            else:
                return ""
        elif self.available and self.current_order.status == "Doručeno":
                return f"Doručovatel {self.name_dp} ({self.phone_number}) doručil objednávku: {self.current_order.customer_name}, {self.current_order.delivery_address} a je opět dostupný."
        elif self.available:
                return f"Doručovatel {self.name_dp} ({self.phone_number}) nemá žádnou objednávku = je dostupný."
        else:
            return f"Doručovatel {self.name_dp} ({self.phone_number}) je nedostupný."

# ********************************************
#          Závěrečné kontrolní tisky 
# ********************************************

print('******************* Vytvoření instance pizzy a manipulace s ní***************************')
# Vytvoření instance pizzy a manipulace s ní
margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olivy", 50, 10)
print(margarita)
hawai = Pizza("Hawai", 220, {"ananas": 100, "sýr": 150})
hawai.add_extra("salám", 50, 60)
print(hawai)
print('*******************Vytvoření instance nápoje***************************')
# Vytvoření instance nápoje
cola = Drink("Cola", 39.5, 500)
print(cola)
juice = Drink("Juice", 29.5, 330)
print(juice)
print('********************Vytvoření a výpis objednávky***************************')
# Vytvoření a výpis objednávky
order1 = Order("Jan Novák", "Pražská 123", [margarita, cola])
print(order1)
order2 = Order("Petr Nový", "Brněnská 123", [cola])
print(order2)
order3 = Order("Jana Nová", "Olomoucká 123", [hawai, margarita, cola, juice])
print(order3)
order4 = Order("Petra Nováková", "Ostravská 123", [hawai, cola, juice])
print(order4)
print('******************** Vytvoření řidiče a přiřazení objednávky***************************')
# Vytvoření řidiče a přiřazení objednávky
delivery_person = DeliveryPerson("Petr Novotný", "777 888 999")
delivery_person.assign_order(order1)
print(delivery_person)
delivery_person2 = DeliveryPerson("Blanka Petrů", "111 222 333")
delivery_person2.assign_order(order2)
print(delivery_person2)
delivery_person3 = DeliveryPerson("Oldřich Pakosta", "555 666 777")
delivery_person3.assign_order(order3)
print(delivery_person3)
delivery_person4 = DeliveryPerson("Martin Marek", "333 145 478")
print(delivery_person4)
delivery_person.assign_order(order4)
print(delivery_person)
print('********************Dodání objednávky***************************')
# Dodání objednávky
delivery_person.complete_delivery()
print(delivery_person)
delivery_person2.complete_delivery()
print(delivery_person2)
print(delivery_person3)
print(delivery_person4)
print('********************Kontrola stavu objednávky po doručení***************************')
# Kontrola stavu objednávky po doručení
print(order1)
print(order2)
print(order3)
print(order4)
print('********************Výpis stavu doručovatele***************************')
# Výpis stavu doručovatele
print(delivery_person)
print(delivery_person2)
print(delivery_person3)
print(delivery_person4)
