import re


class DWRParser:
    REGEX_OBJ_DEF = re.compile(r'var (\w+)={};')
    REGEX_OBJ_ASSIGN = re.compile(r'(\w+).(\w+)=\"?(\w+)\"?;')

    def parse_object_names(self, content):
        """read response content, and parse objects"""
        names = []
        pattern = self.REGEX_OBJ_DEF
        m = pattern.search(content)
        while m:
            names.append(m.group(1))
            m = pattern.search(content, m.span()[1])
        return names

    def parse_objects(self, names, content):
        objects = { name: {} for name in names }
        pattern = self.REGEX_OBJ_ASSIGN
        m = pattern.search(content)
        while m:
            name, attr, val = m.groups()
            if name in objects:
                obj = objects[name]
                if val == 'null':
                    val = None
                elif str.isnumeric(val):
                    val = int(val)
                
                obj[attr] = val
            m = pattern.search(content, m.span()[1])

        return objects
