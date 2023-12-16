import os
from pyairtable import Api
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get("API_TOKEN")

BASE_ID = os.environ.get("BASE_ID")
TABLE_ID = os.environ.get("TABLE_ID")
api = Api(API_TOKEN)
table = api.table(BASE_ID, TABLE_ID)


class BookReview:
    def __init__(self):
        self.api = Api(API_TOKEN)
        self.table = self.api.table(BASE_ID, TABLE_ID)

    def get_book_ratings(self, sort=None, max_records=10):
        if not sort:
            return self.table.all(max_records=max_records)
        elif sort == "ASC":
            rating = ["Rating"]
        elif sort == "DESC":
            rating = ["-Rating"]
        table = self.table.all(sort=rating)[:max_records]
        return table

    def add_book_rating(self, book_title, rating, isbn, notes=None):
        fields = {"ISBN": isbn, "Books": book_title, "Rating": rating, "Notes": notes}
        self.table.create(fields=fields)

def update_book_rating(self, isbn, new_rating, new_notes=None):
    # Fetch records filtered by ISBN
    records = self.table.all(formula=f"{{ISBN}} = '{isbn}'")

    if not records:
        return None  # No record found with the given ISBN

    record_id = records[0]['id']
    updated_fields = {"Rating": new_rating}

    if new_notes is not necessarily None:
        updated_fields["Notes"] = new_notes

    self.table.update(record_id, fields=updated_fields)

if __name__ == "__main__":
    br = BookReview()
