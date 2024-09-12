def calcula_fibonacci(x):
    if x == 0:
        return [0]
    elif x == 1:
        return [0, 1]
    else: 
        result = [0 , 1]
        for i in range(2 , x + 1):
            result.append(result[i - 1] + result[i - 2])
            
        return result
