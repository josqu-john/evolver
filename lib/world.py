import random

class World(object):
    def __init__(self, max_x, max_y, average_food_recovery, food_revovery_randomes):
        self.world_max_x = max_x
        self.world_max_y = max_y
        self.world_amount_cells = 0
        self.world_cells = {}
        self.world_average_food_recovery = average_food_recovery
        self.world_food_recovery_randomes = food_revovery_randomes


        list(self.world_cells)
        self.gen_world()

    def world_make_cell_name(self, x, y):
        cell_name = '%d/%d' % (x, y)
        return cell_name
    def world_make_cell_food_recovery_rate(self, average, y):
        a = random.uniform(0.1, y)
        x = average * a
        return x
    def world_make_cell(self, x, y, is_border):
        name = self.world_make_cell_name(x, y)
        food_recovery = self.world_make_cell_food_recovery_rate(self.world_average_food_recovery,self.world_food_recovery_randomes)

        self.world_cells[name] = Cell(name, x, y, is_border, food_recovery)
        print "create Cell: %s; border: %s; food_recovery: %s" % (name,is_border,food_recovery)

    def gen_world(self):
        wanted_cells = self.world_max_x * self.world_max_y
        i = 1
        actual_x = 0
        actual_y = 1
        is_border = None
        print "-Begin world gen-"
        while i < wanted_cells or i == wanted_cells:
            if actual_x == self.world_max_x: # Check if at End of x
                actual_x = 1
                actual_y += 1
                print ''
            else:
                actual_x += 1
            if actual_x == 1 or actual_y == 1 or actual_x == self.world_max_x or actual_y == self.world_max_y: # Check if it is Border
                is_border = True
            else: is_border = False

            i += 1
            self.world_make_cell(actual_x, actual_y, is_border)
        print "-Finish Cell gen-"

    def world_next_round(self, amount = 3):
        i = 0
        while i < amount:
            print " "
            print "World next Round"
            a = len(self.world_cells)
            x = 0
            while x < a:
                name = list(self.world_cells)[x]
                self.world_cells[name].cell_next_round()
                x += 1
            i += 1

class Cell(object):
    def __init__(self, name, x, y, is_border, food_recovery, food_storage = 1):
        self.name = name

        self.cell_pos_x = x
        self.cell_pos_y = y
        self.cell_is_border = is_border
        self.cell_is_used = False

        self.cell_food_storage = food_recovery
        self.cell_food_recovery =  food_storage
    def cell_next_round(self):
        print "Cell %s next round" % (self.name)
        self.cell_food_storage += self.cell_food_recovery
#w = World(3, 3, 3, 3)
#w.world_next_round()
