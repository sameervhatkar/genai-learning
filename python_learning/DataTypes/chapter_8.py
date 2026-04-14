#Tuples

scores = (56, 70, 35, 48, 43)
print(scores)

(score1, score2, score3, score4, score5) = scores
print(f"The scores are {score1}, {score2}, {score3}, {score4}, {score5}")
print(f"The scores are {score1, score2, score3, score4, score5}")

#membership or contains
print(f"Did someone score 70 ? {70 in scores}")