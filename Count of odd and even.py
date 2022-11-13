
num = (1,2,3,4,5,6,7,8,9)
even = 0
odd = 0
for i in num:
    if i%2 == 0:
        even = even+1
    else:
        odd = odd+1
print('Even Numbers: ', even)
print('Odd Numbers: ', odd)   