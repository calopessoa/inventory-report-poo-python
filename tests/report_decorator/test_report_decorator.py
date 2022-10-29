from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter


colored_report = (
    "\033[32mData de fabricação mais antiga:\033[0m"
    + " \033[36m2020-09-06\033[0m\n"
    "\033[32mData de validade mais próxima:\033[0m"
    + " \033[36m2023-09-17\033[0m\n"
    "\033[32mEmpresa com mais produtos:\033[0m"
    + " \033[31mTarget Corporation\033[0m"
)

file_path = "inventory_report/data/inventory.csv"
csv_file = CsvImporter.import_data(file_path)


def test_decorar_relatorio():
    simple_colored_report = ColoredReport(SimpleReport).generate(csv_file)
    for item, row in enumerate(simple_colored_report):
        assert row == colored_report[item]
