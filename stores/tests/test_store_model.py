import pytest
from stores.models import Store


@pytest.mark.django_db
def test_create_loja():
    store = Store.objects.create(
        name="AutoCenter Guarulhos",
        address="Av. Tiradentes, 123",
        store_type="rental"
    )
    assert store.name == "AutoCenter Guarulhos"
    assert store.store_type == "rental"
    