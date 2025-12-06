import os


def find_fresh(fresh_ranges, id_list):
    fresh_ingredients = 0
    for id in id_list:
        for low, high in fresh_ranges:
            if low <= int(id) <= high:
                fresh_ingredients += 1
                break
    return fresh_ingredients


def find_fresh_id_old(fresh_ranges):
    """
    Too slow, abandoned.
    """
    fresh_id = set()
    for low, high in fresh_ranges:
        for id in range(low, high + 1):
            fresh_id.add(id)
    return len(fresh_id)


def find_fresh_id(fresh_ranges):
    """
    Merge intervals first
    """
    merged_lists = []
    fresh_ranges.sort()
    for low, high in fresh_ranges:
        if not merged_lists:
            merged_lists.append([low, high])
        else:
            last_low, last_high = merged_lists[-1]
            if low <= last_high:
                merged_lists[-1][1] = max(last_high, high)
            else:
                merged_lists.append([low, high])

    total = 0
    for l, r in merged_lists:
        total += (r - l + 1)
    return total


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    # file_path = os.path.join(script_dir, 'example_input.txt')
    file_path = os.path.join(script_dir, 'input.txt')
    if os.path.exists(file_path):
        with open(file_path) as f:
            lines = f.read().splitlines()
        blank_index = lines.index("")
        range_lists = lines[:blank_index]
        id_list = lines[blank_index+1:]
        fresh_ranges = []
        for range_list in range_lists:
            low, high = range_list.split("-")
            fresh_ranges.append((int(low), int(high)))
        print(find_fresh(fresh_ranges, id_list))
        print(find_fresh_id(fresh_ranges))
    else:
        print("Input file not found.")