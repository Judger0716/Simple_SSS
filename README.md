# Simple_SSS
Simple Shamir Secret Sharing on GF(2^n)

## Usage
This is a simple (t,n) threshold shamir secret sharing scheme. 
Adjust `secret` for your input, it then split into `n` shares based on the attribute you set.
When the secret is recovered, it uses lagrange interpolation.

```Python
# Secret
secret = 76581712835468712541234
# Shares
points = secret_int_to_points(secret,3,4)
# Recover
recover = lagrange_interpolation(points,3)
# Check
print('{}\n{}\n{}'.format(secret,recover,secret==recover))
```

## Reference
+ [Lagrange Interpolation](https://zhuanlan.zhihu.com/p/85200990)
+ [shea256-secret-sharing](https://github.com/shea256/secret-sharing.git)