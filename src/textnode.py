from enum import Enum

class TextType(Enum):
    TEXT = "Normal"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINKS = "Links"
    IMAGES = "Images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.text, self.text_type, self.url) == (other.text, other.text_type, other.url)
    
    def __repr__(self):
        if self.url is None:
            return f'TextNode("{self.text}", {self.text_type.value}, {self.url})'
        return f'TextNode("{self.text}", {self.text_type.value}, "{self.url}")'