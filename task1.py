marks = [45, 67, 89, 45, 90, 56, 67]
marks = list(dict.fromkeys(marks))
print(marks)

#Ans: Remove duplicates = [45, 67, 89, 90, 56]
#------------------------------

marks = [45, 67, 89, 45, 90, 56, 67]

avg = sum(marks) / len(marks)

print(avg)

#Ans: Find average marks = 65.6


#------------------------------


marks = [45, 67, 89, 45, 90, 56, 67]

highest = max (marks)
lowest = min (marks)

print("Highest Marks", highest)
print("Lowest Marks", lowest)

#Ans: Highest & Lowest Marks = 90 and 45



marks = [20, 30, 40, 50, 60, 70]

lowest = min (marks)

print("Lowest Marks", lowest)