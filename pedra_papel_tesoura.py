import random

def play():
    user = input("Qual é a sua escolha?  pedra, papel e tesoura\n ")
    comp = random.choice(['pedra', 'papel', 'tesoura'])

    print(f"Voce escolheu {user}, o seu  oponente escolheu {comp}")

    if user == comp:
        return 'Olha só, empatou'

    # pe > t, t > pa. pa > pe
    if is_win(user, comp):
        return 'Voce venceu!!'

    return 'Voce Perdeu!!'

def is_win(jogador, oponente):
    # retorna verdadeiro se o joggagor vencer
    # pe > t, t > pa. pa > pe
    if (jogador == 'pedra' and oponente == 'tesoura') or (jogador == 'tesoura' and oponente == 'papel') or (jogador == 'papel' and oponente == 'pedra'):
        return True
print(play())