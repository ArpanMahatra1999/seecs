import random, string

# Assigning initial values
lower, upper, number, symbol = string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation
lower_list, upper_list, number_list, symbol_list = list(lower), list(upper), list(number), list(symbol)


def create_unverified_password(length):
    all = lower + upper + number + symbol

    # Creating temporary value
    temporary_value = random.sample(all, length)

    return temporary_value


def verify_password(unverified_password):
    lower_verified, upper_verified, number_verified, symbol_verified = [], [], [], []

    for l in lower:
        if l in unverified_password:
            lower_verified.append(True)
        else:
            lower_verified.append(False)

    for u in upper:
        if u in unverified_password:
            upper_verified.append(True)
        else:
            upper_verified.append(False)

    for n in number:
        if n in unverified_password:
            number_verified.append(True)
        else:
            number_verified.append(False)

    for s in symbol:
        if s in unverified_password:
            symbol_verified.append(True)
        else:
            symbol_verified.append(False)

    if any(lower_verified) and any(upper_verified) and any(number_verified) and any(symbol_verified):
        return "".join(unverified_password)
    else:
        return ''


def create_password(length):
    unverified_password = create_unverified_password(length)
    verified_password = verify_password(unverified_password)
    while verified_password == '':
        unverified_password = create_unverified_password(length)
        verified_password = verify_password(unverified_password)
    return verified_password
