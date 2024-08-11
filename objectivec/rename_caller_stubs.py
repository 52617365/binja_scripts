from binaryninja import *

# This script gets all the functions inside the __objc_stubs section in the binary.

objc_stub_section = bv.get_section_by_name("__objc_stubs")

objc_stub_section_start = objc_stub_section.start
objc_stub_section_end = objc_stub_section.end

all_functions = bv.functions
functions_in_objc_stub_section = []

for f in all_functions:
    if f.start > objc_stub_section_start and f.start < objc_stub_section_end:
        functions_in_objc_stub_section.append(f)

for f in functions_in_objc_stub_section:
    insts = list(f.high_level_il.instructions)
    if len(insts) == 1:
        tokens = insts[0].tokens
        rename_function_name = f"objc_stub_caller_{tokens[6]}"
        f.name = rename_function_name

