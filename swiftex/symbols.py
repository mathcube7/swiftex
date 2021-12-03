from IPython.display import Math, display


class Symbol:

    def __init__(self, latex_string):
        self.latex_string = latex_string

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

    def __eq__(self, other):
        s = '%s = %s' % (str(self), str(other))
        return Symbol(s)

    def __neg__(self):
        return Symbol('- %s' % self.latex_string)

    def __mul__(self, other):
        return Symbol('%s %s' % (str(self), str(other)))

    def _ipython_display_(self, **kwargs):
        display(Math(str(self)))

    def _repr_latex_(self):
        return Math(str(self))


class Int(Symbol):

    def __init__(self, lower='', upper=''):
        super().__init__('\\int_{%s}^{%s}' % (str(lower), str(upper)))


def symbols(string):
    parts = string.split(',')
    if len(parts) == 1:
        return Symbol(string)
    return [Symbol(part.strip()) for part in parts]


oo = Symbol(r'\infty')