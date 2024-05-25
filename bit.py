nums = [1]
d = {num: list(int(a) for a in "{:032b}".format(num)) for num in nums}
