
from html.parser import HTMLParser 


class LinkParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        
        
        if tag == 'a':                      # if anchor tag

            # search for href attribute and print its value
            for attr in attrs:
                if attr[0] == 'href' and attr[1][0:6] == 'mailto':
                    #what is it printing?
                    #check if @ is present in attr[1] or mailto: is present
                    print(attr[1][7:])
                    
                    

infile = open('links.html') 
content = infile.read() 
infile.close() 
myParser = LinkParser()
myParser.feed(content)
