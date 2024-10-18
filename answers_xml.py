import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
costs = []

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Value':
                if child.firstChild.nodeType == 3:
                    number = child.firstChild.data
                    price = float(number.replace(",","."))
    costs.append(price)



print(sum(costs)/len(costs))


xml_file.close()