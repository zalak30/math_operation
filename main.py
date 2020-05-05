# mathematical_operation
print('Enter two numbers')
a = int(input())
b = int(input())


def mathematical_operation(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)             # integer division
    print(a/b)              # float division


mathematical_operation(a, b)