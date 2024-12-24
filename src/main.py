from textnode import TextType, TextNode
import os, shutil, pathlib
from markdown_to_html import generate_page, markdown_to_html_node

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
public = os.path.join(base, "public/") 
static = os.path.join(base, "static/")
template_file = "template.html"
content_dir = "content"
public_dir = "public"


def folder_deleter():
    if os.path.exists(public):
        shutil.rmtree(public)
    os.makedirs(public)
    shutil.copytree(static, public, dirs_exist_ok=True)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
   content_path = pathlib.Path(dir_path_content)
   markdown_files = content_path.rglob("*.md")

   for file_path in markdown_files:
       relative_path = file_path.relative_to(content_path)
       output_path = pathlib.Path(dest_dir_path) / relative_path
       output_path = output_path.with_suffix('.html')
       output_path.parent.mkdir(parents=True, exist_ok=True)

       with open(file_path, 'r') as f:
           markdown_content = f.read()
       
       with open(template_path, 'r') as f:
           template = f.read()

       html_node = markdown_to_html_node(markdown_content)
       html_content = html_node.to_html()
       
       dirname = os.path.dirname(file_path)
       title = os.path.basename(dirname)
       final_html = template.replace("{{ Content }}", html_content).replace("{{ Title }}", title)

       with open(output_path, 'w') as f:
           f.write(final_html)

def main():
    folder_deleter()
    generate_pages_recursive(
        os.path.join(base, content_dir),
        os.path.join(base, template_file), 
        os.path.join(base, public_dir)
    )
    print(os.path.join(base, content_dir))
    print(os.path.join(base, template_file))
    print(os.path.join(base, public_dir))

if __name__=="__main__":
    main()