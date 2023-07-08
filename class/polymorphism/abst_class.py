from abc import ABC, abstractmethod


class Bank(ABC):
    def bank_info(self):
        print('Welcome!')

    @abstractmethod
    def interest(self):
        'Abstract'
        pass


class Access(Bank):
    def interest(self):
        'Interest'
        print('Interest is massive!')


s = Access()
s.bank_info()
s.interest()
