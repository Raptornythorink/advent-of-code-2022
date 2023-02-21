def snafu_to_dec(x):
    n = len(x)
    s = 0
    for i in range(n):
        if x[i] == '-':
            s -= 5**(n-1-i)
        elif x[i] == "=":
            s -= 2*5**(n-1-i)
        else:
            s += int(x[i])*5**(n-1-i)
    return s

total = 0

while True:
    a = input()
    if not a:
        break
    total += snafu_to_dec(a)

print(total)

def dec_to_snafu(x):
    nx = x
    digits = []
    while nx > 0:
        digits.append(nx%5)
        nx //= 5
    s = ""
    n = len(digits)
    for i in range(n-1):
        if digits[i] == -2:
            s += '='
        elif digits[i] == -1:
            s += '-'
        elif digits[i] <= 2:
            s += str(digits[i])
        elif digits[i] == 3:
            s += str('=')
            digits[i+1] += 1
        elif digits[i] == 4:
            s += str('-')
            digits[i+1] += 1
        else:
            digits[i] -= 5
            digits[i+1] += 1
            if digits[i] == -2:
                s += '='
            elif digits[i] == -1:
                s += '-'
            elif digits[i] <= 2:
                s += str(digits[i])
            elif digits[i] == 3:
                s += str('=')
                digits[i+1] += 1
            elif digits[i] == 4:
                s += str('-')
                digits[i+1] += 1
    if digits[-1] == -2:
        s += '='
    elif digits[-1] == -1:
        s += '-'
    elif digits[-1] <= 2:
        s += str(digits[-1])
    elif digits[-1] == 3:
        s += '=1'
    elif digits[-1] == 4:
        s += '-1'
    else:
        if digits[-1]-5 <= 2:
            s += str(digits[-1]-5) + '1'
        elif digits[-1]-5 == 3:
            s += '=2'
        else:
            s += '-2'
    return s[::-1]

print(dec_to_snafu(total))

print(snafu_to_dec(dec_to_snafu(total)))