from typing import List

class Word:
    def __init__(
        self,
        word: str,
        language: str,
        definition: str,
        pos: str,
        category: str,
        preceding_words: List[str],
        following_words: List[str],
        synonyms: List[str],
        antonyms: List[str],
        comments: str
    ):
        self.word = word
        self.language = language
        self.definition = definition
        self.pos = pos
        self.category = category
        self.preceding_words = preceding_words
        self.following_words = following_words
        self.synonyms = synonyms
        self.antonyms = antonyms
        self.comments = comments

    def __repr__(self) -> str:
        return (
            f"Word(word={self.word!r}, language={self.language!r}, definition={self.definition!r}, "
            f"pos={self.pos!r}, category={self.category!r}, "
            f"preceding_words={self.preceding_words!r}, following_words={self.following_words!r}, "
            f"synonyms={self.synonyms!r}, antonyms={self.antonyms!r}, comments={self.comments!r})"
        )

    def __str__(self) -> str:
        return (
            f"Word: {self.word}\n"
            f"Language: {self.language}\n"
            f"Definition: {self.definition}\n"
            f"Position: {self.pos}\n"
            f"Category: {self.category}\n"
            f"Preceding words: {self.preceding_words}\n"
            f"Following words: {self.following_words}\n"
            f"Synonyms: {self.synonyms}\n"
            f"Antonyms: {self.antonyms}\n"
            f"Comments: {self.comments}"
        )