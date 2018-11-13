# This file will only run correctly if you are using Python3!

def word_repeat(word, num_times):
    return word * num_times


def calculate_tax(bill, tax_rate):
    tax_rate = tax_rate / 100
    return bill * tax_rate

def total_bill(tax_rate, bill):
    tax_rate = tax_rate / 100
    tax_amount = bill * tax_rate
    return bill + tax_amount

def weeks_elapse(day1, day2):
    return int(abs(day2 - day1) / 7)

def average_grade(grade1, grade2, grade3, grade4):
    worst_grade = min(grade1, grade2, grade3, grade4)
    best_3 = (grade1 + grade2 + grade3 + grade4) - worst_grade
    return best_3 / 3

def bigger(x):
    return (2 * x) ** x

def apply_discount(dollar_amount):
    discount1 = 0.10 
    discount2 = 0.20
    if dollar_amount >= 100: 
        return dollar_amount * (1 - discount2)
    elif dollar_amount >= 50:
        return dollar_amount * (1 - discount1)
    else: 
        return dollar_amount
    
def where_i_live(city, country):
    '''(str, str) -> str
    
    return the country name once the function is run through
    >>> where_i_live("Toronto", "Canada")
    'I live in Toronto Canada'
    
    '''
    return "I live in " + city + ", " + country
    
    
        
def travel_cost(planetix, lodging):
    planetix = planetix * 1.1
    lodging = lodging * 1.1
    return planetix + lodging 

import math
dir(math)

def perimeter(side1, side2, side3):
    '''(number, number, number) -> number
    
    Return the perimeter of a triangle with sides length side1, side2, side3
    >>> perimeter(3, 4, 5)
    12
    >>> perimeter(10.5, 6, 9.3)
    25.8
    '''
    perimeter = side1 + side2 + side3
    return perimeter

def semiperimeter(side1, side2, side3):
    '''(number, number, number) -> float
    Return the semiperimeter of a triangle with sides length side1, side2, side3
    >>> semiperimeter(3, 4, 5)
    6.0
    >>> semiperimeter(10.5, 6, 9.3)
    12.9
    '''
    return perimeter(side1, side2, side3)

def area_hero(side1, side2, side3):
    ''' (number, number, number) -> float
    
    Return the area of a triangle with sides of length side1, side2, side3
    
    >>> area_hero(3, 4, 5)
    6.0
    >>> area_hero(10.3, 6, 9.3)
    27.731
    '''
    semi = semiperimeter(side1, side2, side3)
    area = math.sqrt((semi - side1) * (semi - side2) * (semi - side3))
    return area

def count_vowels(s):
    ''' (str) -> int
    return the number of vowels in s.

    >>>count_vowels("Happy Anniversary!")
    5
    >>>count_vowels("yyz")
    0
    '''
    num_vowels = 0
    for char in s: 
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1
    return num_vowels


