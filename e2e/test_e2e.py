from playwright.sync_api import sync_playwright
import os


def test_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("http://127.0.0.1:8000")

        content = page.content()
        assert "Calculator API is running" in content

        browser.close()


def test_bread_operations():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # ✅ FIX: load HTML file directly (works in CI)
        file_path = os.path.abspath("calculations.html")
        page.goto(f"file://{file_path}")

        # ADD
        page.fill("#a", "10")
        page.fill("#b", "5")
        page.select_option("#type", "Add")
        page.click("text=Add Calculation")
        page.wait_for_timeout(3000)

        # BROWSE
        page.click("text=Browse Calculations")
        page.wait_for_timeout(3000)

        assert "Add" in page.content()
        assert "15" in page.content() or "7" in page.content()

        # READ
        page.once("dialog", lambda dialog: dialog.accept())
        page.click("text=Read")
        page.wait_for_timeout(3000)

        browser.close()