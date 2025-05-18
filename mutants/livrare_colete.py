
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


class Livrare:
    def xǁLivrareǁ__init____mutmut_orig(self, weight, distance, express=False):
        self.weight = weight
        self.distance = distance
        self.express = express
    def xǁLivrareǁ__init____mutmut_1(self, weight, distance, express=True):
        self.weight = weight
        self.distance = distance
        self.express = express
    def xǁLivrareǁ__init____mutmut_2(self, weight, distance, express=False):
        self.weight = None
        self.distance = distance
        self.express = express
    def xǁLivrareǁ__init____mutmut_3(self, weight, distance, express=False):
        self.weight = weight
        self.distance = None
        self.express = express
    def xǁLivrareǁ__init____mutmut_4(self, weight, distance, express=False):
        self.weight = weight
        self.distance = distance
        self.express = None

    xǁLivrareǁ__init____mutmut_mutants = {
    'xǁLivrareǁ__init____mutmut_1': xǁLivrareǁ__init____mutmut_1, 
        'xǁLivrareǁ__init____mutmut_2': xǁLivrareǁ__init____mutmut_2, 
        'xǁLivrareǁ__init____mutmut_3': xǁLivrareǁ__init____mutmut_3, 
        'xǁLivrareǁ__init____mutmut_4': xǁLivrareǁ__init____mutmut_4
    }

    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLivrareǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁLivrareǁ__init____mutmut_mutants"), *args, **kwargs)
        return result 

    __init__.__signature__ = _mutmut_signature(xǁLivrareǁ__init____mutmut_orig)
    xǁLivrareǁ__init____mutmut_orig.__name__ = 'xǁLivrareǁ__init__'



    def xǁLivrareǁcalculate__mutmut_orig(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_1(self):
        if self.weight <= 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_2(self):
        if self.weight < 1 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_3(self):
        if self.weight < 0 or self.distance <= 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_4(self):
        if self.weight < 0 or self.distance < 1:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_5(self):
        if self.weight < 0 and self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_6(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("XXGreutate și distanță trebuie să fie pozitive.XX")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_7(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight <= 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_8(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 2:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_9(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 11
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_10(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = None
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_11(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight < 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_12(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 6:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_13(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 21
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_14(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = None
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_15(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 51

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_16(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = None

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_17(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance <= 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_18(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 11:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_19(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 1
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_20(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = None
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_21(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance < 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_22(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 51:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_23(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 6
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_24(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = None
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_25(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 16

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_26(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = None

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_27(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost - distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_28(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = None

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_29(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total /= 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_30(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total = 1.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_31(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 2.25

        return round(total, 2)

    def xǁLivrareǁcalculate__mutmut_32(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(None, 2)

    def xǁLivrareǁcalculate__mutmut_33(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round(total, 3)

    def xǁLivrareǁcalculate__mutmut_34(self):
        if self.weight < 0 or self.distance < 0:
            raise ValueError("Greutate și distanță trebuie să fie pozitive.")

        # Tariful de bază în funcție de greutate
        if self.weight < 1:
            cost = 10
        elif self.weight <= 5:
            cost = 20
        else:
            cost = 50

        # Costul în funcție de distanță
        if self.distance < 10:
            distance_fee = 0
        elif self.distance <= 50:
            distance_fee = 5
        else:
            distance_fee = 15

        total = cost + distance_fee

        # Creștere 25% pentru livrare expresă
        if self.express:
            total *= 1.25

        return round( 2)

    xǁLivrareǁcalculate__mutmut_mutants = {
    'xǁLivrareǁcalculate__mutmut_1': xǁLivrareǁcalculate__mutmut_1, 
        'xǁLivrareǁcalculate__mutmut_2': xǁLivrareǁcalculate__mutmut_2, 
        'xǁLivrareǁcalculate__mutmut_3': xǁLivrareǁcalculate__mutmut_3, 
        'xǁLivrareǁcalculate__mutmut_4': xǁLivrareǁcalculate__mutmut_4, 
        'xǁLivrareǁcalculate__mutmut_5': xǁLivrareǁcalculate__mutmut_5, 
        'xǁLivrareǁcalculate__mutmut_6': xǁLivrareǁcalculate__mutmut_6, 
        'xǁLivrareǁcalculate__mutmut_7': xǁLivrareǁcalculate__mutmut_7, 
        'xǁLivrareǁcalculate__mutmut_8': xǁLivrareǁcalculate__mutmut_8, 
        'xǁLivrareǁcalculate__mutmut_9': xǁLivrareǁcalculate__mutmut_9, 
        'xǁLivrareǁcalculate__mutmut_10': xǁLivrareǁcalculate__mutmut_10, 
        'xǁLivrareǁcalculate__mutmut_11': xǁLivrareǁcalculate__mutmut_11, 
        'xǁLivrareǁcalculate__mutmut_12': xǁLivrareǁcalculate__mutmut_12, 
        'xǁLivrareǁcalculate__mutmut_13': xǁLivrareǁcalculate__mutmut_13, 
        'xǁLivrareǁcalculate__mutmut_14': xǁLivrareǁcalculate__mutmut_14, 
        'xǁLivrareǁcalculate__mutmut_15': xǁLivrareǁcalculate__mutmut_15, 
        'xǁLivrareǁcalculate__mutmut_16': xǁLivrareǁcalculate__mutmut_16, 
        'xǁLivrareǁcalculate__mutmut_17': xǁLivrareǁcalculate__mutmut_17, 
        'xǁLivrareǁcalculate__mutmut_18': xǁLivrareǁcalculate__mutmut_18, 
        'xǁLivrareǁcalculate__mutmut_19': xǁLivrareǁcalculate__mutmut_19, 
        'xǁLivrareǁcalculate__mutmut_20': xǁLivrareǁcalculate__mutmut_20, 
        'xǁLivrareǁcalculate__mutmut_21': xǁLivrareǁcalculate__mutmut_21, 
        'xǁLivrareǁcalculate__mutmut_22': xǁLivrareǁcalculate__mutmut_22, 
        'xǁLivrareǁcalculate__mutmut_23': xǁLivrareǁcalculate__mutmut_23, 
        'xǁLivrareǁcalculate__mutmut_24': xǁLivrareǁcalculate__mutmut_24, 
        'xǁLivrareǁcalculate__mutmut_25': xǁLivrareǁcalculate__mutmut_25, 
        'xǁLivrareǁcalculate__mutmut_26': xǁLivrareǁcalculate__mutmut_26, 
        'xǁLivrareǁcalculate__mutmut_27': xǁLivrareǁcalculate__mutmut_27, 
        'xǁLivrareǁcalculate__mutmut_28': xǁLivrareǁcalculate__mutmut_28, 
        'xǁLivrareǁcalculate__mutmut_29': xǁLivrareǁcalculate__mutmut_29, 
        'xǁLivrareǁcalculate__mutmut_30': xǁLivrareǁcalculate__mutmut_30, 
        'xǁLivrareǁcalculate__mutmut_31': xǁLivrareǁcalculate__mutmut_31, 
        'xǁLivrareǁcalculate__mutmut_32': xǁLivrareǁcalculate__mutmut_32, 
        'xǁLivrareǁcalculate__mutmut_33': xǁLivrareǁcalculate__mutmut_33, 
        'xǁLivrareǁcalculate__mutmut_34': xǁLivrareǁcalculate__mutmut_34
    }

    def calculate(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLivrareǁcalculate__mutmut_orig"), object.__getattribute__(self, "xǁLivrareǁcalculate__mutmut_mutants"), *args, **kwargs)
        return result 

    calculate.__signature__ = _mutmut_signature(xǁLivrareǁcalculate__mutmut_orig)
    xǁLivrareǁcalculate__mutmut_orig.__name__ = 'xǁLivrareǁcalculate'


