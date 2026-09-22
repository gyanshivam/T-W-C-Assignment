classMates = ["Shahrukh", "Salman", "Aamir", "Gyan Abhijeet", "Larry Page"]

print("The Class∞ has: ", classMates)

print("There are in total ", len(classMates), " members in the class")
print("First student of the class is: ", classMates[0])
print("Last but the most intelligent student of the class is: ", classMates[-1])
print("The first three stupid students are: ", classMates[0: 3])

classMates.append("Sunny")
classMates.append("Sonu")
classMates.append("Bittu")
print("The Class∞ now has: ", classMates)
classMates.pop(2)
classMates.remove("Salman")
print("The Class∞ now has three new stupid students after removing two: ", classMates)
classMates.sort()
print("Now arranging them alphabetically: ", classMates)
classMates.reverse()
print("Now arranging them in reverse order: ", classMates)

teacherProfile = {
    "name": "Laxmi Narayan",
    "domain": "everything",
    "experience": "∞x∞x∞"
}

print("The teacher for all and their details: \n", teacherProfile)
print(f"The subject taught by the teacher: ", teacherProfile["domain"])
print(f"The experience of the teacher: ", teacherProfile["experience"])

teacherProfile["residence"] = "Omnipresent"
print("The teacher for all and their details: \n", teacherProfile)

allTimeRank = [1, 2, 3, 4, 5]
names = ["Gyan Abhijeet","Rishi Paani", "Tesla", "Albert Einstein", "Dhyan Chand"]

geniusTop5 = dict(zip(allTimeRank, names))

print("The final list of top 5 genius are: ", geniusTop5)
print(f"The Rank #1 is {geniusTop5[1]} and Rank #5 is {geniusTop5[5]}")
