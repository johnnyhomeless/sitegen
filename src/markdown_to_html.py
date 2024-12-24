from htmlnode import ParentNode, LeafNode
from text_to_nodes import text_to_textnodes, _error_handling
from markdown_blocks import markdown_to_blocks, block_to_block_type
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
   _error_handling(markdown)
   blocks = markdown_to_blocks(markdown)
   children = []
   parent = ParentNode("div", children)

   for block in blocks:
       block_type = block_to_block_type(block)
       if block_type == "paragraph":
           content = extract_paragraph_content(block)
           text_nodes = text_to_textnodes(content)
           html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
           node = ParentNode("p", html_nodes)
       
       elif block_type == "heading":
           content, level = extract_heading_content(block)
           text_nodes = text_to_textnodes(content)
           html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
           node = ParentNode(f"h{level}", html_nodes)
       
       elif block_type == "code":
           content = extract_code_content(block)
           code_node = LeafNode("code", content)
           node = ParentNode("pre", [code_node])
       
       elif block_type == "quote":
           content = extract_quote_content(block)
           text_nodes = text_to_textnodes(content)
           html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
           node = ParentNode("blockquote", html_nodes)
       
       elif block_type == "unordered_list":
           items = extract_list_content(block)
           list_items = []
           for item in items:
               text_nodes = text_to_textnodes(item)
               html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
               list_items.append(ParentNode("li", html_nodes))
           node = ParentNode("ul", list_items)
       
       elif block_type == "ordered_list":
           items = extract_list_content(block)
           list_items = []
           for item in items:
               text_nodes = text_to_textnodes(item)
               html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
               list_items.append(ParentNode("li", html_nodes))
           node = ParentNode("ol", list_items)
           
       children.append(node)
   
   return parent

def extract_heading_content(block):
   count = 0
   for char in block:
       if char == '#':
           count += 1
           if count > 6:
               raise ValueError("Max # allowed: 6")
       else:
           break
   
   content = block[count:].strip()
   if not content:
       raise ValueError("Heading content cannot be empty")
   
   return content, count

def extract_quote_content(block):
    lines = block.split('\n')
    clean_lines = [line.strip().lstrip('>').strip() for line in lines]
    return '\n'.join(clean_lines)

def extract_list_content(block):
    lines = block.split('\n')
    clean_lines = []
    
    for line in lines:
        line = line.strip()
        if line.startswith(('* ', '- ')):
            clean_lines.append(line[2:])
        elif any(line.startswith(f"{i}. ") for i in range(1, 10)):
            clean_lines.append(line[line.find('. ') + 2:])
            
    return clean_lines

def extract_code_content(block):
    if not (block.startswith("```") and block.endswith("```")):
        raise ValueError("Code blocks must start and end with ```")
    
    lines = block[3:-3].split('\n')
    clean_lines = [line.lstrip() for line in lines]
    return '\n'.join(clean_lines).strip()

def extract_paragraph_content(block):
   return block.strip()