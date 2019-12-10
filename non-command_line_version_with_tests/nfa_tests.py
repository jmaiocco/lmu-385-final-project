import pytest

from nfa import Nondeterministic_Finite_State_Machine 

def test_file_0():
    nfa = Nondeterministic_Finite_State_Machine("testFile0.txt")
    assert nfa.accepts("") == False
    assert nfa.accepts("a") == True		
    assert nfa.accepts("aaaaa") == True	
    assert nfa.accepts("b")	== False	
    assert nfa.accepts("_")	== True	
    assert nfa.accepts("__") == False
    assert nfa.accepts("aaaaaaaaaaaaaaa") == True

def test_file_1():
	nfa = Nondeterministic_Finite_State_Machine("testFile1.txt")
	assert nfa.accepts("") == False
	assert nfa.accepts("_") == False
	assert nfa.accepts("aaaa") == False
	assert nfa.accepts("00110") == False
	assert nfa.accepts("001100") == True
	assert nfa.accepts("0011000") == False

def test_file_2():
	nfa = Nondeterministic_Finite_State_Machine("testFile2.txt")
	assert nfa.accepts("") == True
	assert nfa.accepts("0") == False
	assert nfa.accepts("00") == True
	assert nfa.accepts("1") == False
	assert nfa.accepts("11") == True
	assert nfa.accepts("01") == False
	assert nfa.accepts("1001") == True

def test_file_3():
	nfa = Nondeterministic_Finite_State_Machine("testFile3.txt")
	assert nfa.accepts("") == True
	assert nfa.accepts("_") == False
	assert nfa.accepts("0") == True
	assert nfa.accepts("1") == False
	assert nfa.accepts("10") == False
	assert nfa.accepts("11") == False
	assert nfa.accepts("100") == False
	assert nfa.accepts("101") == True
	assert nfa.accepts("0110") == False 
	assert nfa.accepts("1010") == True
	assert nfa.accepts("1001") == False
	assert nfa.accepts("11100001") == True 

def test_file_4():
	nfa = Nondeterministic_Finite_State_Machine("testFile4.txt")
	assert nfa.accepts("") == False
	assert nfa.accepts("_00") == True
	assert nfa.accepts("_11") == True
	assert nfa.accepts("_111") == False
	assert nfa.accepts("_0000") == False
	assert nfa.accepts("00") == False
	assert nfa.accepts("11") == False

def test_file_5():
	nfa = Nondeterministic_Finite_State_Machine("testFile5.txt")
	assert nfa.accepts("") == False
	assert nfa.accepts("_") == False
	assert nfa.accepts("___") == True
	assert nfa.accepts("_10") == True
	assert nfa.accepts("__0") == True
	assert nfa.accepts("_100") == True
	assert nfa.accepts("___0") == True
	assert nfa.accepts("____") == False
	assert nfa.accepts("_1_0") == True

def test_file_6():
	nfa = Nondeterministic_Finite_State_Machine("testFile6.txt")
	assert nfa.accepts("a") == True
	assert nfa.accepts("ab") == False
	assert nfa.accepts("abc") == True
	assert nfa.accepts("abcb") == False
	assert nfa.accepts("abcbc") == True
	assert nfa.accepts("") == False
	assert nfa.accepts("_") == False

def test_file_7():
	nfa = Nondeterministic_Finite_State_Machine("testFile7.txt")
	assert nfa.accepts("") == True
	assert nfa.accepts("_") == False
	assert nfa.accepts("0011") == True
	assert nfa.accepts("0011_0011") == True
	assert nfa.accepts("0011_0011_0011") == True
	assert nfa.accepts("0011_0011_0011_") == True
	assert nfa.accepts("001") == False
	assert nfa.accepts("0011_0") == False

def test_file_8():
	nfa = Nondeterministic_Finite_State_Machine('testFile8.txt')
	assert nfa.accepts("") == False
	assert nfa.accepts("_") == False
	assert nfa.accepts("0") == True
	assert nfa.accepts("1") == False
	assert nfa.accepts("000000000000") == True
	assert nfa.accepts("0000000000001") == False
	assert nfa.accepts("1000000000000") == False

def test_file_9():
	nfa = Nondeterministic_Finite_State_Machine("testFile9.txt")
	assert nfa.accepts("") == False
	assert nfa.accepts("_") == False
	assert nfa.accepts("0") == True
	assert nfa.accepts("1") == False
	assert nfa.accepts("000000000000") == True
	assert nfa.accepts("0000000000001") == False
	assert nfa.accepts("1000000000000") == False
