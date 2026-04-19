from decimal import Decimal

class PulHisob:
    def __init__(self, pul):
        self.pul = Decimal(str(pul))

    def katta_qism(self):
        return self.pul.quantize(Decimal('1'))

    def kichik_qism(self):
        return self.pul - self.katta_qism()

    def pulni_top(self):
        return self.pul

    def pulni_qisqartir(self):
        return f"{self.katta_qism()} {self.kichik_qism()}"

# Misol
pul = PulHisob(123.456)
print(pul.pulni_top())  # 123.456
print(pul.katta_qism())  # 123
print(pul.kichik_qism())  # 0.456
print(pul.pulni_qisqartir())  # 123.456
