# type: ignore
import os
import sys
import subprocess
from typing import Optional, Any, Union, cast


from antlr4 import *  # type: ignore
from antlr4.FileStream import FileStream  # type: ignore
from antlr4.error.ErrorListener import ConsoleErrorListener  # type: ignore
from antlr4.CommonTokenStream import CommonTokenStream  # type: ignore

from BKOOLLexer import BKOOLLexer  # type: ignore
from BKOOLParser import BKOOLParser  # type: ignore
from lexererr import *
from ASTGeneration import ASTGeneration

from StaticError import StaticError
from StaticCheckMain import StaticCheck
from CodeGen import CodeGen
from typing import Tuple
from AST import *

JASMIN_JAR = "./src/external/jasmin.jar"
Lexer = BKOOLLexer
Parser = BKOOLParser

__all__ = ["MyUtils"]


class SyntaxException(Exception):
    def __init__(self, msg: str):
        self.message: str = msg


#@Singleton
class NewErrorListener(ConsoleErrorListener):
    INSTANCE: Optional["NewErrorListener"] = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException(
            "Error on line " + str(line) + " col " + str(column) + ": " + offendingSymbol.text
        )


NewErrorListener.INSTANCE = NewErrorListener()


class MyUtils:
    def __init__(
        self, inputPath: Union[str, os.PathLike[str]], outputPath: Union[str, os.PathLike[str]]
    ):
        self._input_path = inputPath
        self._output_path = outputPath
        self._input_stream = FileStream(inputPath)

    def resetInputStream(self) -> None:
        self._input_stream = FileStream(self._input_path)

    @staticmethod
    def fullAstObject(ast_tree: Program, reprPath: Union[str, os.PathLike[str]] = None, cp=False):
        """Get the Program(...) object"""
        expect = repr(ast_tree)
        if cp:
            import pyperclip  # type: ignore
            pyperclip.copy(expect)
        if reprPath:
            with open(reprPath, "w") as file:
                if cast(str, reprPath).endswith(".py"):
                    file.write("from AST import *\n")
                file.write(expect)

    @staticmethod
    def getErrorListener():
        return NewErrorListener.INSTANCE

    def test_lexer(self) -> bool:
        lexer = Lexer(self._input_stream)
        try:
            while True:
                tok = lexer.nextToken()
                if tok.type != Token.EOF:
                    print(tok.text + ",")
                else:
                    print("<EOF>")
                    break
        except (ErrorToken, UncloseString, IllegalEscape) as err:
            print(err.message)
        else:
            return True
        return False

    def test_parser(self) -> bool:
        lexer = Lexer(self._input_stream)
        listener = MyUtils.getErrorListener()
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            print("successful")
        except SyntaxException as f:
            print(f.message)
        except BaseException as e:
            print(str(e))
        else:
            return True
        return False

    def test_lexer_silent(self) -> bool:
        lexer = Lexer(self._input_stream)
        try:
            while True:
                tok = lexer.nextToken()
                if tok.type == Token.EOF:
                    break
        except (ErrorToken, UncloseString, IllegalEscape) as err:
            pass
        else:
            return True
        return False

    def test_parser_silent(self, parser: BKOOLParser) -> Tuple[Any, bool]:
        listener = MyUtils.getErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            tree = parser.program()
        except SyntaxException as f:
            print(f)
        except Exception as e:
            print(e)
        else:
            return tree, True
        return None, False

    def prepare_parser(self):
        step0 = self.test_lexer_silent()
        self.resetInputStream()
        lexer = Lexer(self._input_stream)
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        tree, step1 = self.test_parser_silent(parser)
        if not (step0 and step1):
            raise ValueError("Parse error!")
        return tree

    def test_astgen(self, reprPath: Union[str, os.PathLike[str]] = None, cp=False) -> Program:
        tree = self.prepare_parser()
        ast_tree = ASTGeneration().visit(tree)
        MyUtils.fullAstObject(ast_tree, reprPath, cp)
        with open(self._output_path, "w") as dest:
            dest.write(str(ast_tree))
        return ast_tree

    def test_checker(self, input_: Optional[Program] = None):
        if input_ is None:
            tree = self.prepare_parser()
            ast_tree = ASTGeneration().visit(tree)
        else:
            ast_tree = input_

        glob_env = StaticCheck(ast_tree).check()

        with open(self._output_path, "w") as fo:
            print("successful")
            fo.write(str(glob_env))

        return glob_env

    def test_codegen(self, ast_tree: Optional[Program] = None, build: bool = True, run: bool = True):
        if ast_tree is None:
            tree = self.prepare_parser()
            ast_tree = ASTGeneration().visit(tree)

        StaticCheck(ast_tree).check()
        codeGen = CodeGen()
        classpath = "./miscs/"

        env = codeGen.gen(ast_tree, classpath)
        java = os.path.join(os.environ['JAVA_HOME'], "bin", "java")
        cmd = f"{java} -jar {JASMIN_JAR} {classpath}*.j -d {classpath}"
    
        if build:
            subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT, timeout=10)
            subprocess.run("echo Generate Success!", shell=True, timeout=10)

        if run:
            args = sys.argv[1:]
            
            subprocess.run(
                f"""{java} -cp "./src/lib;{classpath}" BKoolClass {" ".join(args)}""",
                shell=True,
                stdout=None,
                timeout=10,
            )
            

        return env
