from requests import get


def fetch(url: str) -> None:
    try:
        response = get(url).content
    except Exception as err:
        exit(1)
    assert len(response) == 399609


if __name__ == "__main__":
    fetch("https://tomdeneire.be/static/homepage/img/profile.png")
