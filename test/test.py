from cpp_utils import split_session
s = [1, 1, 2, 2, 2]
x = [3, 5, 6, 5, 7]
y = [6, 6, 8, 8, 8]
X,Y = split_session(s,x,y)
print('session')
print(s)
print('items viewed')
print(x)
print('items purchased')
print(y)
print('X')
print(X)
print('Y')
print(Y)