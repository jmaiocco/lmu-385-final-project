import sys
import re

def copy_input_to_file():
    filename = input("Please enter a file name ending in .txt: ")
    with open(filename, "w") as file:
        received_input = input("Please write a definition for a NFA, separating new lines with the | symbol: ")
        list_of_lines = received_input.split("|")
        for line in list_of_lines:
            file.write(line + "\n")
    return filename


def take_input_or_test_machine(command_line_arg_count):
    if command_line_arg_count == 1:
        copy_input_to_file()
    elif command_line_arg_count == 2:
        nfa = NondeterministicFiniteStateMachine()
        check_if_in_language(nfa)
    else:
        print("Please make sure you are using the correct number of command line arguments.")

def check_if_in_language(nfa):
    if nfa.accepts(sys.argv[1]):
        print("TRUE: That string is accepted by the given NFA.")
    else:
        print("FALSE: That string is NOT accepted by the given NFA.")

class NondeterministicFiniteStateMachine:
    def __init__(self):
        self.transitions = {}
        file = sys.stdin
        i = 0
        for line in file:
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
                if not state in self.transitions.keys():
                    self.transitions[state] = {symbol: [new_state]}
                elif not symbol in self.transitions[state].keys():
                    self.transitions[state][symbol] = [new_state]
                else:
                    self.transitions[state][symbol].append(new_state)
            i += 1
        print("START STATE IS " + self.start_state)
        print("SET OF ACCEPT STATES IS " + str(self.accept_states))
        print("TRANSITIONS ARE " + str(self.transitions))
        print("\nMACHINE CONSTRUCTED: TESTING INPUT STRING\n")

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
        symbol = input_string[:1]
        next_possible_states = self.return_possible_transition(symbol, state)
        if not next_possible_states:
            return False
        for new_state in next_possible_states:
            possible_moves[new_state] = self.accepts(input_string[1:], new_state)
        if True in possible_moves.values():
            correct_paths = [state for state, success in possible_moves.items() if success is True]
            for next_state in correct_paths:
                return self.accepts(input_string[1:], next_state)
        return False


take_input_or_test_machine(len(sys.argv))
