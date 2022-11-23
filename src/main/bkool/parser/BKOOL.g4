grammar BKOOL;


@lexer::header {
from lexererr import *
}

//@lexer::members {
//def emit(self):
//    tk = self.type
//    result = super().emit()
//    if tk == self.UNCLOSE_STRING:
//        raise UncloseString(result.text)
//    elif tk == self.ILLEGAL_ESCAPE:
//        raise IllegalEscape(result.text)
//    elif tk == self.ERROR_CHAR:
//        raise ErrorToken(result.text)
//    elif tk == self.UNTERMINATED_COMMENT:
//        raise UnterminatedComment(result.text)
//    else: return result;
//}

options {
	language = Python3;
}

/*
 * Rules Region
 * ###########################################################################
 */

program: class_decl* EOF;

//test_Stmt: stmt+ EOF;
test_expr: expr+ EOF;

/* Class Declaration
class {Name} (extends {Name})?
*/
class_decl
    : CLASS ID (EXTENDS ID)?
        class_body;

/* Class body
    { * }
*/
class_body
    : LCB class_body_decl* RCB
    ;

/* Class body declare stuff:
    ffloat a() {}
    s int a;
*/
class_body_decl
    : constructor_decl
    | field_decl
    | static_field_decl
    | const_field_decl
    | static_constant_decl
    | method_decl
    ;

/* field/attribute declaration
    - split `field_decl` into 4 rule?
    - merge them all, which is easier? me like splitting
*/
// int a, b = 0;
field_decl
    : bkooltype var_decl_list SEMI
    ;

const_field_decl
    : FINAL bkooltype const_decl_list SEMI
    ;

static_field_decl
    : STATIC bkooltype var_decl_list SEMI
    ;

static_constant_decl
    : STATIC FINAL bkooltype const_decl_list SEMI
    | FINAL STATIC bkooltype const_decl_list SEMI
    ;

// Id list and initilisation
var_decl_list: var_decl_unit (COMMA var_decl_unit)* ;
var_decl_unit: ID (INIT_OP expr)?;

const_decl_list: const_decl_unit (COMMA const_decl_unit)*;
const_decl_unit: ID (INIT_OP expr)?;  // assignment 3 deal with not initialised

/* method declaration
*/
method_decl
    : STATIC? bkooltype ID LP param_list? RP
        block_stmt
    ;

param_list
    : params (SEMI params)*
    ;

params
    : bkooltype id_list
    ;

id_list: ID (COMMA ID)*;


// constructor declaration
constructor_decl
    : ID LP param_list? RP
        block_stmt
    ;

// ######### TYPES ##########
bkooltype
    : primitive_type
    | array_type
    | ID // className
    ;

array_type:
    (primitive_type | ID) LSB INTEGER_LITERAL RSB
    ;

primitive_type
    : INT
    | FLOAT
    | BOOL
    | STRING
    | VOID
    ;


// ########## Statements #############

stmt
    : block_stmt
    | break_stmt
    | continue_stmt
    | return_stmt
    | method_invoke_stmt // class/object.funcall
    | assign_stmt
    | if_then_stmt
    | if_then_else_stmt
    | for_stmt
    ;


// Block
block_stmt:
    LCB
        local_decl_region?
        stmts?
    RCB;

local_decl_region: local_decl+ ;
stmts: stmt+;

// local variable declairation
local_decl: (local_var_decl | local_const_decl);

// Duplicate with field_decl
local_var_decl: bkooltype var_decl_list SEMI;

local_const_decl: FINAL bkooltype const_decl_list SEMI;


/* #### Assignment statement #### */
assign_stmt: lhs ASSIGN_OP expr SEMI;
// Stupid wrapper, probably unnecessary, but why the heck not?
lhs: LP lhs RP | lhs_base;

lhs_base: ID | lhs_member_access_expr | lhs_index_expr;

// Force [ expr ]
lhs_index_expr
    : member_access_expr (LSB expr RSB)
    ;

// Force .
lhs_member_access_expr
    : new_expr bop=DOT ( ID )
    | new_expr bop=DOT (method_call)
    ;



// ######### IF STATEMENT ############
// AVOID DANGLING ELSE, but honestly, who cares?
if_then_stmt
	:	IF expr THEN stmt
	;

if_then_else_stmt
	:	IF expr THEN stmt_no_short_if ELSE stmt
	;

if_then_else_stmt_no_short_if
	:	IF expr THEN stmt_no_short_if ELSE stmt_no_short_if
	;

