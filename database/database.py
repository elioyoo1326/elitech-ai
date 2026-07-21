import sqlite3
from pathlib import Path

from models.product import Product


class ProductDatabase:
    def __init__(self, database_path: str = "data/products.db"):
        self.database_path = database_path

        Path(database_path).parent.mkdir(parents=True, exist_ok=True)
        self.create_products_table()

    def connect(self):
        return sqlite3.connect(self.database_path)

    def create_products_table(self):
        with self.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id TEXT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    currency TEXT NOT NULL,
                    image_url TEXT NOT NULL,
                    product_url TEXT NOT NULL,
                    source TEXT NOT NULL,
                    rating REAL,
                    review_count INTEGER,
                    seller TEXT,
                    category TEXT,
                    discovered_at TEXT NOT NULL
                )
                """
            )

    def save_product(self, product: Product):
        with self.connect() as connection:
            cursor = connection.execute(
                """
                INSERT INTO products (
                    product_id,
                    name,
                    price,
                    currency,
                    image_url,
                    product_url,
                    source,
                    rating,
                    review_count,
                    seller,
                    category,
                    discovered_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    product.product_id,
                    product.name,
                    product.price,
                    product.currency,
                    product.image_url,
                    product.product_url,
                    product.source,
                    product.rating,
                    product.review_count,
                    product.seller,
                    product.category,
                    product.discovered_at.isoformat(),
                ),
            )

            return cursor.lastrowid

    def get_all_products(self):
        with self.connect() as connection:
            connection.row_factory = sqlite3.Row
            rows = connection.execute(
                """
                SELECT *
                FROM products
                ORDER BY id DESC
                """
            ).fetchall()

            return [dict(row) for row in rows]