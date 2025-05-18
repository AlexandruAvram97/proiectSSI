class Livrare:
    def __init__(self, weight, distance, express=False):
        self.weight = weight
        self.distance = distance
        self.express = express

    def calculate(self):
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
