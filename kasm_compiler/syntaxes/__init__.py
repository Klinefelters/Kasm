'''

'''
from kasm_compiler.syntaxes.ops import *
from kasm_compiler.syntaxes.args import *

OPS = {}
for op in [
    NOP(), HALT(), LDR(), LDL(), LDH(), STR(),
    JMP(), BSGT(), BSEQ(), BSLT(), BGT(), BEQ(), BLT(),
    ADD(), SUB(), MUL(), DIV(), REM(), SLL(), SLR(), SAR(),
    AND(), NAND(), OR(), NOR(), XOR(), XNOR(), NMOV(), MOV(),
    In(), OUT(), OUTL(), OUTH()
]:
    OPS[op.name] = op