"""
Solution for:
  https://projecteuler.net/problem=59
"""

import urllib
import string
from itertools import cycle, product


COMMON_ENGLISH_WORDS = ["the", "and", "to", "with"]
CHIPER_KEY_LENGTH = 3
CHIPER_POSSIBLE_VALUES = map(ord, list(string.ascii_lowercase))


def find_secret_key(encrypted_text):
  for key in product(CHIPER_POSSIBLE_VALUES, repeat=CHIPER_KEY_LENGTH):
    dectypt_text = get_decrypt_text(encrypted_text, key)
    if all(word in dectypt_text for word in COMMON_ENGLISH_WORDS):
      return key


def get_decrypt_text(text, chiper_key):
  ords = [i1 ^ i2 for i1, i2 in zip(text, cycle(chiper_key))]
  return "".join(map(chr, ords))


def get_encrypted_text():
  chiper_url = 'https://projecteuler.net/project/resources/p059_cipher.txt'
  return map(int, urllib.urlopen(chiper_url).read().strip().split(","))


def main():
  return find_secret_key(get_encrypted_text())

