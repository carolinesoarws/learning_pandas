import xml.etree.ElementTree as et
import pandas as pd


# Reding the xml file
myxml_data = open("data.xml", "r").read()

# getting the data that i read and loading as xml
root_xml = et.XML(myxml_data)
data = []
cols = []

for i, child in enumerate(root_xml):
    data.append([subchild.text for subchild in child])
    cols.append(child.tag)

df = pd.DataFrame(data).T  # Write in DF and transpose it
df.columns = cols  # Update column names
print(df)