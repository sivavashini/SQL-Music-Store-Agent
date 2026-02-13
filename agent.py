import os
import google.generativeai as genai

from tools.schema_tool import get_schema
from tools.sql_tool import execute_query
from tools.validation_tool import validate_query
from tools.formatter_tool import format_result

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro-latest")


class SQLAgent:

    def generate_sql(self, question):
        schema = get_schema()

        prompt = f"""
You are a SQL expert.
Only return SQL query.

Database Schema:
{schema}

User Question:
{question}
"""

        response = model.generate_content(prompt)

        return response.text.strip()

    def run(self, question):
        sql_query = self.generate_sql(question)

        if not validate_query(sql_query):
            return "Invalid query generated."

        rows = execute_query(sql_query)

        return format_result(rows)
