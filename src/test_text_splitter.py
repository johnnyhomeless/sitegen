import unittest
from text_splitter import split_nodes_delimiter
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


if __name__ == "__main__":
    unittest.main()
