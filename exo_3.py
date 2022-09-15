import random
score = 0
for i in range(10) :
    A = random.randint(1,10)
    B = random.randint(1,10)
    reponse = int(input('{0} * {1} = '.format(A,B)))
    if reponse == A * B:
        score += 1
        print('bien :)')
    else :
        print('pas bien >:(')
print(score)