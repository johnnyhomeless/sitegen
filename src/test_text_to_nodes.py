import unittest
from text_to_nodes import text_to_textnodes, _error_handling
from textnode import TextNode, TextType

class TestTextToNodes(unittest.TestCase):
    def test_none_text(self):
        with self.assertRaises(ValueError):
            _error_handling(None)

    def test_empty_text(self):
        with self.assertRaises(ValueError):
            _error_handling("")

    def test_non_string_text(self):
        with self.assertRaises(ValueError):
            _error_handling(123)

    def test_plain_text(self):    
        text = "This is plain text"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "This is plain text")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
    
    def test_bold_text(self):
        text = "**bold**"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "bold")
        self.assertEqual(nodes[0].text_type, TextType.BOLD)
    
    def test_italic_text(self):
        text = "*italic*"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "italic")
        self.assertEqual(nodes[0].text_type, TextType.ITALIC)   

    def test_code_text(self):
        text = "`code`"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "code")
        self.assertEqual(nodes[0].text_type, TextType.CODE) 

    def test_link_text(self):
        text = "[doggo](http://dog.go/woof.jpg)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "doggo")
        self.assertEqual(nodes[0].text_type, TextType.LINKS)
        self.assertEqual(nodes[0].url, "http://dog.go/woof.jpg")

    def test_image_text(self):
        text = "![doggo](http://dog.go/woof.jpg)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "doggo")
        self.assertEqual(nodes[0].text_type, TextType.IMAGES)
        self.assertEqual(nodes[0].url, "http://dog.go/woof.jpg")

    def test_bold_italic(self):
        text = "**bold** and *italic*"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "bold")
        self.assertEqual(nodes[0].text_type, TextType.BOLD)
        self.assertEqual(nodes[1].text, " and ")
        self.assertEqual(nodes[1].text_type, TextType.TEXT)
        self.assertEqual(nodes[2].text, "italic")
        self.assertEqual(nodes[2].text_type, TextType.ITALIC)

    def test_multiple_links(self):
        text = "[doggo](http://dog.go/woof.jpg)[doggo1](http://dog.go/woof1.jpg)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "doggo")
        self.assertEqual(nodes[0].text_type, TextType.LINKS)
        self.assertEqual(nodes[0].url, "http://dog.go/woof.jpg")
        self.assertEqual(nodes[1].text, "doggo1")
        self.assertEqual(nodes[1].text_type, TextType.LINKS)
        self.assertEqual(nodes[1].url, "http://dog.go/woof1.jpg")

    def test_multiple_images_and_txt(self):
        text = "![doggo](http://dog.go/woof.jpg) and ![doggo1](http://dog.go/woof1.jpg) **and bold**"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].text, "doggo")
        self.assertEqual(nodes[0].text_type, TextType.IMAGES)
        self.assertEqual(nodes[0].url, "http://dog.go/woof.jpg")
        self.assertEqual(nodes[1].text, " and ")
        self.assertEqual(nodes[1].text_type, TextType.TEXT)
        self.assertEqual(nodes[2].text, "doggo1")
        self.assertEqual(nodes[2].text_type, TextType.IMAGES)
        self.assertEqual(nodes[2].url, "http://dog.go/woof1.jpg")
        self.assertEqual(nodes[3].text, "and bold")
        self.assertEqual(nodes[3].text_type, TextType.BOLD)

    def test_complex_text(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![doggo](http://dog.go/woof.jpg) and a [doggo](http://dog.go/woof.jpg)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 10)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)    
        self.assertEqual(nodes[1].text, "text")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " with an ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)  
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(nodes[4].text, " word and a ")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)
        self.assertEqual(nodes[5].text, "code block")
        self.assertEqual(nodes[5].text_type, TextType.CODE)
        self.assertEqual(nodes[6].text, " and an ")
        self.assertEqual(nodes[6].text_type, TextType.TEXT)
        self.assertEqual(nodes[7].text, "doggo")
        self.assertEqual(nodes[7].text_type, TextType.IMAGES)
        self.assertEqual(nodes[7].url, "http://dog.go/woof.jpg")
        self.assertEqual(nodes[8].text, " and a ")
        self.assertEqual(nodes[8].text_type, TextType.TEXT)
        self.assertEqual(nodes[9].text, "doggo")
        self.assertEqual(nodes[9].text_type, TextType.LINKS)
        self.assertEqual(nodes[9].url, "http://dog.go/woof.jpg")
    



if __name__ == "__main__":
    unittest.main()