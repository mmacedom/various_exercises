def check_password(passwd):
    """ (str) -> bool

    A strong password has a length greater than or equal to 6, contains at
    least one lowercase letter, at least one uppercase letter, and at least
    one digit.  Return True iff passwd is considered strong.

    >>> check_password('I<3csc108')
    True
    """
    lower = False
    upper = False
    digit = False
    
    if len(passwd) < 6: 
        return False
    for char in passwd: 
        if char.islower() and not lower: 
            lower = True
        if char.isupper() and not upper:
            upper = True
        if char.isdigit() and not digit:
            digit = True
    if lower and upper and digit:
        return True
    else:
        return False
 
            
      
   
        
          	  
def contains_no_lowercase_vowels(phrase):
    """ (str) -> bool

    Return True iff (if and only if) phrase does not contain any lowercase vowels.

    >>> contains_no_lowercase_vowels('syzygy')
    True
    >>> contains_no_lowercase_vowels('e')
    False
    >>> contains_no_lowercase_vowels('abc')
    False
    """
    for char in phrase: 
        if char in 'aeiou':
            return False
    return True     


'''check if the length is less than 6
go through each letter:
    check if its upper
    check if its lower
    check if its a digit
if it fufils all the conditions return ture'''




def every_nth_character(s, n):
    result = ''
    i = 0
    while i < len(s):
        result = result + s[i]
        i = i + n
    return result

def find_letter_n_times(s, letter, n):
    i = 0 
    count = 0
    while i < len(s):
        if letter in s:
            count = count + 1
        i = i + 1
    return count

def not_digit(s):
    i = 0
    while i < len(s) and s[i] not in '0123456789':
        i = i + 1
    return i

def count_collatz_steps(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
            steps = steps + 1
        if n % 2 != 0:
            n = (n * 3) + 1
            steps = steps + 1
    return steps

def count_uppercase(s):
    upper = 0 
    for char in s: 
        if char.isupper():
            upper = upper + 1
    return upper

def all_fluffy(s):
    if len(s) == len('fluffy'):
        for char in s:
            if char in 'fluffy':
                return True
            else:
                return False
    else: 
        return False
    
def add_underscore(s):
    underscore = ''
    i = 0
    for char in s:
        if i <= len(s):
            underscore = underscore + char + '_'
            i = i + 1
        else:
            underscore = underscore + char
            i = i
        
    return underscore

def different_types(obj1, obj2):
    if type(obj1) != type(obj2):
        return True
    else: 
        return False
    
            
def is_right_triangle(side1, side2, hypotenuse):
    if hypotenuse ** 2 == side1 ** 2 + side2 ** 2:
        return True
    else: 
        return False