from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://accounts.ecitizen.go.ke/en/login")
    page.get_by_placeholder("Enter your email or ID number").click()
    page.get_by_placeholder("Enter your email or ID number").fill("39794454")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("39794454")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("link", name="To my phone number +254******888").click()
    page.get_by_label("Enter OTP sent to +254******888").press("CapsLock")
    page.get_by_label("Enter OTP sent to +254******888").fill("PAA3FW")
    page.get_by_role("button", name="Next").click()
    page.goto("https://accounts.ecitizen.go.ke/en/")
    page.get_by_role("link", name="Log out").click()
    page.get_by_label("Global").get_by_role("link", name="Sign in").click()
    page.get_by_placeholder("Enter your email or ID number").click()
    page.get_by_placeholder("Enter your email or ID number").fill("from playwright.sync_api import Playwright, sync_playwright, expect   def run(playwright: Playwright) -> None:     browser = playwright.chromium.launch(headless=False)     context = browser.new_context()     page = context.new_page()     page.goto(\"https://accounts.ecitizen.go.ke/en/login\")     page.get_by_placeholder(\"Enter your email or ID number\").click()     page.get_by_placeholder(\"Enter your email or ID number\").fill(\"39794454\")     page.get_by_placeholder(\"Password\").click()     page.get_by_placeholder(\"Password\").fill(\"39794454\")     page.get_by_role(\"button\", name=\"Sign In\").click()     page.get_by_role(\"link\", name=\"To my phone number +254******888\").click()     page.get_by_label(\"Enter OTP sent to +254******888\").press(\"CapsLock\")     page.get_by_label(\"Enter OTP sent to +254******888\").fill(\"PAA3FW\")     page.get_by_role(\"button\", name=\"Next\").click()     page.goto(\"https://accounts.ecitizen.go.ke/en/\")     page.get_by_role(\"link\", name=\"Log out\").click()      # ---------------------     context.close()     browser.close()   with sync_playwright() as playwright:     run(playwright)")
    page.get_by_placeholder("Enter your email or ID number").press("Control+z")
    page.get_by_placeholder("Enter your email or ID number").fill("39794454")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("39794454")
    page.locator("#toggle_button_login_pwd").click()
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("3979445")
    page.get_by_role("button", name="Sign In").click()
    else: 
        page.get_by_text("Invalid username or password")
        
        status="Invalid"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
