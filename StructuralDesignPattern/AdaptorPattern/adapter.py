from NewWebClientInterface import WebClientInterface

class WebClientAdapter(WebClientInterface):
    def __init__(self, web_client) -> None:
        self.web_client = web_client

    def send_get_request(self, url: str, params: dict):
        return self.web_client.get(url, params)

    def send_post_request(self, url: str, payload: dict):
        return self.web_client.post(url, payload)
