def add(x,y):
    return x + y

def mul(x,y):
    return x * y

def sub(x,y):
    return x - y

def div(x,y):
    return x / y

def power(x,y):
    return x ** y

def mod(x,p):
    q = x//p
    return sub(x,(p*q))

def mulmod(x,y,p):
    number = mul(x,y)
    q = number//p
    return sub(number,(p*q))

def powmod(x,y,p):
    number = power(x,y)
    q = number//p
    return sub(number,(p*q))


def ggt(a,b):
    if not b:
        return a
    return ggt(b,mod(a,b))

def ggt_phi(n):
    result = 1
    for i in range(2,n):
        if ggt(i,n) == 1:
            result += 1
    return result

def factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def phi_factors(n):
    phi = n
    for factor in factors(n):
        phi -= phi // factor
    return phi


class H:

    def add_invert(self, x, p):
        return add(-x,p)
    
    def add_mod(self, x,y, p):
        number = add(x,y)
        q = number//p
        return sub(number,(p*q))

    def sub_mod(self, x, y, p):
        number = sub(x,y)
        q = number//p
        return sub(number,(p*q))
    
        #skalar multiplication: x=3,y=2, result = x+x = 6
    def pow_mod(self, x, y, p):
        result = 0
        for i in range(y):
            result = add(result, x)
        return mod(result,p)
    
    def order(self, p):
        return p



class G:
    def mul_mod(self,x,y,m):
        return mulmod(x,y,p)
    
    def pow_mod(self, x, y, p):
        result = x
        for i in range(1,y):
            result = mul(result, x)
        return mod(result,p)
    
    def order(self, n):
        return ggt_phi(n)
    
    def mul_invert(self, x, p):
        return powmod(x,self.order(p)-1,p)
