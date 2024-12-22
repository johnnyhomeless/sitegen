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

# scrivere  i test
