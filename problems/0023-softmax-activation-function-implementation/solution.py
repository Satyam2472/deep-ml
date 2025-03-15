import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here
	probabilities = []
	sum_ = 0

	for i in range(len(scores)):
		sum_ += math.exp(scores[i])

	for i in range(len(scores)):
		softmax = round(math.exp(scores[i])/sum_, 4)
		probabilities.append(softmax)

	return probabilities