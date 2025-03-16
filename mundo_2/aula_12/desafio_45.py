from random import choice
from time import sleep

"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
choices_list = ["pedra", "papel", "tesoura"]
print("""
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
""")

player_prompt = str(input("Você escolhe pedra, papel ou tesoura? \n")).lower()

print("JO")
sleep(0.50)
print("KEN")
sleep(0.5)
print("PÔ!!!")

# computer_choice = choice(choices_list)


def judge(computer, player):
    print(
        f"""
    Jogador: {player_prompt}
    Computador: {computer}
    """
    )

    ### Exceptions:
    if player != "pedra" and player != "papel" and player != "tesoura":
        return print(
            f"{player} não é uma opção válida. Escolha pedra, papel ou tesoura!"
        )

    if player != "pedra" and player != "papel" and player != "tesoura":
        return print(
            f"{player} não é uma opção válida. Escolha pedra, papel ou tesoura!"
        )

    if computer == player:
        return print("Empate. Vamos jogar novamente!")

    ### Valid plays
    if player_prompt == "pedra" and computer == "tesoura":  # Pedra x Tesoura: Pedra
        return print("Pedra vence tesoura. Jogador ganhou.")

    if player_prompt == "tesoura" and computer == "pedra":  # Tesoura x Pedra: Pedra
        return print("Pedra vence tesoura. Computador ganhou.")

    if player_prompt == "papel" and computer == "pedra":  # Papel x Pedra: Papel
        return print("Papel vence pedra. Jogador ganhou.")

    if player_prompt == "pedra" and computer == "papel":  # Pedra x Papel: Papel
        return print("Papel vence pedra. Computador ganhou.")

    if player_prompt == "papel" and computer == "tesoura":  # Papel x Tesoura: Tesoura
        return print("Tesoura vence papel. Computador ganhou.")

    if player_prompt == "tesoura" and computer == "papel":  # Tesoura x Papel: Tesoura
        return print("Tesoura vence papel. Jogador  ganhou.")


judge(choice(choices_list), player_prompt)
