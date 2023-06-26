import string
import secrets

# creation du generateur de mot de passe
lettresalpha = string.ascii_letters  # toutes les lettres de l'aphabet minuscule ou majuscule
decimal = string.digits  # toutes les chiffres decimal
symbole = string.punctuation  # toutes les signes de ponctuation
print(f'{lettresalpha},{decimal}, {symbole}')
passw = ''
for i in range(12):
    passw += ''.join(secrets.choice(lettresalpha+decimal+symbole))
print(passw)
