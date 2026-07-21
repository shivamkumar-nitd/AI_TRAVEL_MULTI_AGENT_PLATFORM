import os
import uuid
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def get_or_create_user(name: str):

    conn = psycopg.connect(DATABASE_URL)

    cur = conn.cursor()

    cur.execute(
        "SELECT user_id FROM users WHERE name = %s",
        (name,)
    )

    row = cur.fetchone()

    if row:
        conn.close()
        return row[0]

    user_id = uuid.uuid4().hex[:12]

    cur.execute(
        "INSERT INTO users(user_id,name) VALUES(%s,%s)",
        (user_id, name)
    )

    conn.commit()

    conn.close()

    return user_id