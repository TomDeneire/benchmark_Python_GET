from urllib3 import PoolManager


def fetch(url: str) -> None:
    http = PoolManager()
    try:
        response = http.request("GET", url).data
    except Exception as err:
        exit(1)
    assert len(response) == 399609


if __name__ == "__main__":
    fetch("https://tomdeneire.be/static/homepage/img/profile.png")
