1#
def litres(time):
    return (0.5*time)//1

#2
def paperwork(n, m):
    return max(n, 0)*max(m, 0)

#3
def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product

#product მეთოდი აბრუნებს ელემენტების ნამრავლს მოცემული iterable-დან.

#4
def fake_bin(x):
    b = str()
    for a in x:
      if a < "5":
          b += "0"
      else:
          b += "1"
    return b

#5
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return list(range(x, x*n+1, x))


#6
def to_jaden_case(string):
      # დაყავით შეყვანის სტრიქონი სიტყვების სიაში
      # split() მეთოდი ყოველგვარი არგუმენტების გარეშე იყოფა  
    words = string.split()

      # გამოიყენეთ სიის გააზრება ახალი სიის შესაქმნელად, სადაც თითოეული სიტყვაა ორიგინალური სიიდან  არის დიდი ასოებით.
      # capitalize() მეთოდი აწერს სტრიქონის პირველ ასოს დიდად.
      # და აკეთებს ყველა სხვა სიმბოლოს სტრიქონში მცირედ.
    capitalized_words = [word.capitalize() for word in words]

    result = ' '.join(capitalized_words)

      # დააბრუნეთ მიღებული სტრიქონი
    return result

#7