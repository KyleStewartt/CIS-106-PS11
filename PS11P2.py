def computeTotalAndAverageScore(scores):
    totalPoints = sum(scores)
    averageScore = totalPoints / len(scores)
    return totalPoints, averageScore
lastName = input("Enter the student's last name: ")
examScores = []
for i in range(3):
    examScore = float(input(f"Enter exam score {i+1}: "))
    examScores.append(examScore)
totalPoints, averageScore = computeTotalAndAverageScore(examScores)
print("Last Name: ", lastName)
print("Total Points: ", totalPoints)
print("Average Score: ", averageScore)