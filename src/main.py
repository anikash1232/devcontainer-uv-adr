"""Synercast.ai weather script.

This module provides a simple command-line tool to fetch and display weather
information for a specified location using the wttr.in service.
"""

import sys

import requests

# Configuration constants
DEFAULT_LOCATION = "Chapel Hill, NC"
WEATHER_FORMAT = "3"  # Short format
UNITS = "u"  # US units (Fahrenheit, mph, etc.)


def main() -> None:
    """Fetches and prints the weather for a given location in Fahrenheit.

    If no location is provided via command line arguments, defaults to Chapel Hill, NC.
    The weather information is retrieved from wttr.in and printed to stdout in Fahrenheit.

    Args:
        None

    Returns:
        None

    Raises:
        requests.exceptions.RequestException: If the HTTP request to wttr.in fails.
    """
    location: str = " ".join(sys.argv[1:]) or DEFAULT_LOCATION
    url: str = f"https://wttr.in/{location}?format={WEATHER_FORMAT}&{UNITS}"
    r: requests.Response = requests.get(url, timeout=10)
    r.raise_for_status()
    print(r.text.strip())


if __name__ == "__main__":
    main()
