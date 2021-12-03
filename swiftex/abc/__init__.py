from ..symbols import Symbol

_letters = (a, b, c, d, e, f,
            g, h, i, j, k, l,
            m, n, o, p, q, r,
            s, t, u, v, w, x,
            y, z) = tuple(Symbol(s) for s in 'abcdefghijklmnopqrstuvwxyz')

_differentials = (da, db, dc, dd, de, df,
                  dg, dh, di, dj, dk, dl,
                  dm, dn, do, dp, dq, dr,
                  ds, dt, du, dv, dw, dx,
                  dy, dz) = tuple(Symbol('d' + s) for s in 'abcdefghijklmnopqrstuvwxyz')