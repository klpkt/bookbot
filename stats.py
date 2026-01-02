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

def sort_on(items):
    return items["num"]

def sort_counts(counts):
    sorted_counts = []
    for key in counts:
        sorted_counts.append({
            "char": key,
            "num": counts[key]
        })
    sorted_counts.sort(reverse=True, key=sort_on)
    return sorted_counts