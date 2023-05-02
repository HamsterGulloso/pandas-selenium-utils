from selenium.webdriver.common.by import By
from selenium.webdriver import Remote as WebDriver
from selenium.webdriver.remote.webelement import WebElement

class Elem:
    def __init__(
            self: Elem,
            by: By,
            elem: str,
            val: str = None,
            driver: WebDriver = None,
            debug: bool = False
        ):
        ...

    def find(self: Elem, driver: WebDriver = None) -> WebElement:
        ...

    def canfind(self: Elem, driver: WebDriver = None) -> bool:
        ...

    def click(self: Elem, driver: WebDriver = None) -> bool:
        ...
    
    def hasvalue(self: Elem, driver: WebDriver = None) -> bool:
        ...

class Script:
    def __init__(self, text: str, driver: WebDriver = None):
        ...
    
    def execuntiltrue(self, driver: WebDriver = None) -> dict:
        ...

class Confere:
    def __init__(self, driver: WebDriver):
        ...

    def done(self):
        ...

    async def start(self):
        ...