# Frozen set is immutable set
list1=[1,2,3,4,1,2,3,10]
x=set(list1)
print('duplicates removed',x)
s1=set([7,9,12,7,9])
s2=set(['abc',12,'b','car',7,10,12])
s3=set([12,14,12,'ab'])
print(s1|s2)
print(s1&s2)
print('b'in s2)
print('ab'in s2)
print('ab'in s3)
print(s2.discard(12))
print((s1&s2) ^ s3) # prints the uncommon parts
s=s1|s2|s3
print('abc' in s)
print(s)