from playwright.sync_api import sync_playwright


def test_register_and_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Open register page
        page.goto("file://" + __import__("os").getcwd() + "/register.html")

        # Fill register form
        page.fill("#email", "playtest@gmail.com")
        page.fill("#username", "playuser")
        page.fill("#password", "password123")
        page.fill("#confirmPassword", "password123")

        page.click("button")

        # Wait for success message
        page.wait_for_timeout(1000)
        assert "Registration successful!" in page.inner_text("#message")

        # Open login page
        page.goto("file://" + __import__("os").getcwd() + "/login.html")

        # Fill login form
        page.fill("#username", "playuser")
        page.fill("#password", "password123")

        page.click("button")

        page.wait_for_timeout(1000)
        assert "Login successful!" in page.inner_text("#message")

        browser.close()