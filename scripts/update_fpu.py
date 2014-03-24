#!/usr/bin/env python
import os.path

divider = open(os.path.join("fpu", "divider", "divider.v")).read()
multiplier = open(os.path.join("fpu", "multiplier", "multiplier.v")).read()
adder = open(os.path.join("fpu", "adder", "adder.v")).read()
double_divider = open(os.path.join("fpu", "double_divider", "double_divider.v")).read()
double_multiplier = open(os.path.join("fpu", "double_multiplier", "double_multiplier.v")).read()
double_adder = open(os.path.join("fpu", "double_adder", "double_adder.v")).read()
int_to_float = open(os.path.join("fpu", "int_to_float", "int_to_float.v")).read()
float_to_int = open(os.path.join("fpu", "float_to_int", "float_to_int.v")).read()
int_to_double = open(os.path.join("fpu", "int_to_double", "int_to_double.v")).read()
double_to_int = open(os.path.join("fpu", "double_to_int", "double_to_int.v")).read()
output_file = open(os.path.join("chips", "compiler", "fpu.py"), "w")

output_file.write("divider = \"\"\"%s\"\"\"\n"%divider)
output_file.write("multiplier = \"\"\"%s\"\"\"\n"%multiplier)
output_file.write("adder = \"\"\"%s\"\"\"\n"%adder)
output_file.write("int_to_float = \"\"\"%s\"\"\"\n"%int_to_float)
output_file.write("float_to_int = \"\"\"%s\"\"\"\n"%float_to_int)
output_file.write("double_divider = \"\"\"%s\"\"\"\n"%double_divider)
output_file.write("double_multiplier = \"\"\"%s\"\"\"\n"%double_multiplier)
output_file.write("double_adder = \"\"\"%s\"\"\"\n"%double_adder)
output_file.write("int_to_double = \"\"\"%s\"\"\"\n"%int_to_double)
output_file.write("double_to_int = \"\"\"%s\"\"\"\n"%double_to_int)