from textnode import TextNode, TextType
from markdown_parser import extract_markdown_images, extract_markdown_links

def _validate_nodes(nodes):
    if nodes is None:
        raise Exception("nodes cannot be None.")
    
    if not isinstance(nodes, list):
        raise ValueError("nodes must be a list.")
    
    if not nodes:
        raise ValueError("nodes cannot be an empty list.")
        
    for node in nodes:
        if not isinstance(node, TextNode):
            raise ValueError("all nodes in list must be TextNode instances")

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

def split_nodes_image(old_nodes):
   _validate_nodes(old_nodes)
   
   new_nodes = []

   for node in old_nodes:
       if node.text_type != TextType.TEXT:
           new_nodes.append(node)
           continue
           
       images = extract_markdown_images(node.text)
       
       if not images:
           new_nodes.append(node)
           continue
       
       remaining_text = node.text
       
       for alt_text, url in images:
           parts = remaining_text.split(f"![{alt_text}]({url})", 1)
           
           if parts[0].strip():
               new_nodes.append(TextNode(parts[0], TextType.TEXT))
               
           new_nodes.append(TextNode(alt_text, TextType.IMAGES, url))
           
           if len(parts) > 1:
               remaining_text = parts[1]
       
       if remaining_text.strip():
           new_nodes.append(TextNode(remaining_text, TextType.TEXT))
           
   return new_nodes

def split_nodes_links(old_nodes):
   _validate_nodes(old_nodes)
   
   new_nodes = []

   for node in old_nodes:
       if node.text_type != TextType.TEXT:
           new_nodes.append(node)
           continue
           
       links = extract_markdown_links(node.text)
       
       if not links:
           new_nodes.append(node)
           continue
       
       remaining_text = node.text
       
       for alt_text, url in links:
           parts = remaining_text.split(f"[{alt_text}]({url})", 1)
           
           if parts[0].strip():
               new_nodes.append(TextNode(parts[0], TextType.TEXT))
               
           new_nodes.append(TextNode(alt_text, TextType.LINKS, url))
           
           if len(parts) > 1:
               remaining_text = parts[1]
       
       if remaining_text.strip():
           new_nodes.append(TextNode(remaining_text, TextType.TEXT))
           
   return new_nodes
