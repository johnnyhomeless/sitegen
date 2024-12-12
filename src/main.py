from textnode import (TextType,
                      TextNode)

def main():
    test_print = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(test_print)

if __name__=="__main__":
    main()