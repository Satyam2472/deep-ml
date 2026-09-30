def unigram_probability(corpus: str, word: str) -> float:
    # Your code here
    voc = corpus.split(" ")
    feq = {}

    for i in voc:
        if i in feq:
            feq[i] += 1
        else:
            feq[i] = 1

    den = 0
    for key, value in feq.items():
        den += value

    return round(feq[word]/den, 4)

