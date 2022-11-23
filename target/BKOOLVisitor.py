# type: ignore
# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_decl.
    def visitClass_decl(self, ctx:BKOOLParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_body.
    def visitClass_body(self, ctx:BKOOLParser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_body_decl.
    def visitClass_body_decl(self, ctx:BKOOLParser.Class_body_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#field_decl.
    def visitField_decl(self, ctx:BKOOLParser.Field_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#const_field_decl.
    def visitConst_field_decl(self, ctx:BKOOLParser.Const_field_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#static_field_decl.
    def visitStatic_field_decl(self, ctx:BKOOLParser.Static_field_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#static_constant_decl.
    def visitStatic_constant_decl(self, ctx:BKOOLParser.Static_constant_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl_list.
    def visitVar_decl_list(self, ctx:BKOOLParser.Var_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl_unit.
    def visitVar_decl_unit(self, ctx:BKOOLParser.Var_decl_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#const_decl_list.
    def visitConst_decl_list(self, ctx:BKOOLParser.Const_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#const_decl_unit.
    def visitConst_decl_unit(self, ctx:BKOOLParser.Const_decl_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_decl.
    def visitMethod_decl(self, ctx:BKOOLParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param_list.
    def visitParam_list(self, ctx:BKOOLParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#params.
    def visitParams(self, ctx:BKOOLParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#id_list.
    def visitId_list(self, ctx:BKOOLParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor_decl.
    def visitConstructor_decl(self, ctx:BKOOLParser.Constructor_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bkooltype.
    def visitBkooltype(self, ctx:BKOOLParser.BkooltypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_stmt.
    def visitBlock_stmt(self, ctx:BKOOLParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#local_decl_region.
    def visitLocal_decl_region(self, ctx:BKOOLParser.Local_decl_regionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmts.
    def visitStmts(self, ctx:BKOOLParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#local_decl.
    def visitLocal_decl(self, ctx:BKOOLParser.Local_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#local_var_decl.
    def visitLocal_var_decl(self, ctx:BKOOLParser.Local_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#local_const_decl.
    def visitLocal_const_decl(self, ctx:BKOOLParser.Local_const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKOOLParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs_base.
    def visitLhs_base(self, ctx:BKOOLParser.Lhs_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs_index_expr.
    def visitLhs_index_expr(self, ctx:BKOOLParser.Lhs_index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs_member_access_expr.
    def visitLhs_member_access_expr(self, ctx:BKOOLParser.Lhs_member_access_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_then_stmt.
    def visitIf_then_stmt(self, ctx:BKOOLParser.If_then_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_then_else_stmt.
    def visitIf_then_else_stmt(self, ctx:BKOOLParser.If_then_else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_then_else_stmt_no_short_if.
    def visitIf_then_else_stmt_no_short_if(self, ctx:BKOOLParser.If_then_else_stmt_no_short_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_no_short_if.
    def visitStmt_no_short_if(self, ctx:BKOOLParser.Stmt_no_short_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_no_trailing_substmt.
    def visitStmt_no_trailing_substmt(self, ctx:BKOOLParser.Stmt_no_trailing_substmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_stmt.
    def visitFor_stmt(self, ctx:BKOOLParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_stmt_no_short_if.
    def visitFor_stmt_no_short_if(self, ctx:BKOOLParser.For_stmt_no_short_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKOOLParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKOOLParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKOOLParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_invoke_stmt.
    def visitMethod_invoke_stmt(self, ctx:BKOOLParser.Method_invoke_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#relational_expr.
    def visitRelational_expr(self, ctx:BKOOLParser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#equality_expr.
    def visitEquality_expr(self, ctx:BKOOLParser.Equality_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#logical_expr.
    def visitLogical_expr(self, ctx:BKOOLParser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#additive_expr.
    def visitAdditive_expr(self, ctx:BKOOLParser.Additive_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#multiply_expr.
    def visitMultiply_expr(self, ctx:BKOOLParser.Multiply_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#concat_expr.
    def visitConcat_expr(self, ctx:BKOOLParser.Concat_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#negate_expr.
    def visitNegate_expr(self, ctx:BKOOLParser.Negate_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#unary_arithmetic_expr.
    def visitUnary_arithmetic_expr(self, ctx:BKOOLParser.Unary_arithmetic_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#index_expr.
    def visitIndex_expr(self, ctx:BKOOLParser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member_access_expr.
    def visitMember_access_expr(self, ctx:BKOOLParser.Member_access_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_call.
    def visitMethod_call(self, ctx:BKOOLParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#new_expr.
    def visitNew_expr(self, ctx:BKOOLParser.New_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primary_expr.
    def visitPrimary_expr(self, ctx:BKOOLParser.Primary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr_list.
    def visitExpr_list(self, ctx:BKOOLParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_literal.
    def visitArray_literal(self, ctx:BKOOLParser.Array_literalContext):
        return self.visitChildren(ctx)



del BKOOLParser