import unittest
import os, shutil, pathlib
from main import generate_pages_recursive

class TestPageGenerator(unittest.TestCase):
   def setUp(self):
       self.test_content = "test_content"
       self.test_public = "test_public"
       self.template = "test_template.html"
       
       os.makedirs(self.test_content, exist_ok=True)
       os.makedirs(self.test_public, exist_ok=True)
       
       with open(self.template, 'w') as f:
           f.write("<html>{{content}}</html>")

   def tearDown(self):
       shutil.rmtree(self.test_content)
       shutil.rmtree(self.test_public)
       os.remove(self.template)

   def test_basic_conversion(self):
       with open(f"{self.test_content}/test.md", 'w') as f:
           f.write("# Test")

       generate_pages_recursive(self.test_content, self.template, self.test_public)
       
       self.assertTrue(os.path.exists(f"{self.test_public}/test.html"))
       with open(f"{self.test_public}/test.html", 'r') as f:
           self.assertIn("<h1>Test</h1>", f.read())

   def test_nested_directories(self):
       os.makedirs(f"{self.test_content}/nested", exist_ok=True)
       with open(f"{self.test_content}/nested/test.md", 'w') as f:
           f.write("# Nested")

       generate_pages_recursive(self.test_content, self.template, self.test_public)
       
       self.assertTrue(os.path.exists(f"{self.test_public}/nested/test.html"))

if __name__ == '__main__':
   unittest.main()