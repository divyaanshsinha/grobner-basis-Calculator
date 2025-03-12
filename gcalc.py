import sympy as sp

# Define symbols for variables
x, y = sp.symbols('x y')

# Define multivariate polynomials
G = {x*y - x, x**2 - y}

H = set()

def S_mod_G(f,g, G):
    p = sp.Poly(f, x, y)
    q = sp.Poly(g, x, y)
    p_lt = p.LT()
    q_lt = q.LT()
    p_monom = sp.Mul(*[var**exp for var, exp in zip(p.gens, p_lt[0])])
    q_monom = sp.Mul(*[var**exp for var, exp in zip(q.gens, q_lt[0])])

    lcm_monom = sp.lcm(p_monom, q_monom)

    multiplier_f = sp.simplify(lcm_monom / p_monom)
    multiplier_g = sp.simplify(lcm_monom / q_monom)
    S_expr = multiplier_f * p.as_expr() - multiplier_g * q.as_expr()
    # final step, take mod G 

while True:
    G_list = list(G)
    for j in range(2, len(G)):
        for i in range(1,j):
            g_i = G_list[i]
            g_j = G_list[j]
            h = S_mod_G(g_i,g_j, G)
            if h != 0:
                H.add(h)
    G.union(H)
    if len(H) == 0:
        break
print(G)
