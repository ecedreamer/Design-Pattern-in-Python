from adapter import WebClientAdapter



def get_website_status(url, params):
    adapter = WebClientAdapter()
    status = adapter.send_get_request(url, params)
    print(status)


def main():
    print("Starting Program.....")
    url = "https://dipakniroula.com.np"
    params = {}
    get_website_status(url, params)


if __name__ == "__main__":
    main()