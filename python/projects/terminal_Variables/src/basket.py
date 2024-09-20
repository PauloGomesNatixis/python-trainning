class Fruit:
    def __init__(self, name: str, color: str | None = None):
        self.name = name
        self.color = color 




class Basket: # atencao a letra inicial em Maiuscua
    def __init__(self, owner, size):
        self.owner = owner
        self.size = size
        self.fruits: list[Fruit] = []
        print(f"Nova cesta iniciada do {owner}, com tamanho de {size} items")
        
    def add_fruit(self, fruit):
        #testar se ainda tem espaço livre no "fruit"
        if not len(self.fruits) < self.size:
            print("cesta cheia!")
            return
        else:
            self.fruits.append(fruit)

    def remove_fruit(self, fruit):
        #testar se ainda tem espaço livre na lista "fruits"
        if fruit in self.fruits:
            self.fruits.remove(fruit)
            print( fruit, "removido da cesta")
            return
        else:
            print("nao existe na cesta!")

    def print_fruit(self):
        #testar se ainda tem espaço livre na lista "fruits"
        if self.fruits:
            fruit_names = [
                fruit.name 
                for fruit in self.fruits 
                # if fruit.name == "Apple" # filtrar por "Apple"
            ]
            
            _ = {
                fruit.name : fruit.color
                for fruit in self.fruits
            }
            
            print(_)
            print(f"Lista de frutos na cesta do {self.owner}:\n", ",".join(fruit_names))
            


# contrutor / inicializa as baskets        
if __name__ == "__main__":  #excutadp apenas quando executado diretamente o basket.py
    
    basket_a = Basket(owner="Diogo", size=10)
    basket_b = Basket(owner="Henrique", size=10)
    
    apple = Fruit("Apple","Red")
    banana= Fruit("Banana","yellow")
     
    basket_a.add_fruit(apple)
    basket_a.add_fruit(banana)
    
    basket_a.print_fruit()
    
    #print(basket_a.owner,"\n",basket_a.size,"\n",basket_a.content)    
