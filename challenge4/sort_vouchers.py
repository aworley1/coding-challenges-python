def sortVouchers(input):
    vouchers = input.split(",")

    current_vouchers = [voucher for voucher in vouchers if is_current(voucher)]
    old_vouchers = [voucher for voucher in vouchers if is_old(voucher)]

    sorted_current_vouchers = sorted(current_vouchers)
    sorted_old_vouchers = sorted(old_vouchers, key=old_voucher_sort_key)

    return ",".join(sorted_current_vouchers + sorted_old_vouchers)


def is_current(voucher):
    return "Available" in voucher or "Activated" in voucher


def is_old(voucher):
    return "Expired" in voucher or "Redeemed" in voucher


def old_voucher_sort_key(voucher):
    split_voucher = voucher.split(":")
    negative_date = -int(split_voucher[0])

    return (negative_date, convert_status_to_sort_key(split_voucher[1]), split_voucher[2])


def convert_status_to_sort_key(status):
    if status == "Redeemed":
        return "a"
    else:
        return "b"
