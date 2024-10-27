#!/usr/bin/env python3
"""
Module for listing all documents in MongoDB
"""


def list_all(mongo_collection):
    """List all documents in Python
    """
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)
    return documents
