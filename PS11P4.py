def computeAverages(gameScores, handicap):
    averageScore = sum(gameScores) / len(gameScores)
    averageScoreWithHandicap = (sum(gameScores) + handicap) / len(gameScores)
    return averageScore, averageScoreWithHandicap
lastName = input("Enter the bowler's last name: ")
gameScores = []
handicap = int(input("Enter the bowler's handicap: "))
for i in range(3):
    gameScore = int(input(f"Enter game score {i+1}: "))
    gameScores.append(gameScore)
averageScore, averageScoreWithHandicap = computeAverages(gameScores, handicap)
print("Last Name: ", lastName)
print("Average Score: ", averageScore)
print("Average Score with Handicap: ", averageScoreWithHandicap)