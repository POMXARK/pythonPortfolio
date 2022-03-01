# Pretty printing XML after parsing
# it from dictionary
from xml.dom.minidom import parseString
from xml.etree import ElementTree

from dicttoxml import dicttoxml

# Data to be parsed
data = {
                'min_speed': 5,
                'max_speed': 15,
                'min_volume': 1,
                'max_volume': 3.5,
                'replay_time': 10,
                'X': 100,
                'Y': 600,
                'offset': 160,
                'height': 410,
                'h1': 21,
                's1': 135,
                'v1': 120,
                'h2': 255,
                's2': 195,
                'v2': 255,
                'rgb1': 153,
                'rgb2': 126,
                'rgb3': 79,
                'mb_h1': 0,
                'mb_s1': 205,
                'mb_v1': 75,
                'mb_h2': 255,
                'mb_s2': 255,
                'mb_v2': 255, }

xml = dicttoxml(data)
dom = parseString(xml)

print(dom.toprettyxml())

xmlfile = open("options/corsairs_3.xml", "w")
xmlfile.write(dom.toprettyxml())
xmlfile.close()

tree = ElementTree.parse('options/corsairs_3.xml')
root = tree.getroot()
print(root[0])
for i in root:
    print(i.text)