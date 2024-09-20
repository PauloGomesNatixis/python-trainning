# Dia 01 - Lab4

diogo_basket = [
    "Apple",
    "Watermellon",
    "Grapes"
]

henrique_basket = []

possible_fruit = input("Qual a fruta que posso levar?\n") 

if possible_fruit in diogo_basket:
    print("Esta fruto já esta na cesta\n")
    print("Frutas na cesta do Diogo:", ",".join(diogo_basket))
    
else:
    henrique_basket.append(possible_fruit)
    print("Fruta no cesto do Henrique:\n", henrique_basket)