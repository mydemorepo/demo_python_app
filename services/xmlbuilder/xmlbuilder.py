import xml.etree.ElementTree as ET


# Функція для перетворення данних ц форматі XML у читабельний 
# вид при використанні функції print(). Взято тут:
# https://ru.stackoverflow.com/questions/1064514/%D0%9A%D0%B0%D0%BA-
# %D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-xml-%D0%BD%D0%B0-python-
# %D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D1%8F-xml-etree-elementtree
def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


# Об'єкт класу MysqlDb використовується для 
# перетворення вхідних данних в XML формат.
class XmlBuilder():

# Функція приймає список параметрів, якщо параметр один,
# то це список словників якиї містить імена таблиць, 
# якщо параметрів більше, то перший параметр це список словників 
# який містить імена таблиць, другий - назва таблиці, 
# третій -то це список словників якиї містить дані з таблиці. 
  
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
            indent(root)          
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
