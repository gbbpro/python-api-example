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
                              type:string
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


api.add_resource(AllReviews, "/all_reviews")


if __name__ == "__main__":
    app.run(debug=True)
