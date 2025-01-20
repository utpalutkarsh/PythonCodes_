import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.nseindia.com/market-data/top-gainers-losers")
    page.get_by_test_id("royal_email").click()
    page.get_by_test_id("royal_email").fill("9065761726")
    page.get_by_test_id("royal_pass").click()
    page.get_by_test_id("royal_pass").fill("9934618843")
    page.get_by_test_id("royal_login_button").click()
    page.get_by_label("Shortcuts", exact=True).get_by_role("link", name="CAT Preparation - iQuanta").click()
    page.wait_for_load_state("networkidle")

    # Wait for the "Media" tab to become visible and clickable
    # Try waiting for a unique element associated with the "Media" tab
    page.get_by_label("Shortcuts", exact=True).get_by_role("link", name="Media").click()


    print("The browser will stay open for 10 minutes.")
    time.sleep(600)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