stmt_no_short_if
    : stmt_no_trailing_substmt
    | if_then_else_stmt_no_short_if
    | for_stmt_no_short_if
    ;

stmt_no_trailing_substmt
    : block_stmt
    | break_stmt
    | continue_stmt
    | return_stmt
    | method_invoke_stmt
    | assign_stmt
    ;

// ########## FOR STATEMENT ################
for_stmt
    : FOR (ID ASSIGN_OP expr) (TO | DOWNTO) (expr) DO stmt
    ;

for_stmt_no_short_if
    : FOR (ID ASSIGN_OP expr) (TO | DOWNTO) (expr) DO stmt_no_short_if
    ;

// #### OTHERS STATEMENT ####
break_stmt: BREAK SEMI;
continue_stmt: CONTINUE SEMI;
return_stmt: RETURN expr SEMI;

// #### Method / funcall. ####
method_invoke_stmt : expr DOT method_call SEMI;

/*
 * ## EXPRESSION ##
 */
// EXPRESSION
expr: relational_expr;

// Relational expression (Greater/Less)
relational_expr
    : equality_expr
    (   LT_OP
    |   GT_OP
    |   LEQ_OP
    |   GEQ_OP
    ) equality_expr
    | equality_expr
    ;

// Relational expression (Equal/Not equal)
equality_expr
    : logical_expr
    (   EQ_OP
    |   NEQ_OP
    ) logical_expr
    | logical_expr
    ;

// Logical expression
logical_expr
    : logical_expr
    (   AND_OP
    |   OR_OP
    ) additive_expr
    | additive_expr
    ;

// Add, Substract expression
additive_expr
    : additive_expr
    (   ADD_OP
    |   SUB_OP
    ) multiply_expr
    | multiply_expr
    ;

// Mul div mod expression
// should op multiplicative_expression but it's f long.
multiply_expr
    : multiply_expr
    (   MUL_OP
    |   FLOAT_DIV_OP
    |   INT_DIV_OP
    |   MOD_OP
    ) concat_expr
    | concat_expr
    ;

// Concat expression
concat_expr
    : concat_expr
    (   CONCAT_OP
    ) negate_expr
    | negate_expr
    ;

// Boolean neg expression
negate_expr
    :
    (   NOT_OP
    ) negate_expr
    | unary_arithmetic_expr
    ;

// unary expression
unary_arithmetic_expr
    :
    ( ADD_OP
    | SUB_OP
    ) unary_arithmetic_expr
    | index_expr
    ;

//// target expression, there is only 1 dimension array, so...
index_expr
    : member_access_expr (LSB expr RSB)
    | member_access_expr
    ;

// op is clear
member_access_expr
    : member_access_expr bop=DOT (method_call)
    | member_access_expr bop=DOT ( ID )
    | new_expr
    ;

method_call: ID LP (expr_list)? RP;


// new expression
new_expr
    : NEW ID LP (expr_list)? RP
    | primary_expr
    ;

// basic shit
primary_expr
    : literal
    | ID
    | THIS
    | LP expr RP
    | NIL
    ;

expr_list: expr (COMMA expr)*;
/*
 * ## EXPRESSION ##
 */

// ######## Literals ############
literal
    : INTEGER_LITERAL
    | FLOAT_LITERAL
    | BOOLEAN_LITERAL
    | STRING_LITERAL
    | array_literal
    ;

// ######## Array literal ############
array_literal: LCB ( literal (COMMA literal)* ) RCB;

// ________________________________________________________________________
/*
 * End Rules Region
 * ###########################################################################
 */

/*
 * TOKEN REGION
 * ###########################################################################
 */

// ######## KEYWORDS ############
// PRIMITIVE TYPES * 5
BOOL: 'boolean';
INT: 'int';
FLOAT: 'float';
STRING: 'string';
VOID: 'void';

// CONDITIONAL * 3
IF: 'if';
ELSE: 'else';
THEN: 'then';

// CONTROLL FLOW * 6
// FOR * TO * DO format, no WHILE statement
FOR: 'for';
TO: 'to';
DOWNTO: 'downto';
DO: 'do';
BREAK: 'break';
CONTINUE: 'continue';

// CLASS KEYWORDS * 5
CLASS: 'class';
EXTENDS: 'extends';
FINAL: 'final';
STATIC: 'static';
THIS: 'this';

// OTHERS * 3
RETURN: 'return';
NEW: 'new';
NIL: 'nil';

