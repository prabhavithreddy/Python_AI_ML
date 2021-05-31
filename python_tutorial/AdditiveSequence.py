def is_additive_sequence(number, start, end, length):
    s_n = str(number)
    if len(s_n)<3:
        return False
    first_num = int(s_n[start:end])
    second_num = int(s_n[end: end+length])
    sum = first_num + second_num
    sum_length = len(str(sum))
    next_num_str = s_n[end+length:end+length+sum_length]
    if not next_num_str:
        return True
    return sum == int(next_num_str) \
           and is_additive_sequence(number,end,end+length,sum_length)

print(is_additive_sequence(51123, 0 ,1, 1))

'''
6,6,121830

'''