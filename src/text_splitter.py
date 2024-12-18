from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not isinstance(old_nodes, list):
        raise ValueError("old_nodes must be a list.")
        
    if not old_nodes:
        raise ValueError("old_nodes cannot be empty.")
        
    if not isinstance(delimiter, str):
        raise ValueError("delimiter must be a string.")
        
    if not isinstance(text_type, TextType):
        raise ValueError("text_type must be a TextType.")

    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise ValueError("all nodes in old_nodes must be TextNode instances")
        
    new_nodes = []

    for check in old_nodes:
        if check.text_type != TextType.TEXT:
            new_nodes.append(check)
        else:
            delimiter_start = check.text.find(delimiter)
            if delimiter_start == -1:
                new_nodes.append(check)
            else:
                delimiter_end = check.text.find(delimiter, delimiter_start + len(delimiter))
                if delimiter_end == -1:
                    new_nodes.append(check)
                else:
                    before_text = check.text[0:delimiter_start]
                    middle_text = check.text[delimiter_start + len(delimiter):delimiter_end]
                    after_text = check.text[delimiter_end + len(delimiter):]
                    
                    if before_text.strip():
                        new_nodes.append(TextNode(before_text, TextType.TEXT))
                    if middle_text.strip():
                        new_nodes.append(TextNode(middle_text, text_type))
                    if after_text.strip():
                        new_nodes.append(TextNode(after_text, TextType.TEXT))

    return new_nodes
