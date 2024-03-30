# #homework1: შექმენით სია სადაც გადასცემთ 10 ინტეგერს, შემდეგ გადაუარეთ ამ სიას და თითოეული მათგანი გაამრავლეთ/გაყეთ/დაუმატეთ/გამოაკელით

HM_list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(HM_list1[0] + HM_list1[1])
print(HM_list1[1] * HM_list1[2])
print(HM_list1[2] / HM_list1[3])
print(HM_list1[3] != HM_list1[4])
print(HM_list1[4] < HM_list1[5])
print(HM_list1[5] > HM_list1[6])
print(HM_list1[6] * HM_list1[7])
print(HM_list1[7] - HM_list1[8])
print(HM_list1[8] + HM_list1[9])

# #homework2:შექმენით სია, სადაც გამოიტანთ სათითაოდ მნიშვნელობებს და ასევე ჩაანაცვლებთ სხვა მნიშვნელობებით.

animals = ["dog", "tiger", "lion"]
print(animals)

animals[0] = 'cat'
animals[2] = 'giraffe'
animals[1] = 'wolf'

print(animals)

#homework3:შექმენით სია და მომხმარებელს აარჩევინეთ სასურველი მნიშვნელობა.

products = ["juice", "twix", 'banana']

user_choice = int(input("Enter a num:"))

print(products[user_choice])



