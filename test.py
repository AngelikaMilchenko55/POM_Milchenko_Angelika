class InsufficientAmount(Exception):
    pass
class Wallet:
    def __init__(self, balance=0):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def add_cash(self, amount):
        self.__balance = self.__balance + amount
        print("Баланс карты: ", self.__balance)

    def spend_cash(self, spend_sum):
        if spend_sum < self.__balance:
            self.__balance = self.__balance - spend_sum
            print("Баланс карты: ",  self.__balance)
        else:
            raise InsufficientAmount("Недостаточно средств на счету.")
import pytest

@pytest.fixture()
def empty_wallet():
    return Wallet()
@pytest.fixture()
def wallet():
    return Wallet(100)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.get_balance() == 0

def test_setting_initial_amount(wallet):
    assert wallet.get_balance() == 100

def test_wallet_add_cash(wallet):
    wallet.add_cash(90)
    assert wallet.get_balance() == 190

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(90)
    assert wallet.get_balance() == 10

def test_wallet_spend_except(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(90)

@pytest.mark.parametrize("earned,spend,expected",[
    (30,10,20),
    (20,2,18),
])
def test_transactions(earned,spend,expected,empty_wallet):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spend)
    assert empty_wallet.get_balance() == expected


