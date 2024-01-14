

def binary_search( x, number  ):

    """
    Returns the index of any occurence of the number = number 
    in the given a sorted array x. Returns -1 if the array doesnt contain number.

    Args:
        x (array or list) sortedin ascending order 
        number: number 
    
    Returns 

        index (int): index of one occurence of number in x

    """

    n1, n2  = 0, len(x)-1
    while n1 <= n2:

        n = int((n1+n2)/2)

        if    x[n] > number: n2 = n - 1 
        elif  x[n] < number: n1 = n + 1
        else: return n


    return -1


def binary_interval_search( x, number ):
    """
    Returns the tuple (i1,i2)
    that corresponds to the indices of the first and second occurences of number in the array x
    Array x must be sorted in ascending order. Both i1, and i2 are set to -1 if number is not 
    found in the array

    Args:
        x (array or list) sorted in ascending order 
        number (number) a number to search for in x
        

    Returns: 
        (i1:int ,i2:int ):  
        indices of the first and second occurences of number in the array x 
        i1=i2=-1 if the array doesnt contain the number 
    

            
    Example:
        x= [1,2,3,3,3,4,5]

        binary_interval_search( x, 3 ) 
        >> ( 2,4 )
    """

    i1 = binary_search( x, number)
    if i1 == -1: return (-1,-1)

    #solution 1
    #n2 = i1 
    #while  n2 <= len(x)-1 and x[n2] == number: n2+=1
    #while  i1 >=0 and x[i1] == number: i1-=1
    #return  i1+1, n2 - 1


    #solution 2 
    n1 = 0
    while n1 < i1 and x[n1] < number: n1 = n1 + int( (i1-n1+1)/2 ) 
    while n1 >=0 and x[n1] == number: n1-=1

    n2 = len(x)-1
    while  n2 > i1 and x[n2] > number: n2 = i1 + int (  (n2-1-i1)/2 )
    while  n2 <= len(x)-1 and x[n2] == number: n2+=1


    return n1 + 1, n2 - 1



x = [1,1,1,3,3,3,7 ]
r = binary_interval_search( x, 3 )

print( r )


'''
print(' binary search ')
print(  binary_search( [1,2,3], 1) )   #  0
print(  binary_search( [1,2,3], 2) )   #  1
print(  binary_search( [1,2,3], 3) )   #  2  
print(  binary_search( [1,2,3], -1) )  # -1 
print(  binary_search( [1,2,3], 11) )  # -1
print(100*'-')
print(  binary_search( [1], 1) )  # 0
print(  binary_search( [1], -1) )  # -1
print(100*'-')
print(  binary_search( [1,2,3,4,4,4,4,6,7], 4) )  # 3

print(100*'-')
print(100*'-')
'''


 

