import re

class Nondeterministic_Finite_State_Machine:
    def __init__(self, given_file):
        self.transitions = {}
        with open(given_file, 'r') as machine_description:
            for line in machine_description:
                split_line = re.split(r'[=:;\->\n]+', line)
                split_line = list(filter(None, split_line))
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
                    if not state in self.transitions.keys():
                        self.transitions[state] = {symbol: [new_state]}
                    elif not symbol in self.transitions[state].keys():
                        self.transitions[state][symbol] = [new_state]
                    else:
                        self.transitions[state][symbol].append(new_state)


    def return_possible_transition(self, symbol, current_state):
        try:
            possible_transitions = self.transitions[current_state][symbol]
            return possible_transitions
        except KeyError:
            return []

    def accepts(self, input_string, state="q0"):
        if len(input_string) == 0 and state in self.accept_states:
            return True
        possible_moves = {}
        consumed_symbol = input_string[:1]
        next_possible_states = self.return_possible_transition(consumed_symbol, state)
        if not next_possible_states:
            return False
        remaining_string = input_string[1:]
        for new_state in next_possible_states:
            possible_moves[new_state] = self.accepts(remaining_string, new_state)
        if True in possible_moves.values():
            correct_paths = [state for state, success in possible_moves.items() if success is True]
            for next_state in correct_paths:
                return self.accepts(remaining_string, next_state)
        return False
