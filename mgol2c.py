#!/usr/bin/env python3
import argparse
from scanners.dfa import load_dfa
from scanners.mgollexical import Lexical
from parsers .slr import SLR

# def read_mgol_code(file_name):
#     codeinlist = [[]]
#     with open(file_name,'r') as F:
#         code = F.read()
#         code = mgol_replaces(code)
#         return [line.split() for line in code.split('\n')]

def read_mgol_code(file_name):
    with open(file_name,'r') as F:
        code = F.read()
        return code

def t1():
    dfa = load_dfa(transitions_file="tables/tab_transitions.csv", accept_states_file="tables/tab_final_states.csv")
    lexical = Lexical(dfa=dfa, chain=mgol_code, symbols_table_file='tables/tab_symbols.csv')

    print("Lexemas")
    for lexeme in lexical.get_lexeme():
        print(lexeme)

def t2():
    dfa = load_dfa(transitions_file="tables/tab_transitions.csv", accept_states_file="tables/tab_final_states.csv")
    lexical = Lexical(dfa=dfa, chain=mgol_code, symbols_table_file='tables/tab_symbols.csv')

    #Passa o lexico como parametro
    syntactic = SLR(scanner=lexical)

    syntactic.run_slr()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Projeto de compilador que converte código em linguagem Mgol em arquivo objeto em C.")
    parser.add_argument("--source", type=str, help="the path to source file with Mgol code.")
    args = parser.parse_args()

    mgol_code = read_mgol_code(args.source)
    #Declara o $ pois ele faz parte da linguagem
    mgol_code += "$"
    
    t2()
    


