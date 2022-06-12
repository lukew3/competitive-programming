def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def first(a, b):
        return a
    return pair(first)

def cdr(pair):
    def last(a, b):
        return b
    return pair(last)

# Tests
print(car(cons(3,4))) # 3
print(cdr(cons(3,4))) # 4
