from html.parser import HTMLParser
class LinkParser(HTMLParser):
    '''HTML doc parser that prints values of
       href attributes in anchor start tags'''

    def handle_starttag(self, tag, attrs):
        'print value of href attribute if any'
        
        if tag == 'a':                      # if anchor tag

            # search for href attribute and print its value
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

infile = open('links.html')
content = infile.read()
infile.close()
linkparser = LinkParser()
linkparser.feed(content)

