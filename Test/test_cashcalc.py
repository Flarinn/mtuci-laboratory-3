from main import CashCalculator
from main import Record

def test_get_today_cash_remained():
    cash = CashCalculator(500)
    cash.add_record(Record(1200, 'jjjjjjj'))
    cash.add_record(Record(200, 'ffff'))
    print(cash.get_today_cash_remained("rub"))
    res = cash.get_today_cash_remained("rub")
    assert res == "Денег нет, держись: твой долг - 900.0 Rub"