import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
        node = LeafNode("p", "This is gasoline... and I set myself on fire.")
        result = '<p>This is gasoline... and I set myself on fire.</p>'
        self.assertEqual(node.to_html(), result)
    
    def test_notag(self):
        node = LeafNode(None, "This is gasoline... and I set myself on fire.")
        result = "This is gasoline... and I set myself on fire."
        self.assertEqual(node.to_html(), result)
    
    def test_missing_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()
    
class TestParentNode(unittest.TestCase):
    def test_onechild(self):
        node = LeafNode("p", "This is gasoline... and I set myself on fire.")
        node1 = ParentNode("div", [node])
        result = "<div><p>This is gasoline... and I set myself on fire.</p></div>"
        self.assertEqual(node1.to_html(), result)
    
    def test_no_tag(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", "This is gasoline... and I set myself on fire.")
            node1 = ParentNode(None, [node])
            node1.to_html()
    
    def test_no_child(self):
        with self.assertRaises(ValueError):
            node = ParentNode("div", None)
            node.to_html()
    
    def test_multiple_child(self):
        node = LeafNode("p", "This is gasoline... and I set myself on fire.")
        node1 = LeafNode("p", "This is gasoline... and I set myself on fire.")
        node2 = ParentNode("div", [node, node1])
        result = "<div><p>This is gasoline... and I set myself on fire.</p><p>This is gasoline... and I set myself on fire.</p></div>"
        self.assertEqual(node2.to_html(), result)

    def test_nested_parent(self):
        node = LeafNode("p", "This is gasoline... and I set myself on fire.")
        node1 = ParentNode("div", [node])
        node2 = ParentNode("section", [node1])
        result = "<section><div><p>This is gasoline... and I set myself on fire.</p></div></section>"
        self.assertEqual(node2.to_html(), result)

if __name__ == "__main__":
    unittest.main()