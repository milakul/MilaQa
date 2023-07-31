import pytest
from modules.common.database import Database



@pytest.mark.database
def test_check_all_addresses():
    db = Database()
    users = db.get_all_addresses()

    print(users)


@pytest.mark.database
def test_check_wrong_user_ivan():
    db = Database()
    user = db.get_user_address_by_name('Ivan')

    assert user 


@pytest.mark.database
def test_check_user_stepan_wrong_address():
    db = Database()
    user = db.get_user_address_by_name('Stepan')

    assert user[0][0] == 'Stepana Bandery, 10'
    assert user[0][1] == 'Kyiv'


@pytest.mark.database
def test_check_all_products():
    db = Database()
    products = db.get_all_products()
    
    print(products)


@pytest.mark.database
def test_check_product_qnt_update_wrong_datatype():
    db = Database()
    db.update_product_qnt_by_id(3, З)
    milk_qnt = db.select_product_qnt_by_id(3)
    
    print(milk_qnt)
    

@pytest.mark.database
def test_check_product_by_id():
    db = Database()
    product = db.select_product_by_id(3)
   
    assert product[0][0] == 'молоко'
    assert product[0][1] == 'натуральне незбиране'



@pytest.mark.database
def test_check_product_by_wrong_id():
    db = Database()
    product = db.select_product_by_id(2)
   
    assert product[0][0] == 'молоко'
    assert product[0][1] == 'натуральне незбиране'



@pytest.mark.database
def test_product_insert_with_integr_error():
    db = Database()
    new_prod = db.insert_product(0.4, 'бублики', 'дивні', 12)
       
    assert new_prod 


@pytest.mark.database
def test_product_insert_without_required_data():
    db = Database()
    db.insert_product(5, 'кругобублик', 35)
    new_prod = db.select_product_by_id(5)

    assert new_prod

   
@pytest.mark.database
def test_product_insert_with_name_notdefined():
    db = Database()
    new_prod = db.insert_product(5, 'кругобублик', cvfxyt, 35)
   
    assert new_prod


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(5, 'кругобублик', 'смачний', 35)
    prod_5 = db.select_product_by_id(5)
    assert prod_5


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(7, 'кругло бублик', 'смачний', 60)
    prod_7 = db.select_product_by_id(7)
    assert prod_7


@pytest.mark.database
def test_update_product_id():
    db = Database()
    db.update_product_id_by_id(7, 6)
    products = db.get_all_products()

    print(products)


@pytest.mark.database
def test_product_delete_by_similiar_name():
    db = Database()
    db.insert_product(7, 'бублик', 'дивний', 21)
    db.delete_product_by_name('бублик')
    qnt = db.select_product_qnt_by_id(7)

    assert len(qnt) == 0


@pytest.mark.database
def test_check_product_by_name_except_some():
    db = Database()
    products = db.select_product_by_name('солодка вода')

    print(products)
   

