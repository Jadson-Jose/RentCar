import pytest
from cars.models import Car


@pytest.mark.django_db
def test_create_car():
    car = Car.objects.create(
        brand = "Toyota",
        model = "Corolla",
        year =  2020,
        fipe_price = 75000.00,
        market_price = 78000.00
    )
    assert car.brand == "Toyota"
    assert car.year == 2020
    