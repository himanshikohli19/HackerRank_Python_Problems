#XML2-Find the Maximum Depth
#You are given a valid XML document, and you have to
#print the maximum level of nesting in it. Take the depth of the root as 0.
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1
        
    for i in elem:
        depth(i, level + 1)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
