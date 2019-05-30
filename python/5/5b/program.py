from stack.create import Stack
from queue.create import Queue
a=Stack([1,2,3,4])
b=Queue([1,2,3,4])
print('Stack:',a)
print('Top:',a.top())
print('Inserting 5 to a')
a.insert(5)
print(a)
print('Popping out top')
a.remove()
print(a)
print('\n\n')
print('Queue:',b)
print('Front:',b.front())
print('Rear:',b.rear())
print('Inserting 5 to b')
b.insert(5)
print(b)
print('Popping out front')
b.remove()
print(b)
print('\n\n')
