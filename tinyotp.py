"""
https://tools.ietf.org/rfc/rfc4226.txt  <= this is implemented
https://tools.ietf.org/rfc/rfc6238.txt  <= this is not (yet)
"""


from base64 import b32decode
from hashlib import sha1
from hmac import new
from time import time


def hotp(secret: str, count: int, length: int = 6) -> int:
    digest = new(b32decode(secret, casefold=True), count.to_bytes(8, 'big'), sha1).digest()
    offset = digest[-1] & 0b00001111  # use the low bits of last byte as offset
    return int.from_bytes(digest[offset:offset +4], 'big') % 10 ** length


def totp(secret: str, interval: int = 30, length: int = 6) -> int:
    return hotp(secret, int(time()) // interval, length)

