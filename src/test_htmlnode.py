import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_single_prop(self):
        node = HTMLNode(props={"id": "test"})
        self.assertEqual(node.props_to_html(), ' id="test"')

    def test_multiple_props(self):
        node = HTMLNode(props={"id": "test", "id1": "test1"})

class TestLeafNode(unittest.TestCase):
    def test_tag_value(self):
        node = LeafNode("a", "Search here!", {"href": "https://www.google.com"})
        result = '<a href="https://www.google.com">Search here!</a>'
        self.assertEqual(node.to_html(), result)

    def test_tag_noprops(self):
        node = LeafNode("p", "This is gasoline, and I put myself on fire")
        result = '<p>This is gasoline, and I put myself on fire</p>'
        self.assertEqual(node.to_html(), result)
    
    def test_notag(self):
        node = LeafNode(None, "This is gasoline, and I put myself on fire")
        result = "This is gasoline, and I put myself on fire"
        self.assertEqual(node.to_html(), result)
    
    def test_missing_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()
    
    


if __name__ == "__main__":
    unittest.main()