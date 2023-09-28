from playwright.sync_api import Playwright, sync_playwright
import openpyxl

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://itax.kra.go.ke")
    page.get_by_role("cell", name="To verify PIN, Click Here", exact=True).get_by_role("link").click()
    page.locator("input[name=\"vo\\.pinNo\"]").click()
    page.locator("input[name=\"vo\\.pinNo\"]").fill("P051411900H")
    page.get_by_role("textbox", name="Please enter the result of arithmetic expression in Security Stamp").click()
    page.get_by_role("textbox", name="Please enter the result of arithmetic expression in Security Stamp").fill("")
    page.get_by_role("button", name="Consult").click()

    # Wait for the "Taxpayer Details" section to load (you may need to adjust the selector)
    page.wait_for_selector("div[name=\"Taxpayer Details\"]")

    # Extract data from the "Taxpayer Details" section (modify selectors as needed)
    taxpayer_details = page.locator("div[name=\"Taxpayer Details\"]").text()

    # Create a new Excel workbook and worksheet
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # Write the scraped data to the Excel worksheet
    worksheet["A1"] = "Taxpayer Details"
    worksheet["A2"] = taxpayer_details

    # Save the Excel file
    workbook.save("taxpayer_details.xlsx")

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
