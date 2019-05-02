def sortVouchers(input):
    split_input = input.split(",")

    sorted_input = sorted(split_input, key=lambda x: x.split(":")[2])

    return ",".join(sorted_input)
