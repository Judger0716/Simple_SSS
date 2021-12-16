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
    # print(secret_i,end=' ')
    shares_i = secret_int_to_points(secret_i,threshold,player_number)
    for j in range(len(shares_i)):
        shares[j].append(shares_i[j][0])
        shares[j].append(shares_i[j][1])
# print()

# Get input data
for i in range(len(shares)):
    print('echo',end=' ')
    for j in range(len(shares[i])):
        print(shares[i][j],end=' ')
    print('> Player-Data/Input-P{}-0'.format(i))

# Generate amount
print('echo',end=' ')
buy_num = randint(round(n/4),round(n/2))
amount = []
for i in range(n):
    amount.append(randint(100,1000))
    print(amount[i],end=' ')
print('> Programs/Public-Input/optimize-'+str(buy_num)+'-'+str(n-buy_num))
print('./compile.py -M optimize '+str(buy_num)+' '+str(n-buy_num))
print('./shamir-party.x 0 '+'optimize-'+str(buy_num)+'-'+str(n-buy_num)+' & '+'./shamir-party.x 1 '+'optimize-'+str(buy_num)+'-'+str(n-buy_num)+' & '+'./shamir-party.x 2 '+'optimize-'+str(buy_num)+'-'+str(n-buy_num))

buy_sum = 0
for i in range(buy_num):
    buy_sum += amount[i]
sell_sum = 0
for i in range(buy_num,len(amount)):
    sell_sum += amount[i]
print('sell: ',sell_sum,'| buy: ',buy_sum)
