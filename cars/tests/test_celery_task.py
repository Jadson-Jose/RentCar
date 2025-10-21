from cars.tasks import test_task

def test_test_task():
    result = test_task()
    assert result == "Celery está funcionando"
    