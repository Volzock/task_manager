class Note:

    def __init__(self, text):
        self.text = text

    def addText(self, text: str):
        self.text = text

    def removeText(self):
        self.text = ""

    def getText(self):
        return self.text