import pytest
from playwright.sync_api import sync_playwright

def test_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("http://127.0.0.1:8000")

        content = page.content()
        assert "Calculator API is running" in content

        browser.close()