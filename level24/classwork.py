num = 1
messege = "ილი კარგია ბიჭია მას უყუარს" + "10 ჯერ აწნვლა ბურთის"+ str(num + 10) + "20 ჯერ კი ბურთის გახეტქვა" + str(num + 10)
new_messege = "ილი კარგია ბიჭია მას უყუარს {} 10 ჯერ აწნვლა ბურთის {} 20 ჯერ კი ბურთის გახეტქვა".format(num, num)
new_messege = "ილი კარგია ბიჭია მას უყუარს {0} 10 ჯერ აწნვლა ბურთის {0} 20 ჯერ კი ბურთის გახეტქვა".format(num, num)
print(messege)
print("new messege")
print(new_messege)

print(messege)


new_string = "შაურმა არ არის  ხინკალზე კაი"
new_split_string = new_string.split(",")
print(new_split_string)

xinkali = ['შაურმა' , 'არ არის' , 'ხინკალზე კაი']
joined_xinkali = "?".join(xinkali)
print(xinkali)