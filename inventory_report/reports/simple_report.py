from collections import Counter


class SimpleReport:
    def _get_oldest_making_date(storage):
        return min(item['data_de_fabricacao'] for item in storage)

    def _get_closest_expiration_date(storage):
        return min(item['data_de_validade'] for item in storage)

    def _get_co_with_most_products(storage):
        product_list = (item['nome_da_empresa'] for item in storage)
        most_products = Counter(product_list).most_common(1)[0][0]
        return most_products

    @staticmethod
    def generate(inv):
        oldest_date = SimpleReport._get_oldest_making_date(inv)
        expiration_date = SimpleReport._get_closest_expiration_date(inv)
        most_products = SimpleReport._get_co_with_most_products(inv)

        return (
          f"Data de fabricação mais antiga: {oldest_date}\n"
          f"Data de validade mais próxima: {expiration_date}\n"
          f"Empresa com mais produtos: {most_products}"
        )
