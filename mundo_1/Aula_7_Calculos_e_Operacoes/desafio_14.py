# Conversor de temperaturas: escreva um programa que converta uma temperatura digitada em ºC para ºF

celsius = float(input("Digite a temperatura em Celsius: \n"))
farenheit = ((1.8 * celsius) + 32)
print("{}ºC correspondem a {:.1f}ºF.".format(celsius, farenheit))
