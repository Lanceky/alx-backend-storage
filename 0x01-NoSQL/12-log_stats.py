#!/usr/bin/env python3
"""
Module for providing stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """Provides stats about Nginx logs in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Get total logs
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    # Get methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Get status check
    status_check = logs_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()