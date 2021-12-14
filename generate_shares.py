'''
Generate multiple shares using Simple_SSS
'''

from utilitybelt import secure_randint as randint
from sss import secret_int_to_points

n = int(input('secret number:')) # Secret number
player_number = 3
threshold = 3

# shares[i] is all the shares player i get
shares = []
for i in range(player_number):
    shares.append([])

# Input secrets
for i in range(n):
    #secret_i = int(input('input a secret:')) # manual input
    secret_i = randint(100,10000) # automatic input
    print(secret_i,end=' ')
    shares_i = secret_int_to_points(secret_i,threshold,player_number)
    for j in range(len(shares_i)):
        shares[j].append(shares_i[j][0])
        shares[j].append(shares_i[j][1])
print()

# Get input data
for i in range(len(shares)):
    print('echo',end=' ')
    for j in range(len(shares[i])):
        print(shares[i][j],end=' ')
    print('> Player-Data/Input-P{}-0'.format(i))

# Generate amount
print('echo',end=' ')
buy_num = randint(0,n)
print(buy_num,end=' ')
print(n-buy_num,end=' ')
for i in range(n):
    print(randint(100,10000),end=' ')
print('> Programs/Public-Input/match_order')
