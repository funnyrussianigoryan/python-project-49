def calc_gcd(num1, num2):
    if num1 == num2:
        return num1
    max_val = max(num1, num2)
    min_val = min(num1, num2)
    remainder = max_val % min_val
    if remainder == 0:
        return min_val
    return calc_gcd(num2, remainder)
