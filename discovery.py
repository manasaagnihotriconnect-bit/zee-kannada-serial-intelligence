import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def search_zee5(serial_name):
    """
    Searches the web for the requested Zee Kannada serial
    and attempts to identify the latest available episode.
    """

    query = f"site:zee5.com {serial_name} Zee Kannada latest episode"

    url = "https://www.google.com/search?q=" + quote(query)

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        results = []

        for result in soup.select("div.MjjYud"):
            link = result.select_one("a")
            title = result.select_one("h3")

            if link and title:
                results.append({
                    "title": title.get_text(" ", strip=True),
                    "url": link.get("href")
                })

        if results:
            return results[:5]

        return None

    except Exception as e:
        return None
