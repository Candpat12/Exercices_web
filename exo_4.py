import random
result = random.randint(1,100)
while True :
    attempt = int(input('Entrez un nombre : '))
    if attempt == result :
        print('vous avez gagné!')
        break
    elif attempt > result :
        print("C'est moins!")
    elif attempt < result :
        print("C'est plus!")