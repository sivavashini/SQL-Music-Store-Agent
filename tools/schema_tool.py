def get_schema():
    return """
Table: artists
- id
- name
- genre

Table: albums
- id
- title
- artist_id
"""
