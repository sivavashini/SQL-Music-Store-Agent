def validate_query(query):
    forbidden = ["DROP", "DELETE", "UPDATE"]

    for word in forbidden:
        if word in query.upper():
            return False

    return True
