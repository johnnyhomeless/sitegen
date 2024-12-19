import re
from textnode import is_valid_url

def _validate_markdown_content(text, urls=None):   
   if text is None:
      raise Exception("text cannot be None.")

   if text == "":
      raise Exception("text cannot be empty.")
   
   if urls:
      for url in urls:
         if not is_valid_url(url):
            raise Exception(f"Invalid url: {url}.")
         

def extract_markdown_images(text):
   _validate_markdown_content(text)
   matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
   urls = [url for _, url in matches]
   _validate_markdown_content(text, urls)
   return matches
      

def extract_markdown_links(text):
   _validate_markdown_content(text)
   matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
   urls = [url for _, url in matches]
   _validate_markdown_content(text, urls)
   return matches