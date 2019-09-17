def validate_field(parameter: str) -> bool:
    return len(parameter) == 2 and parameter[0] in "abcdefgh" and parameter[1] in "12345678"


def validate_piece(parameter: str) -> bool:
    return len(parameter) == 2 and parameter[0] in "wb" and parameter[1] in "pnbrqk"
