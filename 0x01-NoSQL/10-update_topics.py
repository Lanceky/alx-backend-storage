#!/usr/bin/env python3
"""
Module for changing school topics
"""


def update_topics(mongo_collection, name, topics):
    """Change all topics of a school document based on the name
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
