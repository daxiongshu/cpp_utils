import session_split
s = [1, 1, 2, 2, 2]
x = [3, 5, 6, 5, 7]
y = [4,8,8,9,9]
X,Y = session_split.split_session(s,x,y)
print('X')
print(X)
print('Y')
print(Y)