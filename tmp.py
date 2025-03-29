from kasm_compiler.syntaxes.args import Literal
from coloredlogs import install

install(level='DEBUG')  
lit = Literal()
lit.initialize("0x1A")
print(lit)  