# Highest and Lowest
# In this little assignment you are given a string of space separated numbers
# and have to return the highest and lowest number

# Examples

# Input: "1 2 3 4 5" => Output: "5 1"
# Input: "1 2 -3 ...

# parameters: 
def high_lower(_str):
    res = _str.split(" ")
    
    _arr = []
    for elem in res:
        _arr.append( int(elem) )
        
    return f"{ max(_arr) } { min(_arr) }"

# arguments
print( high_lower("1 2 3 4 5") )
#           _str = "1 2 3 4 5"
print( high_lower("2 3 4 6 9 12 44 55 11") )
#           _str = "2 3 4 6 9 12 44 55 11"
print( high_lower("299 11 123 123123") )
#           _str = "299 11 123 123123"

# ----------------------- in / not / ---------------
# in / not 

def find_vowel(x):
    vowel = "a e i o u"
    arr = ["a", "e", "i", "o", "u"]
    # გვეუნება თუ ჩვენი გადმოცემული element არის ჩვენს string ან სიაში
    if x  in arr: # True /    not in False     /
        return "მალედეცც!! შენ აღმოაჩნიე ხმოვნები."
    else:
        return "არა, შენ ვერ იპოვნე ხმოვენბი... წადი სახში."
print("-------------------------")
print( find_vowel("d") )
print( find_vowel("a") )
print( find_vowel(1) )

print("-----------not--operator -example--------------")
print(not False)
print(not True)