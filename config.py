from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def enDownloadHeadless(driver, download_dir):
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    driver.execute("send_command", params)

def config(downpath, headless=None, devtools=None, maximized=True, debug=False):
    opt = ChromeOptions()
    if not debug:
        opt.add_argument('log-level=3')
    else:
        opt.add_argument(f'log-level=0')
    opt.add_argument(f"download.default_directory={downpath}")
    prefs = {
        "download.default_directory": downpath,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    opt.add_experimental_option('prefs', prefs)
    if headless:
        opt.add_argument("--headless")
    if devtools:
        opt.add_argument("--auto-open-devtools-for-tabs")
    if maximized:
        opt.add_argument("--start-maximized")

    driver = Chrome(
        options = opt,
        service = Service(ChromeDriverManager().install())
    )

    if headless:
        enDownloadHeadless(driver, downpath)
    return driver