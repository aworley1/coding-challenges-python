def sortVouchers(input):
    split_input = input.split(",")

    sorted_input = sorted(split_input, key=sorting_key)

    return ",".join(sorted_input)


def sorting_key(voucher):
    return voucher.split(":")[2]
