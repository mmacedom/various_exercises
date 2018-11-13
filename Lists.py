alkaline_earth_metals = [['beryllium', 4], ['calcium', 20], ['strontium', 38], ['barium', 56], ['radium', 88]]

def metal_length(alkaline_earth_metals):
    return len(alkaline_earth_metals)

def highest_num(alkaline_earth_metals):
    print(max(alkaline_earth_metals))

def same_first_last(L):
    if L[0] == L[-1]:
        return True
            
    else:
        return False
    
def is_longer(L1, L2):
    '''(list, list) -> bool
    '''
    if len(L1) > len(L2):
        return True
    else: 
        return False
        
        
def test_function(element):
    for inner_list in element:
        for item in inner_list: 
            for char in item: 
                print(char)
                
                
def test_2(list):
    for num in list:
        print(num)
        
def for_whales(numbers):
    more_whales = []
    for num in range(len(numbers)): 
        more_whales = more_whales + [numbers[num] + 1]
    return more_whales



def metals_func(alkaline_earth_metals):
    alkaline_earth_metals = [[4, 9.012], [12, 24.305]]
    number_and_weight = []
    
    for num in alkaline_earth_metals: 
        for item in num:
            number_and_weight = number_and_weight + [item]
    return number_and_weight
    

def population_of_countries(country_populations):
    total = 0
    
    for num in country_populations: 
        total = total + num
    return total

country_populations = [1295, 23, 7, 3, 47, 21]

def rat_weights(initial_weight):
    '''(float) -> float
    
    Return the numbere of weeks it would take for rat_1 and rat_2 to increase their weights but a certain percentage.
    '''
    rat_1 = initial_weight
    rat_1_rate = 1.05
    day = 0
    
    while rat_1 < (rat_1 * 1.25):
        rat_1 = rat_1 + (rat_1 * (rat_1_rate / 7))
        day = day + 1
        
    return day
        
    


def print_numbers(num1, num2):
    new_list = []
    for num in range(num1, num2, -1):
        new_list = new_list + [num]
    print(new_list)
        
num1 = 10
num2 = 0

def num_average(number1, number2):
    total = 0
    i = 0
    for number in range(number1, number2):
        total = total + number
        i = i + 1
        
    print(total, total/i)
    
number1 = 2
number2 = 23