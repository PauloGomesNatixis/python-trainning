# Dia 01 - Lab4

diogo_basket = [
    "Apple",
    "Watermellon",
    "Grapes"
]

henrique_basket = []


possible_fruit = input("Qual a fruta Henrique pode levar?\n") 

i = 1

while ((len(possible_fruit)>0) and (i <= 10)):
    if possible_fruit in diogo_basket:
        print("Esta fruto já esta na cesta do Diogo:\n", ",".join(diogo_basket))
    else:
        i += 1
        henrique_basket.append(possible_fruit)
        print("Fruta adicionada ao cesto do Henrique:\n", ",".join( henrique_basket))
    if i <= 10:
        possible_fruit = input("Digite outra fruta para adicionar ao cesto ou deixe vazio para terminar?\n") 

if len(henrique_basket) == 0:
    print("malandro")
else:
    print(henrique_basket)
    
    