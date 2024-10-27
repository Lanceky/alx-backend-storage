#!/usr/bin/env python3
"""
Module for returning all students sorted by average score
"""


def top_students(mongo_collection):
    """Returns all students sorted by average score
    """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
