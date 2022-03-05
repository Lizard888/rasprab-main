import pdb
x=0
z=1
print('введите x')
x=int(input())
def dd():
    global x
    global z
    x=x+1
    print(x)
    if x==1:     
        dd()
      
        z=2
    else: z==1
    print(x)
    
if z==1: dd()
print(x)
print(z)
