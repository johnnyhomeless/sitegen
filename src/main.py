from textnode import TextType, TextNode
import os, shutil

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
public = os.path.join(base, "public/") 
static = os.path.join(base, "static/")

def folder_deleter():
    if os.path.exists(public):
        shutil.rmtree(public)
    os.makedirs(public)
    shutil.copytree(static, public, dirs_exist_ok=True)

def main():
    test_print = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(test_print)

if __name__=="__main__":
    main()
    folder_deleter()