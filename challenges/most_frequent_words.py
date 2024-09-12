import re
def top_3_words(text):
    pattern = r"[a-zA-Z']*[a-zA-Z]+[a-zA-Z']*"
    word_list = re.findall(pattern, text.lower())
    words = {}
    for word in word_list:
        if word:
            if word not in words:
                words[f'{word}'] = 1
            else: 
                words[f'{word}'] += 1

    unique_values = (sorted(words.values(), reverse=True))

    if not unique_values:
        return []

    answer = []
    try:
        while True:
            for i in words.keys():
                if words[f'{i}'] == unique_values[0]:
                    answer.append(i)
                    del unique_values[0]
                if len(answer) == 3:
                    return answer
    except:
        return answer