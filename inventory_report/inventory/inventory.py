import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def file_reader(path):
        if path.endswith(".csv"):
            with open(path, "r") as file:
                return list(csv.DictReader(file))

        if path.endswith(".json"):
            with open(path, "r") as file:
                return json.load(file)

        if path.endswith(".xml"):
            with open(path, "r") as file:
                xml_file = xmltodict.parse(file.read())["dataset"]["record"]
                return xml_file

    @staticmethod
    def import_data(path, type):
        data = Inventory.file_reader(path)
        if type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
