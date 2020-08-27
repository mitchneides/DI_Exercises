import random

# randomly selects 0 or 1 as value when instantiated
# can mutate to opposite of those two values
class Gene():

    def __init__(self):
        self.value = random.randint(0, 1)

    def mutate_self(self):
        if self.value == 1:
            self.new_value = 0
        elif self.value == 0:
            self.new_value = 1
        self.value = self.new_value
        return self.value

# instantiates 10 (random) genes and stores in a list
# can mutate to produce a new random list of genes
class Chromosome():

    def __init__(self):
        self.string = []
        for x in range (10):
            x = Gene()
            self.string.append(x.value)

        self.genes_string = ("".join(str(i) for i in self.string))

    def mutate_self(self):
        mutated = Chromosome()
        self.string = mutated.string
        return self.string

# instantiates 10 (random) chromosomes each made of 10 random genes and stores in a list of lists
# can mutate to produce a new random list of chromosomes
class DNA():
    def __init__(self):
        self.sequence = []
        for x in range (10):
            x = Chromosome()
            self.sequence.append(x.string)

    def mutate_self(self):
        mutated = DNA()
        self.sequence = mutated.sequence
        return self.sequence

# takes a dna object and an environment (probability between 1 and 100) to instantiate an organism
# can check 'perfection' level by counting how many ones of of max 100 in dna structure
# can mutate self by replacing it's dna structure with a random new dna structure'
# can mutate until perfect (or until desired level of perfection) via a while loop
# that causes it to mutate (or not) each generation according to it's environment value'
# generations and mutations values tracked until final report displayed at end of potentially long process
class Organism ():
    def __init__(self, dna_object, environment):
        self.mutation_probability = environment
        self.dna_structure = dna_object.sequence

    def check_if_perfect(self):
        total_ones = 0
        for x in range(10):
            for y in range(10):
                if self.dna_structure[x][y] == 1:
                    total_ones += 1

        return total_ones

    def mutate_self(self):
        mutated_dna = DNA()
        self.dna_structure = mutated_dna.sequence
        return self.dna_structure

    def mutate_until_perfect(self):
        mutations = 0
        generations = 0
        while self.check_if_perfect() < 70:
            generations += 1
            if generations % 10000 == 0:
                print(str(generations) + " generation cycles completed. Required perfection level still not reached.")
            if random.randint(0, 100) <= self.mutation_probability:
                self.mutate_self()
                mutations += 1

        print("**********************************")
        print("ORGANISM EVOLUTION REPORT")
        print("Total Generations: " + str(generations))
        print("Total Mutations: " + str(mutations))
        print("Percentage Perfection: " + str(self.check_if_perfect()))
        print("**********************************")


# EXECUTIONS

# initiate and mutate a gene object
g1 = Gene()
print(g1.value)
g1.mutate_self()
print(g1.value)

# initiate and mutate a chromosome object
c1 = Chromosome()
print(c1.string)
c1.mutate_self()
print(c1.string)

# initiate and mutate a dna object
d1 = DNA()
print(d1.sequence)
d1.mutate_self()
print(d1.sequence)

# initiate 3 organisms with different probabilities of mutation
organism1 = Organism(d1, 100)
organism2 = Organism(d1, 75)
organism3 = Organism(d1, 50)

# each organism mutate until 70% perfection
# attempted trying to get 90% perfection and took nearly 500000 cycles to get one for the organism that mutates every generation
#     still no luck with 100%!
organism1.mutate_until_perfect()
organism2.mutate_until_perfect()
organism3.mutate_until_perfect()

