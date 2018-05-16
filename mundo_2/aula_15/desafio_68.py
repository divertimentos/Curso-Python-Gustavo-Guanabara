from random import randint

''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou, 
no final do jogo.'''

while True:
    player = int(input("Escolha um número [entre 0 e 10] \n"))
    
    if player < 0 or player > 10:  # Condição fora dos limites
        print("Digite um número entre 0 e 10 para jogar.")
    else:  # Se estiver dentro dos parâmetros, rode:
        computer = randint(1, 10)
        choice = str(input("Ímpar ou par? [P / I] \n")).strip().upper()
    
        while True:
            if choice == "P":
                soma = player + computer
                if soma % 2 == 0:
                    print(f"Deu {soma}, você venceu!")  # Colocar um contador de vitórias aqui
                else:
                    print(f"Deu {soma}, a máquina venceu!")
                    break
                break
            elif choice != "P":
                    print("Digite P ou I")
                    break
    
            if choice == "I":
                soma = player + computer
                if soma % 2 != 0:
                    print("Você venceu!")  # Colocar um contador de vitórias aqui
                else:
                    print(f"Deu {soma}, a máquina venceu!")
                    break
                break
            elif choice != "I":
                print("Digite P ou I")
                break

        
