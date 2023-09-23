import random

class Gene:
    def __init__(self):
        self.value = random.randint(0, 1)

    def flip(self):
        self.value = 1 - self.value


class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def flip(self):
        for gene in self.genes:
            if random.random() < 0.5:
                gene.flip()

class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def flip(self):
        for chromosome in self.chromosomes:
            chromosome.flip()


class Organism:
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment

    def mutate(self):
        if random.random() < self.environment:
            self.dna.flip()


def simulate():
    generation = 0
    dna = DNA()
    organisms = [Organism(dna, 0.1) for _ in range(100)]

    while True:
        generation += 1

        for organism in organisms:
            organism.mutate()

            # Check if DNA has all 1s
            all_ones = all(
                gene.value == 1 for chromosome in organism.dna.chromosomes for gene in chromosome.genes
            )
            if all_ones:
                return generation

print(simulate())