''' Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.
'''
vel = int(input("Velocidade do carro: \n"))
if vel > 80:
    print("Você está acima do limite permitido! \nVelocidade de {}km/h!".format(vel))
    multa = 7 * (vel - 80)
    print("Sua multa é de R${:.2f}.".format(multa))
else:
    print("Velocidade dentro do limite. Boa viagem.")
