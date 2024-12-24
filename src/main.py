from textnode import TextType, TextNode
import os, shutil
from markdown_to_html import generate_page

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
public = os.path.join(base, "public/") 
static = os.path.join(base, "static/")
content_dir = "content/index.md"
template_file = "template.html"
public_dir = "public/index.html"

def main():
    test_print = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(test_print)

def folder_deleter():
    if os.path.exists(public):
        shutil.rmtree(public)
    os.makedirs(public)
    shutil.copytree(static, public, dirs_exist_ok=True)

if __name__=="__main__":
    main()
    folder_deleter()
    generate_page(
        os.path.join(base, content_dir),
        os.path.join(base, template_file), 
        os.path.join(base, public_dir)
    )