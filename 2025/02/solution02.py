import math

def add_invalid_id(id1, id2):
    """
    Add invalid id from id1 to id2
    Invalid id: repeate twice
    """
    invalid_sum = 0
    start = int(id1)
    end = int(id2)

    if end < start:
        return 0
    else:
        # loop through all ids from start to end
        for id in range(start, end + 1):
            str_id = str(id)
            length = len(str_id)
            if length % 2 != 0:
                continue
            
            half = length // 2
            if str_id[:half] == str_id[half:]:
                invalid_sum += id

    # print(invalid_sum)
    return invalid_sum


def add_invalid_id_new(id1, id2):
    """
    Add invalid id from id1 to id2
    Invalid id: repeate at least twice
    """
    invalid_sum = 0
    start = int(id1)
    end = int(id2)

    if end < start:
        return 0
    else:
        for id in range(start, end + 1):
            str_id = str(id)
            length = len(str_id)
            # find possible patterns
            for p in range(1, (length // 2) + 1):
                if length % p != 0:
                    continue
                else:
                    pattern = str_id[:p]
                    if pattern * (length // p) == str_id:
                        invalid_sum += id
                        break # Prevent counting same id multiple times, for example 111111 have different patterns
            

    # print(invalid_sum)
    return invalid_sum



if __name__ == "__main__":
    example_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    input = "67562556-67743658,62064792-62301480,4394592-4512674,3308-4582,69552998-69828126,9123-12332,1095-1358,23-48,294-400,3511416-3689352,1007333-1150296,2929221721-2929361280,309711-443410,2131524-2335082,81867-97148,9574291560-9574498524,648635477-648670391,1-18,5735-8423,58-72,538-812,698652479-698760276,727833-843820,15609927-15646018,1491-1766,53435-76187,196475-300384,852101-903928,73-97,1894-2622,58406664-58466933,6767640219-6767697605,523453-569572,7979723815-7979848548,149-216"
    # numbers = example_input.split(',')
    numbers = input.split(',')
    all_invalid_sum = 0
    for num_range in numbers:
        nums = num_range.split('-')
        if not nums:
            raise ValueError
        all_invalid_sum += add_invalid_id_new(id1 = nums[0],id2 = nums[1])
    print(all_invalid_sum)