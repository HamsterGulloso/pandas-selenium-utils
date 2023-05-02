from selenium.webdriver import Chrome

def enDownloadHeadless(
        driver: Chrome,
        download_dir: str
    ):
    ...

def config(
        downpath: str,
        headless: bool = None,
        devtools: bool = None,
        maximized: bool = True,
        debug: bool = False
    ) -> Chrome:
    ...