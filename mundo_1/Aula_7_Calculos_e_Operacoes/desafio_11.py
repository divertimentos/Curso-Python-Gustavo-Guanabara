# Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input("Digite a largura: \n"))
altura = float(input("Digite a altura: \n"))
area = largura * altura

print("Sua parede tem a dimensão {}x{} e sua área é de {}m².".format(largura, altura, area))

# Cada litro (L) de tinta pinta uma área de 2m².
tinta_necessaria = area / 2
print("Para pintar essa parede, você precisará de {}L de tinta.".format(tinta_necessaria))
# Conferir a resposta porque não sei se entendi o problema. O velho Guilherme continua o mesmo, só que agora com ímpeto suficiente para continuar
