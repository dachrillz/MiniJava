import sys
sys.path.insert(0, 'ply-3.11') #path to the lexer library

import lex as lex


#Define tokens
tokens = [
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'id',
   'EQUAL',
   'LBRACE',
   'RBRACE',
   'RBRACKET',
   'LBRACKET',
   'SEMI',
   'DOT',
   'BANG',
   'LESS',
   'GREATER'
]


reserved = {
    'if' : 'IF',
    'boolean' : 'BOOLEAN',
    'class' : 'CLASS',
    'else' : 'ELSE',
    'extends' : 'EXTENDS',
    'false' : 'FALSE',
    'true' : 'TRUE',
    'int' : 'INT',
    'main' : 'MAIN',
    'new' : 'NEW',
    'public' : 'PUBLIC',
    'return' : 'RETURN',
    'static' : 'STATIC',
    'String' : 'STRING',
    'this' : 'THIS',
    'void' : 'VOID',
    'while' : 'WHILE'
}


tokens += reserved.values()

#specify the tokens

#operators
t_PLUS = r'\+' #@TODO are these even part of the specification?
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_LESS = r'\<'
t_GREATER = r'\>'

#separators
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMI = r'\;'
t_DOT = r'\.'
t_BANG = r'\!'

def t_id(t):
    r'[a-zA-Z_][a-zA-z0-9_]*'
    t.type = reserved.get(t.value,'id') #check for reserved words
    return t


def t_NUMBER(t):
    r'\d+' 
    try:
        t.value = int(t.value) 
    except ValueError:
        print("Integer value too large %d", t.value) #handle overflow here
        t.value = 0 
    return t

#ignored characters
t_ignore = " \t"



def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)


lexer_instance = lex.lex()

if __name__ == '__main__':
    
    sample_program = """
    class Factorial {
        public static void main(String[] a){
            System.out.println(new Fac().ComputeFac(10));
        }
    }

    class Fac {
        public int ComputeFac(int num){
            in num_aux;
            if (num < 1)
                num_aux = 1;
            else
                num_aux = num * (this.ComputeFac(num-1));
            return num_aux;
        }
    }
    """


    while True:
        try:
            s = input('REPL > ')
        except EOFError:
            break
        if s == 'sample':
            s = sample_program
        lexer_instance.input(s) #feed data to the lexer
        while True:
            current_token = lexer_instance.token() #get next token in queue

            if not current_token:
                break   
            print(current_token)
