def sort_vouchers(input):
    vouchers = input.split(",")

    current_vouchers = [voucher for voucher in vouchers if is_current(voucher)]
    old_vouchers = [voucher for voucher in vouchers if is_old(voucher)]

    sorted_current_vouchers = sorted(current_vouchers, key=current_vouchers_sort_key)

    return ",".join(sorted_current_vouchers + old_vouchers)


def is_current(voucher):
    return "Available" in voucher or "Activated" in voucher


def is_old(voucher):
    return "Expired" in voucher or "Redeemed" in voucher

def current_vouchers_sort_key(voucher):
    return voucher.split(":")[0]