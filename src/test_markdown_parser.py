import unittest
from markdown_parser import extract_markdown_images, extract_markdown_links

class TestMarkdownParser(unittest.TestCase):
    def test_basic_image(self):
        text = "![alt text](https://example.com/image.jpg)"
        expected = [("alt text", "https://example.com/image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)
    
    def test_basic_link(self):
        text = "[google.com](https://www.google.com)"
        expected = [("google.com", "https://www.google.com")]
        self.assertEqual(extract_markdown_links(text), expected)
    
    def test_none(self):
        with self.assertRaises(Exception):
            extract_markdown_images(None)
    
    def test_empty(self):
        with self.assertRaises(Exception):
            extract_markdown_images("")
    
    def test_invalid_url(self):
        with self.assertRaises(Exception):
            text = "![google.com](googlecom)"
            extract_markdown_images(text)
    
    def test_no_images(self):
        text = "This is text without any images"
        self.assertEqual(extract_markdown_images(text), [])
    
    def test_multiple_links(self):
        text = "[google.com](https://www.google.com)[google.com](https://www.google.com)"
        expected = [("google.com", "https://www.google.com"), ("google.com", "https://www.google.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_mixed_content(self):
        text = "Here's a ![image](https://example.com/img.jpg) and a [link](https://example.com)"
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)
        self.assertEqual(len(image_matches), 1)
        self.assertEqual(len(link_matches), 1)

if __name__ == "__main__":
    unittest.main()