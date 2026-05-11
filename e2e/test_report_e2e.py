from playwright.sync_api import sync_playwright


def test_calculation_statistics_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("http://127.0.0.1:5500/calculations.html")

        page.click("text=Load Statistics")

        assert "Total Calculations" in page.content()
        assert "Total Add Operations" in page.content()
        assert "Total Subtract Operations" in page.content()
        assert "Highest Result" in page.content()
        assert "Average Result" in page.content()

        browser.close()