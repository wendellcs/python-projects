# Examples

# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7Test"        -->  "app7_test"
# 1                 -->  "1"

import re
def to_underscore(string):
    if type(string) == int:
        return str(string)
    
    if type(string) == int:
        return str(string)
    
    answer = string
    for i in range(len(string)):
        if string[i].isupper():
            answer = answer.replace(string[i], '_' + string[i])
    
    if answer[0] == '_':
        while answer[0]=='_':
            answer = answer[1:]
    return answer.replace('__', '_').lower()