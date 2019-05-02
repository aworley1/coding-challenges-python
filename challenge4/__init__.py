def sort_vouchers(input):
    vouchers = input.split(",")

    current_vouchers = [voucher for voucher in vouchers if is_current(voucher)]
    old_vouchers = [voucher for voucher in vouchers if is_old(voucher)]

    return ",".join(current_vouchers + old_vouchers)


def is_current(voucher):
    return "Available" in voucher or "Activated" in voucher


def is_old(voucher):
    return "Expired" in voucher or "Redeemed" in voucher
