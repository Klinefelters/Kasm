from attr import define
from logging import error

from kasm_compiler.syntaxes.args import *

@define
class Op():
    name: str = None
    line: int = 0

    def require_args(self, args, reqs) -> tuple:
        rtn = []
        for arg, req in zip(args, reqs):
            if not issubclass(arg.__class__, req):
                tmp = req()
                tmp.initialize(arg, self.line)
                rtn.append(tmp)
            else:
                rtn.append(arg)
        return rtn

    def assemble(self, args):
        raise NotImplementedError("This method should be implemented by subclasses.")


"""NOP/HALT OPERATIONS"""
@define
class NOP(Op):
    name: str  = "NOP"
    def assemble(self, args):
        return "0000000000000000"

@define
class HALT(Op):
    name: str  = "HALT"
    def assemble(self, args):
        return "1111111111111111" 
    

"""LOAD/STORE OPERATIONS"""
@define
class LDR(Op):
    name: str  = "LDR"

    def assemble(self, args):
        rd, ra = self.require_args(args, [Register, Register])
        return f"0100000{rd}{ra}000"
    
@define
class LDL(Op):
    name: str  = "LDL"

    def assemble(self, args):
        rd, imm = self.require_args(args, [Register, Literal])
        return f"01100{imm}{rd}"
    
@define
class LDH(Op):
    name: str  = "LDH"

    def assemble(self, args):
        rd, imm = self.require_args(args, [Register, Literal])
        return f"01101{imm}{rd}"
    
@define
class STR(Op):
    name: str  = "STR"

    def assemble(self, args):
        ra, rb = self.require_args(args, [Register, Register])
        return f"1000000000{ra}{rb}"
    
"""BRANCH OPERATIONS"""
@define
class JMP(Op):
    name: str  = "JMP"
    sel: str  = "111"

    def assemble(self, args):
        rd, ra, rb = self.require_args(args, [Register, Register, Register])
        return f"1010{self.sel}{rd}{ra}{rb}"
    
@define
class BSGT(JMP):
    name: str  = "BSGT"
    sel: str  = "000"

@define
class BSEQ(JMP):
    name: str  = "BSEQ"
    sel: str  = "001"
    
@define
class BSLT(JMP):
    name: str  = "BSLT"
    sel: str  = "010"

@define
class BGT(JMP):
    name: str  = "BGT"
    sel: str  = "011"

@define
class BEQ(JMP):
    name: str  = "BEQ"
    sel: str  = "100"
    
@define
class BLT(JMP):
    name: str  = "BLT"
    sel: str  = "101"

"""MATH OPERATIONS"""

@define
class RType(Op):
    name: str  = None
    func4: str  = "0000"

    def assemble(self, args):
        rd, ra, rb = self.require_args(args, [Register, Register, Register])
        return f"001{self.func4}{rd}{ra}{rb}"
    
@define
class ADD(RType):
    name: str  = "ADD"
    func4: str  = "0000"

@define
class SUB(RType):
    name: str  = "SUB"
    func4: str  = "0001"

@define
class MUL(RType):
    name: str  = "MUL"
    func4: str  = "0010"

@define
class DIV(RType):
    name: str  = "DIV"
    func4: str  = "0011"

@define
class REM(RType):
    name: str  = "REM"
    func4: str  = "0100"

@define
class SLL(RType):
    name: str  = "SLL"
    func4: str  = "0101"

@define
class SLR(RType):
    name: str  = "SLR"
    func4: str  = "0110"

@define
class SAR(RType):
    name: str  = "SAR"
    func4: str  = "0111"

@define
class AND(RType):
    name: str  = "AND"
    func4: str  = "1000"

@define
class NAND(RType):
    name: str  = "NAND"
    func4: str  = "1001"

@define
class OR(RType):
    name: str  = "OR"
    func4: str  = "1010"

@define
class NOR(RType):
    name: str  = "NOR"
    func4: str  = "1011"

@define
class XOR(RType):
    name: str  = "XOR"
    func4: str  = "1100"

@define
class XNOR(RType):
    name: str  = "XNOR"
    func4: str  = "1101"

@define
class NMOV(RType):
    name: str  = "NMOV"
    func4: str  = "1110"

@define
class MOV(RType):
    name: str  = "MOV"
    func4: str  = "1111"

"""INPUT/OUTPUT OPERATIONS"""

@define
class In(Op):
    name: str  = "IN"

    def assemble(self, args):
        rd, da = self.require_args(args, [Register, Device])
        return f"1100000{rd}{da}000"
    
@define
class OUT(Op):
    name: str  = "OUT"

    def assemble(self, args):
        ra, da = self.require_args(args, [Register, Device])
        return f"1100100000{ra}{da}"
    
@define
class OUTL(Op):
    name: str  = "OUTL"

    def assemble(self, args):
        da, imm = self.require_args(args, [Device, Literal])
        return f"11010{imm}{da}"
    
@define
class OUTH(Op):
    name: str  = "OUTH"

    def assemble(self, args):
        da, imm = self.require_args(args, [Device, Literal])
        return f"11011{imm}{da}"
