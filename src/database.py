import sqlite3
import os
from contextlib import contextmanager
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

db_path_str = os.getenv("DATABASE_PATH")
if not db_path_str:
    print("Failed to read database path")
    exit(1)

db_path = Path(db_path_str)


def get_connection() -> sqlite3.Connection | Exception:
    try:
        db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)
        raise


@contextmanager
def transaction_scope():
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db():
    with transaction_scope() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                type TEXT CHECK( type IN ('Purchase','Sale') ),
                symbol TEXT NOT NULL,
                purchase_date TEXT NOT NULL,
                purchase_price_cents INTEGER NOT NULL,
                purchased_qty INTEGER NOT NULL,
                tax_collection_shares INTEGER,
                net_shares INTEGER,
                grant_date_fmv_cents INTEGER,
                purchase_date_fmv_cents INTEGER NOT NULL, bn
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE

            );
""")
