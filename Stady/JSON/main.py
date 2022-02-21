import xmltodict, json
from dicttoxml import dicttoxml
from xml.dom import minidom
my_json_string = """{
   "article": [
      {
         "id":"01",
         "language": "JSON",
         "edition": "first",
         "author": "Derrick Mwiti"
      },
      {
         "id":"02",
         "language": "Python",
         "edition": "second",
         "author": "Derrick Mwiti"
      }
   ],
   "blog":[
   {
       "name": "Datacamp",
       "URL":"datacamp.com"
   }
   ]
}
"""
with open('test_file.json', 'w') as file:
    json.dump(my_json_string, file)


with open('test_file.json', 'r') as j:
    json_data = json.load(j)
    print(json_data)
    print(type(json_data))


for item in json.loads(json_data):
    pass
    #print(item)

test = json.loads(json_data)['article'][0]['id']

_opt_1 = {
    'min_speed': 0,
    'max_speed': 0,
    'min_volume': 0,
    'max_volume': 0,
    'time_replay': 0,
    'X': 0,
    'Y': 0,
    'offset_screen': 0,
    'height': 0,
    'h1': 0,
    's1': 0,
    'v1': 0,
    'h2': 0,
    's2': 0,
    'v2': 0,
    'rgb1': 0,
    'rgb2': 0,
    'rgb3': 0,
    'mb_h1': 0,
    'mb_s1': 0,
    'mb_v1': 0,
    'mb_h2': 0,
    'mb_s2': 0,
    'mb_v2': 0, }


r = json.dumps(_opt_1)
print(type(r))
with open('test_file_.json', 'w') as file:
    json.dump(r , file)

loaded_r = json.loads(r)

print(type(loaded_r))
with open('test_file_.json', 'r') as j:
    json_data = json.load(j)
    print(json_data)

#print(json.loads(json_data)['min_speed'])
#print(dicttoxml(json.loads(json_data)))

def prettify(elem):
    reparsed = minidom.parseString(elem)
    return reparsed.toprettyxml(indent="  ")

#создаём новый файл XML с результатами
myfile = open("items2.xml", "w")
myfile.write(prettify(dicttoxml(json.loads(json_data))))
myfile = open("items2.xml", "r")

o = xmltodict.parse(myfile.read())
json = json.dumps(o)
print(json)