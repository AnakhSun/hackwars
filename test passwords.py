def alphanumeric(password):
    numbers = [str(i) for i in range(0, 10)]
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    return not ((not any([x.lower() in password for x in chars]) and not any([x.upper() in password for x in chars])) or (any([x not in password for x in numbers]) and any([x not in chars and x not in numbers for x in password.lower()])) or any([x not in chars and x not in numbers for x in password.lower()]))


print(alphanumeric("PassW0rd"))