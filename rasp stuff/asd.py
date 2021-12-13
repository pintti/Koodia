def checker(string):
    left = 0
    right = 0
    for letter in string:
        if letter == "(":
            left += 1  
        if letter == ")":
            if left <= right:
                return False
            right += 1

    if left==right:
        return True
    else:
        return False

print(checker(input()))