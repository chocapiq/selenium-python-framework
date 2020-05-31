# Util class implementation for most common utilities
import time
import traceback
import string
import random
import utilities.CustomLogger as cl
import logging

class Util(object):
    log = cl.CustomLogger(logging.INFO)

    def sleep(self, sec, info=""):
        if info is not None:
            self.log.info("Wait: " + str(sec) + " seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type="letters"):
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'numeric':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount="10"):
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        nameList = []
        for i in range (0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def verifyTextContains(self, actualText, expectedText):
        self.log.info("Actual text from application Web UI -> " + actualText)
        self.log.info("Expected text from application Web UI -> " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### Verification contains!")
            return True
        else:
            self.log.info("### Verification DOESN'T contain!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        self.log.info("Actual text from application Web UI -> " + actualText)
        self.log.info("Expected text from applcation Web UI -> " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.log.info("### Verification matches!")
            return True
        else:
            self.log.info("Verification DOESN'T match!")
            return False

    def verifyListMatch(self, expectedList, actualList):
        return set(actualList) == set(expectedList)

    def verifyListConstains(self, expectedList, actualList):
        length = len(expectedList)
        for i in range (0, length):
            if expectedList[i] not in actualList:
                return False
            else:
                return True