from pages.product_page import ProductPage

def test_to_add_to_cart_botton(driver):
    link = 'http://selenium1py.pythonanywhere.com/fr/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(driver, link)
    page.open()
    page.should_be_add_to_card()
