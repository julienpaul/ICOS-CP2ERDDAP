# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


__author__ = ["Julien Paul"]
__credits__ = ""
__license__ = "CC BY-SA 4.0"
__version__ = "0.0.0"
__maintainer__ = "BCDC"
__email__ = ['julien.paul@uib.no','']

import xml.etree.ElementTree as ET
from pathlib import Path
import sys

# a voir
# https://recalll.co/ask/v/topic/python-How-to-output-CDATA-using-ElementTree/5a85893b1126f4033f8b4f82

#
# dessous a l air potable
#
#def _escape_cdata(text):
#    try:
#        if "&" in text:
#            text = text.replace("&", "&amp;")
#        # if "<" in text:
#            # text = text.replace("<", "&lt;")
#        # if ">" in text:
#            # text = text.replace(">", "&gt;")
#        return text
#    except TypeError:
#        raise TypeError(
#            "cannot serialize %r (type %s)" % (text, type(text).__name__)
#        )
#
#ET._escape_cdata = _escape_cdata

class CommentedTreeBuilder(ET.TreeBuilder):
    """
    parse comment too

    from ('name')https://stackoverflow.com/questions/33573807/faithfully-preserve-comments-in-parsed-xml/34324359#34324359
    """
    def comment(self, data):
        self.start(ET.Comment, {})
        self.data(data)
        self.end(ET.Comment)

def addDummyTag(i,o):
    """

    :param i:
    :param o:
    :return:
    """

def prettify(element, indent='  '):
    """
    re-indent xml file

    from https://stackoverflow.com/questions/749796/pretty-printing-xml-in-python
    """
    queue = [(0, element)]  # (level, element)
    while queue:
        level, element = queue.pop(0)
        children = [(level + 1, child) for child in list(element)]
        if children:
            element.text = '\n' + indent * (level+1)  # for child open
        if queue:
            element.tail = '\n' + indent * queue[0][0]  # for sibling open
        else:
            element.tail = '\n' + indent * (level-1)  # for parent close
        queue[0:0] = children  # prepend so children come before siblings

class CamelCase:
    def formatted(self, word, sep=' '):
        if isinstance(word, list):
            words = word
        else:
            words = word.split(sep=sep)

        s = "".join(word[0].upper() + word[1:].lower() for word in words)
        return s[0].lower() + s[1:]

    def datasetID(self,dict):
        fname = dict['name'].value[:dict['name'].value.rfind(".")]
        newDatasetId = 'icos'+self.formatted(fname, sep='_')
        return 'icos'+self.formatted(fname, sep='_')

cc = CamelCase()
#words = ["Hello", "World", "Python", "Programming"]
#print(cc.formatted(words))
#words='toto_25_tutu'
#print(cc.formatted(words, sep='_'))
#print(cc.formatted(words))

def renameDatasetId(i, newDatasetId):
    """
    search for and replace datasetId name.

    :param i: file to search/replace in
    :param newDatasetId: datasetId name to be put in
    :return: overwrite input file
    """
    import re

    content = i.read_text()
    regex = '(^<dataset .* datasetID=")(.*)(" .*>$)'
    i.write_text(re.sub(regex, r'\1' + newDatasetId + r'\3', content, flags=re.M))

def replaceHeader(i, f):
    """
    search for and replace datasetId name.

    :param i: file to search/replace in
    :param newDatasetId: datasetId name to be put in
    :return: overwrite input file
    """
    import re

    newHeader = f.read_text()
    content = i.read_text()
    regex = '(^<erddapDatasets>$)'
    i.write_text(re.sub(regex, newHeader, content, flags=re.M))

def truc(dic,key,uri):
    dict1 = {}
    if key in dic:
        if uri in dic[key]:
            print('\nexplore dic[',key,'][',uri,'] \n')
            for k, v in dic[key][uri].items():
                if v.type != 'uri':
                    print('attr name:', k, ' value:', v.value)
                    dict1[k]=v.value
                else:
                    print('dic[',k,'][',v.value,'] \n')
                    dict2 = truc(dic,k,v.value)
                    # Merge contents of dict2 in dict1
                    dict1.update(dict2)
        else:
            print('\ncan not found dic[',key,'][',uri,'] \n')
    else:
        print('\ncan not found dic[', key, '] \n')

    return dict1


