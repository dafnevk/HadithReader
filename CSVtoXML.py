from lxml import etree
import os
import pandas as pd

csv_dir = 'csv_output'
xml_dir = 'xml_output'

for fn in os.listdir(csv_dir):
    print(fn)
    data = pd.read_csv(os.path.join(csv_dir, fn), encoding='utf-8')
    root = etree.Element('root')
    for i, row in data.iterrows():
        hadith_el = etree.Element('hadith')
        for att in row.keys():
            el = etree.Element(att)
            el.text = str(row[att])
            hadith_el.append(el)
        root.append(hadith_el)
    with open(os.path.join(xml_dir, fn.replace('csv', 'xml')), 'wb') as o:
        o.write(etree.tostring(root, encoding='utf-8', xml_declaration=True))
