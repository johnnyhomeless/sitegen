class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        result = []
        for key, value in self.props.items():
            result.append(f' {key}="{value}"')
        return "".join(result)
    
    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag is None:
            return self.value
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("A tag argument is required.")

        if self.children is None:
            raise ValueError("A children argument is required.")

        children_html = []
        for child in self.children:
            children_html.append(child.to_html())
        return f'<{self.tag}>{"".join(children_html)}</{self.tag}>'

