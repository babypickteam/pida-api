from .bootpay.lib.BootpayApi import BootpayApi

def validate_receipt(receipt_id, price):
    bootpay = BootpayApi(
        '[[ application_id ]]',
        '[[ private_key ]]'
    )
    result = bootpay.get_access_token()

    if result['status'] == 200:
        verify_result = bootpay.verify(receipt_id)
        if verify_result['status'] == 200:
            return (verify_result['data']['status'] == 1) and (verify_result['data']['price'] == price)

    return False
