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
                    self.accept_states = split_line[3].split(',')
                if split_line[0].startswith('q'):
                    state = split_line[0]
                    if len(split_line) == 3:
                        symbol = split_line[1]
                        new_state = split_line[2]
                    else:     
                        symbol = ""
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
        print("\nMACHINE CONSTRUCTED: TESTING INPUT STRING")

    def return_possible_transition(self, symbol, current_state):
        return self.transitions[current_state][symbol]

    def accepts(self, input_string, state="q0"):
        if( len(input_string) == 0 and state in self.accept_states ):
        	return True
        symbol = input_string[:1]
        next_possible_states = self.return_possible_transition(symbol, state)
        for new_state in next_possible_states:
        	if(c.accepts(input_string[1:], new_state)):
        		return True
        return False


c = Nondeterministic_Finite_State_Machine()
print(c.accepts("a", c.start_state))
print(c.accepts("", c.start_state))
