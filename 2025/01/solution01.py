import os

def hit_zero(instructions, start=50, dial_size=100):
    """
    Calculate how many times it hits zero
    """
    pos = start
    hits = 0
    for i in instructions:
        i = i.strip()
        if not i:
            continue
        dir_char = i[0].upper()
        dist = int(i[1:])
        if dir_char == "L":
            pos = (pos - dist) % dial_size
        elif dir_char == "R":
            pos = (pos + dist) % dial_size
        if pos == 0:
            hits += 1
    return hits


def pass_zeros(instructions, start=50, dial_size=100):
    """
    Calculate how many times it passes zero
    Abandoned function
    """
    pos = start
    hits = 0
    for i in instructions:
        i = i.strip()
        if not i:
            continue
        dir_char = i[0].upper()
        dist = int(i[1:])
        
        # full circles
        hits += dist // dial_size
        # handle remainder
        remainder = dist % dial_size
        if remainder == 0:
            continue
            
        old_pos = pos
        if dir_char == "L":
            pos = (pos - remainder) % dial_size
            if pos == 0 or (pos > old_pos and old_pos != 0):
                hits += 1
        elif dir_char == "R":
            pos = (pos + remainder) % dial_size
            if pos < old_pos:
                hits += 1
    return hits


def count_all_zeros(instructions, start=50, dial_size=100):
    """
    Calculate how many times it passes zero
    Better way
    """
    pos = start
    hits = 0
    for i in instructions:
        i = i.strip()
        if not i:
            continue
        dir_char = i[0].upper()
        dist = int(i[1:])
        if dir_char == "R":
            # pos < k * 100 <= pos + dist
            hits += (pos + dist) // dial_size - pos // dial_size
            pos = (pos + dist) % dial_size
        elif dir_char == "L":
            # pos - dist <= k * 100 < pos
            hits += (pos - 1) // dial_size - (pos - dist - 1) // dial_size
            pos = (pos - dist) % dial_size
            
    return hits

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'input.txt')
    if os.path.exists(file_path):
        with open(file_path) as f:
            lines = f.readlines()
        print(hit_zero(lines))
        print(pass_zeros(lines))
        print(count_all_zeros(lines))
    else:
        print("Input file not found.")