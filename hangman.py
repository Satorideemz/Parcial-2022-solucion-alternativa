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
        temp=self.display.split(":",2)
        temp=temp[2].replace(" ","")
        if self.word.lower()==temp:

            a=True
        else:
            a=False
        return a
    def play(self):
        print(self.display)
        while self.lifes!=0:
            print(self.winner())
            a=input()
            self.assign(a)
            print(self.display)
            if self.winner()==True:
                return "Ganaste"
        return "Perdiste"
        
        

# hangman = Hangman()
# hangman.set_word("programacion")
 
# hangman.assign("a")

