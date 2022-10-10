from dataclasses import dataclass

@dataclass
class Wallet:
    public_key: str
    private_key: str
    name: str