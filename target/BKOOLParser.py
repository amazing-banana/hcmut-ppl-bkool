# type: ignore
# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0227\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\7\2|\n\2\f\2\16\2\177\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3\u0087\n\3\3\3\3\3\3\4\3\4\7\4\u008d")
        buf.write("\n\4\f\4\16\4\u0090\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\u009a\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\t\u00b6\n\t\3\n\3\n\3\n\7\n\u00bb\n\n\f")
        buf.write("\n\16\n\u00be\13\n\3\13\3\13\3\13\5\13\u00c3\n\13\3\f")
        buf.write("\3\f\3\f\7\f\u00c8\n\f\f\f\16\f\u00cb\13\f\3\r\3\r\3\r")
        buf.write("\5\r\u00d0\n\r\3\16\5\16\u00d3\n\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00d9\n\16\3\16\3\16\3\16\3\17\3\17\3\17\7\17\u00e1")
        buf.write("\n\17\f\17\16\17\u00e4\13\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\7\21\u00ec\n\21\f\21\16\21\u00ef\13\21\3\22\3\22")
        buf.write("\3\22\5\22\u00f4\n\22\3\22\3\22\3\22\3\23\3\23\3\23\5")
        buf.write("\23\u00fc\n\23\3\24\3\24\5\24\u0100\n\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\5\26\u0111\n\26\3\27\3\27\5\27\u0115\n\27\3\27\5")
        buf.write("\27\u0118\n\27\3\27\3\27\3\30\6\30\u011d\n\30\r\30\16")
        buf.write("\30\u011e\3\31\6\31\u0122\n\31\r\31\16\31\u0123\3\32\3")
        buf.write("\32\5\32\u0128\n\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u013d\n\36\3\37\3\37\3\37\5\37\u0142\n\37\3")
        buf.write(" \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\5!\u0151\n!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\5%\u0169\n%\3&\3&\3&\3&\3&\3&\5&\u0171\n")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(")
        buf.write("\3(\3(\3(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3,\3-\3-\3.\3.\3.\3.\3.\5.\u019d\n.\3/\3/\3/\3")
        buf.write("/\3/\5/\u01a4\n/\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u01ac")
        buf.write("\n\60\f\60\16\60\u01af\13\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\7\61\u01b7\n\61\f\61\16\61\u01ba\13\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\7\62\u01c2\n\62\f\62\16\62\u01c5")
        buf.write("\13\62\3\63\3\63\3\63\3\63\3\63\3\63\7\63\u01cd\n\63\f")
        buf.write("\63\16\63\u01d0\13\63\3\64\3\64\3\64\5\64\u01d5\n\64\3")
        buf.write("\65\3\65\3\65\5\65\u01da\n\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\5\66\u01e2\n\66\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\7\67\u01ed\n\67\f\67\16\67\u01f0\13\67\3")
        buf.write("8\38\38\58\u01f5\n8\38\38\39\39\39\39\59\u01fd\n9\39\3")
        buf.write("9\59\u0201\n9\3:\3:\3:\3:\3:\3:\3:\3:\5:\u020b\n:\3;\3")
        buf.write(";\3;\7;\u0210\n;\f;\16;\u0213\13;\3<\3<\3<\3<\3<\5<\u021a")
        buf.write("\n<\3=\3=\3=\3=\7=\u0220\n=\f=\16=\u0223\13=\3=\3=\3=")
        buf.write("\2\7^`bdl>\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvx\2")
        buf.write("\t\3\2\3\7\3\2\f\r\3\2!$\3\2\37 \3\2%&\3\2\31\32\3\2\33")
        buf.write("\36\2\u022f\2}\3\2\2\2\4\u0082\3\2\2\2\6\u008a\3\2\2\2")
        buf.write("\b\u0099\3\2\2\2\n\u009b\3\2\2\2\f\u009f\3\2\2\2\16\u00a4")
        buf.write("\3\2\2\2\20\u00b5\3\2\2\2\22\u00b7\3\2\2\2\24\u00bf\3")
        buf.write("\2\2\2\26\u00c4\3\2\2\2\30\u00cc\3\2\2\2\32\u00d2\3\2")
        buf.write("\2\2\34\u00dd\3\2\2\2\36\u00e5\3\2\2\2 \u00e8\3\2\2\2")
        buf.write("\"\u00f0\3\2\2\2$\u00fb\3\2\2\2&\u00ff\3\2\2\2(\u0105")
        buf.write("\3\2\2\2*\u0110\3\2\2\2,\u0112\3\2\2\2.\u011c\3\2\2\2")
        buf.write("\60\u0121\3\2\2\2\62\u0127\3\2\2\2\64\u0129\3\2\2\2\66")
        buf.write("\u012d\3\2\2\28\u0132\3\2\2\2:\u013c\3\2\2\2<\u0141\3")
        buf.write("\2\2\2>\u0143\3\2\2\2@\u0150\3\2\2\2B\u0152\3\2\2\2D\u0157")
        buf.write("\3\2\2\2F\u015e\3\2\2\2H\u0168\3\2\2\2J\u0170\3\2\2\2")
        buf.write("L\u0172\3\2\2\2N\u017c\3\2\2\2P\u0186\3\2\2\2R\u0189\3")
        buf.write("\2\2\2T\u018c\3\2\2\2V\u0190\3\2\2\2X\u0195\3\2\2\2Z\u019c")
        buf.write("\3\2\2\2\\\u01a3\3\2\2\2^\u01a5\3\2\2\2`\u01b0\3\2\2\2")
        buf.write("b\u01bb\3\2\2\2d\u01c6\3\2\2\2f\u01d4\3\2\2\2h\u01d9\3")
        buf.write("\2\2\2j\u01e1\3\2\2\2l\u01e3\3\2\2\2n\u01f1\3\2\2\2p\u0200")
        buf.write("\3\2\2\2r\u020a\3\2\2\2t\u020c\3\2\2\2v\u0219\3\2\2\2")
        buf.write("x\u021b\3\2\2\2z|\5\4\3\2{z\3\2\2\2|\177\3\2\2\2}{\3\2")
        buf.write("\2\2}~\3\2\2\2~\u0080\3\2\2\2\177}\3\2\2\2\u0080\u0081")
        buf.write("\7\2\2\3\u0081\3\3\2\2\2\u0082\u0083\7\21\2\2\u0083\u0086")
        buf.write("\7;\2\2\u0084\u0085\7\22\2\2\u0085\u0087\7;\2\2\u0086")
        buf.write("\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u0089\5\6\4\2\u0089\5\3\2\2\2\u008a\u008e\7/\2")
        buf.write("\2\u008b\u008d\5\b\5\2\u008c\u008b\3\2\2\2\u008d\u0090")
        buf.write("\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write("\u0091\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0092\7\60\2")
        buf.write("\2\u0092\7\3\2\2\2\u0093\u009a\5\"\22\2\u0094\u009a\5")
        buf.write("\n\6\2\u0095\u009a\5\16\b\2\u0096\u009a\5\f\7\2\u0097")
        buf.write("\u009a\5\20\t\2\u0098\u009a\5\32\16\2\u0099\u0093\3\2")
        buf.write("\2\2\u0099\u0094\3\2\2\2\u0099\u0095\3\2\2\2\u0099\u0096")
        buf.write("\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u0098\3\2\2\2\u009a")
        buf.write("\t\3\2\2\2\u009b\u009c\5$\23\2\u009c\u009d\5\22\n\2\u009d")
        buf.write("\u009e\7\61\2\2\u009e\13\3\2\2\2\u009f\u00a0\7\23\2\2")
        buf.write("\u00a0\u00a1\5$\23\2\u00a1\u00a2\5\26\f\2\u00a2\u00a3")
        buf.write("\7\61\2\2\u00a3\r\3\2\2\2\u00a4\u00a5\7\24\2\2\u00a5\u00a6")
        buf.write("\5$\23\2\u00a6\u00a7\5\22\n\2\u00a7\u00a8\7\61\2\2\u00a8")
        buf.write("\17\3\2\2\2\u00a9\u00aa\7\24\2\2\u00aa\u00ab\7\23\2\2")
        buf.write("\u00ab\u00ac\5$\23\2\u00ac\u00ad\5\26\f\2\u00ad\u00ae")
        buf.write("\7\61\2\2\u00ae\u00b6\3\2\2\2\u00af\u00b0\7\23\2\2\u00b0")
        buf.write("\u00b1\7\24\2\2\u00b1\u00b2\5$\23\2\u00b2\u00b3\5\26\f")
        buf.write("\2\u00b3\u00b4\7\61\2\2\u00b4\u00b6\3\2\2\2\u00b5\u00a9")
        buf.write("\3\2\2\2\u00b5\u00af\3\2\2\2\u00b6\21\3\2\2\2\u00b7\u00bc")
        buf.write("\5\24\13\2\u00b8\u00b9\7\64\2\2\u00b9\u00bb\5\24\13\2")
        buf.write("\u00ba\u00b8\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba\3")
        buf.write("\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\23\3\2\2\2\u00be\u00bc")
        buf.write("\3\2\2\2\u00bf\u00c2\7;\2\2\u00c0\u00c1\7*\2\2\u00c1\u00c3")
        buf.write("\5X-\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\25")
        buf.write("\3\2\2\2\u00c4\u00c9\5\30\r\2\u00c5\u00c6\7\64\2\2\u00c6")
        buf.write("\u00c8\5\30\r\2\u00c7\u00c5\3\2\2\2\u00c8\u00cb\3\2\2")
        buf.write("\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\27\3")
        buf.write("\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cf\7;\2\2\u00cd\u00ce")
        buf.write("\7*\2\2\u00ce\u00d0\5X-\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\31\3\2\2\2\u00d1\u00d3\7\24\2\2\u00d2\u00d1")
        buf.write("\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\u00d5\5$\23\2\u00d5\u00d6\7;\2\2\u00d6\u00d8\7+\2\2\u00d7")
        buf.write("\u00d9\5\34\17\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2")
        buf.write("\2\u00d9\u00da\3\2\2\2\u00da\u00db\7,\2\2\u00db\u00dc")
        buf.write("\5,\27\2\u00dc\33\3\2\2\2\u00dd\u00e2\5\36\20\2\u00de")
        buf.write("\u00df\7\61\2\2\u00df\u00e1\5\36\20\2\u00e0\u00de\3\2")
        buf.write("\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3\35\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6")
        buf.write("\5$\23\2\u00e6\u00e7\5 \21\2\u00e7\37\3\2\2\2\u00e8\u00ed")
        buf.write("\7;\2\2\u00e9\u00ea\7\64\2\2\u00ea\u00ec\7;\2\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2")
        buf.write("\u00ed\u00ee\3\2\2\2\u00ee!\3\2\2\2\u00ef\u00ed\3\2\2")
        buf.write("\2\u00f0\u00f1\7;\2\2\u00f1\u00f3\7+\2\2\u00f2\u00f4\5")
        buf.write("\34\17\2\u00f3\u00f2\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5\u00f6\7,\2\2\u00f6\u00f7\5,\27\2")
        buf.write("\u00f7#\3\2\2\2\u00f8\u00fc\5(\25\2\u00f9\u00fc\5&\24")
        buf.write("\2\u00fa\u00fc\7;\2\2\u00fb\u00f8\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc%\3\2\2\2\u00fd\u0100")
        buf.write("\5(\25\2\u00fe\u0100\7;\2\2\u00ff\u00fd\3\2\2\2\u00ff")
        buf.write("\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\7-\2\2")
        buf.write("\u0102\u0103\7\65\2\2\u0103\u0104\7.\2\2\u0104\'\3\2\2")
        buf.write("\2\u0105\u0106\t\2\2\2\u0106)\3\2\2\2\u0107\u0111\5,\27")
        buf.write("\2\u0108\u0111\5P)\2\u0109\u0111\5R*\2\u010a\u0111\5T")
        buf.write("+\2\u010b\u0111\5V,\2\u010c\u0111\58\35\2\u010d\u0111")
        buf.write("\5B\"\2\u010e\u0111\5D#\2\u010f\u0111\5L\'\2\u0110\u0107")
        buf.write("\3\2\2\2\u0110\u0108\3\2\2\2\u0110\u0109\3\2\2\2\u0110")
        buf.write("\u010a\3\2\2\2\u0110\u010b\3\2\2\2\u0110\u010c\3\2\2\2")
        buf.write("\u0110\u010d\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u010f\3")
        buf.write("\2\2\2\u0111+\3\2\2\2\u0112\u0114\7/\2\2\u0113\u0115\5")
        buf.write(".\30\2\u0114\u0113\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117")
        buf.write("\3\2\2\2\u0116\u0118\5\60\31\2\u0117\u0116\3\2\2\2\u0117")
        buf.write("\u0118\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a\7\60\2")
        buf.write("\2\u011a-\3\2\2\2\u011b\u011d\5\62\32\2\u011c\u011b\3")
        buf.write("\2\2\2\u011d\u011e\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f")
        buf.write("\3\2\2\2\u011f/\3\2\2\2\u0120\u0122\5*\26\2\u0121\u0120")
        buf.write("\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0121\3\2\2\2\u0123")
        buf.write("\u0124\3\2\2\2\u0124\61\3\2\2\2\u0125\u0128\5\64\33\2")
        buf.write("\u0126\u0128\5\66\34\2\u0127\u0125\3\2\2\2\u0127\u0126")
        buf.write("\3\2\2\2\u0128\63\3\2\2\2\u0129\u012a\5$\23\2\u012a\u012b")
        buf.write("\5\22\n\2\u012b\u012c\7\61\2\2\u012c\65\3\2\2\2\u012d")
        buf.write("\u012e\7\23\2\2\u012e\u012f\5$\23\2\u012f\u0130\5\26\f")
        buf.write("\2\u0130\u0131\7\61\2\2\u0131\67\3\2\2\2\u0132\u0133\5")
        buf.write(":\36\2\u0133\u0134\7)\2\2\u0134\u0135\5X-\2\u0135\u0136")
        buf.write("\7\61\2\2\u01369\3\2\2\2\u0137\u0138\7+\2\2\u0138\u0139")
        buf.write("\5:\36\2\u0139\u013a\7,\2\2\u013a\u013d\3\2\2\2\u013b")
        buf.write("\u013d\5<\37\2\u013c\u0137\3\2\2\2\u013c\u013b\3\2\2\2")
        buf.write("\u013d;\3\2\2\2\u013e\u0142\7;\2\2\u013f\u0142\5@!\2\u0140")
        buf.write("\u0142\5> \2\u0141\u013e\3\2\2\2\u0141\u013f\3\2\2\2\u0141")
        buf.write("\u0140\3\2\2\2\u0142=\3\2\2\2\u0143\u0144\5l\67\2\u0144")
        buf.write("\u0145\7-\2\2\u0145\u0146\5X-\2\u0146\u0147\7.\2\2\u0147")
        buf.write("?\3\2\2\2\u0148\u0149\5p9\2\u0149\u014a\7\63\2\2\u014a")
        buf.write("\u014b\7;\2\2\u014b\u0151\3\2\2\2\u014c\u014d\5p9\2\u014d")
        buf.write("\u014e\7\63\2\2\u014e\u014f\5n8\2\u014f\u0151\3\2\2\2")
        buf.write("\u0150\u0148\3\2\2\2\u0150\u014c\3\2\2\2\u0151A\3\2\2")
        buf.write("\2\u0152\u0153\7\b\2\2\u0153\u0154\5X-\2\u0154\u0155\7")
        buf.write("\n\2\2\u0155\u0156\5*\26\2\u0156C\3\2\2\2\u0157\u0158")
        buf.write("\7\b\2\2\u0158\u0159\5X-\2\u0159\u015a\7\n\2\2\u015a\u015b")
        buf.write("\5H%\2\u015b\u015c\7\t\2\2\u015c\u015d\5*\26\2\u015dE")
        buf.write("\3\2\2\2\u015e\u015f\7\b\2\2\u015f\u0160\5X-\2\u0160\u0161")
        buf.write("\7\n\2\2\u0161\u0162\5H%\2\u0162\u0163\7\t\2\2\u0163\u0164")
        buf.write("\5H%\2\u0164G\3\2\2\2\u0165\u0169\5J&\2\u0166\u0169\5")
        buf.write("F$\2\u0167\u0169\5N(\2\u0168\u0165\3\2\2\2\u0168\u0166")
        buf.write("\3\2\2\2\u0168\u0167\3\2\2\2\u0169I\3\2\2\2\u016a\u0171")
        buf.write("\5,\27\2\u016b\u0171\5P)\2\u016c\u0171\5R*\2\u016d\u0171")
        buf.write("\5T+\2\u016e\u0171\5V,\2\u016f\u0171\58\35\2\u0170\u016a")
        buf.write("\3\2\2\2\u0170\u016b\3\2\2\2\u0170\u016c\3\2\2\2\u0170")
        buf.write("\u016d\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u016f\3\2\2\2")
        buf.write("\u0171K\3\2\2\2\u0172\u0173\7\13\2\2\u0173\u0174\7;\2")
        buf.write("\2\u0174\u0175\7)\2\2\u0175\u0176\5X-\2\u0176\u0177\3")
        buf.write("\2\2\2\u0177\u0178\t\3\2\2\u0178\u0179\5X-\2\u0179\u017a")
        buf.write("\7\16\2\2\u017a\u017b\5*\26\2\u017bM\3\2\2\2\u017c\u017d")
        buf.write("\7\13\2\2\u017d\u017e\7;\2\2\u017e\u017f\7)\2\2\u017f")
        buf.write("\u0180\5X-\2\u0180\u0181\3\2\2\2\u0181\u0182\t\3\2\2\u0182")
        buf.write("\u0183\5X-\2\u0183\u0184\7\16\2\2\u0184\u0185\5H%\2\u0185")
        buf.write("O\3\2\2\2\u0186\u0187\7\17\2\2\u0187\u0188\7\61\2\2\u0188")
        buf.write("Q\3\2\2\2\u0189\u018a\7\20\2\2\u018a\u018b\7\61\2\2\u018b")
        buf.write("S\3\2\2\2\u018c\u018d\7\26\2\2\u018d\u018e\5X-\2\u018e")
        buf.write("\u018f\7\61\2\2\u018fU\3\2\2\2\u0190\u0191\5X-\2\u0191")
        buf.write("\u0192\7\63\2\2\u0192\u0193\5n8\2\u0193\u0194\7\61\2\2")
        buf.write("\u0194W\3\2\2\2\u0195\u0196\5Z.\2\u0196Y\3\2\2\2\u0197")
        buf.write("\u0198\5\\/\2\u0198\u0199\t\4\2\2\u0199\u019a\5\\/\2\u019a")
        buf.write("\u019d\3\2\2\2\u019b\u019d\5\\/\2\u019c\u0197\3\2\2\2")
        buf.write("\u019c\u019b\3\2\2\2\u019d[\3\2\2\2\u019e\u019f\5^\60")
        buf.write("\2\u019f\u01a0\t\5\2\2\u01a0\u01a1\5^\60\2\u01a1\u01a4")
        buf.write("\3\2\2\2\u01a2\u01a4\5^\60\2\u01a3\u019e\3\2\2\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a4]\3\2\2\2\u01a5\u01a6\b\60\1\2\u01a6")
        buf.write("\u01a7\5`\61\2\u01a7\u01ad\3\2\2\2\u01a8\u01a9\f\4\2\2")
        buf.write("\u01a9\u01aa\t\6\2\2\u01aa\u01ac\5`\61\2\u01ab\u01a8\3")
        buf.write("\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae")
        buf.write("\3\2\2\2\u01ae_\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1")
        buf.write("\b\61\1\2\u01b1\u01b2\5b\62\2\u01b2\u01b8\3\2\2\2\u01b3")
        buf.write("\u01b4\f\4\2\2\u01b4\u01b5\t\7\2\2\u01b5\u01b7\5b\62\2")
        buf.write("\u01b6\u01b3\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3")
        buf.write("\2\2\2\u01b8\u01b9\3\2\2\2\u01b9a\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01bb\u01bc\b\62\1\2\u01bc\u01bd\5d\63\2\u01bd")
        buf.write("\u01c3\3\2\2\2\u01be\u01bf\f\4\2\2\u01bf\u01c0\t\b\2\2")
        buf.write("\u01c0\u01c2\5d\63\2\u01c1\u01be\3\2\2\2\u01c2\u01c5\3")
        buf.write("\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4c")
        buf.write("\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7\b\63\1\2\u01c7")
        buf.write("\u01c8\5f\64\2\u01c8\u01ce\3\2\2\2\u01c9\u01ca\f\4\2\2")
        buf.write("\u01ca\u01cb\7(\2\2\u01cb\u01cd\5f\64\2\u01cc\u01c9\3")
        buf.write("\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf")
        buf.write("\3\2\2\2\u01cfe\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d2")
        buf.write("\7\'\2\2\u01d2\u01d5\5f\64\2\u01d3\u01d5\5h\65\2\u01d4")
        buf.write("\u01d1\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5g\3\2\2\2\u01d6")
        buf.write("\u01d7\t\7\2\2\u01d7\u01da\5h\65\2\u01d8\u01da\5j\66\2")
        buf.write("\u01d9\u01d6\3\2\2\2\u01d9\u01d8\3\2\2\2\u01dai\3\2\2")
        buf.write("\2\u01db\u01dc\5l\67\2\u01dc\u01dd\7-\2\2\u01dd\u01de")
        buf.write("\5X-\2\u01de\u01df\7.\2\2\u01df\u01e2\3\2\2\2\u01e0\u01e2")
        buf.write("\5l\67\2\u01e1\u01db\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e2")
        buf.write("k\3\2\2\2\u01e3\u01e4\b\67\1\2\u01e4\u01e5\5p9\2\u01e5")
        buf.write("\u01ee\3\2\2\2\u01e6\u01e7\f\5\2\2\u01e7\u01e8\7\63\2")
        buf.write("\2\u01e8\u01ed\5n8\2\u01e9\u01ea\f\4\2\2\u01ea\u01eb\7")
        buf.write("\63\2\2\u01eb\u01ed\7;\2\2\u01ec\u01e6\3\2\2\2\u01ec\u01e9")
        buf.write("\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01efm\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1")
        buf.write("\u01f2\7;\2\2\u01f2\u01f4\7+\2\2\u01f3\u01f5\5t;\2\u01f4")
        buf.write("\u01f3\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f6\3\2\2\2")
        buf.write("\u01f6\u01f7\7,\2\2\u01f7o\3\2\2\2\u01f8\u01f9\7\27\2")
        buf.write("\2\u01f9\u01fa\7;\2\2\u01fa\u01fc\7+\2\2\u01fb\u01fd\5")
        buf.write("t;\2\u01fc\u01fb\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fe\u0201\7,\2\2\u01ff\u0201\5r:\2\u0200\u01f8")
        buf.write("\3\2\2\2\u0200\u01ff\3\2\2\2\u0201q\3\2\2\2\u0202\u020b")
        buf.write("\5v<\2\u0203\u020b\7;\2\2\u0204\u020b\7\25\2\2\u0205\u0206")
        buf.write("\7+\2\2\u0206\u0207\5X-\2\u0207\u0208\7,\2\2\u0208\u020b")
        buf.write("\3\2\2\2\u0209\u020b\7\30\2\2\u020a\u0202\3\2\2\2\u020a")
        buf.write("\u0203\3\2\2\2\u020a\u0204\3\2\2\2\u020a\u0205\3\2\2\2")
        buf.write("\u020a\u0209\3\2\2\2\u020bs\3\2\2\2\u020c\u0211\5X-\2")
        buf.write("\u020d\u020e\7\64\2\2\u020e\u0210\5X-\2\u020f\u020d\3")
        buf.write("\2\2\2\u0210\u0213\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212")
        buf.write("\3\2\2\2\u0212u\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u021a")
        buf.write("\7\65\2\2\u0215\u021a\7\66\2\2\u0216\u021a\7\67\2\2\u0217")
        buf.write("\u021a\78\2\2\u0218\u021a\5x=\2\u0219\u0214\3\2\2\2\u0219")
        buf.write("\u0215\3\2\2\2\u0219\u0216\3\2\2\2\u0219\u0217\3\2\2\2")
        buf.write("\u0219\u0218\3\2\2\2\u021aw\3\2\2\2\u021b\u021c\7/\2\2")
        buf.write("\u021c\u0221\5v<\2\u021d\u021e\7\64\2\2\u021e\u0220\5")
        buf.write("v<\2\u021f\u021d\3\2\2\2\u0220\u0223\3\2\2\2\u0221\u021f")
        buf.write("\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0224\3\2\2\2\u0223")
        buf.write("\u0221\3\2\2\2\u0224\u0225\7\60\2\2\u0225y\3\2\2\2/}\u0086")
        buf.write("\u008e\u0099\u00b5\u00bc\u00c2\u00c9\u00cf\u00d2\u00d8")
        buf.write("\u00e2\u00ed\u00f3\u00fb\u00ff\u0110\u0114\u0117\u011e")
        buf.write("\u0123\u0127\u013c\u0141\u0150\u0168\u0170\u019c\u01a3")
        buf.write("\u01ad\u01b8\u01c3\u01ce\u01d4\u01d9\u01e1\u01ec\u01ee")
        buf.write("\u01f4\u01fc\u0200\u020a\u0211\u0219\u0221")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'boolean'", "'int'", "'float'", "'string'", 
                     "'void'", "'if'", "'else'", "'then'", "'for'", "'to_block'",
                     "'downto'", "'do'", "'break'", "'continue'", "'class'", 
                     "'extends'", "'final'", "'static'", "'this'", "'return'", 
                     "'new'", "'nil'", "'+'", "'-'", "'*'", "'/'", "'\\'", 
                     "'%'", "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", 
                     "'||'", "'&&'", "'!'", "'^'", "':='", "'='", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "';'", "':'", "'.'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "BOOL", "INT", "FLOAT", "STRING", "VOID", 
                      "IF", "ELSE", "THEN", "FOR", "TO", "DOWNTO", "DO", 
                      "BREAK", "CONTINUE", "CLASS", "EXTENDS", "FINAL", 
                      "STATIC", "THIS", "RETURN", "NEW", "NIL", "ADD_OP", 
                      "SUB_OP", "MUL_OP", "FLOAT_DIV_OP", "INT_DIV_OP", 
                      "MOD_OP", "NEQ_OP", "EQ_OP", "LT_OP", "GT_OP", "LEQ_OP", 
                      "GEQ_OP", "OR_OP", "AND_OP", "NOT_OP", "CONCAT_OP", 
                      "ASSIGN_OP", "INIT_OP", "LP", "RP", "LSB", "RSB", 
                      "LCB", "RCB", "SEMI", "COLON", "DOT", "COMMA", "INTEGER_LITERAL", 
                      "FLOAT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ID", "WS", "COMMENT", 
                      "BLOCK_COMMENT", "LINE_COMMENT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_class_body = 2
    RULE_class_body_decl = 3
    RULE_field_decl = 4
    RULE_const_field_decl = 5
    RULE_static_field_decl = 6
    RULE_static_constant_decl = 7
    RULE_var_decl_list = 8
    RULE_var_decl_unit = 9
    RULE_const_decl_list = 10
    RULE_const_decl_unit = 11
    RULE_method_decl = 12
    RULE_param_list = 13
    RULE_params = 14
    RULE_id_list = 15
    RULE_constructor_decl = 16
    RULE_bkooltype = 17
    RULE_array_type = 18
    RULE_primitive_type = 19
    RULE_stmt = 20
    RULE_block_stmt = 21
    RULE_local_decl_region = 22
    RULE_stmts = 23
    RULE_local_decl = 24
    RULE_local_var_decl = 25
    RULE_local_const_decl = 26
    RULE_assign_stmt = 27
    RULE_lhs = 28
    RULE_lhs_base = 29
    RULE_lhs_index_expr = 30
    RULE_lhs_member_access_expr = 31
    RULE_if_then_stmt = 32
    RULE_if_then_else_stmt = 33
    RULE_if_then_else_stmt_no_short_if = 34
    RULE_stmt_no_short_if = 35
    RULE_stmt_no_trailing_substmt = 36
    RULE_for_stmt = 37
    RULE_for_stmt_no_short_if = 38
    RULE_break_stmt = 39
    RULE_continue_stmt = 40
    RULE_return_stmt = 41
    RULE_method_invoke_stmt = 42
    RULE_expr = 43
    RULE_relational_expr = 44
    RULE_equality_expr = 45
    RULE_logical_expr = 46
    RULE_additive_expr = 47
    RULE_multiply_expr = 48
    RULE_concat_expr = 49
    RULE_negate_expr = 50
    RULE_unary_arithmetic_expr = 51
    RULE_index_expr = 52
    RULE_member_access_expr = 53
    RULE_method_call = 54
    RULE_new_expr = 55
    RULE_primary_expr = 56
    RULE_expr_list = 57
    RULE_literal = 58
    RULE_array_literal = 59

    ruleNames =  [ "program", "class_decl", "class_body", "class_body_decl", 
                   "field_decl", "const_field_decl", "static_field_decl", 
                   "static_constant_decl", "var_decl_list", "var_decl_unit", 
                   "const_decl_list", "const_decl_unit", "method_decl", 
                   "param_list", "params", "id_list", "constructor_decl", 
                   "bkooltype", "array_type", "primitive_type", "stmt", 
                   "block_stmt", "local_decl_region", "stmts", "local_decl", 
                   "local_var_decl", "local_const_decl", "assign_stmt", 
                   "lhs", "lhs_base", "lhs_index_expr", "lhs_member_access_expr", 
                   "if_then_stmt", "if_then_else_stmt", "if_then_else_stmt_no_short_if", 
                   "stmt_no_short_if", "stmt_no_trailing_substmt", "for_stmt", 
                   "for_stmt_no_short_if", "break_stmt", "continue_stmt", 
                   "return_stmt", "method_invoke_stmt", "expr", "relational_expr", 
                   "equality_expr", "logical_expr", "additive_expr", "multiply_expr", 
                   "concat_expr", "negate_expr", "unary_arithmetic_expr", 
                   "index_expr", "member_access_expr", "method_call", "new_expr", 
                   "primary_expr", "expr_list", "literal", "array_literal" ]

    EOF = Token.EOF
    BOOL=1
    INT=2
    FLOAT=3
    STRING=4
    VOID=5
    IF=6
    ELSE=7
    THEN=8
    FOR=9
    TO=10
    DOWNTO=11
    DO=12
    BREAK=13
    CONTINUE=14
    CLASS=15
    EXTENDS=16
    FINAL=17
    STATIC=18
    THIS=19
    RETURN=20
    NEW=21
    NIL=22
    ADD_OP=23
    SUB_OP=24
    MUL_OP=25
    FLOAT_DIV_OP=26
    INT_DIV_OP=27
    MOD_OP=28
    NEQ_OP=29
    EQ_OP=30
    LT_OP=31
    GT_OP=32
    LEQ_OP=33
    GEQ_OP=34
    OR_OP=35
    AND_OP=36
    NOT_OP=37
    CONCAT_OP=38
    ASSIGN_OP=39
    INIT_OP=40
    LP=41
    RP=42
    LSB=43
    RSB=44
    LCB=45
    RCB=46
    SEMI=47
    COLON=48
    DOT=49
    COMMA=50
    INTEGER_LITERAL=51
    FLOAT_LITERAL=52
    BOOLEAN_LITERAL=53
    STRING_LITERAL=54
    UNCLOSE_STRING=55
    ILLEGAL_ESCAPE=56
    ID=57
    WS=58
    COMMENT=59
    BLOCK_COMMENT=60
    LINE_COMMENT=61
    ERROR_CHAR=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_declContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CLASS:
                self.state = 120
                self.class_decl()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def class_body(self):
            return self.getTypedRuleContext(BKOOLParser.Class_bodyContext,0)


        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = BKOOLParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(BKOOLParser.CLASS)
            self.state = 129
            self.match(BKOOLParser.ID)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 130
                self.match(BKOOLParser.EXTENDS)
                self.state = 131
                self.match(BKOOLParser.ID)


            self.state = 134
            self.class_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def class_body_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_body_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_body_declContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = BKOOLParser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(BKOOLParser.LCB)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOL) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 137
                self.class_body_decl()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_body_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constructor_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Constructor_declContext,0)


        def field_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Field_declContext,0)


        def static_field_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Static_field_declContext,0)


        def const_field_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Const_field_declContext,0)


        def static_constant_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Static_constant_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_body_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body_decl" ):
                return visitor.visitClass_body_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_body_decl(self):

        localctx = BKOOLParser.Class_body_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body_decl)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.constructor_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.field_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.static_field_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.const_field_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 149
                self.static_constant_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 150
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def var_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_field_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_decl" ):
                return visitor.visitField_decl(self)
            else:
                return visitor.visitChildren(self)




    def field_decl(self):

        localctx = BKOOLParser.Field_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_field_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.bkooltype()
            self.state = 154
            self.var_decl_list()
            self.state = 155
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_field_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def const_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Const_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_const_field_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_field_decl" ):
                return visitor.visitConst_field_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_field_decl(self):

        localctx = BKOOLParser.Const_field_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_const_field_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(BKOOLParser.FINAL)
            self.state = 158
            self.bkooltype()
            self.state = 159
            self.const_decl_list()
            self.state = 160
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_field_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def var_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_static_field_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_field_decl" ):
                return visitor.visitStatic_field_decl(self)
            else:
                return visitor.visitChildren(self)




    def static_field_decl(self):

        localctx = BKOOLParser.Static_field_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_static_field_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(BKOOLParser.STATIC)
            self.state = 163
            self.bkooltype()
            self.state = 164
            self.var_decl_list()
            self.state = 165
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_constant_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def const_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Const_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_static_constant_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_constant_decl" ):
                return visitor.visitStatic_constant_decl(self)
            else:
                return visitor.visitChildren(self)




    def static_constant_decl(self):

        localctx = BKOOLParser.Static_constant_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_static_constant_decl)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(BKOOLParser.STATIC)
                self.state = 168
                self.match(BKOOLParser.FINAL)
                self.state = 169
                self.bkooltype()
                self.state = 170
                self.const_decl_list()
                self.state = 171
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.FINAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(BKOOLParser.FINAL)
                self.state = 174
                self.match(BKOOLParser.STATIC)
                self.state = 175
                self.bkooltype()
                self.state = 176
                self.const_decl_list()
                self.state = 177
                self.match(BKOOLParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_unit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_decl_unitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_decl_unitContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_list" ):
                return visitor.visitVar_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_list(self):

        localctx = BKOOLParser.Var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_decl_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.var_decl_unit()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 182
                self.match(BKOOLParser.COMMA)
                self.state = 183
                self.var_decl_unit()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INIT_OP(self):
            return self.getToken(BKOOLParser.INIT_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl_unit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_unit" ):
                return visitor.visitVar_decl_unit(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_unit(self):

        localctx = BKOOLParser.Var_decl_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_decl_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(BKOOLParser.ID)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INIT_OP:
                self.state = 190
                self.match(BKOOLParser.INIT_OP)
                self.state = 191
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_decl_unit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Const_decl_unitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Const_decl_unitContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_const_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl_list" ):
                return visitor.visitConst_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def const_decl_list(self):

        localctx = BKOOLParser.Const_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_const_decl_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.const_decl_unit()
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 195
                self.match(BKOOLParser.COMMA)
                self.state = 196
                self.const_decl_unit()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_decl_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INIT_OP(self):
            return self.getToken(BKOOLParser.INIT_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_const_decl_unit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl_unit" ):
                return visitor.visitConst_decl_unit(self)
            else:
                return visitor.visitChildren(self)




    def const_decl_unit(self):

        localctx = BKOOLParser.Const_decl_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_const_decl_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(BKOOLParser.ID)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INIT_OP:
                self.state = 203
                self.match(BKOOLParser.INIT_OP)
                self.state = 204
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = BKOOLParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 207
                self.match(BKOOLParser.STATIC)


            self.state = 210
            self.bkooltype()
            self.state = 211
            self.match(BKOOLParser.ID)
            self.state = 212
            self.match(BKOOLParser.LP)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOL) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.ID))) != 0):
                self.state = 213
                self.param_list()


            self.state = 216
            self.match(BKOOLParser.RP)
            self.state = 217
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParamsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParamsContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMI)
            else:
                return self.getToken(BKOOLParser.SEMI, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = BKOOLParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.params()
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.SEMI:
                self.state = 220
                self.match(BKOOLParser.SEMI)
                self.state = 221
                self.params()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def id_list(self):
            return self.getTypedRuleContext(BKOOLParser.Id_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = BKOOLParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.bkooltype()
            self.state = 228
            self.id_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = BKOOLParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(BKOOLParser.ID)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 231
                self.match(BKOOLParser.COMMA)
                self.state = 232
                self.match(BKOOLParser.ID)
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_decl" ):
                return visitor.visitConstructor_decl(self)
            else:
                return visitor.visitChildren(self)




    def constructor_decl(self):

        localctx = BKOOLParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_constructor_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(BKOOLParser.ID)
            self.state = 239
            self.match(BKOOLParser.LP)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOL) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.ID))) != 0):
                self.state = 240
                self.param_list()


            self.state = 243
            self.match(BKOOLParser.RP)
            self.state = 244
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BkooltypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_bkooltype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBkooltype" ):
                return visitor.visitBkooltype(self)
            else:
                return visitor.visitChildren(self)




    def bkooltype(self):

        localctx = BKOOLParser.BkooltypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_bkooltype)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.array_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(BKOOLParser.INTEGER_LITERAL, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOL, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.VOID]:
                self.state = 251
                self.primitive_type()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 252
                self.match(BKOOLParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 255
            self.match(BKOOLParser.LSB)
            self.state = 256
            self.match(BKOOLParser.INTEGER_LITERAL)
            self.state = 257
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(BKOOLParser.BOOL, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = BKOOLParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOL) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def method_invoke_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invoke_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stmtContext,0)


        def if_then_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_then_stmtContext,0)


        def if_then_else_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_then_else_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.For_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.break_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 263
                self.continue_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 264
                self.return_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 265
                self.method_invoke_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 266
                self.assign_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 267
                self.if_then_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 268
                self.if_then_else_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 269
                self.for_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def local_decl_region(self):
            return self.getTypedRuleContext(BKOOLParser.Local_decl_regionContext,0)


        def stmts(self):
            return self.getTypedRuleContext(BKOOLParser.StmtsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(BKOOLParser.LCB)
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 273
                self.local_decl_region()


            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.IF) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.ADD_OP) | (1 << BKOOLParser.SUB_OP) | (1 << BKOOLParser.NOT_OP) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.INTEGER_LITERAL) | (1 << BKOOLParser.FLOAT_LITERAL) | (1 << BKOOLParser.BOOLEAN_LITERAL) | (1 << BKOOLParser.STRING_LITERAL) | (1 << BKOOLParser.ID))) != 0):
                self.state = 276
                self.stmts()


            self.state = 279
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_decl_regionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Local_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Local_declContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_local_decl_region

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_decl_region" ):
                return visitor.visitLocal_decl_region(self)
            else:
                return visitor.visitChildren(self)




    def local_decl_region(self):

        localctx = BKOOLParser.Local_decl_regionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_local_decl_region)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 281
                    self.local_decl()

                else:
                    raise NoViableAltException(self)
                self.state = 284 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = BKOOLParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 286
                self.stmt()
                self.state = 289 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.IF) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.ADD_OP) | (1 << BKOOLParser.SUB_OP) | (1 << BKOOLParser.NOT_OP) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.INTEGER_LITERAL) | (1 << BKOOLParser.FLOAT_LITERAL) | (1 << BKOOLParser.BOOLEAN_LITERAL) | (1 << BKOOLParser.STRING_LITERAL) | (1 << BKOOLParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_var_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Local_var_declContext,0)


        def local_const_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Local_const_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_local_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_decl" ):
                return visitor.visitLocal_decl(self)
            else:
                return visitor.visitChildren(self)




    def local_decl(self):

        localctx = BKOOLParser.Local_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_local_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOL, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.state = 291
                self.local_var_decl()
                pass
            elif token in [BKOOLParser.FINAL]:
                self.state = 292
                self.local_const_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def var_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_local_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_var_decl" ):
                return visitor.visitLocal_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def local_var_decl(self):

        localctx = BKOOLParser.Local_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_local_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.bkooltype()
            self.state = 296
            self.var_decl_list()
            self.state = 297
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def const_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Const_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_local_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_const_decl" ):
                return visitor.visitLocal_const_decl(self)
            else:
                return visitor.visitChildren(self)




    def local_const_decl(self):

        localctx = BKOOLParser.Local_const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_local_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(BKOOLParser.FINAL)
            self.state = 300
            self.bkooltype()
            self.state = 301
            self.const_decl_list()
            self.state = 302
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN_OP(self):
            return self.getToken(BKOOLParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKOOLParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.lhs()
            self.state = 305
            self.match(BKOOLParser.ASSIGN_OP)
            self.state = 306
            self.expr()
            self.state = 307
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def lhs_base(self):
            return self.getTypedRuleContext(BKOOLParser.Lhs_baseContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_lhs)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(BKOOLParser.LP)
                self.state = 310
                self.lhs()
                self.state = 311
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.lhs_base()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_baseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def lhs_member_access_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Lhs_member_access_exprContext,0)


        def lhs_index_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Lhs_index_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs_base

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_base" ):
                return visitor.visitLhs_base(self)
            else:
                return visitor.visitChildren(self)




    def lhs_base(self):

        localctx = BKOOLParser.Lhs_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_lhs_base)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.lhs_member_access_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                self.lhs_index_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Member_access_exprContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_index_expr" ):
                return visitor.visitLhs_index_expr(self)
            else:
                return visitor.visitChildren(self)




    def lhs_index_expr(self):

        localctx = BKOOLParser.Lhs_index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_lhs_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.member_access_expr(0)

            self.state = 322
            self.match(BKOOLParser.LSB)
            self.state = 323
            self.expr()
            self.state = 324
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_member_access_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.bop = None # Token

        def new_expr(self):
            return self.getTypedRuleContext(BKOOLParser.New_exprContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def method_call(self):
            return self.getTypedRuleContext(BKOOLParser.Method_callContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs_member_access_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_member_access_expr" ):
                return visitor.visitLhs_member_access_expr(self)
            else:
                return visitor.visitChildren(self)




    def lhs_member_access_expr(self):

        localctx = BKOOLParser.Lhs_member_access_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_lhs_member_access_expr)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.new_expr()
                self.state = 327
                localctx.bop = self.match(BKOOLParser.DOT)

                self.state = 328
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.new_expr()
                self.state = 331
                localctx.bop = self.match(BKOOLParser.DOT)

                self.state = 332
                self.method_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_then_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_if_then_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_then_stmt" ):
                return visitor.visitIf_then_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_then_stmt(self):

        localctx = BKOOLParser.If_then_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_if_then_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(BKOOLParser.IF)
            self.state = 337
            self.expr()
            self.state = 338
            self.match(BKOOLParser.THEN)
            self.state = 339
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_then_else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt_no_short_if(self):
            return self.getTypedRuleContext(BKOOLParser.Stmt_no_short_ifContext,0)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_if_then_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_then_else_stmt" ):
                return visitor.visitIf_then_else_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_then_else_stmt(self):

        localctx = BKOOLParser.If_then_else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_if_then_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(BKOOLParser.IF)
            self.state = 342
            self.expr()
            self.state = 343
            self.match(BKOOLParser.THEN)
            self.state = 344
            self.stmt_no_short_if()
            self.state = 345
            self.match(BKOOLParser.ELSE)
            self.state = 346
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_then_else_stmt_no_short_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt_no_short_if(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Stmt_no_short_ifContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Stmt_no_short_ifContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_then_else_stmt_no_short_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_then_else_stmt_no_short_if" ):
                return visitor.visitIf_then_else_stmt_no_short_if(self)
            else:
                return visitor.visitChildren(self)




    def if_then_else_stmt_no_short_if(self):

        localctx = BKOOLParser.If_then_else_stmt_no_short_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_if_then_else_stmt_no_short_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(BKOOLParser.IF)
            self.state = 349
            self.expr()
            self.state = 350
            self.match(BKOOLParser.THEN)
            self.state = 351
            self.stmt_no_short_if()
            self.state = 352
            self.match(BKOOLParser.ELSE)
            self.state = 353
            self.stmt_no_short_if()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_no_short_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_no_trailing_substmt(self):
            return self.getTypedRuleContext(BKOOLParser.Stmt_no_trailing_substmtContext,0)


        def if_then_else_stmt_no_short_if(self):
            return self.getTypedRuleContext(BKOOLParser.If_then_else_stmt_no_short_ifContext,0)


        def for_stmt_no_short_if(self):
            return self.getTypedRuleContext(BKOOLParser.For_stmt_no_short_ifContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt_no_short_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_no_short_if" ):
                return visitor.visitStmt_no_short_if(self)
            else:
                return visitor.visitChildren(self)




    def stmt_no_short_if(self):

        localctx = BKOOLParser.Stmt_no_short_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_stmt_no_short_if)
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.THIS, BKOOLParser.RETURN, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.ADD_OP, BKOOLParser.SUB_OP, BKOOLParser.NOT_OP, BKOOLParser.LP, BKOOLParser.LCB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.BOOLEAN_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.stmt_no_trailing_substmt()
                pass
            elif token in [BKOOLParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.if_then_else_stmt_no_short_if()
                pass
            elif token in [BKOOLParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 357
                self.for_stmt_no_short_if()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_no_trailing_substmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def method_invoke_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invoke_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt_no_trailing_substmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_no_trailing_substmt" ):
                return visitor.visitStmt_no_trailing_substmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt_no_trailing_substmt(self):

        localctx = BKOOLParser.Stmt_no_trailing_substmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_stmt_no_trailing_substmt)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.break_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 362
                self.continue_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 363
                self.return_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 364
                self.method_invoke_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 365
                self.assign_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN_OP(self):
            return self.getToken(BKOOLParser.ASSIGN_OP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKOOLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(BKOOLParser.FOR)

            self.state = 369
            self.match(BKOOLParser.ID)
            self.state = 370
            self.match(BKOOLParser.ASSIGN_OP)
            self.state = 371
            self.expr()
            self.state = 373
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            self.state = 374
            self.expr()
            self.state = 375
            self.match(BKOOLParser.DO)
            self.state = 376
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmt_no_short_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt_no_short_if(self):
            return self.getTypedRuleContext(BKOOLParser.Stmt_no_short_ifContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN_OP(self):
            return self.getToken(BKOOLParser.ASSIGN_OP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_for_stmt_no_short_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt_no_short_if" ):
                return visitor.visitFor_stmt_no_short_if(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt_no_short_if(self):

        localctx = BKOOLParser.For_stmt_no_short_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_for_stmt_no_short_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(BKOOLParser.FOR)

            self.state = 379
            self.match(BKOOLParser.ID)
            self.state = 380
            self.match(BKOOLParser.ASSIGN_OP)
            self.state = 381
            self.expr()
            self.state = 383
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            self.state = 384
            self.expr()
            self.state = 385
            self.match(BKOOLParser.DO)
            self.state = 386
            self.stmt_no_short_if()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKOOLParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(BKOOLParser.BREAK)
            self.state = 389
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKOOLParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(BKOOLParser.CONTINUE)
            self.state = 392
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(BKOOLParser.RETURN)
            self.state = 395
            self.expr()
            self.state = 396
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invoke_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def method_call(self):
            return self.getTypedRuleContext(BKOOLParser.Method_callContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invoke_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invoke_stmt" ):
                return visitor.visitMethod_invoke_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invoke_stmt(self):

        localctx = BKOOLParser.Method_invoke_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_method_invoke_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.expr()
            self.state = 399
            self.match(BKOOLParser.DOT)
            self.state = 400
            self.method_call()
            self.state = 401
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Relational_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.relational_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Equality_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Equality_exprContext,i)


        def LT_OP(self):
            return self.getToken(BKOOLParser.LT_OP, 0)

        def GT_OP(self):
            return self.getToken(BKOOLParser.GT_OP, 0)

        def LEQ_OP(self):
            return self.getToken(BKOOLParser.LEQ_OP, 0)

        def GEQ_OP(self):
            return self.getToken(BKOOLParser.GEQ_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_relational_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)




    def relational_expr(self):

        localctx = BKOOLParser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_relational_expr)
        self._la = 0 # Token type
        try:
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.equality_expr()
                self.state = 406
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT_OP) | (1 << BKOOLParser.GT_OP) | (1 << BKOOLParser.LEQ_OP) | (1 << BKOOLParser.GEQ_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 407
                self.equality_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.equality_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equality_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Logical_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Logical_exprContext,i)


        def EQ_OP(self):
            return self.getToken(BKOOLParser.EQ_OP, 0)

        def NEQ_OP(self):
            return self.getToken(BKOOLParser.NEQ_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_equality_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality_expr" ):
                return visitor.visitEquality_expr(self)
            else:
                return visitor.visitChildren(self)




    def equality_expr(self):

        localctx = BKOOLParser.Equality_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_equality_expr)
        self._la = 0 # Token type
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.logical_expr(0)
                self.state = 413
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NEQ_OP or _la==BKOOLParser.EQ_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 414
                self.logical_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.logical_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Additive_exprContext,0)


        def logical_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Logical_exprContext,0)


        def AND_OP(self):
            return self.getToken(BKOOLParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(BKOOLParser.OR_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_logical_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr" ):
                return visitor.visitLogical_expr(self)
            else:
                return visitor.visitChildren(self)



    def logical_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Logical_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_logical_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.additive_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Logical_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                    self.state = 422
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 423
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR_OP or _la==BKOOLParser.AND_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 424
                    self.additive_expr(0) 
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Additive_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiply_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Multiply_exprContext,0)


        def additive_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Additive_exprContext,0)


        def ADD_OP(self):
            return self.getToken(BKOOLParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(BKOOLParser.SUB_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_additive_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive_expr" ):
                return visitor.visitAdditive_expr(self)
            else:
                return visitor.visitChildren(self)



    def additive_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Additive_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_additive_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.multiply_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Additive_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_expr)
                    self.state = 433
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 434
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD_OP or _la==BKOOLParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 435
                    self.multiply_expr(0) 
                self.state = 440
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiply_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concat_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Concat_exprContext,0)


        def multiply_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Multiply_exprContext,0)


        def MUL_OP(self):
            return self.getToken(BKOOLParser.MUL_OP, 0)

        def FLOAT_DIV_OP(self):
            return self.getToken(BKOOLParser.FLOAT_DIV_OP, 0)

        def INT_DIV_OP(self):
            return self.getToken(BKOOLParser.INT_DIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(BKOOLParser.MOD_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_multiply_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply_expr" ):
                return visitor.visitMultiply_expr(self)
            else:
                return visitor.visitChildren(self)



    def multiply_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Multiply_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_multiply_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.concat_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 449
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Multiply_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiply_expr)
                    self.state = 444
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 445
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL_OP) | (1 << BKOOLParser.FLOAT_DIV_OP) | (1 << BKOOLParser.INT_DIV_OP) | (1 << BKOOLParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 446
                    self.concat_expr(0) 
                self.state = 451
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Concat_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negate_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Negate_exprContext,0)


        def concat_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Concat_exprContext,0)


        def CONCAT_OP(self):
            return self.getToken(BKOOLParser.CONCAT_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_concat_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat_expr" ):
                return visitor.visitConcat_expr(self)
            else:
                return visitor.visitChildren(self)



    def concat_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Concat_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_concat_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.negate_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 460
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Concat_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_concat_expr)
                    self.state = 455
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 456
                    self.match(BKOOLParser.CONCAT_OP)
                    self.state = 457
                    self.negate_expr() 
                self.state = 462
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Negate_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negate_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Negate_exprContext,0)


        def NOT_OP(self):
            return self.getToken(BKOOLParser.NOT_OP, 0)

        def unary_arithmetic_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Unary_arithmetic_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_negate_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegate_expr" ):
                return visitor.visitNegate_expr(self)
            else:
                return visitor.visitChildren(self)




    def negate_expr(self):

        localctx = BKOOLParser.Negate_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_negate_expr)
        try:
            self.state = 466
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.match(BKOOLParser.NOT_OP)
                self.state = 464
                self.negate_expr()
                pass
            elif token in [BKOOLParser.THIS, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.ADD_OP, BKOOLParser.SUB_OP, BKOOLParser.LP, BKOOLParser.LCB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.BOOLEAN_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.unary_arithmetic_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_arithmetic_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_arithmetic_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Unary_arithmetic_exprContext,0)


        def ADD_OP(self):
            return self.getToken(BKOOLParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(BKOOLParser.SUB_OP, 0)

        def index_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Index_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_unary_arithmetic_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_arithmetic_expr" ):
                return visitor.visitUnary_arithmetic_expr(self)
            else:
                return visitor.visitChildren(self)




    def unary_arithmetic_expr(self):

        localctx = BKOOLParser.Unary_arithmetic_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_unary_arithmetic_expr)
        self._la = 0 # Token type
        try:
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD_OP, BKOOLParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD_OP or _la==BKOOLParser.SUB_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 469
                self.unary_arithmetic_expr()
                pass
            elif token in [BKOOLParser.THIS, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.LP, BKOOLParser.LCB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.BOOLEAN_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.index_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Member_access_exprContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = BKOOLParser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_index_expr)
        try:
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.member_access_expr(0)

                self.state = 474
                self.match(BKOOLParser.LSB)
                self.state = 475
                self.expr()
                self.state = 476
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.member_access_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_access_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.bop = None # Token

        def new_expr(self):
            return self.getTypedRuleContext(BKOOLParser.New_exprContext,0)


        def member_access_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Member_access_exprContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def method_call(self):
            return self.getTypedRuleContext(BKOOLParser.Method_callContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_member_access_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access_expr" ):
                return visitor.visitMember_access_expr(self)
            else:
                return visitor.visitChildren(self)



    def member_access_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Member_access_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_member_access_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.new_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 492
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 490
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Member_access_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_expr)
                        self.state = 484
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 485
                        localctx.bop = self.match(BKOOLParser.DOT)

                        self.state = 486
                        self.method_call()
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Member_access_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_expr)
                        self.state = 487
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 488
                        localctx.bop = self.match(BKOOLParser.DOT)

                        self.state = 489
                        self.match(BKOOLParser.ID)
                        pass

             
                self.state = 494
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = BKOOLParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(BKOOLParser.ID)
            self.state = 496
            self.match(BKOOLParser.LP)
            self.state = 498
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.THIS) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.ADD_OP) | (1 << BKOOLParser.SUB_OP) | (1 << BKOOLParser.NOT_OP) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.INTEGER_LITERAL) | (1 << BKOOLParser.FLOAT_LITERAL) | (1 << BKOOLParser.BOOLEAN_LITERAL) | (1 << BKOOLParser.STRING_LITERAL) | (1 << BKOOLParser.ID))) != 0):
                self.state = 497
                self.expr_list()


            self.state = 500
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class New_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_listContext,0)


        def primary_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Primary_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_new_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew_expr" ):
                return visitor.visitNew_expr(self)
            else:
                return visitor.visitChildren(self)




    def new_expr(self):

        localctx = BKOOLParser.New_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_new_expr)
        self._la = 0 # Token type
        try:
            self.state = 510
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 502
                self.match(BKOOLParser.NEW)
                self.state = 503
                self.match(BKOOLParser.ID)
                self.state = 504
                self.match(BKOOLParser.LP)
                self.state = 506
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.THIS) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.ADD_OP) | (1 << BKOOLParser.SUB_OP) | (1 << BKOOLParser.NOT_OP) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.INTEGER_LITERAL) | (1 << BKOOLParser.FLOAT_LITERAL) | (1 << BKOOLParser.BOOLEAN_LITERAL) | (1 << BKOOLParser.STRING_LITERAL) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 505
                    self.expr_list()


                self.state = 508
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.THIS, BKOOLParser.NIL, BKOOLParser.LP, BKOOLParser.LCB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.BOOLEAN_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.primary_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primary_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expr" ):
                return visitor.visitPrimary_expr(self)
            else:
                return visitor.visitChildren(self)




    def primary_expr(self):

        localctx = BKOOLParser.Primary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_primary_expr)
        try:
            self.state = 520
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LCB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.BOOLEAN_LITERAL, BKOOLParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.literal()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 514
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 4)
                self.state = 515
                self.match(BKOOLParser.LP)
                self.state = 516
                self.expr()
                self.state = 517
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 519
                self.match(BKOOLParser.NIL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = BKOOLParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.expr()
            self.state = 527
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 523
                self.match(BKOOLParser.COMMA)
                self.state = 524
                self.expr()
                self.state = 529
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(BKOOLParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(BKOOLParser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(BKOOLParser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(BKOOLParser.STRING_LITERAL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(BKOOLParser.Array_literalContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_literal)
        try:
            self.state = 535
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.match(BKOOLParser.INTEGER_LITERAL)
                pass
            elif token in [BKOOLParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
                self.match(BKOOLParser.FLOAT_LITERAL)
                pass
            elif token in [BKOOLParser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 532
                self.match(BKOOLParser.BOOLEAN_LITERAL)
                pass
            elif token in [BKOOLParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 533
                self.match(BKOOLParser.STRING_LITERAL)
                pass
            elif token in [BKOOLParser.LCB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 534
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = BKOOLParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(BKOOLParser.LCB)

            self.state = 538
            self.literal()
            self.state = 543
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 539
                self.match(BKOOLParser.COMMA)
                self.state = 540
                self.literal()
                self.state = 545
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 546
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[46] = self.logical_expr_sempred
        self._predicates[47] = self.additive_expr_sempred
        self._predicates[48] = self.multiply_expr_sempred
        self._predicates[49] = self.concat_expr_sempred
        self._predicates[53] = self.member_access_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with target:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expr_sempred(self, localctx:Logical_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def additive_expr_sempred(self, localctx:Additive_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiply_expr_sempred(self, localctx:Multiply_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def concat_expr_sempred(self, localctx:Concat_exprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def member_access_expr_sempred(self, localctx:Member_access_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




