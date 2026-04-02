import random

array_a = random.sample(range(-100,100), 10)
print(array_a)
print(min(array_a, key=abs))
array_a.reverse()
print(array_a)

array_b = random.sample(range(-100, 100), 10)
print(array_b)
array_a, array_b = array_b, array_a
print(array_a,'\n',array_b)