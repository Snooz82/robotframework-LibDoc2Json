import sys
import json
import os
from robot.libdoc import libdoc
from xml.dom import minidom


class libdoc2json:

    def __init__(self, inputxmlfilepath, outputjsonfilepath):

        self.inputxmlfilepath = inputxmlfilepath
        self.outputjsonfilepath = outputjsonfilepath

        self.libdocxml = None

        self.library_name = ''
        self.library_version = ''
        self.library_keywords = []

        self.library_as_dictionary = {}

        self.parse_xml_from_file()
        self.get_library_name()
        self.get_library_version()
        self.get_library_keywords()
        self.create_lib_dict_from_data()
        self.write_json_to_file()
        print(f'Successfully written {self.library_name} Library')
        print(f'Version: {self.library_version}')
        print(f'Number of Keywords: {len(self.library_keywords)}')

    def parse_xml_from_file(self):
        # parse an xml file by name
        self.libdocxml = minidom.parse(self.inputxmlfilepath)

    def get_library_name(self):
        keywordspec = self.libdocxml.getElementsByTagName('keywordspec')
        self.library_name = keywordspec[0].attributes['name'].value

    def get_library_version(self):
        version = self.libdocxml.getElementsByTagName('version')
        if version[0].firstChild:
            self.library_version = version[0].firstChild.data

    def get_library_keywords(self):
        array_of_kw = self.libdocxml.getElementsByTagName('kw')
        for i, kw in enumerate(array_of_kw):
            if i == (len(self.library_keywords)):
                self.library_keywords.append(dict())
            self.library_keywords[i]['name'] = kw.attributes['name'].value
            arguments = kw.getElementsByTagName('arg')
            self.library_keywords[i]['args'] = []
            if arguments:
                for arg in arguments:
                    self.library_keywords[i]['args'].\
                        append(arg.firstChild.data)
            doc = kw.getElementsByTagName('doc')[0].firstChild
            if doc:
                doc_text = doc.data
                self.library_keywords[i]['doc'] = doc_text
            else:
                self.library_keywords[i]['doc'] = ''

    def create_lib_dict_from_data(self):
        self.library_as_dictionary['name'] = self.library_name
        self.library_as_dictionary['version'] = self.library_version
        self.library_as_dictionary['keywords'] = self.library_keywords

    def write_json_to_file(self):
        with open(self.outputjsonfilepath, 'w') as outfile:
            json.dump(self.library_as_dictionary, outfile)


def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print(f'Usage: python -m libdoc2json <LIBRARY or *.robot or *.py> <Outputfile.json>!\n'
              f'Example: python -m libdoc2json SeleniumLibrary SeleniumLibrary4.0.json\n'
              f'\nArguments: {args}')
    else:
        libdoc(args[0], 'tml_file.xml')
        libdoc2json('tml_file.xml', args[1])
        os.remove('tml_file.xml')


if __name__ == "__main__":
    main()
