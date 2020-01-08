
import os,sys

print(sys.argv)

################################################ Marvin Minsky's extended frame

class Frame:
    def __init__(self,V):
        # class/type tag
        self.type = self.__class__.__name__.lower()
        # scalar value: frame name, string/number,..
        self.val  = V
        # slot{}s = attrbites = string-keyed associative array = dictionary
        self.slot = {}
        # nest[]ed = ordered container = vector = stack
        self.nest = []

    ###################################################################### dump

    def __repr__(self): return self.dump()

    ## full tree-form text dump
    def dump(self,depth=0,prefix=''):
        # header
        tree = self._pad(depth) + self.head(prefix)
        # infinitive recursion block
        if not depth: Frame.dumped = []
        if self in Frame.dumped: return tree + ' _/'
        else: Frame.dumped.append(self)
        # slot{}s
        for i in self.slot:
            tree += self.slot[i].dump(depth+1,prefix='%s = '%i)
        # nest[]ed
        idx = 0
        for j in self.nest:
            tree += j.dump(depth+1,prefix='%s : '%idx) ; idx += 1
        # subtree
        return tree

    ## short form `<T:V>` header dump
    def head(self,prefix=''):
        return '%s<%s:%s> @%x' % (prefix, self.type, self._val(), id(self))

    ## tree padding
    def _pad(self,depth):
        return '\n' + ' '*4 * depth

    ## special `val` representation for dumps
    def _val(self):
        return self.val

    ################################################################# operators

    ## `A[key]` get slot by name
    def __getitem__(self,key):
        return self.slot[key]

    ## `A[key] = B` set slot by name
    def __setitem__(self,key,that):
        self.slot[key] = that ; return self

    ## `A << B -> A[B.type] = B` set slot name as class name
    def __lshift__(self,that):
        self[that.type] = that ; return self

    ## `A >> B -> A[B.val] = B` set slot name as value
    def __rshift__(self,that):
        self[that.val ] = that ; return self

    ## `A // B -> A.push(B)` append as stack
    def __floordiv__(self,that):
        self.nest.append(that) ; return self


########################################################## Hello World (Python)

print( Frame('Hello') // Frame('World') << Frame('left') >> Frame('right') )

