#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dan
#
# Created:     13/04/2013
# Copyright:   (c) Dan 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
f1=open("C-large-1.in","r")
f2=open("C-large-2.out","w")
nrcases=f1.readline()
def is_palindrom(x):
    pal=True;
    i=0;
    while (i <= len(str(x))/2) and pal:
        y=str(x);
        if y[i]!=y[len(y)-i-1]:
            pal=False
        else:
            i=i+1
    return pal
array=[]
for line in f1: # read rest of lines
        array.append([int(x) for x in line.split()])

for count2 in range(0,int(nrcases)):
 array2=[]
 array3=[]
 x=0
 A=int(array[count2][0])
 B=int(array[count2][1])
 for count in range(A,B+1):
    for j in range(0,int(count+1/2)):
        y2=str(j)
        y=j*j
        if y==count and is_palindrom(count) and is_palindrom(j):

             array2.append(count)


 print("Case #"+str(count2)+":",len(array2),file=f2)
f2.close()











