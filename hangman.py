from logging import raiseExceptions
from invalidassignmentexception import InvalidAssignmentException

class Hangman:
    def __init__(self,word=None,tries=None,display=None,lifes=None):
        self.word=word 
        self.tries=[]
        self.display=display
        self.lifes=5
    def set_word(self,word):
        self.word=word
        self.display="Lifes: 5 - Word: "
        for i in range(len(word)):
            self.display=self.display+"_ "
         
    def assign(self,letter):
        letter=letter.lower()
        words=self.word.lower()
        if words.find(letter.lower())==-1:
            self.lifes=self.lifes-1
        #    raise InvalidAssignmentException
        #convierto el string en lista y si matchea lo voy reemplazando por las letras que van ingresando como parametros al metodo
        #caso contrario no hace nada y pierde una vida
        temp=list(self.word.lower())
        temp2=self.display.split(":",2)
        temp2=list(temp2[2].replace(" ","")) 
        for i in range(len(temp)):
            if temp[i]==letter:
                temp2[i]=letter
        for i in range(len(temp2)):
            temp2[i]=temp2[i]+" "
        temp2=("".join(temp2))        
        self.display="Lifes: 5 - Word: "+temp2
    def show(self):
        return self.display                 
    def winner(self):
        #comparo, mi win condition es que el display coincida con el atributo palabra
        temp=self.display.split(":",2)
        temp=temp[2].replace(" ","")
        if self.word.lower()==temp:

            a=True
        else:
            a=False
        return a
    def play(self):
        #metodo que arranca el juego, mientras tenga vidas voy a tomar caracteres
        #el juego se frena cuando se gana o se pierde
        print(self.display)
        while self.lifes!=0:
            a=input()
            self.assign(a)
            print(self.display)
            if self.winner()==True:
                return "Ganaste"
        return "Perdiste"
        
        




