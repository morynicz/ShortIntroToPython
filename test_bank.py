import unittest

import bank


class BankTests(unittest.TestCase):
    def test_given_total_is_40_when_200_euro_deposited_on_account_total_is_increased_by_200(self):
        total = 40
        deposited = 200
        expected_total = 240

        new_total = bank.deposit(total, deposited)

        self.assertEqual(new_total, expected_total)

    def test_given_total_is_70_when_47_euro_deposited_on_account_total_is_increased_by_47(self):
        total = 70
        deposited = 47
        expected_total = 117

        new_total = bank.deposit(total, deposited)

        self.assertEqual(new_total, expected_total)

    def test_when_35_euro_withdrawn_from_account_total_is_decreased_by_35(self):
        total = 40
        withdrawn = 35
        expected_total = 5

        new_total = bank.withdraw(total, withdrawn)

        self.assertEqual(new_total, expected_total)

    def test_when_19_euro_withdrawn_from_account_total_is_decreased_by_19(self):
        total = 25
        withdrawn = 19
        expected_total = 6

        new_total = bank.withdraw(total, withdrawn)

        self.assertEqual(new_total, expected_total)

    def test_given_total_is_30_withdrawal_of_35_is_rejected(self):
        total = 30
        withdrawn = 35
        expected_total = 30

        new_total = bank.withdraw(total, withdrawn)

        self.assertEqual(new_total, expected_total)

    def test_total_30_euro_exchanged_to_usd_is_40(self):
        total_euro = 30
        euro = "EUR"
        usd = "USD"
        expected_total_usd = 40
        new_total_usd = bank.exchange(total_euro, euro, usd)

        self.assertEqual(new_total_usd, expected_total_usd)

    def test_total_30_euro_exchanged_to_pln_is_120(self):
        total_euro = 30
        euro = "EUR"
        pln = "PLN"
        expected_total_usd = 40
        new_total_usd = bank.exchange(total_euro, euro, pln)

        self.assertEqual(new_total_usd, expected_total_usd)

    def test_transfer_30_euro_from_one_account_to_another_withdraws_from_first_account_and_deposits_to_second(self):
        first_total = 60
        second_total = 40
        transferred_amount = 30
        expected_first_total = 30
        expected_second_total = 70
        new_first_total, new_second_total = bank.transfer(first_total, second_total, transferred_amount)

        self.assertEqual((new_first_total, new_second_total), (expected_first_total, expected_second_total))

    def test_transfer_30_euro_from_account_that_has_only_25_available_to_another_is_rejected(self):
        first_total = 25
        second_total = 40
        transferred_amount = 30
        expected_first_total = 25
        expected_second_total = 40
        new_first_total, new_second_total = bank.transfer(first_total, second_total, transferred_amount)

        self.assertEqual((new_first_total, new_second_total), (expected_first_total, expected_second_total))

        # This is the moment where I finally think that class has to be introduced
        # test_account_totals_are_persisted_in_json(self):
        accounts = [("user1", 40), ("user2", 68)]


if __name__ == '__main__':
    unittest.main()
