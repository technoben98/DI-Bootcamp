# Exercise 1

# # Base class Temperature
# class Temperature:
#     def __init__(self, value):
#         self.value = value

#     def convert(self, temperature_type):
#         raise NotImplementedError("Subclasses must implement convert() method")


# # Subclass Celsius
# class Celsius(Temperature):
#     def convert(self, temperature_type):
#         if temperature_type == "Kelvin":
#             return Kelvin(self.value + 273.15)
#         elif temperature_type == "Fahrenheit":
#             return Fahrenheit((self.value * 9/5) + 32)
#         else:
#             raise ValueError("Invalid temperature type")


# # Subclass Kelvin
# class Kelvin(Temperature):
#     def convert(self, temperature_type):
#         if temperature_type == "Celsius":
#             return Celsius(self.value - 273.15)
#         elif temperature_type == "Fahrenheit":
#             return Fahrenheit((self.value - 273.15) * 9/5 + 32)
#         else:
#             raise ValueError("Invalid temperature type")


# # Subclass Fahrenheit
# class Fahrenheit(Temperature):
#     def convert(self, temperature_type):
#         if temperature_type == "Celsius":
#             return Celsius((self.value - 32) * 5/9)
#         elif temperature_type == "Kelvin":
#             return Kelvin((self.value - 32) * 5/9 + 273.15)
#         else:
#             raise ValueError("Invalid temperature type")


# # Test
# celsius = Celsius(20)
# kelvin = celsius.convert("Kelvin")
# fahrenheit = celsius.convert("Fahrenheit")

# print(kelvin.value)
# print(fahrenheit.value)


# Exercise 2
import random
class QuantumParticle: 
    def __init__(self, x=None, p=None): 
        self.position = x if x is not None else self.generate_random_position() 
        self.momentum = p if p is not None else self.generate_random_momentum() 
        self.spin = self.generate_random_spin()

    def generate_random_position(self):
        return random.randint(1, 10000)

    def generate_random_momentum(self):
        return random.uniform(0, 1)

    def generate_random_spin(self):
        return random.choice([0.5, -0.5])

    def disturbance(self):
        self.position = self.generate_random_position()
        self.momentum = self.generate_random_momentum()
        print('Quantum Interferences!!')

    def entangle(self, other_particle):
        if isinstance(other_particle, QuantumParticle):
            self.spin = -self.spin
            print('Spooky Action at a Distance !!')
        else:
            raise ValueError('Can only entangle with another QuantumParticle')

    def __repr__(self):
        return f'QuantumParticle(x={self.position}, p={self.momentum}, spin={self.spin})'
    
p1 = QuantumParticle(x=1,p=5.0)
p2 = QuantumParticle(x=2,p=5.0)
p1.entangle(p2)

p1 = QuantumParticle()
p2 = QuantumParticle()
p1.entangle(p2)