import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkDown_To_Html(unittest.TestCase):
    def test_paragraph_basic(self):
        text = "This is a paragraph"
        node = markdown_to_html_node(text)
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph</p></div>")
    
    def test_heading_basic(self):
        text = "# Heading"
        node = markdown_to_html_node(text)
        self.assertEqual(node.to_html(), "<div><h1>Heading</h1></div>")
    
    def test_code_basic(self):
        text = "```code\ntest```"
        node = markdown_to_html_node(text)
        self.assertEqual(node.to_html(), "<div><pre><code>code\ntest</code></pre></div>")
    
    def test_quote_basic(self):
        text = ">boing\n>test"
        node = markdown_to_html_node(text)
        self.assertEqual(node.to_html(), "<div><blockquote>boing\ntest</blockquote></div>")

    def test_unordered_list(self):
        text = "* First item\n* Second item\n* Third item"
        node = markdown_to_html_node(text)
        self.assertEqual(node.to_html(), "<div><ul><li>First item</li><li>Second item</li><li>Third item</li></ul></div>")

    def test_ordered_list(self):
        text = "1. First item\n2. Second item\n3. Third item"
        node = markdown_to_html_node(text)
        self.assertEqual(node.to_html(), "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>")

    def test_paragraph_with_text_formatting(self):
        text = "This is a **bold** paragraph with *italic* and `code` and a [link](https://www.test.com)"
        node = markdown_to_html_node(text)
        expected = '<div><p>This is a <b>bold</b> paragraph with <i>italic</i> and <code>code</code> and a <a href="https://www.test.com">link</a></p></div>'
        self.assertEqual(node.to_html(), expected)

    def test_blockquote_with_formatting(self):
        text = "> This is a **quoted** text"
        node = markdown_to_html_node(text)
        expected = '<div><blockquote>This is a <b>quoted</b> text</blockquote></div>'
        self.assertEqual(node.to_html(), expected)

    def test_complex_markdown(self):
        text = """# Main Title

        This is a **bold** paragraph with *italic* and `code` and a [link](https://www.test.com).

        ## Sub Heading

        > This is a **quoted** text with *formatting*
        > And a second line

        1. First **bold** item
        2. Second item with [link](https://test.com)
        3. *Italic* item

        * Unordered with `code`
        * And *italic*

        ```code block
        with **formatting**
        ```"""
        
        expected = '<div><h1>Main Title</h1><p>This is a <b>bold</b> paragraph with <i>italic</i> and <code>code</code> and a <a href="https://www.test.com">link</a>.</p><h2>Sub Heading</h2><blockquote>This is a <b>quoted</b> text with <i>formatting</i>\nAnd a second line</blockquote><ol><li>First <b>bold</b> item</li><li>Second item with <a href="https://test.com">link</a></li><li><i>Italic</i> item</li></ol><ul><li>Unordered with <code>code</code></li><li>And <i>italic</i></li></ul><pre><code>code block\nwith **formatting**</code></pre></div>'

        self.maxDiff = None
        node = markdown_to_html_node(text)
        self.assertEqual(node.to_html(), expected)

    def test_comprehensive_markdown(self):
        markdown = """# Top Level Heading

This is a **bold** paragraph with *italic* text and `inline code`. Here's a [link](https://example.com).

## Second Level Heading

> A blockquote with **bold** and *italic* text
> And another line

1. First list item with **bold**
2. Second item with *italic*
3. Third item with `code`

* Bullet with [link](https://test.com)
* Another bullet

```
Code block with multiple
lines of code
```"""
        
        expected = '<div><h1>Top Level Heading</h1><p>This is a <b>bold</b> paragraph with <i>italic</i> text and <code>inline code</code>. Here\'s a <a href="https://example.com">link</a>.</p><h2>Second Level Heading</h2><blockquote>A blockquote with <b>bold</b> and <i>italic</i> text\nAnd another line</blockquote><ol><li>First list item with <b>bold</b></li><li>Second item with <i>italic</i></li><li>Third item with <code>code</code></li></ol><ul><li>Bullet with <a href="https://test.com">link</a></li><li>Another bullet</li></ul><pre><code>Code block with multiple\nlines of code</code></pre></div>'

        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()