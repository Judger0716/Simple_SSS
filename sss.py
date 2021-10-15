'''
Shamir Secret Sharing Scheme on GF(2^n)
'''

from utilitybelt import secure_randint as randint
from decimal import Decimal
#import random

def secret_int_to_points(secret,threshold,num):
    coefficients = [secret]
    for i in range(threshold-1):
        # Take GF(2^16) as an example
        coefficients.append(randint(0,2**16-1))
    points = []
    for x_value in range(1,num+1):
        cur_point = [x_value]
        y_value = 0
        for i in range(len(coefficients)):
            y_value += coefficients[i]*pow(x_value,i)
        cur_point.append(y_value)
        points.append(cur_point)
    #print(points)
    return points

def lagrange_interpolation(points,threshold):
    points_num = len(points)
    if(points_num<threshold):
        raise(ValueError('Not enough shares.'))
    zero_coefficient = 0
    for i in range(points_num):
        multi_sum = Decimal('1.0')
        for j in range(points_num):
            if(i==j):
                continue
            else:
                multi_sum *= Decimal(0-points[j][0])/Decimal(points[i][0]-points[j][0])
        #print(multi_sum, points[i][1])
        zero_coefficient += multi_sum*points[i][1]
    #print('{:.2f}'.format(zero_coefficient))
    secret = zero_coefficient
    return round(secret)

# Secret, 2^64=18446744073709551616
secret = 18273912
# Shares
points = secret_int_to_points(secret,3,4)
#print(points)
for p in points:
    print(p[1])
# Recover
recover = lagrange_interpolation(points,3)
# Check
print('\nCheck:\n{}\n{}\n{}'.format(secret,recover,secret==recover))