import xml.etree.ElementTree as ET



def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

class XmlBuilder():
    
    def get_xml(self, *args):
        if(len(args) == 1):
            root = ET.Element("data")
            tables = ET.Element("tables")
           
            for tables_list in args:
                for tabl in tables_list:
                    for key in tabl:
                        table = ET.Element('table')
                        table.text = f'{tabl[key]}'
                        tables.append(table)
             
            root.append(tables)          
            xml_str = ET.tostring(root, encoding='utf8', method='xml')
            return  xml_str   
        else:
            tables_list = args[0]
            table_name = args[1]
            table_content = args[2]
            
            root = ET.Element("data")
            tables = ET.Element("tables")
            content = ET.Element(args[1])           
            
            for tabl in tables_list:
                for key in tabl:
                    table = ET.Element(key)
                    table.text = f'{tabl[key]}'
                    tables.append(table)
                     
            for table_row in table_content:
                row_content = ET.Element(args[1][0:-1])
                for key in table_row:
                    cell = ET.Element(key)
                    cell.text = f'{table_row[key]}'
                    row_content.append(cell)
                content.append(row_content)
                
            root.append(tables)
            root.append(content) 
            
            indent(root)
                                    
            xml_str = ET.tostring(root, encoding='unicode', method='xml')
            return  xml_str
