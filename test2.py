from playwright.sync_api import Playwright, sync_playwright, expect


def test_water(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(4)").screenshot(path='output/task2_2.png')
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_water(playwright)