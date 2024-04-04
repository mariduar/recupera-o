import forca
import adivinhacao

def escolhe_jogo():
    print("um presente formado pelas maos de Deus")
    print("escolha seu jogo"
    print(" i love you ferias")
    
    print("(1) forca (2) adivinhacao")
    
    jogo = int(input(" Qual jogo? "))
    
    if(jogo == 1):
         print("jogando forca")
         forca.jogar()
    elif(jogo == 2):
        print("jogando adivinhacao")
        adivinhaçao.jogar()
        
    if(__name__ == "__main__"):
        escolhe_jogo()
        
import random

numeroSecreto = random.randint(1, 101)
tentativas = 101

def jogar():
    
    print("i love you cama")
    print("bem vindo ao jogo de adivinhacao!")
    print("quero ficar em casa ou escola")
     
    NivelDificuldade()
    
    print("numero secreto ", numeroSecreto)
    global tentativas
    while tentativas > 0:
        numeroDigitado = int(
            input("Digite m numero de 1 a 100 para tentar adivinhar o numero secreto:"))
         if numeroDigitado == numeroSecreto:
             print("Parabens o numero")
           
        
        