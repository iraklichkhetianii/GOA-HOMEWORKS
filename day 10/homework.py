# #homework 1: შექმენით სია პროგრამირების ენების შესახებ, შეიტანეთ 5 პროგრამირების ენა. დაპრინტეთ  ჯერ მთლიანი სია, შემდეგ კი ბოლო ელემენტი.
HM_list1 = ["c++", "python", "html", "javascript", "c#"]

print(HM_list1)
print(HM_list1[4])
  

#homework 2: შექმენით სია, სადაც გექნებათ შეტანილი string, integer, float, boolean. საბოლოოდ ყველა ელემენტი ცალ-ცალკე გამოიტანეთ.

HM_list2 = [5, "I am string", 2.5, True]
print(HM_list2[0])
print(HM_list2[1])
print(HM_list2[2])
print(HM_list2[3])

#homework 3: შექმენით სია, სადაც გექნებათ 0-იდან 20-ის ჩათვლით 4-ის ჯერადები და პრინტით გამოიტანეთ უდიდესი.

HM_list3 = []

for i in range (0,21):
    if i % 4 == 0 and i != 0:
       HM_list3.append(i)
       print(max(HM_list3))

#homework 4: შექმენით სია სადაც შეტანილი გექნებათ 30-იდან 50-ის ჩათვლით კენტი რიცხვები. შემდეგ დაპტინტეთ სამი უმცირესი ელემენტის ჯამი.
       
HM_list4 = []

for x in range (30,51):
    if x % 2 == 1:
       HM_list4.append(x)

HM_list4.sort()
print(HM_list4[0] + HM_list4[1] + HM_list4[2]) 

#homework 5:დაპრინტეთ სამის ჯერადები დავალება 4-ის სიიდან. 
HM_list5 = ()
for y in HM_list4:
    if y % 3 == 0:
       
       HM_list5.append(y) 