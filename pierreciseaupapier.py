import random, time, sys, os

# Effacer le terminal
os.system('cls')

def separator(char='-', length=40):
    print(char * length)

print('''Jeu de Pierre, Feuille, Ciseaux,
Régle du jeu :
- Pierre bat Ciseaux
- Feuille bat Pierre
- Cieaux bat Feuille
''')

separator()

victoires = 0
pertes = 0
egale = 0

while True:
    # Boucle tant que pour les instructions du jeu 
    while True:
        print('{} vitoires, {} pertes, {} egale'.format(victoires,pertes,egale))

        separator()

        print('A toi de jouer:')
        print('(P)ierre (F)euille (C)iseaux ou (A)rrête')

        actionJoueur = input('> ').upper()

        if actionJoueur == 'A':
            print('Merci d\'avoir joué.')
            sys.exit()

        if actionJoueur == 'P' or actionJoueur == 'F' or actionJoueur == 'C':
            break
        else:
            print('Attention il faut choisir P,F,C ou A !')

    separator('=')

    if actionJoueur == 'P':
        print('PIERRE contre...')
        actionJoueur = 'PIERRE'
    elif actionJoueur == 'F':
        print('FEUILLE contre...')
        actionJoueur = 'FEUILLE'
    elif actionJoueur == 'C':
        print('CISEAUX contre...')
        actionJoueur = 'CISEAUX'

    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        actionOrdi = 'PIERRE'
    elif randomNumber == 2:
        actionOrdi = 'FEUILLE'
    elif randomNumber == 3:
        actionOrdi = 'CISEAUX'

    #print(actionOrdi)

    separator('=')

    if actionJoueur == actionOrdi:
        print('Egalité !')
        egale = egale + 1
    elif actionJoueur == 'PIERRE' and actionOrdi == 'CISEAUX':
        print('Gagné !')
        victoires = victoires + 1
    elif actionJoueur == 'FEUILLE' and actionOrdi == 'PIERRE':
        print('Gagné !')
        victoires = victoires + 1
    elif actionJoueur == 'CISEAUX' and actionOrdi == 'FEUILLE':
        print('Gagné !')
        victoires = victoires + 1
    elif actionJoueur == 'PIERRE' and actionOrdi == 'FEUILLE':
        print('Perdu !')
        pertes = pertes + 1
    elif actionJoueur == 'FEUILLE' and actionOrdi == 'CISEAUX':
        print('Perdu !')
        pertes = pertes + 1
    elif actionJoueur == 'CISEAUX' and actionOrdi == 'PIERRE':
        print('Perdu !')
        pertes = pertes + 1
 