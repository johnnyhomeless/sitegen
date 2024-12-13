import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_single_prop(self):
        node = HTMLNode(props={"id": "test"})
        self.assertEqual(node.props_to_html(), ' id="test"')

    def test_multiple_props(self):
        node = HTMLNode(props={"id": "test", "id1": "test1"})

if __name__ == "__main__":
    unittest.main()