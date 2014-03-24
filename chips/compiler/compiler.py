#!/usr/bin/env python
"""A C to Verilog compiler"""

__author__ = "Jon Dawson"
__copyright__ = "Copyright (C) 2013, Jonathan P Dawson"
__version__ = "0.1"

import sys
import os

from chips.compiler.parser import Parser
from chips.compiler.exceptions import C2CHIPError
from chips.compiler.macro_expander import expand_macros
from chips.compiler.optimizer import cleanup_functions
from chips.compiler.optimizer import cleanup_registers
from chips.compiler.tokens import Tokens
from chips.compiler.verilog_area import generate_CHIP as generate_CHIP_area
import fpu

def generate_library():
    output_file = open("chips_lib.v", "w")
    output_file.write(fpu.adder)
    output_file.write(fpu.divider)
    output_file.write(fpu.multiplier)
    output_file.write(fpu.int_to_float)
    output_file.write(fpu.float_to_int)
    output_file.close()

def comp(input_file, options=[]):

    reuse = "no_reuse" not in options
    initialize_memory = "no_initialize_memory" not in options
    generate_library()

    try:
            #Optimize for area
            parser = Parser(input_file, reuse, initialize_memory)
            process = parser.parse_process()
            name = process.main.name
            instructions = process.generate()
            if "dump_raw" in options:
                for i in instructions:
                    print i
            instructions = expand_macros(instructions, parser.allocator)
            instructions = cleanup_functions(instructions)
            instructions, registers = cleanup_registers(instructions, parser.allocator.all_registers)
            if "dump_optimised" in options:
                for i in instructions:
                    print i
            output_file = name + ".v"
            output_file = open(output_file, "w")
            inputs, outputs = generate_CHIP_area(
                    input_file,
                    name,
                    instructions,
                    output_file,
                    registers,
                    parser.allocator,
                    initialize_memory)
            output_file.close()

    except C2CHIPError as err:
        print "Error in file:", err.filename, "at line:", err.lineno
        print err.message
        sys.exit(-1)


    return name, inputs, outputs, ""