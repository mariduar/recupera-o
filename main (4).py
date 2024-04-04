def jogar():
    print("oi good morning")
    print("Bem vindo a Forca")
    print("i am ")
    
    palavra_secreta = "maça" .upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_acertadas2 = []
    
    for letra in (palavra_secreta):
       letras_acertadas2.append("_")
       
       enforcou = False
       acertou = false
       errou = 0
       
       print(letras_acertadas)
       
       while (not enforcou and not acertou):
           
           chute = input("Qual letra? ")
           chute = chute.strip() . upper()
           
           if (chute in palavra_secreta):
               index = 0
               for letra in palvra_secreta:
                   if (chute == letra):
                       letras_acertadas[index] = letras
                    index += 1 
                else:
                    erros += 1 
                    
                    enforcou = erros == 6 
                    acertou = "_" not in letras_acertadas
                    print(letras_acertadas)
                    
                if (acertou):
                    print(" você ganhou!!")
                else:
                     print("você perdeu !!")
                print(" fim do jogo")
            
            if (__name__ == "__main__"):
                jogar()
        
        