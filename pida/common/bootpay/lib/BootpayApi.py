import requests


class BootpayApi:
    base_url = {
        'development': 'https://dev-api.bootpay.co.kr',
        'production': 'https://api.bootpay.co.kr'
    }

    def __init__(self, application_id, private_key, mode='production'):
        self.application_id = application_id
        self.pk = private_key
        self.mode = mode
        self.token = None

    def api_url(self, uri=None):
        if uri is None:
            uri = []
        return '/'.join([self.base_url[self.mode]] + uri)

    def get_access_token(self):
        data = {
            'application_id': self.application_id,
            'private_key': self.pk
        }
        response = requests.post(self.api_url(['request', 'token']), data=data)
        result = response.json()
        if result['status'] is 200:
            self.token = result['data']['token']
        return result

    def cancel(self, receipt_id, price=None, name=None, reason=None):
        payload = {'receipt_id': receipt_id,
                   'price': price,
                   'name': name,
                   'reason': reason}

        return requests.post(self.api_url(['cancel.json']), data=payload, headers={
            'Authorization': self.token
        }).json()

    def verify(self, receipt_id):
        return requests.get(self.api_url(['receipt', receipt_id]), headers={
            'Authorization': self.token
        }).json()

    def subscribe_billing(self, billing_key, item_name, price, order_id, items=None):
        if items is None:
            items = {}
        payload = {
            'billing_key': billing_key,
            'item_name': item_name,
            'price': price,
            'order_id': order_id,
            'items': items
        }
        return requests.post(self.api_url(['subscribe', 'billing.json']), data=payload, headers={
            'Authorization': self.token
        }).json()

    def subscribe_billing_reserve(self, billing_key, item_name, price, order_id, execute_at, feedback_url, items=None):
        if items is None:
            items = []
        payload = {
            'billing_key': billing_key,
            'item_name': item_name,
            'price': price,
            'order_id': order_id,
            'items': items,
            'scheduler_type': 'oneshot',
            'execute_at': execute_at,
            'feedback_url': feedback_url
        }
        return requests.post(self.api_url(['subscribe', 'billing', 'reserve.json']), data=payload, headers={
            'Authorization': self.token
        }).json()

    def get_subscribe_billing_key(self, pg, order_id, item_name, card_no, card_pw, expire_year, expire_month,
                                  identify_number, user_info=None):
        if user_info is None:
            user_info = {}
        payload = {
            'order_id': order_id,
            'pg': pg,
            'item_name': item_name,
            'card_no': card_no,
            'card_pw': card_pw,
            'expire_year': expire_year,
            'expire_month': expire_month,
            'identify_number': identify_number,
            'user_info': user_info
        }
        return requests.post(self.api_url(['request', 'card_rebill.json']), data=payload, headers={
            'Authorization': self.token
        }).json()

    def destroy_subscribe_billing_key(self, billing_key):
        return requests.delete(self.api_url(['subscribe', 'billing', billing_key]), headers={
            'Authorization': self.token
        }).json()
