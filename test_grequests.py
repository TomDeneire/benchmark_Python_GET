from grequests import get
from grequests import map as gmap


def fetch(url: str) -> None:
    try:
        rs = (get(u) for u in [url])
        for resp in gmap(rs):
            assert len(resp.content) == 399609
    except Exception as err:
        exit(1)


if __name__ == "__main__":
    fetch("https://tomdeneire.be/static/homepage/img/profile.png")