def changeAttr(i,o,m):
    """
    d: str
       input directory
    i: str
       input filename
    m: Attribute's instance
       global and variable attribute to be added
    o: str
        output filename

    """
    text = """
    <?xml version='1.0' encoding='utf-8'?>
    <text>
    This is just some sample text.
    </text>
    """

    text = """
    <?xml version='1.0' encoding='utf-8'?>
    <text>
    This is just some sample text.
    </text>
    """

    print('\n------------------\n')


    # parse comment too
    parser = ET.XMLParser(target=CommentedTreeBuilder())

    print('tree : ',i)

    tree =  ET.parse(i, parser)
    root =  tree.getroot()

    varval='var2'
    varnam='variable'
    gloval='title8'
    glonam='title'
    print('root :',root.tag, root.attrib)
    # node = context.find('dataset')
    print('\nmeta:=================================\n')

    #gloatt = {}
    #for k in m['dataObj'].keys():
    #    fname = m['dataObj'][k]['name'].value[:m['dataObj'][k]['name'].value.rfind(".")]
    #    newDatasetId = 'icos'+cc.formatted(fname, sep='_')
    #    gloatt[newDatasetId] = truc(m,'dataObj',k)
    #    #gloatt[k] = truc(m,'dataObj',k)
    gloatt = {}
    gloatt['title']='toto'
    gloatt['summay']='tutu'

    print('gloatt\n',gloatt)

    print('\n---------------')
    #for node in list(root):
    #   if node is not None:
    for node in root.findall('dataset'):
        print('node :', node.tag, node.attrib)
        if 'datasetID' in node.attrib:
            for attrNode in node.findall('addAttributes'):
                print('attrNode :', attrNode.tag, attrNode.attrib)
                for att in attrNode.iter('att'):
                    print('att name:', att.get('name'), 'val:', att.text)
                    # if att.get('name') in gloatt[dsID]:
                    if att.get('name') in gloatt:
                        attrNode.remove(att)
                # for k,v in gloatt[dsID].items():
                for k, v in gloatt.items():
                    ET.SubElement(attrNode, 'att', name=k).text = str(v)
            dsID = node.attrib.get('datasetID')
            if dsID in gloatt:
                print('dsID:',dsID)
                for attrNode in node.findall('addAttributes'):
                    print('attrNode :', attrNode.tag, attrNode.attrib)
                    for att in attrNode.iter('att'):
                        print('att name:',att.get('name'),'val:',att.text)
                        #if att.get('name') in gloatt[dsID]:
                        if att.get('name') in gloatt:
                            attrNode.remove(att)
                    #for k,v in gloatt[dsID].items():
                    for k, v in gloatt.items():
                        ET.SubElement(attrNode, 'att', name=k).text = str(v)

        #    for varNode in node.iter('dataVariable'):
        #        for attrNode in varNode.findall('addAttributes'):
        #            print('attrNode :', attrNode.tag, attrNode.attrib)
        #            for att in attrNode.iter('att'):
        #                if att.get('name') == varnam:
        #                    attrNode.remove(att)
        #            ET.SubElement(attrNode, 'att', name=varnam, type='string').text = str(varval)


    # write xml output
    prettify(root)
    tree.write(i) #, encoding="ISO-8859-1", xml_declaration=True)
    #tree.write(o, encoding="UTF-8", xml_declaration=True)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #d = Path('/home/jpa029/Data/ICOS2ERDDAP/dataset/58GS20190711_SOCAT_enhanced')
    #i = d / 'dataset.58GS20190711_SOCAT_enhanced.xml'
    #renameDatasetId(i, 'toto')


    #d='/home/jpa029/PycharmProjects/ICOS2ERDDAP/data'
    d = Path('/home/jpa029/Data/ICOS2ERDDAP/dataset')
    i = d / 'datasets.xml'
    o = d / 'datasets.new.xml'
    m = {}
    changeAttr(i,o,m)






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
