numbers = [1,2,3,4,5,6,7,8,9,10]

result = []

new_result = [i for i in numbers if i%2==0]

print(new_result)

#Ans:list comprehension [2, 4, 6, 8, 10]