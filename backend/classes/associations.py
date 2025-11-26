import csv
from .word import Word
from typing import List
from .helpers import * 

class Associations:
    def __init__(self, csv_file: str):
        self.file = csv_file
        self.associations = self.read_word_data_from_csv()

    def add_word(self, word: Word):
        """Add a Word object to the associations list and write it to CSV."""
        if any(w.word.lower() == word.word.lower() for w in self.associations):
            raise ValueError(f"Word '{word.word}' already exists.")
        
        self.associations.append(word)
        self.write_word_to_csv(word)

    def read_word_data_from_csv(self) -> List[Word]:
        """Read CSV and convert each row to a Word object."""
        words: List[Word] = []
        with open(self.file, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                words.append(
                    Word(
                        word=row["Word"],
                        language=row.get("Language", ""),
                        definition=row.get("Definition", ""),
                        pos=row.get("Part of Speech", ""),
                        category=row.get("Category", ""),
                        preceding_words=process_word_list(row.get("Preceding Words", "")),
                        following_words=process_word_list(row.get("Following Words", "")),
                        synonyms=process_word_list(row.get("Synonyms", "")),
                        antonyms=process_word_list(row.get("Antonyms", "")),
                        comments=row.get("Comments", ""),
                    )
                )
        return words

 

    def write_word_to_csv(self, word: Word):
        """Append a new Word object to the CSV file."""
        with open(self.file, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                word.word,
                word.language,
                word.definition,
                word.pos,
                word.category,
                ",".join(word.preceding_words),
                ",".join(word.following_words),
                ",".join(word.synonyms),
                ",".join(word.antonyms),
                word.comments
            ])

    def show_associations(self):
        """Print all Word objects."""
        for word in self.associations:
            print(word)

    def get_word(self, search_word: str) -> Word | None:
        """Return a Word object by its word string, or None if not found."""
        for word in self.associations:
            if word.word.lower() == search_word.lower():
                return word
        return None