from enum import Enum
from htmlnode import LeafNode
from urllib.parse import urlparse

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

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
    
def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise TypeError("Input must be a TextNode instance")
    
    if text_node is None:
        raise Exception("text_node cannot be None.")
    
    if text_node.text_type != TextType.IMAGES and not text_node.text.strip():
        raise ValueError("Text content cannot be empty")
        
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    
    if text_node.text_type == TextType.LINKS:
        if not is_valid_url(text_node.url):
            raise ValueError(f"Invalid URL for link: {text_node.url}. URL must include scheme (http/https) and domain.")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
    if text_node.text_type == TextType.IMAGES:
        if not is_valid_url(text_node.url):
            raise ValueError(f"Invalid URL for image source: {text_node.url}. URL must include scheme (http/https) and domain.")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    
    raise ValueError(f"Unsupported text type: {text_node.text_type}. Available types: {', '.join([t.name for t in TextType])}")

