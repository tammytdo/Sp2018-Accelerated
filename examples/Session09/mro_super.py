# super() logic explanation from:
# http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods

class ChildB(Base):
    def __init__(self):
        mro = type(self).mro()
        for next_class in mro[mro.index(ChildB) + 1:]: # slice to end
            if hasattr(next_class, '__init__'):
                next_class.__init__(self)
                break