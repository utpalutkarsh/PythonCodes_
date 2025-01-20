

import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.nseindia.com/market-data/top-gainers-losers")
    # page.wait_for_load_state("networkidle")
    # page.get_by_label("Shortcuts", exact=True).get_by_role("link", name="Download").click()
    #
    #
    # print("The browser will stay open for 10 minutes.")
    time.sleep(600)
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
        run(playwright)
print