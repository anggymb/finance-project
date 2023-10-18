"""Class for Stocks model."""

from dataclasses import dataclass

@dataclass
class Stock():
    name: str
    price: int
    code: str