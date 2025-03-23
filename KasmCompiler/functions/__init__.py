from KasmCompiler.functions.LoadL import LoadL
from KasmCompiler.functions.Load import Load
from KasmCompiler.functions.Store import Store
from KasmCompiler.functions.Jump import Jump
from KasmCompiler.functions.NoOp import NoOp
from KasmCompiler.functions.Halt import Halt
from KasmCompiler.functions.In import In
from KasmCompiler.functions.Out import Out

functions = {
    "LoadL": LoadL(),
    "Load": Load(),
    "Store": Store(),
    "Jump": Jump(),
    "NoOp": NoOp(),
    "Halt": Halt(),
    "In": In(),
    "Out": Out(),
}

__all__ = ["functions, LoadL", "Load", "Store", "NoOp", "Halt", "In", "Out"]