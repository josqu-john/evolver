import random
class Animal(object):
    def __init__(self, spawn_x, spawn_y, max_world_x, max_world, border,
                 a_speed):
        self.pos_x = spawn_x
        self.pos_y = spawn_y
        self.max_world_x = max_world_x
        self.max_world_y = max_world_y
        self.pos_is_border = border
        self.food_storage = 1


        self.dna = {}
        self.dna['animal_speed'] = a_speed
        self.dna['food_consume'] = 1.0
        self.dna['possible_split'] = 3.0
    def move_x(self, amount):
        self.pos_x += amount
    def move_y(self, amount):
        self.pos_y += amount

    def should_mutate(self):
        mutation = random.randint(1, 1000)
        if mutation == 54:
            return True
        else:
            return False
    def give_random_dna(self):
        amount_dna = len(self.dna)
        which_dna = random.randint(0, amount_dna)
        dna_name = list(self.dna)[which_dna - 1]
        print dna_name
        return dna_name
    def random_mutation_value(self,):
        mutation_rate = 0
        while mutation_rate == 0:
            mutation_rate = random.randint(-1, +1)
        return mutation_rate


    def animal_give_dna(self, mutate = True):
        if mutate == False:
            return self.dna
        elif True:
            if self.should_mutate() == True:
                mutate_dna = self.dna
                broken_dna = self.give_random_dna()
                mutate_dna[broken_dna] += self.random_mutation_value()
                print "DNA MUTATION in: %s!" % (broken_dna)
                return mutate_dna
                global o
            else:
                return self.dna

    def animal_next_round_is_survive(self):
        survive = False
        self.food_storage -= self.food_consume
        if self.food_storage > 0:
            survive = True
        return survive
'''
    def animal_next_round_movement(self):
        direction = None
        world_min =
        possible_direction = {'up': True, 'down': True, 'left': True, 'right': True}
        if self.pos_x == self.max_world_x:
            print "Foo not finished yet sry"
'''
    def animal_give_pos_x(self):
        return self.pos_x
    def animal_give_pos_y(self):
        return self.pos_y
    def animal_give_is_border(self):
        return self.is_border
    def animal_set_is_border(self, boolean):
        self.pos_is_border = boolean
#o = False
#monkey = Animal(3, 3, 2, False)
#while o == False:
    #print monkey.animal_give_dna()
