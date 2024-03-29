import csv
import io
from decimal import Decimal

from icon_rhizome_dev.constants import EXA
from icon_rhizome_dev.http_client import HttpClient


class Utils:
    """"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def format_asset_amount(
        amount: Decimal | int,
        decimal_places: int = 4,
    ) -> str:

        if isinstance(amount, int) is True:
            amount_str = f"{amount:,.0f}"
        else:
            amount_str = f"{amount:,.{decimal_places}f}".rstrip("0")
        return amount_str

    @staticmethod
    def format_asset_symbol(symbol: str) -> str:
        symbols = {
            "bnusd": "bnUSD",
            "btcb": "BTCB",
            "eth": "ETH",
            "sicx": "sICX",
        }
        return symbols[symbol]

    @staticmethod
    def generate_csv_file(
        header_row: list[str], body_rows: list[list[str]]
    ) -> io.StringIO:
        csv_buffer = io.StringIO()
        csv.writer(csv_buffer).writerow(header_row)
        csv.writer(csv_buffer).writerows(body_rows)
        return csv_buffer

    @staticmethod
    async def get_ipfs_content(ipfs_hash: str) -> dict | str:
        url = f"https://{ipfs_hash}.ipfs.cf-ipfs.com"
        r = await HttpClient.get(url)
        data = r.json()
        return data

    @staticmethod
    def get_validator_name_from_address(address: str) -> str:
        if address == "hx2e7db537ca3ff73336bee1bab4cf733a94ae769b":
            return "Eye on ICON"
        return "UNKNOWN"

    @staticmethod
    def int_to_string(
        value: int,
        decimals: int = 4,
        exa: int = EXA,
    ):
        value_decimal = Decimal(value) / Decimal(10**exa)
        value_str = f"{value_decimal:,.{decimals}f}"
        return value_str

    @staticmethod
    def hex_to_int(value: str):
        return int(value, 16)

    @staticmethod
    def int_to_hex(value: int):
        return hex(value)

    @staticmethod
    def fmt(value: float | int) -> str:
        if isinstance(value, int):
            return f"{value:,}"
        else:
            value_str = f"{value:,.4f}".rstrip("0")
            return value_str

    @staticmethod
    def format_number(value: float | int, decimal_places: int = 4) -> str:
        if float(value) == int(value):
            value = int(value)
        if decimal_places == 0:
            value = int(value)
        if isinstance(value, int):
            return f"{value:,}"
        else:
            value_str = f"{value:,.{decimal_places}f}".rstrip("0")
            return value_str

    @staticmethod
    def format_percentage(value: float) -> str:
        if int(value) == float(value):
            return f"{int(value)}%"
        return f"{value:.2%}"
