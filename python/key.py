

'''
Key Functions
Both list.sort() and sorted() have a key parameter to specify a function (or other callable) to be called on 
each list element prior to making comparisons. The function should take a single argument and must return a 
key (an object) that python can use for sorting purposes. 

In this example we have a function that returns an integer code for a string passed as argument. 
Being an integer, it can be directly compared by the python interpreter.  The code returned by the 
function  is just the sum of the integer representation of the first and last characters of s. 
If s is only of character loong, then the int is twice the int code of the single character.   
'''
def end_letters_as_int( s ): 
    '''
    This function returns an integer number which is the sum of the integer representation of the first 
    and last letter of the string s 
    '''
    
    #print('being called wuit arg', s, ord( s[0] ) + ord( s[-1:]   ))
    return ord( s[0] ) + ord( s[-1:] )  
    


names = ['aaaa','azzz','ac','ab','bb','czzzzd','cxxxxd']



print( 'sorted', sorted( names, key = end_letters_as_int ))
#That means that when multiple records have the same key, their original order is preserved.

print( 'max',max(names))
print( 'max',max(names, key = end_letters_as_int))