import pytest


@pytest.mark.run(order=2)
def test_order_1():
    print("Order_1")


@pytest.mark.run(order=1)
def test_order_2():
    print("Order_2")


@pytest.mark.run(order=5)
def test_order_3():
    print("Order_3")


@pytest.mark.run(order=4)
def test_order_4():
    print("Order_4")


@pytest.mark.run(order=3)
def test_order_5():
    print("Order_5")