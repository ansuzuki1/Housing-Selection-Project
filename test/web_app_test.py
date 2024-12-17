
'''
from app.models.product import Product

# tests for each page (update the tests if you change the page contents):


def test_home_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"<h1>Home</h1>" in response.data


def test_about_page(test_client):
    response = test_client.get("/about")
    assert response.status_code == 200
    assert b"<h1>About</h1>" in response.data


def test_products_page(test_client):
    # setup (seed database with some products):
    Product.destroy_all()
    Product.seed()

    products = Product.all()
    assert len(products) == 3

    # given certain products in the database,
    # we expect to see corresponding information on the page:
    response = test_client.get("/products")
    assert response.status_code == 200
    assert b"<h1>Products</h1>" in response.data
    assert b"Textbook" in response.data
    assert b"Cup of Tea" in response.data
    assert b"Strawberries" in response.data

    # clean up (clear products sheet):
    Product.destroy_all()
'''