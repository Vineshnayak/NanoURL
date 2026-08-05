BASE62_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
BASE = len(BASE62_ALPHABET)

def encode(num: int) -> str:
    """Encode an integer to a Base62 string."""
    if num == 0:
        return BASE62_ALPHABET[0]
    
    encoded = []
    while num > 0:
        num, rem = divmod(num, BASE)
        encoded.append(BASE62_ALPHABET[rem])
        
    return "".join(reversed(encoded))

def decode(short_code: str) -> int:
    """Decode a Base62 string back to an integer."""
    num = 0
    for char in short_code:
        num = num * BASE + BASE62_ALPHABET.index(char)
    return num
