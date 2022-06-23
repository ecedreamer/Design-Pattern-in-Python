import requests


class WebClient:
    def get(self, url, params):
        resp = requests.get(url, params=params)
        return resp.status_code

    def post(self, url, payload):
        resp = requests.post(url, data=payload)
        return resp.status_code
