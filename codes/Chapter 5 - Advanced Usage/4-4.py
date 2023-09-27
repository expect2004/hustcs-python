import xml.sax
class Handler(xml.sax.ContentHandler):
    #********** Begin *********#
    ElementId = ''
    def startDocument(self):
        None
    def endDocument(self):
        None
    def startElement(self,name,attrs):
        self.ElementId = name
    def endElement(self,name):
        self.ElementId = ''
    def characters(self,content):
        if self.ElementId == 'info':
            print(content)
    #********** End **********#            

def GetHandler():
    return Handler()