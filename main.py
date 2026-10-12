from pilas import Pilas

p = Pilas()
p.push("A")
p.push("B")
print(p.peek())   # B
print(p.pop())    # B
print(p.pop())    # A
print(p.pop())