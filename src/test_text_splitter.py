import unittest
from text_splitter import split_nodes_delimiter, split_nodes_image
from textnode import TextNode, TextType

class TestTextSplitter(unittest.TestCase):
    def test_just_text(self):
        node = TextNode("This is text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "", TextType.TEXT)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is text.")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

    def test_code(self):
        node = TextNode("This `code` here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " here")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_bold(self):
        node = TextNode("This is **Massimo Bold** text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "Massimo Bold")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " text.")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_italic(self):
        node = TextNode("This is *Italo Calvino* text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "Italo Calvino")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text, " text.")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
    
    def test_text_mix(self):
        node = TextNode("This is *Italo Calvino* and **Massimo Bold**.", TextType.TEXT)
        first_split = split_nodes_delimiter([node], "**", TextType.BOLD)
        second_split = split_nodes_delimiter(first_split, "*", TextType.ITALIC)
        self.assertEqual(len(second_split), 5)
        self.assertEqual(second_split[0].text, "This is ")
        self.assertEqual(second_split[0].text_type, TextType.TEXT)
        self.assertEqual(second_split[1].text, "Italo Calvino")
        self.assertEqual(second_split[1].text_type, TextType.ITALIC)
        self.assertEqual(second_split[2].text, " and ")
        self.assertEqual(second_split[2].text_type, TextType.TEXT)
        self.assertEqual(second_split[3].text, "Massimo Bold")
        self.assertEqual(second_split[3].text_type, TextType.BOLD)
        self.assertEqual(second_split[4].text, ".")
        self.assertEqual(second_split[4].text_type, TextType.TEXT)

    def test_invalid_txt_type(self):
        node = TextNode("Text", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "", "TextTypeBONGHLD")
    
    def test_none_delimiter(self):
        node = TextNode("**Text**", TextType.BOLD)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], None, TextType.BOLD)

    def test_basic_image(self):
        node = [TextNode("![doggo](http://dog.go/woof.jpg)", TextType.TEXT)]
        new_nodes = split_nodes_image(node)
        self.assertEqual(new_nodes, [TextNode("doggo", TextType.IMAGES, "http://dog.go/woof.jpg")])
    
    def test_just_txt(self):
        node = [TextNode("boing", TextType.TEXT)]
        new_nodes = split_nodes_image(node)
        self.assertEqual(new_nodes, [TextNode("boing", TextType.TEXT)])
    
    def test_none_nodes(self):
        node = [TextNode(None, TextType.TEXT)]
        with self.assertRaises(Exception):
            split_nodes_image(node)

    def test_empty_url(self):
        node = [TextNode("![doggo]()", TextType.TEXT)]
        with self.assertRaises(Exception):
            split_nodes_image(node)
    
    def test_multiple_images(self):
        node = [TextNode("![doggo](http://dog.go/woof.jpg)![doggo2](http://dog.go/woof2.jpg)", TextType.TEXT)]
        new_nodes = split_nodes_image(node)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes, [
            TextNode("doggo", TextType.IMAGES, "http://dog.go/woof.jpg"),
            TextNode("doggo2", TextType.IMAGES, "http://dog.go/woof2.jpg")
        ])        

    def test_text_between_images(self):
        node = [TextNode("![doggo](http://dog.go/woof.jpg) boing boing ![doggo2](http://dog.go/woof2.jpg)", TextType.TEXT)]
        new_nodes = split_nodes_image(node)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes, [
            TextNode("doggo", TextType.IMAGES, "http://dog.go/woof.jpg"),
            TextNode(" boing boing ", TextType.TEXT),
            TextNode("doggo2", TextType.IMAGES, "http://dog.go/woof2.jpg")
        ])
    
    def test_invalid_image_syntax(self):
        node = [TextNode("![doggo](9ub)", TextType.TEXT)]
        with self.assertRaises(Exception):
            split_nodes_image(node)

    def test_empty_alt_text(self):
        node = [TextNode("![](http://dog.go/woof.jpg)", TextType.TEXT)]
        new_nodes = split_nodes_image(node)
        self.assertEqual(new_nodes, [TextNode("", TextType.IMAGES, "http://dog.go/woof.jpg")])

    def test_non_text_node(self):
        node = [TextNode("![doggo](http://dog.go/woof.jpg)", TextType.BOLD)]
        new_nodes = split_nodes_image(node)
        self.assertEqual(new_nodes, node)

    def test_empty_list(self):
        node = []
        with self.assertRaises(Exception):
            split_nodes_image(node)
        
    def test_empty_node(self):
        with self.assertRaises(Exception):
            split_nodes_image()
    
    def test_non_textnode(self):
        node = "hawktuah"
        with self.assertRaises(Exception):
            split_nodes_image(node)

if __name__ == "__main__":
    unittest.main()
