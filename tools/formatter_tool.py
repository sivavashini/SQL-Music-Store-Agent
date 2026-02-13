def format_result(rows):
    if not rows:
        return "No results found."

    output = ""
    for row in rows:
        output += str(row) + "\n"

    return output
