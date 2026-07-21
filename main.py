from database.database import ProductDatabase
from models.product import Product


def main():
    database = ProductDatabase()

    product = Product(
        name="Portable Charger",
        price=24.99,
        currency="USD",
        image_url="https://example.com/charger.jpg",
        product_url="https://example.com/charger",
        source="test",
        rating=4.7,
        review_count=250,
        seller="Test Seller",
        category="Electronics",
    )

    product_id = database.save_product(product)

    print(f"\nProduct saved with database ID: {product_id}")

    products = database.get_all_products()

    print("\nSaved products:")

    for saved_product in products:
        print(
            f"{saved_product['id']}: "
            f"{saved_product['name']} - "
            f"{saved_product['currency']} "
            f"{saved_product['price']}"
        )


if __name__ == "__main__":
    main()