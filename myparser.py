from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def error(self, message):
        pass

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__()
        self.path = []
        self.data = []
        self.valid_tags = []
        self.skip_tags = []
        self.parsers = {}
        self.current_tag = None
        self.is_current_tag_valid = False
        for arg in args:
            for key in arg:
                setattr(self, key, arg[key])
        # print("Parsing of tags:", self.valid_tags)

    def handle_starttag(self, tag, attrs):
        if tag == 'br':
            return
        self.path.append(tag)
        self.is_current_tag_valid = self.valid(tag)
        self.current_tag = tag
        if not self.is_current_tag_valid:
            return
        if self.is_skip(tag):
            return
        self.data.append((tag, attrs))
        super(self.__class__, self).handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag == 'br':
            return
        i = len(self.path) - 1 - self.path[::-1].index(tag)
        self.path = self.path[:i]
        self.current_tag = self.path[-1] if self.path else None
        self.is_current_tag_valid = self.valid(self.current_tag)
        if not self.is_current_tag_valid:
            return
        super(self.__class__, self).handle_endtag(tag)

    def handle_data(self, data):
        if not self.current_tag or not self.is_current_tag_valid:
            return
        if not self.parsers:
            self.default_parser(data)
        else:
            if not self.parsers[self.current_tag]:
                self.default_parser(data)
            else:
                self.parsers[self.current_tag](data, self)
        super(self.__class__, self).handle_data(data)

    def default_parser(self, data):
        if self.data:
            idx = len(self.data) - 1
            last = self.data[idx]
            if len(last) > 2:
                self.data[idx] += (data,)
            else:
                self.data[idx] = (last[0], last[1], data)

    def valid(self, tag):
        if self.valid_tags:
            return True if tag in self.valid_tags else False
        return True

    def is_skip(self, tag):
        if len(self.skip_tags) > 0:
            return True if tag in self.skip_tags else False
        return False

    def feed_and_return(self, data):
        self.feed(data)
        return self


class AnektodHTMLParser(HTMLParser):
    def error(self, message):
        pass

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.ready = []
        self.lines = ""
        self.collecting = False
        self.begin = False
        self.internal_divs = []

    def handle_starttag(self, tag, attrs):
        if tag not in ['div', 'p']:
            return
        for attr in attrs:
            if 'anekdot' in attr:
                if not self.collecting:
                    self.collecting = True
                else:
                    self.internal_divs.append('div')
                return
        if tag == 'p':
            self.begin = True

    def handle_data(self, data):
        if self.collecting:
            if data:
                self.lines += data

    def handle_endtag(self, tag):
        if tag not in ['div', 'p']:
            return

        if tag == 'div':
            if self.internal_divs:
                self.internal_divs.pop('div')

            if not self.internal_divs:
                self.collecting = False
            return

        if tag == 'p':
            self.begin = False
            if self.lines.replace('\n', '').replace('\r', ''):
                self.ready.append(self.lines)
            self.lines = ""


class LinksHTMLParser(HTMLParser):

    def error(self, message):
        pass

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.ready = []
        self.lines = ""
        self.collecting = False
        self.begin = False
        self.internal_divs = []
        self.media_heading = False
        self.links = []
        self.info_add = False
        self.info = []
        self.info_buffer = []

    def handle_starttag(self, tag, attrs):
        if tag not in ['p', 'h4', 'a']:
            return

        for attr in attrs:
            if 'media-heading' in attr:
                self.media_heading = True
            if 'link-reverse' in attr:
                self.info_add = True

        if tag == 'a' and self.media_heading:
            self.collecting = True
            self.links.append(attr[1])

        if tag == 'p':
            self.begin = True

    def handle_data(self, data):
        if self.collecting:
            if data:
                self.lines += data
        if self.info_add:
            self.info_buffer.append(data)

    def handle_endtag(self, tag):
        if tag not in ['p', 'h4', 'a']:
            return

        if tag == 'a' and self.media_heading:
            self.collecting = False

        if tag == 'h4':
            self.media_heading = False
            self.collecting = False
            if self.lines.replace('\n', '').replace('\r', '').strip():
                self.ready.append(self.lines.replace('\n', '').replace('\r', '').strip())
            self.lines = ""

        if tag == 'p' and self.info_add:
            self.info_add = False
            self.info.append(' '.join(self.info_buffer))
            self.info_buffer = []


class StoryHTMLParser(HTMLParser):

    def error(self, message):
        pass

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.ready = []
        self.lines = ""
        self.collecting = False
        self.begin = False
        self.internal_divs = []
        self.pages = []
        self.page_buffer = ''
        self.pages_collect = False

    def handle_starttag(self, tag, attrs):
        if tag not in ['div', 'p', 'ul', 'a']:
            return
        for attr in attrs:
            if 'full_text' in attr:
                if not self.collecting:
                    self.collecting = True
                else:
                    self.internal_divs.append('div')
                return
        if tag == 'p':
            self.begin = True

        if tag == 'ul':
            for attr in attrs:
                if 'pagination' in attr:
                    self.pages_collect = True

        if tag == 'a' and self.pages_collect:
            self.page_buffer = attrs[0][1]

    def handle_data(self, data):
        if self.collecting:
            if data:
                self.lines += data

    def handle_endtag(self, tag):
        if tag not in ['div', 'p', 'ul', 'a']:
            return

        if tag == 'div':
            if self.internal_divs:
                self.internal_divs.pop('div')

            if not self.internal_divs:
                self.collecting = False
            return

        if tag == 'p':
            self.begin = False
            if self.lines.replace('\n', '').replace('\r', ''):
                self.ready.append(self.lines)
            self.lines = ""

        if tag == 'ul' and self.pages_collect:
            self.pages_collect = False

        if tag == 'a' and self.pages_collect:
            self.pages.append(self.page_buffer)
            self.page_buffer = ''