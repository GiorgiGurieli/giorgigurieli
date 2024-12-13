list_of_numbers = [4,1,3,2,9] #3
len_list_of_numbers = len(list_of_numbers) #3✅

res = []
for i in range(len_list_of_numbers):
    res += list_of_numbers
print(res)


new_arr = ["davit", "gela"]
new_arr_1 = ["giorgi"]

print("----------------------------------------------------------------")

num = 1
messege = "gamarjoba" + "yvenebi rogor arian" +  str(num + 10) + "madloba kargad" + str(num + 10)
new_messege = "gamarjoba tqvenebi {} rogor arian madloba kargad {}" .format(num, num)
new_messege = "gamarjoba tqvenebi {x} rogor arian madloba kargad {y}" .format(y = 10 , x = 155)
print(messege)
print("new messege")
print(new_messege)

print(messege)


_string = "jobnis jobni ar dailevao!"
_split_str = str.split(" ")
print(_split_str)

new_string = "kvici,gvarze,xtis"
new_split_string = new_string.split(",")
print(new_split_string)

print("------------------join-----------------------------")

arr_of_madness = ['jobnis', 'jobni' , 'ar' , 'dailevao']
joined_arr_of_madness = "!".join(arr_of_madness)
print(joined_arr_of_madness)

print("-------------------------replace-----------------------------")

_str_of_vowels = "aeiou"
_updated_str_of_vowels = _str_of_vowels.replace(""," ")
_updated_str_of_vowels = _updated_str_of_vowels.split()
_updated_str_of_vowels = "⏭️ ".join(_updated_str_of_vowels)
_updated_str_of_vowels = _updated_str_of_vowels.split()
_updated_str_of_vowels = "✅ ".join(_updated_str_of_vowels)
print(_updated_str_of_vowels)

print("-------------------lower-upper---------------------")

name = "group 47"
print(name.upper()) # ადიდებს
print(name.lower()) # აპატარავებს
print(name.capitalize()) # პირველ ასოს ადიდებს მხოლოდ

