import time

import pytest
from playwright.sync_api import Page, expect


#Login with valid username & Password
def test_positiveLogin(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    time.sleep(2)

def test_negativeLogin(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    #asserting/comparing the error
    expect(page.get_by_text("Epic sadface: Sorry, this user has been locked out.")).to_be_visible()

def test_invalidLogin(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sa")
    page.get_by_role("button", name="Login").click()
    #asserting/comparing the error
    expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()

def test_emptyLogin(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("")
    page.get_by_placeholder("Password").fill("")
    page.get_by_role("button", name="Login").click()
    #asserting/comparing the error
    expect(page.get_by_text("Epic sadface: Username is required")).to_be_visible()

def test_logoutFunction(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()
    #page.locator("#logout_sidebar_link").click() -- It is through ID.
    expect(page.get_by_text("Accepted usernames are:")).to_be_visible()

def test_itemCount(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    product_box = page.locator(".inventory_item")
    expect(product_box).to_have_count(6)

def test_specificProductDetails(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    product_name = "Sauce Labs Bike Light"
    product_row = page.locator(".inventory_item").filter(has_text=product_name)
    product_row.locator(".inventory_item_name ").click()
    expect(page.get_by_text("Sauce Labs Bike Light")).to_be_visible()
    expect(page.get_by_text("$9.99")).to_be_visible()

def test_productSorter(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    #page.locator(".product_sort_container").click()
    page.select_option(".product_sort_container", label="Price (low to high)")


def test_addItem(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    time.sleep(2)
    product_name= "Sauce Labs Bike Light"
    product_row = page.locator(".inventory_item").filter(has_text=product_name)
    product_row.get_by_role("button", name="Add to cart").click()
    print(f"Clicked 'Add to cart' for: {product_name}")
    #verification
    expect(product_row.get_by_role("button")).to_have_text("Remove")

def test_removeItem(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    time.sleep(2)
    product_name= "Sauce Labs Bike Light"
    product_row = page.locator(".inventory_item").filter(has_text=product_name)
    product_row.get_by_role("button", name="Add to cart").click()
    product_row.get_by_role("button", name="Remove").click()
    #verification
    expect(product_row.get_by_role("button")).to_have_text("Add to cart")

def test_checkout(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    product_name = "Sauce Labs Bike Light"
    product_row = page.locator(".inventory_item").filter(has_text=product_name)
    product_row.get_by_role("button", name="Add to cart").click()
    page.locator(".shopping_cart_link").click()
    expect(page.get_by_text("Sauce Labs Bike Light")).to_be_visible()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_placeholder("First Name").fill("Rohan")
    page.get_by_placeholder("Last Name").fill("Mishra")
    page.get_by_placeholder("Zip/Postal Code").fill("700056")
    page.locator("[data-test='continue']").click()
    page.get_by_role("button", name="Finish").click()
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
    page.get_by_role("button", name="Back Home").click()

def test_invalidCheckout(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    product_name = "Sauce Labs Bike Light"
    product_row = page.locator(".inventory_item").filter(has_text=product_name)
    product_row.get_by_role("button", name="Add to cart").click()
    page.locator(".shopping_cart_link").click()
    expect(page.get_by_text("Sauce Labs Bike Light")).to_be_visible()
    page.get_by_role("button", name="Checkout").click()
    #page.get_by_placeholder("First Name").fill("Rohan")
    #page.get_by_placeholder("Last Name").fill("Mishra")
    #page.get_by_placeholder("Zip/Postal Code").fill("700056")
    page.locator("[data-test='continue']").click()
    # page.get_by_role("button", name="Finish").click()
    # expect(page.get_by_text("Thank you for your order!")).to_be_visible()
    # time.sleep(2)
    # page.get_by_role("button", name="Back Home").click()
    expect(page.get_by_text("Error: First Name is required")).to_be_visible()

