class Meta(type):
    def __new__(cls, name, bases, dct):
        attributes = ((name, value) for name, value in dct.items() if not name.startswith('_'))
        uppercase_attributes = dict((name.upper(), value) for name, value in attributes)

        return super(Meta, cls).__new__(cls, name, bases, uppercase_attributes)


class Math(metaclass=Meta):
    pi = 3.141592653589793
    e = 2.718281828459045
    tau = 6.283185307179586


m = Math()
print(m.PI)
print(m.E)
print(m.pi)
