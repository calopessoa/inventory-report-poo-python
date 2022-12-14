import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        else:
            with open(path, "r") as file:
                xml_file = xmltodict.parse(file.read())["dataset"]["record"]
                return xml_file
