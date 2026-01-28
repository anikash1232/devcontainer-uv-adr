"""Tests for src/main.py."""

import sys
from unittest.mock import MagicMock, patch

import pytest

from src.main import DEFAULT_LOCATION, main


class TestMain:
    """Test suite for the main module."""

    def test_main_no_args(self) -> None:
        """Test main() uses DEFAULT_LOCATION when no arguments provided."""
        with patch("src.main.sys.argv", ["main.py"]):
            with patch("src.main.requests.get") as mock_get:
                mock_response = MagicMock()
                mock_response.text = "Chapel Hill, NC\nPartly cloudy\n+72°F"
                mock_get.return_value = mock_response

                main()

                # Verify that the default location was used in the URL
                call_args = mock_get.call_args
                assert DEFAULT_LOCATION in call_args[0][0]
                mock_response.raise_for_status.assert_called_once()

    def test_main_with_custom_location(self) -> None:
        """Test main() uses custom location from command line args."""
        test_location = "New York, NY"
        with patch("src.main.sys.argv", ["main.py", "New", "York,", "NY"]):
            with patch("src.main.requests.get") as mock_get:
                mock_response = MagicMock()
                mock_response.text = "New York, NY\nCloudy\n+65°F"
                mock_get.return_value = mock_response

                main()

                # Verify that the custom location was used in the URL
                call_args = mock_get.call_args
                assert test_location in call_args[0][0]
                mock_response.raise_for_status.assert_called_once()

    def test_main_network_error(self) -> None:
        """Test main() handles network errors gracefully."""
        with patch("src.main.sys.argv", ["main.py"]):
            with patch("src.main.requests.get") as mock_get:
                mock_get.side_effect = Exception("Network error")

                with pytest.raises(Exception):
                    main()

    def test_default_location_is_string(self) -> None:
        """Test DEFAULT_LOCATION is properly configured."""
        assert isinstance(DEFAULT_LOCATION, str)
        assert len(DEFAULT_LOCATION) > 0
