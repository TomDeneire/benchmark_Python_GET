from urllib.request import urlopen


def fetch(url: str) -> None:
    try:
        with urlopen(url) as urlreader:
            response = urlreader.read()
    except Exception as err:
        exit(1)
    assert len(response) == 399609


if __name__ == "__main__":
    fetch("https://tomdeneire.be/static/homepage/img/profile.png")
