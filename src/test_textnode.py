import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()