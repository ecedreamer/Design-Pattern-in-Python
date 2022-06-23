from NewWebClientInterface import WebClientInterface
from LegacyWebClient import WebClient

class WebClientAdapter(WebClientInterface):
    def __init__(self) -> None:
        self.web_client = WebClient()

    def send_get_request(self, url: str, params: dict):
        return self.web_client.get(url, params)

    def send_post_request(self, url: str, payload: dict):
        return self.web_client.post(url, payload)
