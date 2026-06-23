from html.parser import HTMLParser

class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.self_closing_tags = {
            'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
            'link', 'meta', 'param', 'source', 'track', 'wbr', '!doctype'
        }

    def handle_starttag(self, tag, attrs):
        if tag in self.self_closing_tags:
            return
        self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.self_closing_tags:
            return
        if not self.stack:
            self.errors.append(f"Unexpected end tag </{tag}> at line {self.getpos()[0]}")
            return
        
        expected, pos = self.stack.pop()
        if expected != tag:
            self.errors.append(f"Mismatch: expected </{expected}> (opened at line {pos[0]}), found </{tag}> at line {self.getpos()[0]}")
            # Re-push expected if we think the current tag is just a wrong close
            # but usually we just log and proceed
            self.stack.append((expected, pos))

    def check(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.feed(content)
        
        if self.stack:
            for tag, pos in self.stack:
                self.errors.append(f"Unclosed tag <{tag}> opened at line {pos[0]}")
        
        return self.errors

validator = HTMLValidator()
errors = validator.check('c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/index.html')
if errors:
    print(f"Found {len(errors)} HTML structure errors:")
    for err in errors:
        print(f"  - {err}")
else:
    print("HTML structure is perfectly valid and balanced!")
