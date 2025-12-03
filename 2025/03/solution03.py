import os

def find_joltage_2(s):
    s = s.strip()
    digits = [int(c) for c in s]
    tens_digit = max(digits[:-1])
    j = digits.index(tens_digit)
    unit_digit = max(digits[(j+1):])
    joltage = 10 * tens_digit + unit_digit
    return joltage


def find_joltage_12(s, num_of_digits = 12):
    s = s.strip()
    length = len(s)
    stack = []
    pop_num = length - num_of_digits
    if num_of_digits > length:
        return int(s)
    for char in s:
        while stack and pop_num > 0 and stack[-1] < char:
            stack.pop()
            pop_num -= 1
        stack.append(char)
    if pop_num > 0:
        stack = stack[:-pop_num]
    final_joltage = int(''.join(stack))
    return final_joltage


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'input.txt')
    sum_joltage = 0
    if os.path.exists(file_path):
        with open(file_path) as f:
            lines = f.readlines()
        for line in lines:
            sum_joltage += find_joltage_12(line)
        print(sum_joltage)
            
    else:
        print("Input file not found.")