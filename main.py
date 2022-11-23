# import pyperclip
import os
import re
import sys
from typing import Generic, List, TypeVar, Union, cast

sys.path.append("./target/")
sys.path.append("./src/test/")
sys.path.append("./src/main/bkool/parser/")
sys.path.append("./src/main/bkool/utils/")
sys.path.append("./src/main/bkool/astgen/")
sys.path.append("./src/main/bkool/checker/")
sys.path.append("./src/main/bkool/codegen/")


from AdditionalTypes import *
from AST import *
from MyUtils import MyUtils  # type: ignore

if __name__ == "__main__":
    MUtils("test.java", "expect.txt").test_codegen()
