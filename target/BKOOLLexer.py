# type: ignore
# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01e1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&")
        buf.write("\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\6\67\u015b\n\67")
        buf.write("\r\67\16\67\u015c\38\38\39\39\59\u0163\n9\39\39\39\59")
        buf.write("\u0168\n9\3:\3:\3:\5:\u016d\n:\3;\3;\5;\u0171\n;\3;\3")
        buf.write(";\3<\3<\3=\3=\5=\u0179\n=\3>\3>\7>\u017d\n>\f>\16>\u0180")
        buf.write("\13>\3>\3>\3?\3?\5?\u0186\n?\3@\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\5@\u0196\n@\3A\3A\3A\7A\u019b\nA\fA\16")
        buf.write("A\u019e\13A\3A\5A\u01a1\nA\3A\3A\3B\3B\7B\u01a7\nB\fB")
        buf.write("\16B\u01aa\13B\3B\3B\3B\3C\3C\5C\u01b1\nC\3D\3D\7D\u01b5")
        buf.write("\nD\fD\16D\u01b8\13D\3E\6E\u01bb\nE\rE\16E\u01bc\3E\3")
        buf.write("E\3F\3F\5F\u01c3\nF\3F\3F\3G\3G\3G\3G\7G\u01cb\nG\fG\16")
        buf.write("G\u01ce\13G\3G\3G\3G\5G\u01d3\nG\3H\3H\7H\u01d7\nH\fH")
        buf.write("\16H\u01da\13H\3H\5H\u01dd\nH\3I\3I\3I\3\u01cc\2J\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\2\61")
        buf.write("\2\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'")
        buf.write("Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\2o\2q\66s\2")
        buf.write("u\2w\2y\67{8}\2\177\2\u00819\u0083:\u0085\2\u0087;\u0089")
        buf.write("<\u008b=\u008d>\u008f?\u0091@\3\2\f\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\6\2\f\f\16\17$$^^\4\3\f\f\16\17\t\2$$^^ddhhppt")
        buf.write("tvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\3\2\f")
        buf.write("\f\2\u01ef\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2q\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\3\u0093\3\2\2\2\5\u009b\3\2\2\2\7\u009f\3\2\2")
        buf.write("\2\t\u00a5\3\2\2\2\13\u00ac\3\2\2\2\r\u00b1\3\2\2\2\17")
        buf.write("\u00b4\3\2\2\2\21\u00b9\3\2\2\2\23\u00be\3\2\2\2\25\u00c2")
        buf.write("\3\2\2\2\27\u00c5\3\2\2\2\31\u00cc\3\2\2\2\33\u00cf\3")
        buf.write("\2\2\2\35\u00d5\3\2\2\2\37\u00de\3\2\2\2!\u00e4\3\2\2")
        buf.write("\2#\u00ec\3\2\2\2%\u00f2\3\2\2\2\'\u00f9\3\2\2\2)\u00fe")
        buf.write("\3\2\2\2+\u0105\3\2\2\2-\u0109\3\2\2\2/\u010d\3\2\2\2")
        buf.write("\61\u0112\3\2\2\2\63\u0118\3\2\2\2\65\u011a\3\2\2\2\67")
        buf.write("\u011c\3\2\2\29\u011e\3\2\2\2;\u0120\3\2\2\2=\u0122\3")
        buf.write("\2\2\2?\u0124\3\2\2\2A\u0127\3\2\2\2C\u012a\3\2\2\2E\u012c")
        buf.write("\3\2\2\2G\u012e\3\2\2\2I\u0131\3\2\2\2K\u0134\3\2\2\2")
        buf.write("M\u0137\3\2\2\2O\u013a\3\2\2\2Q\u013c\3\2\2\2S\u013e\3")
        buf.write("\2\2\2U\u0141\3\2\2\2W\u0143\3\2\2\2Y\u0145\3\2\2\2[\u0147")
        buf.write("\3\2\2\2]\u0149\3\2\2\2_\u014b\3\2\2\2a\u014d\3\2\2\2")
        buf.write("c\u014f\3\2\2\2e\u0151\3\2\2\2g\u0153\3\2\2\2i\u0155\3")
        buf.write("\2\2\2k\u0157\3\2\2\2m\u015a\3\2\2\2o\u015e\3\2\2\2q\u0167")
        buf.write("\3\2\2\2s\u0169\3\2\2\2u\u016e\3\2\2\2w\u0174\3\2\2\2")
        buf.write("y\u0178\3\2\2\2{\u017a\3\2\2\2}\u0185\3\2\2\2\177\u0195")
        buf.write("\3\2\2\2\u0081\u0197\3\2\2\2\u0083\u01a4\3\2\2\2\u0085")
        buf.write("\u01ae\3\2\2\2\u0087\u01b2\3\2\2\2\u0089\u01ba\3\2\2\2")
        buf.write("\u008b\u01c2\3\2\2\2\u008d\u01c6\3\2\2\2\u008f\u01d4\3")
        buf.write("\2\2\2\u0091\u01de\3\2\2\2\u0093\u0094\7d\2\2\u0094\u0095")
        buf.write("\7q\2\2\u0095\u0096\7q\2\2\u0096\u0097\7n\2\2\u0097\u0098")
        buf.write("\7g\2\2\u0098\u0099\7c\2\2\u0099\u009a\7p\2\2\u009a\4")
        buf.write("\3\2\2\2\u009b\u009c\7k\2\2\u009c\u009d\7p\2\2\u009d\u009e")
        buf.write("\7v\2\2\u009e\6\3\2\2\2\u009f\u00a0\7h\2\2\u00a0\u00a1")
        buf.write("\7n\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4")
        buf.write("\7v\2\2\u00a4\b\3\2\2\2\u00a5\u00a6\7u\2\2\u00a6\u00a7")
        buf.write("\7v\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa")
        buf.write("\7p\2\2\u00aa\u00ab\7i\2\2\u00ab\n\3\2\2\2\u00ac\u00ad")
        buf.write("\7x\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af\7k\2\2\u00af\u00b0")
        buf.write("\7f\2\2\u00b0\f\3\2\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3")
        buf.write("\7h\2\2\u00b3\16\3\2\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6")
        buf.write("\7n\2\2\u00b6\u00b7\7u\2\2\u00b7\u00b8\7g\2\2\u00b8\20")
        buf.write("\3\2\2\2\u00b9\u00ba\7v\2\2\u00ba\u00bb\7j\2\2\u00bb\u00bc")
        buf.write("\7g\2\2\u00bc\u00bd\7p\2\2\u00bd\22\3\2\2\2\u00be\u00bf")
        buf.write("\7h\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1\7t\2\2\u00c1\24")
        buf.write("\3\2\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7q\2\2\u00c4\26")
        buf.write("\3\2\2\2\u00c5\u00c6\7f\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8")
        buf.write("\7y\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb")
        buf.write("\7q\2\2\u00cb\30\3\2\2\2\u00cc\u00cd\7f\2\2\u00cd\u00ce")
        buf.write("\7q\2\2\u00ce\32\3\2\2\2\u00cf\u00d0\7d\2\2\u00d0\u00d1")
        buf.write("\7t\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4")
        buf.write("\7m\2\2\u00d4\34\3\2\2\2\u00d5\u00d6\7e\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da")
        buf.write("\7k\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\36\3\2\2\2\u00de\u00df\7e\2\2\u00df\u00e0")
        buf.write("\7n\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7u\2\2\u00e2\u00e3")
        buf.write("\7u\2\2\u00e3 \3\2\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6")
        buf.write("\7z\2\2\u00e6\u00e7\7v\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\u00ea\7f\2\2\u00ea\u00eb\7u\2\2\u00eb\"")
        buf.write("\3\2\2\2\u00ec\u00ed\7h\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef")
        buf.write("\7p\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1\7n\2\2\u00f1$\3")
        buf.write("\2\2\2\u00f2\u00f3\7u\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5")
        buf.write("\7c\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8")
        buf.write("\7e\2\2\u00f8&\3\2\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb")
        buf.write("\7j\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd\7u\2\2\u00fd(\3")
        buf.write("\2\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7g\2\2\u0100\u0101")
        buf.write("\7v\2\2\u0101\u0102\7w\2\2\u0102\u0103\7t\2\2\u0103\u0104")
        buf.write("\7p\2\2\u0104*\3\2\2\2\u0105\u0106\7p\2\2\u0106\u0107")
        buf.write("\7g\2\2\u0107\u0108\7y\2\2\u0108,\3\2\2\2\u0109\u010a")
        buf.write("\7p\2\2\u010a\u010b\7k\2\2\u010b\u010c\7n\2\2\u010c.\3")
        buf.write("\2\2\2\u010d\u010e\7v\2\2\u010e\u010f\7t\2\2\u010f\u0110")
        buf.write("\7w\2\2\u0110\u0111\7g\2\2\u0111\60\3\2\2\2\u0112\u0113")
        buf.write("\7h\2\2\u0113\u0114\7c\2\2\u0114\u0115\7n\2\2\u0115\u0116")
        buf.write("\7u\2\2\u0116\u0117\7g\2\2\u0117\62\3\2\2\2\u0118\u0119")
        buf.write("\7-\2\2\u0119\64\3\2\2\2\u011a\u011b\7/\2\2\u011b\66\3")
        buf.write("\2\2\2\u011c\u011d\7,\2\2\u011d8\3\2\2\2\u011e\u011f\7")
        buf.write("\61\2\2\u011f:\3\2\2\2\u0120\u0121\7^\2\2\u0121<\3\2\2")
        buf.write("\2\u0122\u0123\7\'\2\2\u0123>\3\2\2\2\u0124\u0125\7#\2")
        buf.write("\2\u0125\u0126\7?\2\2\u0126@\3\2\2\2\u0127\u0128\7?\2")
        buf.write("\2\u0128\u0129\7?\2\2\u0129B\3\2\2\2\u012a\u012b\7>\2")
        buf.write("\2\u012bD\3\2\2\2\u012c\u012d\7@\2\2\u012dF\3\2\2\2\u012e")
        buf.write("\u012f\7>\2\2\u012f\u0130\7?\2\2\u0130H\3\2\2\2\u0131")
        buf.write("\u0132\7@\2\2\u0132\u0133\7?\2\2\u0133J\3\2\2\2\u0134")
        buf.write("\u0135\7~\2\2\u0135\u0136\7~\2\2\u0136L\3\2\2\2\u0137")
        buf.write("\u0138\7(\2\2\u0138\u0139\7(\2\2\u0139N\3\2\2\2\u013a")
        buf.write("\u013b\7#\2\2\u013bP\3\2\2\2\u013c\u013d\7`\2\2\u013d")
        buf.write("R\3\2\2\2\u013e\u013f\7<\2\2\u013f\u0140\7?\2\2\u0140")
        buf.write("T\3\2\2\2\u0141\u0142\7?\2\2\u0142V\3\2\2\2\u0143\u0144")
        buf.write("\7*\2\2\u0144X\3\2\2\2\u0145\u0146\7+\2\2\u0146Z\3\2\2")
        buf.write("\2\u0147\u0148\7]\2\2\u0148\\\3\2\2\2\u0149\u014a\7_\2")
        buf.write("\2\u014a^\3\2\2\2\u014b\u014c\7}\2\2\u014c`\3\2\2\2\u014d")
        buf.write("\u014e\7\177\2\2\u014eb\3\2\2\2\u014f\u0150\7=\2\2\u0150")
        buf.write("d\3\2\2\2\u0151\u0152\7<\2\2\u0152f\3\2\2\2\u0153\u0154")
        buf.write("\7\60\2\2\u0154h\3\2\2\2\u0155\u0156\7.\2\2\u0156j\3\2")
        buf.write("\2\2\u0157\u0158\5m\67\2\u0158l\3\2\2\2\u0159\u015b\5")
        buf.write("o8\2\u015a\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015a")
        buf.write("\3\2\2\2\u015c\u015d\3\2\2\2\u015dn\3\2\2\2\u015e\u015f")
        buf.write("\t\2\2\2\u015fp\3\2\2\2\u0160\u0162\5s:\2\u0161\u0163")
        buf.write("\5u;\2\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0168")
        buf.write("\3\2\2\2\u0164\u0165\5m\67\2\u0165\u0166\5u;\2\u0166\u0168")
        buf.write("\3\2\2\2\u0167\u0160\3\2\2\2\u0167\u0164\3\2\2\2\u0168")
        buf.write("r\3\2\2\2\u0169\u016a\5m\67\2\u016a\u016c\5g\64\2\u016b")
        buf.write("\u016d\5m\67\2\u016c\u016b\3\2\2\2\u016c\u016d\3\2\2\2")
        buf.write("\u016dt\3\2\2\2\u016e\u0170\t\3\2\2\u016f\u0171\5w<\2")
        buf.write("\u0170\u016f\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172\u0173\5m\67\2\u0173v\3\2\2\2\u0174\u0175")
        buf.write("\t\4\2\2\u0175x\3\2\2\2\u0176\u0179\5/\30\2\u0177\u0179")
        buf.write("\5\61\31\2\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("z\3\2\2\2\u017a\u017e\7$\2\2\u017b\u017d\5}?\2\u017c\u017b")
        buf.write("\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017f\u0181\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0181\u0182\7$\2\2\u0182|\3\2\2\2\u0183\u0186\n\5\2\2")
        buf.write("\u0184\u0186\5\177@\2\u0185\u0183\3\2\2\2\u0185\u0184")
        buf.write("\3\2\2\2\u0186~\3\2\2\2\u0187\u0188\7^\2\2\u0188\u0196")
        buf.write("\7d\2\2\u0189\u018a\7^\2\2\u018a\u0196\7h\2\2\u018b\u018c")
        buf.write("\7^\2\2\u018c\u0196\7p\2\2\u018d\u018e\7^\2\2\u018e\u0196")
        buf.write("\7t\2\2\u018f\u0190\7^\2\2\u0190\u0196\7v\2\2\u0191\u0192")
        buf.write("\7^\2\2\u0192\u0196\7$\2\2\u0193\u0194\7^\2\2\u0194\u0196")
        buf.write("\7^\2\2\u0195\u0187\3\2\2\2\u0195\u0189\3\2\2\2\u0195")
        buf.write("\u018b\3\2\2\2\u0195\u018d\3\2\2\2\u0195\u018f\3\2\2\2")
        buf.write("\u0195\u0191\3\2\2\2\u0195\u0193\3\2\2\2\u0196\u0080\3")
        buf.write("\2\2\2\u0197\u019c\7$\2\2\u0198\u019b\n\5\2\2\u0199\u019b")
        buf.write("\5\177@\2\u019a\u0198\3\2\2\2\u019a\u0199\3\2\2\2\u019b")
        buf.write("\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2")
        buf.write("\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a1\t")
        buf.write("\6\2\2\u01a0\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3")
        buf.write("\bA\2\2\u01a3\u0082\3\2\2\2\u01a4\u01a8\7$\2\2\u01a5\u01a7")
        buf.write("\5}?\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01ab\u01ac\5\u0085C\2\u01ac\u01ad\bB\3")
        buf.write("\2\u01ad\u0084\3\2\2\2\u01ae\u01b0\7^\2\2\u01af\u01b1")
        buf.write("\n\7\2\2\u01b0\u01af\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("\u0086\3\2\2\2\u01b2\u01b6\t\b\2\2\u01b3\u01b5\t\t\2\2")
        buf.write("\u01b4\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3")
        buf.write("\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u0088\3\2\2\2\u01b8\u01b6")
        buf.write("\3\2\2\2\u01b9\u01bb\t\n\2\2\u01ba\u01b9\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2")
        buf.write("\u01bd\u01be\3\2\2\2\u01be\u01bf\bE\4\2\u01bf\u008a\3")
        buf.write("\2\2\2\u01c0\u01c3\5\u008dG\2\u01c1\u01c3\5\u008fH\2\u01c2")
        buf.write("\u01c0\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2")
        buf.write("\u01c4\u01c5\bF\4\2\u01c5\u008c\3\2\2\2\u01c6\u01c7\7")
        buf.write("\61\2\2\u01c7\u01c8\7,\2\2\u01c8\u01cc\3\2\2\2\u01c9\u01cb")
        buf.write("\13\2\2\2\u01ca\u01c9\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01d2\3\2\2\2")
        buf.write("\u01ce\u01cc\3\2\2\2\u01cf\u01d0\7,\2\2\u01d0\u01d3\7")
        buf.write("\61\2\2\u01d1\u01d3\7\2\2\3\u01d2\u01cf\3\2\2\2\u01d2")
        buf.write("\u01d1\3\2\2\2\u01d3\u008e\3\2\2\2\u01d4\u01d8\7%\2\2")
        buf.write("\u01d5\u01d7\n\13\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01da")
        buf.write("\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9")
        buf.write("\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01dd\7\2\2\3")
        buf.write("\u01dc\u01db\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u0090\3")
        buf.write("\2\2\2\u01de\u01df\13\2\2\2\u01df\u01e0\bI\5\2\u01e0\u0092")
        buf.write("\3\2\2\2\30\2\u015c\u0162\u0167\u016c\u0170\u0178\u017e")
        buf.write("\u0185\u0195\u019a\u019c\u01a0\u01a8\u01b0\u01b6\u01bc")
        buf.write("\u01c2\u01cc\u01d2\u01d8\u01dc\6\3A\2\3B\3\b\2\2\3I\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOL = 1
    INT = 2
    FLOAT = 3
    STRING = 4
    VOID = 5
    IF = 6
    ELSE = 7
    THEN = 8
    FOR = 9
    TO = 10
    DOWNTO = 11
    DO = 12
    BREAK = 13
    CONTINUE = 14
    CLASS = 15
    EXTENDS = 16
    FINAL = 17
    STATIC = 18
    THIS = 19
    RETURN = 20
    NEW = 21
    NIL = 22
    ADD_OP = 23
    SUB_OP = 24
    MUL_OP = 25
    FLOAT_DIV_OP = 26
    INT_DIV_OP = 27
    MOD_OP = 28
    NEQ_OP = 29
    EQ_OP = 30
    LT_OP = 31
    GT_OP = 32
    LEQ_OP = 33
    GEQ_OP = 34
    OR_OP = 35
    AND_OP = 36
    NOT_OP = 37
    CONCAT_OP = 38
    ASSIGN_OP = 39
    INIT_OP = 40
    LP = 41
    RP = 42
    LSB = 43
    RSB = 44
    LCB = 45
    RCB = 46
    SEMI = 47
    COLON = 48
    DOT = 49
    COMMA = 50
    INTEGER_LITERAL = 51
    FLOAT_LITERAL = 52
    BOOLEAN_LITERAL = 53
    STRING_LITERAL = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ID = 57
    WS = 58
    COMMENT = 59
    BLOCK_COMMENT = 60
    LINE_COMMENT = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'int'", "'float'", "'string'", "'void'", "'if'", 
            "'else'", "'then'", "'for'", "'to_block'", "'downto'", "'do'", "'break'",
            "'continue'", "'class'", "'extends'", "'final'", "'static'", 
            "'this'", "'return'", "'new'", "'nil'", "'+'", "'-'", "'*'", 
            "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", "'>'", "'<='", 
            "'>='", "'||'", "'&&'", "'!'", "'^'", "':='", "'='", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "BOOL", "INT", "FLOAT", "STRING", "VOID", "IF", "ELSE", "THEN", 
            "FOR", "TO", "DOWNTO", "DO", "BREAK", "CONTINUE", "CLASS", "EXTENDS", 
            "FINAL", "STATIC", "THIS", "RETURN", "NEW", "NIL", "ADD_OP", 
            "SUB_OP", "MUL_OP", "FLOAT_DIV_OP", "INT_DIV_OP", "MOD_OP", 
            "NEQ_OP", "EQ_OP", "LT_OP", "GT_OP", "LEQ_OP", "GEQ_OP", "OR_OP", 
            "AND_OP", "NOT_OP", "CONCAT_OP", "ASSIGN_OP", "INIT_OP", "LP", 
            "RP", "LSB", "RSB", "LCB", "RCB", "SEMI", "COLON", "DOT", "COMMA", 
            "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ID", "WS", "COMMENT", "BLOCK_COMMENT", 
            "LINE_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "BOOL", "INT", "FLOAT", "STRING", "VOID", "IF", "ELSE", 
                  "THEN", "FOR", "TO", "DOWNTO", "DO", "BREAK", "CONTINUE", 
                  "CLASS", "EXTENDS", "FINAL", "STATIC", "THIS", "RETURN", 
                  "NEW", "NIL", "TRUE", "FALSE", "ADD_OP", "SUB_OP", "MUL_OP", 
                  "FLOAT_DIV_OP", "INT_DIV_OP", "MOD_OP", "NEQ_OP", "EQ_OP", 
                  "LT_OP", "GT_OP", "LEQ_OP", "GEQ_OP", "OR_OP", "AND_OP", 
                  "NOT_OP", "CONCAT_OP", "ASSIGN_OP", "INIT_OP", "LP", "RP", 
                  "LSB", "RSB", "LCB", "RCB", "SEMI", "COLON", "DOT", "COMMA", 
                  "INTEGER_LITERAL", "DigitSequence", "DIGIT", "FLOAT_LITERAL", 
                  "FractionalConstant", "ExponentPart", "SIGN", "BOOLEAN_LITERAL", 
                  "STRING_LITERAL", "CHAR_LITERAL", "ESCAPE_SEQUENCE", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ILLEGAL_ESCAPE_SEQ", "ID", "WS", "COMMENT", 
                  "BLOCK_COMMENT", "LINE_COMMENT", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[71] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    __forbid = ['\n']
                    if self.text[-1] in __forbid:
                        # unclose string due to_block new new line
                        if len(self.text) > 2 and self.text[-2] == '\r':
                            # On windows NewLine is (\r\n),
                            # raise txt[:-1] cause a new line with (\r)
                            # Hopefully no testcase on linux will include (\r\n)
                            raise UncloseString(self.text[:-2])
                        else:
                            raise UncloseString(self.text[:-1])
                    else:
                        # Unclose string due to_block EOF
                        raise UncloseString(self.text)
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    raise IllegalEscape(self.text)
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


