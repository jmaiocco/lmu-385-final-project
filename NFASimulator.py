import sys
import re

    
class Nondeterministic_Finite_State_Machine:
    def __init__(self):
        self.transitions = {}
        given_file = ''.join(sys.argv[1])
        with open(given_file, 'r') as machine_description:
            i = 0
            for line in machine_description:
                split_line = re.split(r'[=:;\->\n]+', line)
                split_line = list(filter(None, split_line))
                print(split_line)
                if split_line[0].startswith('START'):
                    self.start_state = split_line[1]
                    if "," in split_line[3]:
                        self.accept_states = split_line[3].split(',')
                    else:
                        self.accept_states = split_line[3]
                if split_line[0].startswith('q'):
                    state = split_line[0]
                    if len(split_line) == 3:
                        symbol = split_line[1]
                        new_state = split_line[2]
                    else:     
                        symbol = "_"
                        new_state = split_line[1]
                    if not (state in self.transitions.keys()):
                    	self.transitions[state] = { symbol: [new_state] }
                    elif not (symbol in self.transitions[state].keys()):
                        self.transitions[state][symbol] = [new_state]
                    else:
                    	self.transitions[state][symbol].append(new_state) 
            i+=1
        print("START STATE IS " + self.start_state)
        print("SET OF ACCEPT STATES IS " + str(self.accept_states))
        print("TRANSITIONS ARE " + str(self.transitions))
        print("\nMACHINE CONSTRUCTED: TESTING INPUT STRING\n")

    def return_possible_transition(self, symbol, current_state):
        try: 
            possible_transitions = self.transitions[current_state][symbol]
            return possible_transitions
        except Exception as error:
        	return []

    def accepts(self, input_string, state="q0"):
        if( len(input_string) == 0 and state in self.accept_states ):
        	return True
        possible_moves = {}
        #print("Current state: " + state)
        #print("Checking string: " + input_string)
        symbol = input_string[:1]
        next_possible_states = self.return_possible_transition(symbol, state)
        #print(next_possible_states)
        if not next_possible_states:
            return False
        for new_state in next_possible_states:
            possible_moves[new_state] = self.accepts(input_string[1:], new_state)
       	#print(possible_moves)
        if True in possible_moves.values():
            correct_paths = [state for state,success in possible_moves.items() if success == True]
            for next_state in correct_paths:
                return self.accepts(input_string[1:], next_state)
        return False



c = Nondeterministic_Finite_State_Machine()
print(c.accepts(sys.argv[2]))
#print(c.accepts("a", c.start_state))		#TRUE
#print(c.accepts("aaaaa", c.start_state))	#TRUE
#print(c.accepts("b", c.start_state))		#FALSE
#print(c.accepts("_", c.start_state))		#TRUE
#print(c.accepts("__", c.start_state)) 		#FALSE
#print(c.accepts("aaaaaaaaaaaaaaa", c.start_state))	#TRUE
