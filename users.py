import os
import uuid
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def get_or_create_user(name: str):
    """
    Returns the existing user_id if the user already exists.
    Otherwise creates a new user and returns the generated user_id.
    """

    conn = psycopg.connect(DATABASE_URL)

    try:
        with conn.cursor() as cur:

            # Check if user already exists
            cur.execute(
                "SELECT user_id FROM users WHERE name = %s",
                (name,)
            )

            row = cur.fetchone()

            if row:
                return row[0]

            # Create new user
            user_id = uuid.uuid4().hex[:12]

            cur.execute(
                """
                INSERT INTO users(user_id, name)
                VALUES (%s, %s)
                """,
                (user_id, name)
            )

            conn.commit()

            return user_id

    finally:
        conn.close()