from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def _get_stored_products(inv):
        product_list = (item["nome_da_empresa"] for item in inv)
        qty_list = Counter(product_list).most_common()

        stock_list = ""
        for co, counter in qty_list:
            stock_list += f"- {co}: {counter}\n"
        return stock_list

    @staticmethod
    def generate(inv):
        co_inventory_products = CompleteReport._get_stored_products(inv)

        return (
          f"{SimpleReport.generate(inv)}\n"
          "Produtos estocados por empresa:\n"
          f"{co_inventory_products}"
        )
