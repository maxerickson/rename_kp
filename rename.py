#! /bin/python3
import xml.etree.ElementTree as ElementTree

infile="highways.osm"
outfile="renamed.osm"
renames=open("renames.txt", "w")

tree=ElementTree.parse(infile)
osm=tree.getroot()
osm.set('generator', 'rename.py')
for child in osm:
    if child.tag in {"way"}:
        try:
            # round the height.
            t=child.findall("./tag[@k='name']")[0]
            n=t.get('v')
            newname=n.replace(' Kp',' Key Peninsula')
            renames.write(n+';'+newname+'\n')
            t.set('v', newname)
            # mark element as modified.
            child.set('action', 'modify')
        except: # should only be child ways of relations
            print(child.get('id'))
tree.write(outfile)