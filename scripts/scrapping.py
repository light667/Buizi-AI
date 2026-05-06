from playwright.sync_api import sync_playwright

url = "https://swipefile.com/category/business-ideas"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)

    page.wait_for_timeout(60000)  # laisser charger JS

    links = page.eval_on_selector_all(
        "a",
        "elements => elements.map(e => e.href)"
    )

    # filtrage
    article_links = [
        link for link in links
        if "swipefile.com" in link and "/category/" not in link
    ]

    print(len(article_links), "articles trouvés")

    browser.close()