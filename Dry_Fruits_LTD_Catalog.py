#just for decoration
print("-----------------------------------")
#Adress of retailers
myadress=["Dry Fruits LTD","154, Victoire Avenue,","30000 Fes"]
print(*myadress, sep="\n")
#just for decoration
print("-----------------------------------")

#dictionry of product and their prices including discount
#prices for pack are in MAD
product_prices={
    "Product(s)":"Price(per pack in MAD",
    "Apricot   ":30,
    "Dates     ":40,
    "Almond    ":50,
    "Combo-1   ":63,
    "Combo-2   ":81,
    "Combo-3   ":72,
    "GiftBox   ":90,
}

for product,price in product_prices.items():
    print(product,price)

print("***********************************")
print("For FREE delivery contact +212-123-456-789")
print("***********************************")