import pytest
from stores.models import Store
from cars.models import Car


@pytest.mark.django_db
def test_store_car_relationship():
    store = Store.objects.create(
        name="AutoCenter Guarulhos",
        address="Av. Tiradentes, 123",
        store_type="rental"
    )
    
    car1 = Car.objects.create(
        brand="Toyota",
        model="Corolla",
        year=2020,
        fipe_price=75000.00,
        market_price=78000.00
    )
    
    car2 = Car.objects.create(
        brand="Honda",
        model="Civic",
        year=2021,
        fipe_price=80000.00,
        market_price=82000.00
    )
    
    store.cars.add(car1, car2)
    
    assert store.cars.count() == 2
    assert car1 in store.cars.all()
    assert car2 in store.cars.all()
    