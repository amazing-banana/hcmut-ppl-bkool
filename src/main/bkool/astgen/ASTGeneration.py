# type: ignore
from typing import (
    List,
    Union,
    Optional,
    Tuple,
    Any,
    Type as _Type_,
    Sequence,
    TypeVar,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from typing import Iterable, Callable

from AST import *
from BKOOLParser import BKOOLParser  # type: ignore
from BKOOLVisitor import BKOOLVisitor  # type: ignore


class _Utils:
    R = TypeVar("R", VarDecl, ConstDecl)

    @staticmethod
    def map_reduce(func: "Callable[[Any], Iterable[Any]]", list_: "Iterable[Any]") -> "Iterable[Any]":
        from functools import reduce
        from itertools import chain
        return reduce(lambda a, b: chain(a, b), map(func, list_))

    @staticmethod
    def _flatten(lst):
        # (Any) -> List[MemDecl] | List[StoreDecl]
        from typing import Iterable  # works with list, map object, filter, ...
        from functools import reduce

        flat = _Utils._flatten
        isIns = isinstance
        isIter = lambda _lst: isIns(_lst, Iterable) and not isIns(_lst, (str, bytes))
        yield_expr = lambda acc, ele: [*acc, *flat(ele)] if isIter(ele) else [*acc, ele]
        return list(reduce(yield_expr, lst, []))  # the [] is important

    @staticmethod
    def flatten_list(lst):
        from typing import Iterable
        # (Any) -> List[MemDecl] | List[StoreDecl]
        def _yield(lt):
            for e in lt:
                if isinstance(e, Iterable) and not isinstance(e, (str, bytes)):
                    yield from _Utils.flatten_list(e)
                else:
                    yield e

        return list(_yield(lst))

    @staticmethod
    # Looks dangerous but actually type-safe?
    # try: _.get_stores_(Any(), None, None, 'types not VarDecl,ConstDecl') -> warning
    def get_stores_(self: "ASTGeneration", ctx_type, ctx_decls, StoreType: _Type_[R]) -> List[R]:
        bktype = self.visit(ctx_type)  # type: Type

        # List[Tuple[Id, Expr | NoneType]]
        id_init = self.visit(ctx_decls)  # type: List[Tuple[Id, Optional[Expr]]]

        decl_list = map(lambda e: StoreType(e[0], bktype, e[1]), id_init)

        return list(decl_list)

    @staticmethod
    def get_attrs(self, ctx_type, ctx_decls, kind, StoreType):
        # type: (ASTGeneration, Any, Any, SIKind, _Type_[R]) -> List[AttributeDecl]
        var_decls: Sequence["StoreDecl"] = _Utils.get_stores_(self, ctx_type, ctx_decls, StoreType)
        return list(map(lambda e: AttributeDecl(kind, e), var_decls))


class ASTGeneration(BKOOLVisitor):
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return Program([self.visit(decl) for decl in ctx.class_decl()])

    def visitClass_decl(self, ctx: BKOOLParser.Class_declContext):
        class_name = Id(ctx.ID(0).getText())
        parent_name = Id(ctx.ID(1).getText()) if ctx.EXTENDS() else None
        mem_list = self.visit(ctx.class_body())  # type: List[MemDecl]

        return ClassDecl(class_name, mem_list, parent_name)

    def visitClass_body(self, ctx):
        # type: (BKOOLParser.Class_bodyContext) ->  List[MemDecl]
        # List[MethodDecl | List[StoreDecl]]
        may_nested_list: List[Union[MethodDecl, List[AttributeDecl]]]
        may_nested_list = [self.visit(mem_decl) for mem_decl in ctx.class_body_decl()]
        return _Utils.flatten_list(may_nested_list)

    def visitClass_body_decl(self, ctx):
        # type: (BKOOLParser.Class_body_declContext) -> MemDecl
        return self.visitChildren(ctx)

    def visitField_decl(self, ctx):
        # type: (BKOOLParser.Field_declContext) -> List[AttributeDecl]
        return _Utils.get_attrs(self, ctx.bkooltype(), ctx.var_decl_list(), Instance(), VarDecl)

    def visitConst_field_decl(self, ctx):
        # type: (BKOOLParser.Const_field_declContext) -> List[AttributeDecl]
        return _Utils.get_attrs(self, ctx.bkooltype(), ctx.const_decl_list(), Instance(), ConstDecl)

    def visitStatic_field_decl(self, ctx):
        # type: (BKOOLParser.Static_field_declContext) -> List[AttributeDecl]
        return _Utils.get_attrs(self, ctx.bkooltype(), ctx.var_decl_list(), Static(), VarDecl)

    def visitStatic_constant_decl(self, ctx):
        # type: (BKOOLParser.Static_constant_declContext) -> List[AttributeDecl]
        return _Utils.get_attrs(self, ctx.bkooltype(), ctx.const_decl_list(), Static(), ConstDecl)

    def visitVar_decl_list(self, ctx):
        # type: (BKOOLParser.Var_decl_listContext) -> List[Tuple[Id, Optional[Expr]]]
        return [self.visit(unit) for unit in ctx.var_decl_unit()]

    def visitVar_decl_unit(self, ctx):
        # type: (BKOOLParser.Var_decl_unitContext)-> Tuple[Id, Optional[Expr]]
        ident = Id(ctx.ID().getText())
        init = self.visit(ctx.expr()) if ctx.INIT_OP() else None
        return ident, init

    def visitConst_decl_list(self, ctx):
        # type: (BKOOLParser.Const_decl_listContext) -> List[Tuple[Id, Expr]]
        return [self.visit(unit) for unit in ctx.const_decl_unit()]

    def visitConst_decl_unit(self, ctx):
        # type: (BKOOLParser.Const_decl_unitContext) -> Tuple[Id, Expr]
        ident = Id(ctx.ID().getText())
        init = self.visit(ctx.expr()) if ctx.INIT_OP() else None
        return ident, init

    def visitMethod_decl(self, ctx):
        # type: (BKOOLParser.Method_declContext) -> MethodDecl
        kind: SIKind = Static() if ctx.STATIC() else Instance()
        name = Id(ctx.ID().getText())
        formal_params: List[VarDecl]
        formal_params = self.visit(ctx.param_list()) if ctx.param_list() else []
        bktype: Type = self.visit(ctx.bkooltype())
        body = self.visit(ctx.block_stmt())
        return MethodDecl(kind, name, formal_params, bktype, body)

    def visitParam_list(self, ctx):
        # type: (BKOOLParser.Param_listContext) -> List[StoreDecl]
        # return flat_map(lambda e: self.visit(param), ctx.params)
        # return map_reduce(lambda e: self.visit(param), ctx.params)
        nested_param_list = [self.visit(param) for param in ctx.params()]
        return _Utils.flatten_list(nested_param_list)

    def visitParams(self, ctx):
        # type:(BKOOLParser.ParamsContext) -> List[VarDecl]
        return _Utils.get_stores_(self, ctx.bkooltype(), ctx.id_list(), VarDecl)

    def visitId_list(self, ctx):
        # type: (BKOOLParser.Id_listContext) -> List[Tuple[Id, None]]
        return [(Id(ident.getText()), None) for ident in ctx.ID()]

    def visitConstructor_decl(self, ctx):
        # type: (BKOOLParser.Constructor_declContext) -> MethodDecl
        kind = Instance()
        name = Id("<init>")  # invokespecial java/lang/Object/<init>()V
        formal_params: List[VarDecl]
        formal_params = self.visit(ctx.param_list()) if ctx.param_list() else []
        bktype = None
        body = self.visit(ctx.block_stmt())
        return MethodDecl(kind, name, formal_params, bktype, body)

    def visitBkooltype(self, ctx):
        # type: (BKOOLParser.BkooltypeContext) -> Type
        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        else:
            return self.visitChildren(ctx)

    def visitArray_type(self, ctx):
        # type: (BKOOLParser.Array_typeContext) -> ArrayType
        ele_type: Type = (
            ClassType(Id(ctx.ID().getText())) if ctx.ID() else self.visit(ctx.primitive_type())
        )

        size = int(ctx.INTEGER_LITERAL().getText())
        return ArrayType(size, ele_type)

    def visitPrimitive_type(self, ctx):
        # type: (BKOOLParser.Primitive_typeContext) -> Type
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOL():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        else:
            return VoidType()

    def visitStmt(self, ctx: BKOOLParser.StmtContext):
        return self.visitChildren(ctx)

    def visitBlock_stmt(self, ctx: BKOOLParser.Block_stmtContext):
        local_vars: List["StoreDecl"]
        local_vars = self.visit(ctx.local_decl_region()) if ctx.local_decl_region() else []
        stmts: List[Stmt] = self.visit(ctx.stmts()) if ctx.stmts() else []
        return Block(local_vars, stmts)

    def visitLocal_decl_region(self, ctx: BKOOLParser.Local_decl_regionContext) -> List[StoreDecl]:
        nested_local_vars: List[List["StoreDecl"]]
        nested_local_vars = [self.visit(decl) for decl in ctx.local_decl()]
        return _Utils.flatten_list(nested_local_vars)

    def visitStmts(self, ctx: BKOOLParser.StmtsContext) -> List[Stmt]:
        return [self.visit(stmt) for stmt in ctx.stmt()]

    def visitLocal_decl(self, ctx: BKOOLParser.Local_declContext) -> List["StoreDecl"]:
        return self.visitChildren(ctx)

    def visitLocal_var_decl(self, ctx: BKOOLParser.Local_var_declContext) -> List[VarDecl]:
        return _Utils.get_stores_(self, ctx.bkooltype(), ctx.var_decl_list(), VarDecl)

    def visitLocal_const_decl(self, ctx: BKOOLParser.Local_const_declContext) -> List[ConstDecl]:
        return _Utils.get_stores_(self, ctx.bkooltype(), ctx.const_decl_list(), ConstDecl)

    def visitAssign_stmt(self, ctx: BKOOLParser.Assign_stmtContext):
        lhs: Expr = self.visit(ctx.lhs())
        expr = self.visit(ctx.expr())
        return Assign(lhs, expr)

    def visitLhs(self, ctx: BKOOLParser.LhsContext) -> Union[Id, ArrayCell, FieldAccess]:
        return self.visitChildren(ctx)

    def visitLhs_base(self, ctx: BKOOLParser.Lhs_baseContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visitChildren(ctx)

    def visitLhs_index_expr(self, ctx: BKOOLParser.Lhs_index_exprContext):
        arr: Expr = self.visit(ctx.member_access_expr())
        index: Expr = self.visit(ctx.expr())
        return ArrayCell(arr, index)

    def visitLhs_member_access_expr(self, ctx: BKOOLParser.Lhs_member_access_exprContext):
        obj = self.visit(ctx.new_expr())
        if ctx.ID():
            id_ = Id(ctx.ID().getText())
            return FieldAccess(obj, id_)
        else:
            ident, params = self.visit(ctx.method_call())
            return CallExpr(obj, ident, params)

    def visitIf_then_stmt(self, ctx: BKOOLParser.If_then_stmtContext):
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return If(expr, stmt)

    def visitIf_then_else_stmt(self, ctx: BKOOLParser.If_then_else_stmtContext):
        expr = self.visit(ctx.expr())
        then_stmt = self.visit(ctx.stmt_no_short_if())
        else_stmt = self.visit(ctx.stmt())
        return If(expr, then_stmt, else_stmt)

    def visitIf_then_else_stmt_no_short_if(
        self, ctx: BKOOLParser.If_then_else_stmt_no_short_ifContext
    ):
        expr = self.visit(ctx.expr())
        then_stmt = self.visit(ctx.stmt_no_short_if(0))
        else_stmt = self.visit(ctx.stmt_no_short_if(1))
        return If(expr, then_stmt, else_stmt)

    def visitStmt_no_short_if(self, ctx: BKOOLParser.Stmt_no_short_ifContext) -> Stmt:
        return self.visitChildren(ctx)

    def visitStmt_no_trailing_substmt(
        self, ctx: BKOOLParser.Stmt_no_trailing_substmtContext
    ) -> Stmt:
        return self.visitChildren(ctx)

    def visitFor_stmt(self, ctx: BKOOLParser.For_stmtContext):
        ident = Id(ctx.ID().getText())
        from_expr = self.visit(ctx.expr(0))
        up = True if ctx.TO() else False
        to_expr = self.visit(ctx.expr(1))
        stmt = self.visit(ctx.stmt())
        return For(ident, from_expr, to_expr, up, stmt)

    def visitFor_stmt_no_short_if(self, ctx: BKOOLParser.For_stmt_no_short_ifContext):
        ident = Id(ctx.ID().getText())
        from_expr = self.visit(ctx.expr(0))
        up = bool(ctx.TO())  # either TO or DOWNTO
        to_expr = self.visit(ctx.expr(1))
        stmt = self.visit(ctx.stmt_no_short_if())
        return For(ident, from_expr, to_expr, up, stmt)

    def visitBreak_stmt(self, ctx: BKOOLParser.Break_stmtContext):
        return Break()

    def visitContinue_stmt(self, ctx: BKOOLParser.Continue_stmtContext):
        return Continue()

    def visitReturn_stmt(self, ctx: BKOOLParser.Return_stmtContext):
        expr: Expr = self.visit(ctx.expr())
        return Return(expr)

    def visitMethod_invoke_stmt(self, ctx: BKOOLParser.Method_invoke_stmtContext):
        expr = self.visit(ctx.expr())
        ident, param = self.visit(ctx.method_call())
        return CallStmt(expr, ident, param)

    def visitExpr(self, ctx: BKOOLParser.ExprContext) -> Expr:
        return self.visitChildren(ctx)

    def visitRelational_expr(self, ctx: BKOOLParser.Relational_exprContext):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            left = self.visit(ctx.equality_expr(0))
            right = self.visit(ctx.equality_expr(1))
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitEquality_expr(self, ctx: BKOOLParser.Equality_exprContext):

        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            left = self.visit(ctx.logical_expr(0))
            right = self.visit(ctx.logical_expr(1))
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitLogical_expr(self, ctx: BKOOLParser.Logical_exprContext):

        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            left = self.visit(ctx.logical_expr())
            right = self.visit(ctx.additive_expr())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitAdditive_expr(self, ctx: BKOOLParser.Additive_exprContext):

        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            left = self.visit(ctx.additive_expr())
            right = self.visit(ctx.multiply_expr())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitMultiply_expr(self, ctx: BKOOLParser.Multiply_exprContext):

        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            left = self.visit(ctx.multiply_expr())
            right = self.visit(ctx.concat_expr())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitConcat_expr(self, ctx: BKOOLParser.Concat_exprContext):

        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            left = self.visit(ctx.concat_expr())
            right = self.visit(ctx.negate_expr())
            op = ctx.CONCAT_OP().getText()
            return BinaryOp(op, left, right)

    def visitNegate_expr(self, ctx: BKOOLParser.Negate_exprContext):

        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            operand = self.visit(ctx.negate_expr())
            op = ctx.NOT_OP().getText()
            return UnaryOp(op, operand)

    def visitUnary_arithmetic_expr(self, ctx: BKOOLParser.Unary_arithmetic_exprContext):

        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            operand = self.visit(ctx.unary_arithmetic_expr())
            op = ctx.getChild(0).getText()
            return UnaryOp(op, operand)

    def visitIndex_expr(self, ctx: BKOOLParser.Index_exprContext):

        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            arr = self.visit(ctx.member_access_expr())
            idx = self.visit(ctx.expr())
            return ArrayCell(arr, idx)

    def visitMember_access_expr(self, ctx: BKOOLParser.Member_access_exprContext):

        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            obj = self.visit(ctx.member_access_expr())
            if ctx.ID():
                field = Id(ctx.ID().getText())
                return FieldAccess(obj, field)
            else:
                ident, param = self.visit(ctx.method_call())
                return CallExpr(obj, ident, param)

    def visitMethod_call(self, ctx: BKOOLParser.Method_callContext) -> Tuple[Id, List[Expr]]:
        ident = Id(ctx.ID().getText())
        expr_list = self.visit(ctx.expr_list()) if ctx.expr_list() else []
        return ident, expr_list

    def visitNew_expr(self, ctx: BKOOLParser.New_exprContext):

        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary_expr())
        else:
            class_name = Id(ctx.ID().getText())
            param = self.visit(ctx.expr_list()) if ctx.expr_list() else []
            return NewExpr(class_name, param)

    def visitPrimary_expr(self, ctx):
        # type: (BKOOLParser.Primary_exprContext) -> Union[Id, SelfLiteral, NullLiteral, Expr]
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.THIS():
            return SelfLiteral()
        elif ctx.NIL():
            return NullLiteral()
        else:
            return self.visit(ctx.literal())

    def visitExpr_list(self, ctx: BKOOLParser.Expr_listContext) -> List[Expr]:
        return [self.visit(expr) for expr in ctx.expr()]

    def visitLiteral(self, ctx: BKOOLParser.LiteralContext) -> Literal:
        if ctx.INTEGER_LITERAL():
            return IntLiteral(int(ctx.INTEGER_LITERAL().getText()))
        elif ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        elif ctx.BOOLEAN_LITERAL():
            return BooleanLiteral(ctx.BOOLEAN_LITERAL().getText() == "true")
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        else:
            return self.visit(ctx.array_literal())

    def visitArray_literal(self, ctx: BKOOLParser.Array_literalContext):
        return ArrayLiteral([self.visit(c) for c in ctx.literal()])
