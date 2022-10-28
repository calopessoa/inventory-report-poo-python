from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        'Borracha',
        'Papelaria Solar',
        '2021-07-04',
        '2029-02-09',
        'FR48',
        'Ao abrigo de luz solar'
    )
    assert type(product.id) == int
    assert product.id == 1
    assert product.nome_do_produto == 'Borracha'
    assert product.nome_da_empresa == 'Papelaria Solar'
    assert product.data_de_fabricacao == '2021-07-04'
    assert product.data_de_validade == '2029-02-09'
    assert product.numero_de_serie == 'FR48'
    assert product.instrucoes_de_armazenamento == 'Ao abrigo de luz solar'
