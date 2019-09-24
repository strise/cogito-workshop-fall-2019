import re
from typing import List

import nltk


class TimestampedText:
    def __init__(self, raw_text: str, published: int) -> None:
        self.raw_text: str = raw_text
        self.published: int = published

    def sentences(self) -> List[str]:
        return nltk.sent_tokenize(self.raw_text)

    def words(self) -> List[str]:
        return nltk.word_tokenize(self.raw_text)
