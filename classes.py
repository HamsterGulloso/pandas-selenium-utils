from time import sleep

class Elem:
    def __init__(self, by, elem, val=None, driver=None, debug=False):
        self.by = by
        self.elem = elem
        self.debug = debug
        if val:
            self.val = val
        if driver:
            self.driver = driver

    def find(self, driver=None):
        if driver:
            return driver.find_element(self.by, self.elem)
        else:
            return self.driver.find_element(self.by, self.elem)

    def canfind(self, driver=None):
        if not driver:
            driver = self.driver
        
        try:
            if self.debug:
                print(f"trying to find {self.elem}")
                self.started = False
            driver.find_element(self.by, self.elem)
        except:
            return False
        else:
            if self.debug:
                print(f"found {self.elem}")
            return True

    def click(self, driver=None):
        if not driver:
            driver = self.driver
        
        try:
            driver.find_element(self.by, self.elem).click()
            if self.debug:
                print(f"trying to click {self.elem}")
        except:
            return False
        else:
            if self.debug:
                print(f"clicked {self.elem}")
            return True
    
    def hasvalue(self, driver=None):
        if not driver:
            driver = self.driver
        
        return (driver.find_element(self.by, self.elem).get_attribute("value") == self.val)

class Script:
    def __init__(self, text, driver=None):
        self.text = text
        if driver:
            self.driver = driver
    
    def execuntiltrue(self, driver=None):
        if driver:
            crdriver = driver
        elif self.driver:
            crdriver = self.driver
        else:
            raise Exception("No driver chose in execuntiltrue from Script object")

        return driver.execute_script(self.text)

class Confere:
    def __init__(self, driver):
        self.__done = False
        self.driver = driver

    def done(self):
        self.__done = True

    async def start(self):
        while self.driver.current_url != "https://ser.saude.rj.gov.br/ser/login" and not self.__done:
            sleep(1)

        if not self.__done:
            raise Exception("Falha no login")