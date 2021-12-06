from IPython.display import Math, display


class Symbol:

    def __init__(self, latex_string, tag=None):
        if isinstance(latex_string, Symbol):
            latex_string = str(latex_string)
        self.latex_string = latex_string
        if tag:
            assert isinstance(tag, str)
            _expr_store[tag] = self

    def __str__(self):
        return self.latex_string

    def __repr__(self):
        return str(self)

    def __call__(self, *args, **kwargs):
        s = self.latex_string + '\\left( '
        for i, arg in enumerate(args):
            s += str(arg)
            if i < len(args) - 1:
                s += ', '
        s += ' \\right)'
        return Symbol(s)

    def __pow__(self, power):
        s = '%s^{%s}' % (str(self), power)
        return Symbol(s)

    def __add__(self, other):
        s = '%s + %s' % (str(self), str(other))
        return Symbol(s)

    def __radd__(self, other):
        s = '%s + %s' % (str(other), str(self))
        return Symbol(s)

    def __eq__(self, other):
        s = '%s = %s' % (str(self), str(other))
        return Symbol(s)

    def __neg__(self):
        return Symbol('- %s' % self.latex_string)

    def __mul__(self, other):
        return Symbol('%s %s' % (str(self), str(other)))

    def __rmul__(self, other):
        return Symbol('%s %s' % (str(other), str(self)))

    def __sub__(self, other):
        s = '%s - %s' % (str(self), str(other))
        return Symbol(s)

    def __rsub__(self, other):
        s = '%s - %s' % (str(other), str(self))
        return Symbol(s)

    def __rshift__(self, other):
        assert isinstance(other, str)
        return self

    def _ipython_display_(self, **kwargs):
        display(Math(str(self)))

    def _repr_latex_(self):
        return Math(str(self))


class Int(Symbol):

    def __init__(self, lower='', upper='', **kwargs):
        super().__init__('\\int_{%s}^{%s}' % (str(lower), str(upper)), **kwargs)


class Frac(Symbol):

    def __init__(self, numer, denom, **kwargs):
        self.numer = Symbol(numer)
        self.denom = Symbol(denom)
        super().__init__('\\frac{%s}{%s}' % (self.numer, self.denom), **kwargs)


class Sqrt(Symbol):

    def __init__(self, arg, **kwargs):
        self.arg = Symbol(arg)
        super().__init__('\\sqrt{%s}' % self.arg, **kwargs)


class Matrix(Symbol):

    def __init__(self, nrows, ncols, default='', **kwargs):
        self.values = {}
        self.nrows = nrows
        self.ncols = ncols

        for i in range(nrows):
            for j in range(ncols):
                self.values[(i, j)] = Symbol(str(default))

        super().__init__(str(self), **kwargs)

    def __setitem__(self, idx, value):
        assert len(idx) == 2

        row_inds = self._expand_slice(idx[0], self.nrows)
        col_inds = self._expand_slice(idx[1], self.ncols)

        k = 0
        for i in row_inds:

            for j in col_inds:
                if hasattr(value, '__len__'):
                    self.values[i, j] = Symbol(str(value[k]))
                else:
                    self.values[i, j] = Symbol(str(value))
                k += 1

    def _expand_slice(self, slice_or_ind, max_vals):
        if isinstance(slice_or_ind, slice):
            if slice_or_ind.start is None:
                start = 0
            else:
                start = slice_or_ind.start
            if slice_or_ind.stop is None:
                stop = max_vals
            else:
                stop = slice_or_ind.stop
            inds = list(range(start, stop))
        else:
            inds = [slice_or_ind]
        return inds

    def __str__(self):
        s = r'\left(\begin{matrix}'
        for i in range(self.nrows):
            for j in range(self.ncols):
                s += str(self.values[i, j])
                if j < self.ncols - 1:
                    s += ' & '
                elif i < self.nrows - 1:
                    s += r'\\'
        s += r'\end{matrix}\right)'
        return s

    def __repr__(self):
        return self.__str__()


def symbols(string):
    parts = string.split(',')
    if len(parts) == 1:
        return Symbol(string)
    return [Symbol(part.strip()) for part in parts]


def brace(expr):
    return r'\left(' * expr * r'\right)'

def get(tag):
    return _expr_store.get(tag)


_expr_store = {}

oo = Symbol(r'\infty')