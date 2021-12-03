from ..symbols import Symbol

(a, b, c, d, e, f,
 g, h, i, j, k, l,
 m, n, o, p, q, r,
 s, t, u, v, w, x,
 y, z) = tuple(Symbol(s) for s in 'abcdefghijklmnopqrstuvwxyz')
