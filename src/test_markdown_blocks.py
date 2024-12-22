import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type 

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

    def test_basic_paragraph(self):
        text = "basic paragraph"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks, "paragraph")
    
    def test_basic_heading(self):
        text = "# boing"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks, "heading")

    def test_basic_code(self):
        text = "```boing```"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks, "code") 
    
    def test_basic_quote(self):
        text = ">boing"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks, "quote") 
    
    def test_basic_unordered_list(self):
        text = "- boing\n* boing"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks, "unordered_list") 

    def test_basic_ordered_list(self):
        text = "1. boing"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks, "ordered_list") 

    def test_multiple_lines_paragraph(self):
        text = "hey\nhey\nhey hey\n\n hey"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks, "paragraph")
    
    def test_heading_levels(self):
        text = "# oof\n\n###  hehe\n## hehe"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks, "heading")
    
    def test_multiline_quote(self):
        text = ">oof\n>hehe\n>hehe"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks, "quote")
    
    def test_long_ordered_list(self):
        text = "1. boing\n2. boing\n3. boing"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks, "ordered_list")

    def test_code_with_content(self):
        text = "```blocks = block_to_block_type(text)\nblocks = block_to_block_type(text)```"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks, "code") 

if __name__ == "__main__":
    unittest.main()