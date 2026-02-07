import time

from playwright.sync_api import expect

from Pages.cartPage import CartPage
from Pages.inventoryPage import InventoryPage
from Pages.loginPage import LoginPage
from Pages.checkoutPage import CheckoutPage
from Pages.finalPage import FinalPage
from Pages.thankYouPage import ThankYouPage


def test_add_item_to_cart(page):

    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    final = FinalPage(page)
    thankYou = ThankYouPage(page)
    login.login("standard_user", "secret_sauce")  # Login
    inventory.add_item_to_cart()  # Add item
    assert inventory.get_cart_count() == "1"   # Verify cart badge count
    cart.open_cart()  # Open cart
    assert cart.get_cart_items_count() == 1 # Verify item count in cart
    cart.go_to_checkout()   #checkout
    checkout.fill_options()  #continue
    checkout.continue_to_Payment()
    final.click_final_button()  #final/finish
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
    thankYou.back_to_home()  #Back to home Page