from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger

import book

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)
br = book.BookReview()


class AllReviews(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns a list of book reviews.
        ---
        tags:
        - Book Reviews
        parameters:
            - name: sort
              in: query
              type: string
              required: false
              enum: ['ASC','DESC']
              description: The parameter to sort the reviews by (e.g., 'rating', 'book')
            - name: max_records
              in: query
              type: integer
              required: false
              description: The maximum number of records to return
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: array
                        items:
                          type: object
                          properties:
                            Books:
                              type: string
                            ISBN:
                              type: string
                            Rating:
                              type: number
                            Notes:
                              type: string
        """
        sort = request.args.get("sort", default=None)
        max_records = request.args.get("max_records", default=10, type=int)

        if sort == "ASC":
            book_reviews = br.get_book_ratings(sort=sort, max_records=max_records)
        elif sort == "DESC":
            book_reviews = br.get_book_ratings(sort=sort, max_records=max_records)
        else:
            book_reviews = br.get_book_ratings(max_records=max_records)
        return book_reviews, 200


class PostReview(Resource):
    def post(self):
        """
        This method responds to the POST request for this endpoint and adds a new book review.
        ---
        tags:
        - Book Reviews
        consumes:
        - application/json
        parameters:
            - in: body
              name: body
              description: Book review data
              required: true
              schema:
                id: BookReview
                required:
                - Book
                - Rating
                - ISBN
                properties:
                    Book:
                        type: string
                        description: The name of the book
                    Rating:
                        type: number
                        description: The review text
                    ISBN:
                        type: string
                        description: Book Serial Number
                    Notes:
                        type: string
                        description: Additional notes (optional)
        responses:
            201:
                description: Review added successfully
        """
        data = request.get_json()
        book = data.get("Book")
        rating = data.get("Rating")
        notes = data.get("Notes", None)

        # Here you would add logic to insert the review data into your database
        br.add_book_rating(book, rating, notes)

        return {"message": "Review added successfully"}, 201


api.add_resource(PostReview, "/post_review")
api.add_resource(AllReviews, "/all_reviews")


if __name__ == "__main__":
    app.run(debug=True)
