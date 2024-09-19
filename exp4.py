class Agent:
    def __init__(self):
        self.wumpus_world = [['', '', 'p', ''], 
                             ['', '', '', ''], 
                             ['w', '', '', ''], 
                             ['', '', '', '']]
        self.cur_loc = [1, 1]
        self.is_alive = True
        self.has_exited = False
    
    def find_indices_for_location(self, loc):
        x, y = loc
        i, j = y-1, x-1
        return i, j

    def check_for_pit_wumpus(self):
        ww = self.wumpus_world
        i, j = self.find_indices_for_location(self.cur_loc)
        if 'p' in ww[i][j] or 'w' in ww[i][j]:
            print(ww[i][j])
            self.is_alive = False
            print("Agent is DEAD")
        return self.is_alive

    def take_action(self, action):
        valid_actions = ('Up', 'Down', 'Left', 'Right')
        assert action in valid_actions, "Invalid Action!"
        
        if not self.is_alive:
            print(f'Exited the world: {self.cur_loc}')
            return False
        
        index = valid_actions.index(action)
        valid_moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        move = valid_moves[index]
        new_loc = []
        
        for u, v in zip(self.cur_loc, move):
            z = u + v
            z = u if z < 1 else z
            new_loc.append(z)
        
        self.cur_loc = new_loc
        print(f"Action Taken: {action}, current location: {self.cur_loc}")
        
        if self.cur_loc == [4, 4]:
            self.has_exited = True
        return self.check_for_pit_wumpus()

    def find_adjacent_rooms(self):
        c_loc = self.cur_loc
        valid_moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        adj_rooms = []
        
        for rm in valid_moves:
            room = []
            valid = True
            for v, inc in zip(c_loc, rm):
                z = v + inc
                if z < 1 or z > 4:
                    valid = False
                    break
                else:
                    room.append(z)
            if valid:
                adj_rooms.append(room)
        return adj_rooms

    def perceive_current_location(self):
        breeze, stench = False, False
        ww = self.wumpus_world
        
        if not self.is_alive:
            print(f"Agent Cannot Perceive: Agent is dead. Location: {self.cur_loc}")
            return (None, None)
        
        if self.has_exited:
            print("Agent Cannot Perceive: Agent has exited the Wumpus world.")
            return (None, None)
        
        adj_rooms = self.find_adjacent_rooms()
        for room in adj_rooms:
            i, j = self.find_indices_for_location(room)
            if 'p' in ww[i][j]:
                breeze = True
            if 'w' in ww[i][j]:
                stench = True
        
        return (breeze, stench)

    def find_current_location(self):
        return self.cur_loc

def main():
    ag = Agent()
    print("Percept (Breeze, Stench):", ag.perceive_current_location())
    ag.take_action('Right')
    print("Percept (Breeze, Stench):", ag.perceive_current_location())
    ag.take_action('Right')
    print("Percept (Breeze, Stench):", ag.perceive_current_location())
    ag.take_action('Up')
    print("Percept (Breeze, Stench):", ag.perceive_current_location())
    ag.take_action('Up')
    print("Percept (Breeze, Stench):", ag.perceive_current_location())
    ag.take_action('Up')
    print("Percept (Breeze, Stench):", ag.perceive_current_location())

if __name__ == "__main__":
    main()
