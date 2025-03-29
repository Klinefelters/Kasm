'''

'''
from kasm_compiler.syntaxes.ops import *
from kasm_compiler.syntaxes.args import *
from kasm_compiler.syntaxes.variables import *

OPS = {}
for op in [
    NOP(), HALT(), LDR(), LDRL(), LDRH(), LDL(), LDH(), STR(),
    JMP(), BSGT(), BSEQ(), BSLT(), BGT(), BEQ(), BLT(),
    ADD(), SUB(), MUL(), DIV(), REM(), SLL(), SLR(), SAR(),
    AND(), DEC(), OR(), INC(), XOR(), RST(), NMOV(), MOV(),
    In(), OUT(), OUTL(), OUTH(), PUSH(), POP()
]:
    OPS[op.name] = op

VARS = {}
for var in [
    Ascii(),
]:
    VARS[var.name] = var