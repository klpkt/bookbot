def count_words(text):
    flattened_lines = ' '.join(text.split('\n'))
    words = flattened_lines.split(' ')

    num_words = 0
    for word in words:
        if len(word): num_words += 1
    return num_words

def count_chars(text):
    counts = {}
    lowered = text.lower()

    for c in lowered:
        counts[c] = counts.get(c, 0) + 1
    return counts