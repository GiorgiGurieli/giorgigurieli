# დავალება 1:
# შექმენით სია სადაც იქნება სხვადასხვა ასოები და მხოლოდ ხმოვნები დაითვალეთ

arr = ["a","d","d","f","f","s","a","y"]
arr_of_vowels = ["a","e","i","o","u","y"]
counter_of_vowles = 0

for char in arr:
    for vowel in arr_of_vowels:
        if char == vowel:
            counter_of_vowles += 1

# print(counter_of_vowles)

# დავალება 2:
# შექმნი სიას სადაც იქნება სადაც იქნება ციფრები რომელიც გამოიყვანს 5 სა და 3ის ჯერადებს
new_arr = [1,23,4,5,6,7,8,9,11,3,3,4,5,6,15]
for i in range(len(new_arr)):
    if (new_arr[i] % 5 == 0) and (new_arr[i] % 3 == 0):
        print(new_arr[i])
# დავალება 3 :
# შექმნი სიას სადაც იქნება სხვადასხვა ასოები და ციფრები
# ხოლო წარმოდგინე ეს ელემენტები ერთ სტრინგში

# დავალება 4 :
# შექმნით რომბი
# ******
#  ******
#   ******
#    ******
Shaurma = "******"
for i in range(4):
    print(" " * i + Shaurma)
# დავალება 5 :
# მომხმარებელს შეეკითხეთ თუ რამდენი წლის არის მომხმარებელი შემდეგ შევანახინოთ თუ ეს მომხმარებელი არის 12 წლის ზემოთ მაშინ დაგვიპრინტოს "შენ არ ხარ 12 წლის"     


# ფუნქიებს აქვს გამხსნელი და დამხურავი ფრჩხილები
# ხოლო მის შიგნით კი იწერება არგუმენტები/ მაგალითად
# ყველა ყველა ფუნქციას აქვს სხვადასხვა დანიშნულება
# ხოლო ფუნქციები გვეხმარებიან კოდის შემცირებაში და უკეთ დაწერაში
#        argument / მაგალითი
print("group 47")
print("group 48")


new_list = [1,2,3,4,5,6,7]
# list
# len() ---- სიგრძეს ჩვენი list ისას
print(len(new_list))
x ="abc"
x *= 2

letters = ["a","b","c"]
letters += ["d"]
print(letters)


# append() ---- სიაში დამატება იღონდ როგორც ბოლო ელემენტი ისე

arr = []
print('-------append-------')
arr.append(2.7)
arr.append(True)
arr.append("daviti")

print(arr)

# classwork 1, დან 100 ჩათვლით გამოიტანეთ ციფრები და დაამატეთ სიაში
#           0         1       2          3         4           5
bro_arr = ["davit","ucha","MR.Gurams","bro", "ტელეფონი", "პროგრამირება"]
bro_arr.insert(4,"is")
print('-------insert--------')

print(bro_arr)
print('-------INDEX-------')
letters = ['p','q','r','s','p','u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('q'))


print('-------------------------------------------------------------')
#         -4 -3    -2   -1
x = [2, 4, 6, 2, 7,4, 2, 9]
print(x.count(7))

x.remove(4)
print(x)

x.reverse
print(x[::-1])