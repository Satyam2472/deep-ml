def dup_ngram_ratio(text: str, n: int) -> float:
    text = text.lower()
    text = text.split()
    print(text)
    
    freq_counter = {}
    
    # Slide the window across the text
    for i in range(len(text) - n + 1):
        context_window = text[i:i+n]
        context_window = " ".join(context_window)
        print(i, n, context_window, "\n")
        
        if context_window in freq_counter:
            freq_counter[context_window] += 1
        else:
            freq_counter[context_window] = 1
    
    total = 0
    dup = 0
    
    for key, value in freq_counter.items():
        total += value
        if value > 1:
            dup += value
    
    if total == 0:
        return 0.0  # Avoid division by zero
    
    return round(dup / total, 4)