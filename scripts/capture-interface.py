from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:7860"
OUT = Path("artifacts/interface")
OUT.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    desktop = browser.new_page(viewport={"width": 1440, "height": 1100}, device_scale_factor=1)
    response = desktop.goto(BASE_URL, wait_until="networkidle", timeout=90000)
    assert response and response.status == 200, "Gradio did not return HTTP 200"
    desktop.get_by_text("AURORA GEOINTELLIGENCE COMMAND CENTER", exact=False).first.wait_for(timeout=30000)
    assert desktop.get_by_role("button", name="Executar análise").count() == 1
    assert desktop.get_by_text("Transparência científica", exact=False).count() >= 1
    desktop.screenshot(path=str(OUT / "aurora-geointelligence-desktop.png"), full_page=True)

    mobile = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
    mobile.goto(BASE_URL, wait_until="networkidle", timeout=90000)
    mobile.get_by_role("button", name="Executar análise").wait_for(timeout=30000)
    mobile.screenshot(path=str(OUT / "aurora-geointelligence-mobile.png"), full_page=True)

    print("PASS: live Gradio UI loaded, key controls were found, desktop/mobile screenshots saved.")
    browser.close()
