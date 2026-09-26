import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def search_zee5(serial_name):

    query = f'site:zee5.com/tv-shows/details/ "{serial_name}" "Kannada"'

    url = "https://www.google.com/search"

    params = {
        "q": query
    }

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/140.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=20
        )

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        results = []

        # Google search result links
        for link in soup.find_all("a"):

            href = link.get("href", "")

            text = link.get_text(
                " ",
                strip=True
            )

            if (
                "zee5.com/tv-shows/details/" in href
                and text
            ):

                results.append({
                    "title": text,
                    "url": href
                })

        # Remove duplicates
        unique_results = []

        seen = set()

        for result in results:

            if result["url"] not in seen:

                seen.add(result["url"])
                unique_results.append(result)

        if unique_results:

            return unique_results[:5]

        return None

    except Exception:

        return None
