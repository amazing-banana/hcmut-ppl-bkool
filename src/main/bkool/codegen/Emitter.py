# type: ignore
from math import isclose
from typing import TYPE_CHECKING, Union, cast, overload

from AST import *
from AdditionalTypes import AnyType, FuncType, NullType, AnyRefType, FlexibleType
from CodeGenError import *
from Frame import Frame
from MachineCode import JasminCode
from Utils import *

# from StaticCheck import *
# from StaticError import *

if TYPE_CHECKING:
    from CodeGenSymbol import Access

__all__ = ["Emitter"]


def emitFCMPG(self):
    # type: (JasminCode) -> str
    return self.INDENT + "fcmpg" + self.END


class Emitter:
    def __init__(self, filename: str):
        self.filename: str = filename
        self.buff: List[str] = list()
        self.jvm: JasminCode = JasminCode()

    def END(self):
        return self.jvm.END

    def INDENT(self):
        return self.jvm.INDENT

    @staticmethod
    def emitFCMPG() -> str:
        return JasminCode.INDENT + "fcmpg" + JasminCode.END

    def emit_jump_if_false(self, label: "int", f: "Optional[Frame]" = None):
        # Jump if False, or else Continue
        if f:
            f.pop()
        return self.jvm.emitIFEQ(label)

    def emit_jump_if_true(self, label: "int", f: "Optional[Frame]" = None):
        if f:
            f.pop()
        return self.jvm.emitIFNE(label)

    def emitIF_JUST_FALSE(self, label: int, frame: Frame):
        frame.pop()
        return self.jvm.emitIFEQ(label)

    def emitCOMMENT(self, c: str):
        return ";; " + c + self.jvm.END

    def and_or_jump(
        self,
        is_and: bool,
        true_label: int,
        false_label: int,
        ac: "Access",
        last: bool = False,
    ):
        if last:
            op = ac.sc.op_for_last_expr_or_none()
            cond = op == "if" or op == "&&"
        else:
            cond = is_and

        ac.frame.pop()

        if cond:
            return self.emit_jump_if_false(false_label)
        else:
            return self.emit_jump_if_true(true_label)

    def compare_to_0(self, op, true_label, false_label, ac):
        # type: (str, int, int, Access) -> str
        if ac.sc.is_current_last():
            upper_op = ac.sc.op_for_last_expr_or_none()
        else:
            upper_op = ac.sc.upper_op_or_none()

        if upper_op == "||":
            label = true_label
            cond = True
        elif upper_op == "&&" or upper_op == "if" or upper_op == "for":
            label = false_label
            cond = False
        elif upper_op is NotImplemented:
            raise IllegalOperandException(upper_op)
        else:
            raise IllegalOperandException(upper_op)

        ac.frame.pop()
        if op == ">":
            return self.jvm.emitIFGT(label) if cond else self.jvm.emitIFLE(label)
        elif op == ">=":
            return self.jvm.emitIFGE(label) if cond else self.jvm.emitIFLT(label)
        elif op == "<":
            return self.jvm.emitIFLT(label) if cond else self.jvm.emitIFGE(label)
        elif op == "<=":
            return self.jvm.emitIFLE(label) if cond else self.jvm.emitIFGT(label)
        elif op == "==":
            return self.jvm.emitIFEQ(label) if cond else self.jvm.emitIFNE(label)
        elif op == "!=":
            return self.jvm.emitIFNE(label) if cond else self.jvm.emitIFEQ(label)
        raise IllegalRuntimeException("Unknown op: " + op)

    def int_compare(self, op, true_label, false_label, ac):
        # type: (str, int, int, Access)->str

        if ac.sc.is_current_last():
            """
            op_for_last_expr is None => standalone (a > b) => true first, false second
            op_for_last_expr == "if" => if (a > b) {...} => true first, false second
            op_for_last_expr == "for" =>  (a > b) , => true first, false second
            op_for_last_expr == "&&", => c && (a > b) => true first, false second
            op_for_last_expr == "||", => c || (a > b) => false first, true second
            Do short-circuit
                if term is last, ex. (a > b):
                 - and not satisfied, jump to the second label.
                 - satisfied, continue to next instruction
            """
            op_for_last_expr = ac.sc.op_for_last_expr_or_none()
            jump_to_true = op_for_last_expr == "||"
        else:
            upper_op = ac.sc.upper_op_or_none()
            jump_to_true = upper_op == "||"

        ac.frame.pop()
        ac.frame.pop()
        if op == ">":
            return (
                self.jvm.emitIFICMPGT(true_label)
                if jump_to_true
                else self.jvm.emitIFICMPLE(false_label)
            )
        elif op == ">=":
            return (
                self.jvm.emitIFICMPGE(true_label)
                if jump_to_true
                else self.jvm.emitIFICMPLT(false_label)
            )
        elif op == "<":
            return (
                self.jvm.emitIFICMPLT(true_label)
                if jump_to_true
                else self.jvm.emitIFICMPGE(false_label)
            )
        elif op == "<=":
            return (
                self.jvm.emitIFICMPLE(true_label)
                if jump_to_true
                else self.jvm.emitIFICMPGT(false_label)
            )
        elif op == "==":
            return (
                self.jvm.emitIFICMPEQ(true_label)
                if jump_to_true
                else self.jvm.emitIFICMPNE(false_label)
            )
        elif op == "!=":
            return (
                self.jvm.emitIFICMPNE(true_label)
                if jump_to_true
                else self.jvm.emitIFICMPEQ(false_label)
            )
        raise IllegalRuntimeException("Unknown op: " + op)

    def float_compare(self, op, true_label, false_label, ac):
        # type: (str, int, int, Access)->str
        if ac.sc.is_current_last():
            op_for_last_expr = ac.sc.op_for_last_expr_or_none()
            jump_to_true = op_for_last_expr == "||"
        else:
            upper_op = ac.sc.upper_op_or_none()
            jump_to_true = upper_op == "||"

        if not hasattr(self.jvm, "emitFCMPG"):
            from types import MethodType

            self.jvm.emitFCMPG = MethodType(emitFCMPG, self.jvm)

        ac.frame.pop()
        ac.frame.pop()
        if op == ">":
            return self.jvm.emitFCMPL() + (
                self.jvm.emitIFGT(true_label) if jump_to_true else self.jvm.emitIFGE(false_label)
            )
        elif op == ">=":
            return self.jvm.emitFCMPL() + (
                self.jvm.emitIFGE(true_label) if jump_to_true else self.jvm.emitIFLT(false_label)
            )
        elif op == "<":
            return self.jvm.emitFCMPG() + (
                self.jvm.emitIFLT(true_label) if jump_to_true else self.jvm.emitIFGE(false_label)
            )
        elif op == "<=":
            return self.jvm.emitFCMPG() + (
                self.jvm.emitIFLE(true_label) if jump_to_true else self.jvm.emitIFGT(false_label)
            )
        elif op == "==":
            return self.jvm.emitFCMPL() + (
                self.jvm.emitIFEQ(true_label) if jump_to_true else self.jvm.emitIFNE(false_label)
            )
        elif op == "!=":
            return self.jvm.emitFCMPL() + (
                self.jvm.emitIFNE(true_label) if jump_to_true else self.jvm.emitIFEQ(false_label)
            )
        raise IllegalRuntimeException("Unknown op: " + op)

    def emitNEGATE(self, true_label, false_label, ac, standalone=True):
        # type: (int, int, Access, bool) -> str
        if standalone:
            ac.frame.pop()

        if ac.sc.is_current_last():
            cond = ac.sc.absolute_last() or ac.sc.op_for_last_expr_or_none() == "&&"
        else:
            cond = ac.sc.upper_op_or_none() == "&&"

        if standalone:
            return self.jvm.emitIFNE(false_label) if cond else self.jvm.emitIFLE(true_label)
        else:
            return (
                self.jvm.emitGOTO(str(false_label)) if cond else self.jvm.emitGOTO(str(true_label))
            )

    def emitATTRIBUTE(
        self, lexeme: str, kind: SIKind, in_: Type, isFinal: bool, value: Optional[str]
    ):
        # lexeme: String
        # in_: Type
        # isFinal: Boolean
        # value: String

        if isinstance(kind, Static) and isFinal:
            value_str = (" = " + value) if value else ""
            return (
                ".field static final "
                + lexeme
                + " "
                + self.getJVMType(in_)
                + value_str
                + JasminCode.END
            )
        elif isinstance(kind, Static) and (not isFinal):
            return ".field static " + lexeme + " " + self.getJVMType(in_) + JasminCode.END
        elif isinstance(kind, Instance) and isFinal:
            value_str = (" = " + value) if value else ""
            return (
                ".field final " + lexeme + " " + self.getJVMType(in_) + value_str + JasminCode.END
            )
        else:
            return ".field " + lexeme + " " + self.getJVMType(in_) + JasminCode.END

    """ ___________________________________________________________________________________ """

    def getJVMType(self, inType: Type) -> str:
        typeIn = type(inType)
        if typeIn is IntType:
            return "I"
        elif typeIn is FloatType:
            return "F"
        elif typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is BoolType:
            return "Z"
        elif typeIn is VoidType:
            return "V"
        elif isinstance(inType, ArrayType):
            return "[" + self.getJVMType(inType.eleType)
        elif isinstance(inType, FuncType):
            return (
                "("
                + "".join(map(lambda e: self.getJVMType(e), inType.param_types))
                + ")"
                + self.getJVMType(inType.return_type)
            )
        elif isinstance(inType, ClassType):
            return "L" + inType.classname.name + ";"
        elif isinstance(inType, (AnyType, AnyRefType)):
            return "Ljava/lang/Object;"
        elif isinstance(inType, FlexibleType):
            return self.getJVMType(inType.inner)
        else:
            raise IllegalRuntimeException("Unknown JVM type?: " + str(inType))

    def getFullType(self, inType) -> str:
        typeIn = type(inType)
        if typeIn is IntType:
            return "int"
        elif typeIn is FloatType:
            return "float"
        elif typeIn is BoolType:
            return "boolean"
        elif typeIn is StringType:
            return "java/lang/String"
        elif isinstance(inType, ClassType):
            return inType.classname.name
        elif typeIn is VoidType:
            return "void"
        elif isinstance(inType, (AnyType, AnyRefType)):
            return "java/lang/Object"
        elif isinstance(inType, FlexibleType):
            return self.getJVMType(inType.inner)
        elif isinstance(inType, ArrayType):
            return self.getJVMType(inType)

    def emitPUSHICONST(self, in_: Union[int, str], frame: Frame) -> str:
        # in: _Int or Sring
        # frame: Frame

        if type(in_) is int:
            frame.push()  # push a value onto stacks, stacks + 1
            if -1 <= in_ <= 5:
                return self.jvm.emitICONST(in_)
            elif -128 <= in_ <= 127:
                return self.jvm.emitBIPUSH(in_)
            elif -32768 <= in_ <= 32767:
                return self.jvm.emitSIPUSH(in_)
            else:
                return self.jvm.emitLDC(str(in_))
        elif isinstance(in_, str):
            if in_ == "true":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "false":
                return self.emitPUSHICONST(0, frame)
            else:
                return self.emitPUSHICONST(int(in_), frame)
        raise IllegalOperandException("in_ parameter should be str or int!")

    def emitPUSHFCONST(self, in_: str, frame: Frame):
        # in_: String
        # frame: Frame
        # stacks + 1 -> push()

        f = float(in_)
        frame.push()

        if isclose(f, 0.0) or isclose(f, 1.0) or isclose(f, 2.0):
            rst = "{0:.1f}".format(f)
            return self.jvm.emitFCONST(rst)
        else:
            return self.jvm.emitLDC(in_)

    """ 
    *    generate code to push a constant onto the operand stacks.
    *    @param in the lexeme of the constant
    *    @param typ the type of the constant
    """

    def emitPUSHCONST(self, in_: str, typ: Type, frame: Frame):
        # in_: String
        # typ: Type
        # frame: Frame

        if isinstance(typ, (IntType, BoolType)):
            return self.emitPUSHICONST(in_, frame)
        elif isinstance(typ, FloatType):
            return self.emitPUSHFCONST(in_, frame)
        elif type(typ) is StringType:
            frame.push()
            return self.jvm.emitLDC(in_)
        elif isinstance(typ, NullType):
            frame.push()
            return self.jvm.emitPUSHNULL()
        else:
            raise IllegalOperandException(f"{in_} and {typ}")

    ##############################################################

    def emitALOAD(self, in_: Type, frame: Frame):
        # in_: Type
        # frame: Frame
        # ..., arrayref, target -> ..., value -> -1 stacks
        # elif type(in_) is cgen.ArrayPointerType or type(in_) is cgen.ClassType or type(in_) is StringType:

        frame.pop()
        if type(in_) is IntType:
            return self.jvm.emitIALOAD()
        elif isinstance(in_, FloatType):
            return self.jvm.emitFALOAD()
        elif isinstance(in_, BoolType):
            return self.jvm.emitBALOAD()
        elif type(in_) in (ClassType, StringType, ArrayType):
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(str(in_))

    def emitASTORE(self, in_: Type, frame: Frame):
        # in_: Type
        # frame: Frame
        # ..., arrayref, target, value -> ...
        # elif type(in_) is cgen.ArrayPointerType or type(in_) is cgen.ClassType or type(in_) is StringType:

        frame.pop()
        frame.pop()
        frame.pop()
        if type(in_) is IntType:
            return self.jvm.emitIASTORE()
        elif isinstance(in_, FloatType):
            return self.jvm.emitFASTORE()
        elif isinstance(in_, BoolType):
            return self.jvm.emitBASTORE()
        elif type(in_) in (ClassType, StringType, ArrayType):
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(str(in_))

    """    generate the var directive for a local variable.
    *   @param in the target of the local variable.
    *   @param varName the op of the local variable.
    *   @param inType the type of the local variable.
    *   @param fromLabel the starting true_label of the scope where the variable is active.
    *   @param toLabel the ending true_label  of the scope where the variable is active.
    """

    def emitVAR(
        self,
        in_: int,
        varName: str,
        inType: Type,
        fromLabel: int,
        toLabel: int,
        frame: Frame,
    ):
        # in_: _Int
        # varName: String
        # inType: Type
        # fromLabel: _Int
        # toLabel: _Int
        # frame: Frame

        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

    def emitREADVAR(self, name: str, inType: Type, index: int, frame: Frame):
        # op: String
        # inType: Type
        # target: _Int
        # frame: Frame
        # ... -> ..., value
        # elif type(inType) is cgen.ArrayPointerType or type(inType) is cgen.ClassType or type(inType) is StringType:

        frame.push()
        if isinstance(inType, (BoolType, IntType)):
            return self.jvm.emitILOAD(index)
        elif isinstance(inType, FloatType):
            return self.jvm.emitFLOAD(index)
        elif type(inType) in (ClassType, StringType, ArrayType):
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(name)

    """ generate the second instruction for array cell access
    *   Don't Use this?
    """

    def emitREADVAR2(self, name: str, typ: Type, frame: Frame):
        # op: String
        # typ: Type
        # frame: Frame
        # ... -> ..., value

        # frame.push()

        raise IllegalOperandException(name)

    """
    *   generate code to pop a value on top of the operand stacks and store it to a block-scoped variable.
    *   @param op the symbol entry of the variable.
    """

    def emitWRITEVAR(self, name: str, inType: Type, index: int, frame: Frame):
        # op: String
        # inType: Type
        # target: _Int
        # frame: Frame
        # ..., value -> ...
        # elif type(inType) is cgen.ArrayPointerType or type(inType) is cgen.ClassType or type(inType) is StringType:

        frame.pop()

        if isinstance(inType, (IntType, BoolType)):
            return self.jvm.emitISTORE(index)
        elif isinstance(inType, FloatType):
            return self.jvm.emitFSTORE(index)
        elif type(inType) in (ClassType, StringType, ArrayType):
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(name)

    """ generate the second instruction for array cell access
    *
    """

    def emitWRITEVAR2(self, name: str, typ: Type, frame: Frame):
        # op: String
        # typ: Type
        # frame: Frame
        # ..., value -> ...

        # frame.push()
        raise IllegalOperandException(name)

    """ generate the field (s) directive for a class mutable or immutable attribute.
    *   @param lexeme the op of the attribute.
    *   @param in the type of the attribute.
    *   @param isFinal true in case of constant; false otherwise
    """

    def emitGETSTATIC(self, lexeme: str, in_: Type, frame: Frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    def emitPUTSTATIC(self, lexeme: str, in_: Type, frame: Frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    def emitGETFIELD(self, lexeme: str, in_: Type, frame: Frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme: str, in_: Type, frame: Frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()
        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

    """ generate code to invoke a static method
    *   @param lexeme the qualified op of the method(i.e., class-op/method-op)
    *   @param in the type descriptor of the method.
    """

    def emitINVOKESTATIC(self, lexeme: str, in_: Type, frame: Frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        typ: FuncType = cast(FuncType, in_)
        list(map(lambda x: frame.pop(), typ.param_types))
        if not type(typ.return_type) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

    """ generate code to invoke a special method
    *   @param lexeme the qualified op of the method(i.e., class-op/method-op)
    *   @param in the type descriptor of the method.
    """

    @overload
    def emitINVOKESPECIAL(self, frame: Frame) -> str:
        """Emit: invokespecial {java/lang/Object/<init>}{()V}"""
        ...

    @overload
    def emitINVOKESPECIAL(self, frame: Frame, lexeme: str, in_: Type) -> str:
        """Emit: invokespecial {lexeme}{in_}"""
        ...

    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        # type: (Frame, Optional[str], Optional[Type]) -> str
        # lexeme: String
        # in_: Type
        # frame: Frame

        if (lexeme is not None) and (in_ is not None):
            typ: "FuncType" = cast(FuncType, in_)
            for _ in typ.param_types:
                frame.pop()
            frame.pop()
            if type(typ.return_type) is not VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()
        raise IllegalOperandException(f"emitINVOKESPECIAL {lexeme}{in_}")

    """ generate code to invoke a virtual method
    * @param lexeme the qualified op of the method(i.e., class-op/method-op)
    * @param in the type descriptor of the method.
    """

    def emitINVOKEVIRTUAL(self, lexeme: str, in_: Type, frame: Frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        assert isinstance(in_, FuncType)

        # map(lambda x: frame.pop(), typ.partype)
        [frame.pop() for _ in in_.param_types]

        frame.pop()
        if type(in_.return_type) is not VoidType:
            frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))

    """
    *   generate ineg, fneg.
    *   @param in the type of the operands.
    """

    def emitNEGOP(self, in_: Type, frame: Frame):
        # in_: Type
        # frame: Frame
        # ..., value -> ..., result

        if type(in_) is IntType:
            return self.jvm.emitINEG()
        else:
            return self.jvm.emitFNEG()

    def emitNOT(self, in_: Type, frame: Frame):
        # in_: Type
        # frame: Frame

        label_t = frame.getNewLabel()
        label_f = frame.getNewLabel()

        result = list()

        result.append(self.emitIFTRUE(label_t, frame))
        result.append(self.emitPUSHCONST("true", in_, frame))
        result.append(self.emitGOTO(label_f, frame))
        result.append(self.emitLABEL(label_t, frame))
        result.append(self.emitPUSHCONST("false", in_, frame))
        result.append(self.emitLABEL(label_f, frame))
        return "".join(result)

    """
    *   generate iadd, isub, fadd or fsub.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    """

    def emitADDOP(self, lexeme: str, in_: Type, frame: Frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "+":
            if type(in_) is IntType:
                return self.jvm.emitIADD()
            else:
                return self.jvm.emitFADD()
        else:
            if type(in_) is IntType:
                return self.jvm.emitISUB()
            else:
                return self.jvm.emitFSUB()

    """
    *   generate imul, idiv, fmul or fdiv.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    """

    def emitMULOP(self, lexeme: str, in_: Type, frame: Frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "*":
            if type(in_) is IntType:
                return self.jvm.emitIMUL()
            else:
                return self.jvm.emitFMUL()
        else:
            if type(in_) is IntType:
                return self.jvm.emitIDIV()
            else:
                return self.jvm.emitFDIV()

    def emitDIV(self, frame: Frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIDIV()

    def emitMOD(self, frame: Frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIREM()

    """
    *   generate iand
    """

    def emitANDOP(self, frame: Frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIAND()

    """
    *   generate ior
    """

    def emitOROP(self, frame: Frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIOR()

    def emitREOP(self, op: str, in_: Type, frame: Frame):
        # op: String                            val b = (1 + 1) >= 2.2  ;; compare with float.
        # in_: Type                                     iconst_1
        # frame: Frame                                  iconst_1
        # ..., value1, value2 -> ..., result            iadd
        #                                               i2f
        #                                               ldc 2.2
        #                                               fcmpl
        #                                               iflt Label_false
        #                                           	iconst_1   ;; Push true on stacks
        #                                               goto Label_out ;; Goto out
        #                                           Label_false:
        #                                           	iconst_0   ;; Push false on stacks
        #                                           Label_out:
        #                                               istore_b   ;; store back.

        result = list()
        label_f = frame.getNewLabel()
        label_out = frame.getNewLabel()
        is_float = isinstance(in_, FloatType)

        frame.pop()
        frame.pop()
        if is_float:  # There is no FCMPG()
            # FCMPL:
            #   -1: lt/NaN
            #    0: eq
            #    1: gt
            result.append(self.jvm.emitFCMPL())
        jvm = self.jvm

        def _repeat(emit_float: Callable[[int], str], emit_int: Callable[[int], str]):
            _comparer = emit_float(label_f) if is_float else emit_int(label_f)
            result.append(_comparer)

        if op == ">":
            _repeat(jvm.emitIFLE, jvm.emitIFICMPLE)
        elif op == ">=":
            _repeat(jvm.emitIFLT, jvm.emitIFICMPLT)
        elif op == "<":
            _repeat(jvm.emitIFGE, jvm.emitIFICMPGE)
        elif op == "<=":
            _repeat(jvm.emitIFGT, jvm.emitIFICMPGT)
        elif op == "!=":
            _repeat(jvm.emitIFEQ, jvm.emitIFICMPEQ)
        elif op == "==":
            _repeat(jvm.emitIFNE, jvm.emitIFICMPNE)
        result.append(self.emitPUSHCONST("1", IntType(), frame))
        frame.pop()
        result.append(self.emitGOTO(label_out, frame))
        result.append(self.emitLABEL(label_f, frame))
        result.append(self.emitPUSHCONST("0", IntType(), frame))
        result.append(self.emitLABEL(label_out, frame))
        return "".join(result)

    def emitRELOP(
        self,
        op: str,
        in_: "Optional[Type]",
        sc_label: int,
        esc_label: int,
        frame: Frame,
    ):
        # op: String
        # in_: Type
        # firstLabel: _Int
        # secondLabel: _Int
        # frame: Frame
        # ..., value1, value2 -> ..., result
        """Perhaps this function is for emit short-circut boolean ?"""

        result = list()

        if in_ is not None:
            if isinstance(in_, BoolType):
                frame.pop()
            else:
                frame.pop()
                frame.pop()

        if op == "&&":
            result.append(self.emit_jump_if_false(sc_label))
        elif op == "||":
            result.append(self.emit_jump_if_true(sc_label))
        ###
        elif op == ">":
            result.append(self.jvm.emitIFICMPLE(esc_label))
            # result.append(self.emitGOTO(firstLabel, frame))
        elif op == ">=":
            result.append(self.jvm.emitIFICMPLT(esc_label))
        elif op == "<":
            result.append(self.jvm.emitIFICMPGE(esc_label))
        elif op == "<=":
            result.append(self.jvm.emitIFICMPGT(esc_label))
        elif op == "!=":
            result.append(self.jvm.emitIFICMPEQ(esc_label))
        elif op == "==":
            result.append(self.jvm.emitIFICMPNE(esc_label))

        # result.append(self.jvm.emitGOTO(str(firstLabel)))
        return "".join(result)

    """   generate the method directive for a function.
    *   @param lexeme the qualified op of the method(i.e., class-op/method-op).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is s; <code>false</code> otherwise.
    """

    def emitMETHOD(self, lexeme: str, in_: Type, isStatic: bool, frame: Frame):
        # lexeme: String
        # in_: Type
        # isStatic: Boolean
        # frame: Frame

        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

    """   generate the end directive for a function.
    """

    def emitENDMETHOD(self, frame: Frame):
        # frame: Frame

        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return "".join(buffer)

    @staticmethod
    def getConst(ast: Literal, frame: Frame):
        # ast: Literal
        if isinstance(ast, IntLiteral):
            return str(ast.value), IntType()
        elif isinstance(ast, FloatLiteral):
            return str(ast.value), FloatType()
        elif isinstance(ast, StringLiteral):
            return ast.value, StringType()
        elif isinstance(ast, BooleanLiteral):
            return str(ast.value), BoolType()
        elif isinstance(ast, NullLiteral):
            return "nil", NullType()
        elif isinstance(ast, SelfLiteral):
            return "this", frame.returnType

    """   generate code to initialize a local array variable.<p>
    *   @param target the target of the local variable.
    *   @param in the type of the local array variable.
    """

    def emitNEW(self, in_: ClassType, frame: Frame) -> str:
        frame.push()
        return self.jvm.emitNEW(in_.classname.name)

    """   generate code to initialize local array variables.
    *   @param in the list of symbol entries corresponding to local array variable.    
    """

    """   generate code to jump to true_label if the value on top of operand stacks is true.<p>
    *   ifgt true_label
    *   @param true_label the true_label where the flow continues if the value on top of stacks is true.
    """

    def emitIFTRUE(self, label: int, frame: Frame):
        # true_label: _Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFGT(label)

    """
    *   generate code to jump to true_label if the value on top of operand stacks is false.<p>
    *   ifle true_label
    *   @param true_label the true_label where the flow continues if the value on top of stacks is false.
    """

    def emitIFFALSE(self, label: int, frame: Frame):
        # true_label: _Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFLE(label)

    def emitIFICMPGT(self, label: int, frame: Frame):
        # true_label: _Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label: int, frame: Frame):
        # true_label: _Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPLT(label)

    """   generate code to duplicate the value on the top of the operand stacks.<p>
    *   Stack:<p>
    *   Before: ...,value1<p>
    *   After:  ...,value1,value1<p>
    """

    def emitDUP(self, frame: Frame):
        # frame: Frame

        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame: Frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitPOP()

    """   generate code to exchange an integer on top of stacks to a floating-point number.
    """

    def emitI2F(self, frame: Frame):
        # frame: Frame

        return self.jvm.emitI2F()

    """ generate code to return.
    *   <ul>
    *   <li>ireturn if the type is IntegerType or BooleanType
    *   <li>freturn if the type is RealType
    *   <li>return if the type is null
    *   </ul>
    *   @param in the type of the returned expression.
    """

    def emitRETURN(self, in_: Type, frame: Frame):
        # in_: Type
        # frame: Frame
        if type(in_) is VoidType:
            return self.jvm.emitRETURN()
        frame.pop()
        if type(in_) in (IntType, BoolType):
            return self.jvm.emitIRETURN()
        elif isinstance(in_, FloatType):
            return self.jvm.emitFRETURN()
        # elif isinstance(in_, (ArrayType, ClassType, StringType)):
        else:
            return self.jvm.emitARETURN()

    """ generate code that represents a true_label	
    *   @param true_label the true_label
    *   @return code Label<true_label>:
    """

    def emitLABEL(self, label: int, frame: Frame):
        # true_label: _Int
        # frame: Frame

        return self.jvm.emitLABEL(label)

    """ generate code to jump to a true_label	
    *   @param true_label the true_label
    *   @return code goto Label<true_label>
    """

    def emitGOTO(self, label: int, frame: Frame):
        # true_label: _Int
        # frame: Frame

        return self.jvm.emitGOTO(str(label))

    """ generate some starting directives for a class.<p>
    *   .source MPC.CLASSNAME.java<p>
    *   .class public MPC.CLASSNAME<p>
    *   .super java/lang/Object<p>
    """

    def emitPROLOG(self, name: str, parent: str):
        # op: String
        # parent: String

        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER("java/lang/Object" if parent == "" else parent))
        result.append(JasminCode.END)
        return "".join(result)

    def emitLIMITSTACK(self, num: int):
        # num: _Int

        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num: int):
        # num: _Int

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write("".join(self.buff))
        file.close()

    """ print out the code to screen
    *   @param in the code to be printed out
    """

    def printout(self, in_: str):
        # in_: String

        self.buff.append(in_)

    def printout_local_var(self, in_: str):
        # in_: String
        buff_index = len(self.buff)
        while (buff_index - 1) > 0:
            if self.buff[buff_index - 1][0:4] in (".var", ".met"):
                self.buff.insert(buff_index, in_)
                return
            buff_index -= 1
        pass

    def clearBuff(self):
        self.buff.clear()

    """ __________________________________________________________________________ """

    def emit_ARRAY_ALLOC_ANEWARRAY(self, in_: "ArrayType", frame: Frame):
        # type ~ Union[IntType, FloatType, BoolType, StringType,
        #              ArrayType, ClassType, VoidType, MType]
        # Primitive ~ Union[IntType, FloatType, BoolType]
        # Ref. Type ~ Union[StringType, ArrayType, ClassType]
        # Not valid ~ [VoidType, MType]

        buff = self.emitPUSHICONST(in_.size, frame)
        if isinstance(in_.eleType, (IntType, FloatType, BoolType)):
            return buff + self.jvm.emitNEWARRAY(self.getFullType(in_.eleType))
        elif isinstance(in_.eleType, (StringType, ArrayType, ClassType)):
            return buff + self.jvm.emitANEWARRAY(self.getFullType(in_.eleType))
        else:
            raise IllegalRuntimeException("Array element: Void or Method type is not support!")

    def emit_ARRAY_ALLOC_MULTI_ANEARRAY(self, in_: ArrayType, frame: Frame):
        ele_type = in_.eleType
        code = [self.emitPUSHICONST(in_.size, frame)]
        while isinstance(ele_type, ArrayType):
            code.append(self.emitPUSHICONST(ele_type.size, frame))
            ele_type = ele_type.eleType
        for _ in range(len(code) - 1):
            frame.pop()
        code.append(self.jvm.emitMULTIANEWARRAY(self.getJVMType(in_), str(len(code))))

        return "".join(code)
