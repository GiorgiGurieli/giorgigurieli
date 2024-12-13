# user1 = input("enter item :")
# user2 = input("enter item :")
# user3 = input("enter item :")
# user4 = input("enter item :")
# user5 = input("enter item :")

# arr = (user1, user2, user3, user4, user5)
# len() ----> სიგრძეს ჩვენი item-ისას
# for i in range(len(arr)):
    #print([i])

arr = [9,5,94,711,52,96,71,8]
min_number = arr[0]

for num in arr:
    if num >= min_number:
       min_number = num
print(min_number)
# ცვლადი = მნიშვნელობა
print(min(arr))
print(max(arr))


devices = ["TV" , "Notebook" , "PC"]
print(devices[1])

words = ["shelf", "store", "book"]
print(words[2] + words[1])

products =["apples", "oranges", "bananas"]
products[1] = "lime"
print(products[2])

name = "n"
surname = "g"
print(name + surname)
print(10 % 4)

games = ["snake", "puzzle", "shooter"]
games[1] = "Race"

products = ["juice" , "chocolate", "water"]
user_choice = 1
print(products[user_choice])

#      0 1  2  3  4  5  6  7
#                      -1
arr = [9,5,94,711,52,96,71,8]
#           index ებით მუშაობს
#       start/end/step
print(arr[0:5:2])
print(arr[4:])
print(arr[::1])
print(arr[::-1])
