a = 500
b = 100

if (a == b):
    print("inside if")
else:
    print("inside else")

i = 0
while(i < 5):
    print("value of i ", i)
    i = i + 1
else:
    print("value of i ",i)
print('outside of while')


names = ['a','b','c']
for i in names:
    print(i) 

for i in range(0,5):
    print(i)
    i = i + 1
else:
    print(i)

numbers=[10,20,30,40]
for i in (11,22,30):
    if i in numbers:
        print(i)
    