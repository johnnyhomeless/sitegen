from text_to_nodes import _error_handling

def markdown_to_blocks(markdown):
   _error_handling(markdown)
   
   blocks = []
   current_block = []
   splitted_txt = markdown.split('\n')
   
   for line in splitted_txt:
       if line.strip():
           current_block.append(line)
       elif current_block:
           blocks.append('\n'.join(current_block))
           current_block = []
           
   if current_block:
       blocks.append('\n'.join(current_block))
   
   return [block.strip() for block in blocks if block.strip()]

def block_to_block_type(block):
    block = block.strip()
    lines = block.split('\n')
    
    if block.startswith("```") and block.endswith("```"):
        return "code"
    
    if block.startswith("#") and " " in block[1:7]:
        return "heading"
    
    if all(line.strip().startswith('>') for line in lines):
        return "quote"
    
    if all(line.strip().startswith(('* ', '- ')) for line in lines):
        return "unordered_list"
    
    if all(line.strip().startswith(f"{i+1}. ") for i, line in enumerate(lines)):
        return "ordered_list"
    
    return "paragraph"

    
def is_ordered_list(lines):
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            return False
    return True

    
    



