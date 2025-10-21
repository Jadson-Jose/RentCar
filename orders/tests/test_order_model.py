import pytest
from orders.models import Order
from users.models import User
from cars.models import Car
from datetime import date


@pytest.mark.django_db
def test_create_order():
    user = User.objects.create(
        name = "Jadson",
        email = "jadson@email.com",
        password = "pass123",
        types="client"
    )
    car = Car.objects.create(
        brand = "Toyota",
        model = "Corolla",
        year = 2020,
        fipe_price = 75000.00,
        market_price = 78000.00
    )
    order = Order.objects.create(
        user=user,
        car=car,
        order_type="rental",
        date=date.today()
    )
    assert order.user.name == "Jadson"
    assert order.car.model == "Corolla"
    assert order.order_type == "rental"