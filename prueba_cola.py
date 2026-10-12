from cola import Cola

c = Cola()
c.enqueue("A")
c.enqueue("B")
c.enqueue("C")
print(c.dequeue())
print(c.dequeue())
print(c.dequeue())
print(c.dequeue())