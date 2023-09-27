import xml.etree.ElementTree as ET
class InfoManager:
    doc = None
    root = None
    def LoadInfo(self):
        #********** Begin *********#
        self.doc = ET.parse("step5/data.xml")
        self.root = self.doc.getroot()
        #********** End **********#
        
    def GetInfoCount(self):
        #********** Begin *********#
        return int(self.root.get("count"))
        #********** End **********#   
            
    def GetAge(self,name):
        #********** Begin *********#
        for i in self.root.findall('info'):
            if i.get('name') == name:
                return int(i.get("age"))
        #********** End **********#
        
    def GetDescription(self,name):
        #********** Begin *********#
        for i in self.root.findall('info'):
            if i.get('name') == name:
                return i.text
        #********** End **********#