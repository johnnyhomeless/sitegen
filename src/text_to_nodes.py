from textnode import TextNode, TextType
from text_splitter import split_nodes_delimiter, split_nodes_image, split_nodes_links

def _error_handling(text):
    if text is None:
        raise ValueError(f"{text} cannot be None")
    if not isinstance(text, str):
        raise ValueError(f"{text} must be a string")
    if text.strip() == "":
        raise ValueError(f"{text} cannot be empty")

def text_to_textnodes(text):
    _error_handling(text)
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)
    return nodes