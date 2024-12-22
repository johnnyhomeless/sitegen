import unittest

from markdown_blocks import markdown_to_blocks

class TestMarkdownBlocks(unittest.TestCase):
    def test_single_paragraph(self):
        text = "This is a simple paragraph."
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0], "This is a simple paragraph.")
    
    def test_single_heading(self):
        text = "# This is a simple heading."
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0], "# This is a simple heading.")
    
    def test_single_list(self):
        text = "multiple\nlines\nok?"
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0], "multiple\nlines\nok?")
    
    def test_multiple_paragraphs(self):
        text = "First paragraph\n\nSecond paragraph\n\nThird paragraph"
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "First paragraph")
        self.assertEqual(blocks[1], "Second paragraph")
        self.assertEqual(blocks[2], "Third paragraph")
    
    def test_mixed_blocks(self):
        text = "# Heading\n\nThis is a paragraph.\n\n* List item 1\n* List item 2\n* List item 3"
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "# Heading")
        self.assertEqual(blocks[1], "This is a paragraph.")
        self.assertEqual(blocks[2], "* List item 1\n* List item 2\n* List item 3")

    def test_multiple_empty_lines(self):
        text = "\n\nFirst block\n\n\n\nSecond block\n\n\n"
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 2)
        self.assertEqual(blocks[0], "First block")
        self.assertEqual(blocks[1], "Second block")

if __name__ == "__main__":
    unittest.main()