import crypto as c

h = s.H()
g = s.G()
print(h.add_mod(2,3,6))

print(g.pow_mod(2,3,10))

print(c.factors(8))

print(c.ggt(8,12))

print(c.ggt_phi(c.ggt(8,12)))

print(g.order(9))

print(g.mul_invert(2, 5))
