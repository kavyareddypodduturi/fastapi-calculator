from playwright.sync_api import sync_playwright
import time


def test_register_and_login():
    unique_id = str(int(time.time()))
    email = f"playtest{unique_id}@gmail.com"
    username = f"playuser{unique_id}"
    password = "password123"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Open register page
        page.goto("file://" + __import__("os").getcwd() + "/register.html")

        # Fill register form
        page.fill("#email", email)
        page.fill("#username", username)
        page.fill("#password", password)
        page.fill("#confirmPassword", password)

        page.click("button")

        page.wait_for_timeout(1000)
        assert "Registration successful!" in page.inner_text("#message")

        # Open login page
        page.goto("file://" + __import__("os").getcwd() + "/login.html")

        # Fill login form
        page.fill("#username", username)
        page.fill("#password", password)

        page.click("button")

        page.wait_for_timeout(1000)
        assert "Login successful!" in page.inner_text("#message")

        browser.close()