// BOOLEAN LITERAL * 2
fragment TRUE: 'true';
fragment FALSE: 'false';

// ######## END KEYWORDS ############

// ________________________________________________________________________

// ######## OPERATORS ############
ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
FLOAT_DIV_OP: '/';
INT_DIV_OP: '\\';
MOD_OP: '%';
NEQ_OP: '!=';
EQ_OP: '==';
LT_OP:'<';
GT_OP: '>';
LEQ_OP:'<=';
GEQ_OP:'>=';
OR_OP:'||';
AND_OP:'&&';
NOT_OP:'!';
CONCAT_OP:'^';
ASSIGN_OP: ':=';
INIT_OP: '=';
// new op in KEYWODS

// ######## END OPERATORS ############

// ________________________________________________________________________

// ######## SEPERATORS ############
/*  notes:
 *  BKOOL spec states: ' ... left parenthesis (’{’) ... '  (3.6, pg. 7)
 *  this seems to_block be incorrect (https://en.wikipedia.org/wiki/Bracket)
 */

LP: '('; // Left Parenthesis
RP: ')'; // Right Parenthesis
LSB: '['; // Left Square Bracket
RSB: ']'; // Right Square Bracket
LCB: '{'; // Left Curly Bracket
RCB: '}'; // Right Curly Bracket

SEMI: ';'; // Semicolon
COLON: ':'; // Colon
DOT: '.';
COMMA: ','; // Comma

// ######## END SEPERATORS ############

// ________________________________________________________________________

// ######## LITERALS ############
/*
 * Array does not seem to_block be a TOKEN but more likely to_block be a rule, so it is not here
 */
// INT LITERAL
INTEGER_LITERAL: DigitSequence;

fragment DigitSequence: DIGIT+;
fragment DIGIT: [0-9];

// FLOAT LITERAL
FLOAT_LITERAL
    : FractionalConstant ExponentPart?
	| DigitSequence ExponentPart
	;

fragment FractionalConstant
    : DigitSequence DOT DigitSequence?
    ;

fragment ExponentPart
    : [Ee] SIGN? DigitSequence;

fragment SIGN: [+-];

// BOOLEAN LITERAL
BOOLEAN_LITERAL: TRUE | FALSE;

//test_Str: STRING_LITERAL* EOF;
//test_unclose: UNCLOSE_STRING* EOF;

// STRING LITERAL
STRING_LITERAL: ('"') CHAR_LITERAL* ('"');

fragment CHAR_LITERAL:
    (~[\f\n\r"\\]) | ESCAPE_SEQUENCE ;
//  ~( '\b' | '\f' | '\n' | '\r' | '\t' | '\\' ) | ESCAPE_SEQUENCE;

fragment ESCAPE_SEQUENCE
	: '\\b'
	| '\\f'
	| '\\n'
	| '\\r'
	| '\\t'
	| '\\"'
    | '\\\\'
    ;

UNCLOSE_STRING: '"' (~([\f\n\r"\\]) | ESCAPE_SEQUENCE)* ( [\r\n\f] | EOF )
	{
        __forbid = ['\n']
        if self.text[-1] in __forbid:
            # unclose string due to new new line
            if len(self.text) > 2 and self.text[-2] == '\r':
                # On windows NewLine is (\r\n),
                # raise txt[:-1] cause a new line with (\r)
                # Hopefully no testcase on linux will include (\r\n)
                raise UncloseString(self.text[:-2])
            else:
                raise UncloseString(self.text[:-1])
        else:
            # Unclose string due to EOF
            raise UncloseString(self.text)
    }
	;

ILLEGAL_ESCAPE: ('"') CHAR_LITERAL* ILLEGAL_ESCAPE_SEQ
    {
        raise IllegalEscape(self.text)
    };

fragment ILLEGAL_ESCAPE_SEQ
    : '\\' ~[bfnrt"\\]?
    ;

// ######## END LITERALS ############

// ________________________________________________________________________

// ######## OTHER ############
// Identifier
ID: [_a-zA-Z][_a-zA-Z0-9]*;

// Skip Stuff
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

// COMMENT
COMMENT: (BLOCK_COMMENT | LINE_COMMENT) -> skip;
BLOCK_COMMENT: '/*' .*? ('*/' | EOF);
LINE_COMMENT: '#' ~([\n])* EOF?;


// ERROR REGION
ERROR_CHAR: . {raise ErrorToken(self.text)};

// ######## END OTHER ############
/*
 * TOKEN REGION
 * ###########################################################################
 */