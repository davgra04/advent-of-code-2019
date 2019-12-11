from pprint import pprint, pformat

puzzle_input = "254032-789860"
[range_start, range_end] = [int(x) for x in puzzle_input.split("-")]

# brute force method

valid_passwords = []

for n in range(range_start, range_end):
    # print(n)

    n_str = str(n)

    # test double digits
    has_double = False
    for i in range(1, len(n_str)):
        # print(i)
        if n_str[i] == n_str[i-1]:
            has_double = True

    if not has_double:
        continue

    # test increasing digits
    has_inc_digits = True
    for i in range(1, len(n_str)):
        if int(n_str[i]) < int(n_str[i-1]):
            has_inc_digits = False
            break
    
    if not has_inc_digits:
        continue

    valid_passwords.append(n)


print("valid passwords:", valid_passwords)
print("# valid passwords:", len(valid_passwords))