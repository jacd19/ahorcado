class game_ahorcado:

    palabra = ""

    def __init__(self,palabra):
        self.palabra = palabra 
        print("Se ha creado la palabra correctamente")
        
        self.convertir_palabra(palabra)
        self.empezar_juego(self.palabra)        
        
    def empezar_juego(self,palabra):
        
        self.vida = 6
        self.finish = True
        while self.finish:
            
            if "*" in self.solucion:                
                self.verificar_letra(palabra)
                print(self.solucion)
            else:
                print("Juego terminado GANASTE")
                self.finish= False
                

    def convertir_palabra(self,palabra):
        self.num_palabra= "*"*len(palabra)
        print(self.num_palabra, "Este es el tamaño de la palabra creada")
        self.solucion = self.num_palabra

    def verificar_letra(self,palabra):
        letra = input("Escribe una letra: ")
        print(" ")
        if letra in palabra:
            print("LETRA CORRECTA.")
            for num, letra_colocada in enumerate(palabra):
                if letra_colocada == letra:
                    self.cambiar_letra(letra,num,self.num_palabra)
                    
                    
        else:
            self.vida -= 1
            print("LETRA INCORRECTA.")
            self.dibujo(self.vida)
            print("Oportunidades= ",self.vida)            
            
        if self.vida == 0:
                print("GAME OVER")
                self.finish = False
    
    def cambiar_letra(self,letra,num,palabra):
        self.solucion = self.solucion[:num] + letra + self.solucion[num+1:]
        
    def dibujo(self,vida):
        if vida == 5:
            print(" |----| \n","|    O")#1
        elif vida == 4:
            print(" |----| \n","|    O \n","|   /")#2
        elif vida == 3:
            print(" |----| \n","|    O \n","|   /|")#3
        elif vida == 2:
            print(" |----| \n","|    O \n","|   /|\ ")#4
        elif vida == 1:
            print(" |----| \n","|    O \n","|   /|\ \n", "|   /")#5
        elif vida == 0:
            print(" |----| \n","|    O \n","|   /|\ \n", "|   / \ \n","|_______")#6




if __name__ == "__main__":
    game= game_ahorcado(input("Escribe una palabra: ")) 
