import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_none_url(self):
        node = TextNode("Hey", TextType.TEXT, None)
        node2 = TextNode("Hey", TextType.TEXT, None)
        self.assertEqual(node, node2)
    
    def test_wrong_texttype(self):
        node = TextNode("Hey", TextType.TEXT, None)
        node2 = TextNode("Hey", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

    def test_invalid_texttype(self):
        with self.assertRaises(AttributeError):
            TextNode("Hey", TextType.TSDF, None)

    def test_text_to_html(self):
        node = TextNode("Hello", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "Hello")
    
    def test_bold_to_html(self):
        node = TextNode("Massimo Bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>Massimo Bold</b>")

    def test_italic_to_html(self):
        node = TextNode("Itali Calvino", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>Itali Calvino</i>")

    def test_code_to_html(self):
        node = TextNode("Code fratello orso", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>Code fratello orso</code>")
    
    def test_links_to_html(self):
        node = TextNode("Google.com", TextType.LINKS, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">Google.com</a>')

    def test_images_to_html(self):
        node = TextNode("Puppy!", TextType.IMAGES, "https://i.imgur.com/2EVsgX0.jpeg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<img src="https://i.imgur.com/2EVsgX0.jpeg" alt="Puppy!">')

    def test_none_input(self):
        with self.assertRaises(Exception):
            text_node_to_html_node(None)

    def test_invalid_link_url(self):
        node = TextNode("Click me", TextType.LINKS, "goongle")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_invalid_image_url(self):
        node = TextNode("Puppy", TextType.IMAGES, "puppy.jpg")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()