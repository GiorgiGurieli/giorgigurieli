# 1)
#        0           1       2        3
#       -4         -3        -2      -1
arr = ["flower" , "gela", "vardi", "lomi"]
print(arr[0])
print(arr[-1])

# 2)
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr[0], arr[4], arr[-1])

# 3)
ცხობელები = ["დათვი", "ვეფხვი", "მგელი", "ზებრა"]
ცხობელები[0] = "ლომი"
print(ცხობელები)

# 4)
films = ["maze runner", "matrix", "interstellar"]
print(films[-1])

# 5)
numb = [1,23,4,5,5,6,6,1212312,31,4,5,12,3]
# slicing   დასაწყისი, დასასრული, გადახტომა
print('---------------------------------------------')
#print(numb[-2:])

vechicle = "motorbike"
print(vechicle[:])

platform = ["IOS", "android", "web"]
print(platform[:])

options = ['A','B','C','D']
print(options[1:3])

animals = ['cat', 'dog', 'bird']
print(animals[1])

for i in range(len(numb)):
    print(numb[i])