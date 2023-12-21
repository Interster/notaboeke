# Lees JSBsim XML lêers met python
# Gebruik die elementtree module:  Hier is die amptelike tutoriaal:
# https://docs.python.org/3/library/xml.etree.elementtree.html
#
# Gebruik hierdie tutoriaal die meeste:
# https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/


# %%
# importing element tree
# under the alias of ET
import xml.etree.ElementTree as ET

# Passing the path of the
# xml document to enable the
# parsing process
tree = ET.parse('mv.xml')

# getting the parent tag of
# the xml document
root = tree.getroot()

# printing the root (parent) tag
# of the xml document, along with
# its memory location
print(root)

# printing the attributes of the
# first tag from the parent 
print(root[0].attrib)

# printing the text contained within
# first subtag of the 5th tag from
# the parent
print(root[2][0].text)


# %%
import xml.etree.ElementTree as ET

# This is the parent (root) tag 
# onto which other tags would be
# created
data = ET.Element('chess')

# Adding a subtag named `Opening`
# inside our root tag
element1 = ET.SubElement(data, 'Opening')

# Adding subtags under the `Opening`
# subtag 
s_elem1 = ET.SubElement(element1, 'E4')
s_elem2 = ET.SubElement(element1, 'D4')

# Adding attributes to the tags under
# `items`
s_elem1.set('type', 'Accepted')
s_elem2.set('type', 'Declined')

# Adding text between the `E4` and `D5` 
# subtag
s_elem1.text = "King's Gambit Accepted"
s_elem2.text = "Queen's Gambit Declined"

# Converting the xml data to byte object,
# for allowing flushing data to file 
# stream
b_xml = ET.tostring(data)

# Opening a file under the name `items2.xml`,
# with operation mode `wb` (write + binary)
with open("skaak.xml", "wb") as f:
	f.write(b_xml)

# %%
b_xml = ET.tostring(root)

# Opening a file under the name `items2.xml`,
# with operation mode `wb` (write + binary)
with open("mvnuut.xml", "wb") as f:
	f.write(b_xml)
# %%
