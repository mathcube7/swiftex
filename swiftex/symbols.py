

class Symbol:

    def __init__(self, latex_string):
        self.latex_string = latex_string

    def __str__(self):
        return self.latex_string

    def __repr__(self):
        return str(self)

    def __pow__(self, power):
        s = '%s^{%s}' % (str(self), power)
        return Symbol(s)

    def __add__(self, other):
        s = '%s + %s' % (str(self), str(other))
        return Symbol(s)

    def __eq__(self, other):
        s = '%s = %s' % (str(self), str(other))
        return Symbol(s)


def symbols(string):
    parts = string.split(',')
    if len(parts) == 1:
        return Symbol(string)
    return [Symbol(part.strip()) for part in parts]
