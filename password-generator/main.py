import string, random
def generate_password(length = 10, letters = True, special_characters = True):
    if length < 10:
        return 'Your password is not long enough'
    
    alphabet = list(string.ascii_letters)
    special_characters_list = list(string.punctuation)   

    password = [str(random.randint(0, 9)) for i in range(length)]

    if not letters and not special_characters:
        return ''.join(password)

    if letters:
        unique_indexes = get_unique_index(length, length // 4)
        for index in unique_indexes:
            random_char = random.randint(0, len(alphabet) - 1)
            password[index] = alphabet[random_char]

    if special_characters:
        unique_indexes = get_unique_index(length, length // 3)
        for index in unique_indexes:
            random_char = random.randint(0 , len(special_characters_list) - 1)
            password[index] = special_characters_list[random_char]

    return ''.join(password)

def get_unique_index(length, indexes):
    unique_indexes = set()
    while len(unique_indexes) < indexes:
        unique_indexes.add(random.randint(0 , length - 1))

    return unique_indexes

print(generate_password(30))