class Note:

    def __init__(self, name, text):
        self.text = text
        self.name = name

    def addText(self, text: str):
        self.text = text

    def removeText(self):
        self.text = ""

    def getText(self):
        return self.text