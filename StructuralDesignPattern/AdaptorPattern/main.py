from adapter import WebClientAdapter
from LegacyWebClient import WebClient


def get_website_status(url, params):
    old_web_client = WebClient()
    adapter = WebClientAdapter(old_web_client)
    status = adapter.send_get_request(url, params)
    print(status)


def main():
    print("Starting Program.....")
    url = "https://dipakniroula.com.np"
    params = {}
    get_website_status(url, params)


if __name__ == "__main__":
    main()