# type: ignore
import unittest

from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 102))

    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3", "aAsVN3,<EOF>", 103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 104))

    def test_105(self):
        """test integers"""
        self.assertTrue(TestLexer.test(""" "abc\\h def"  """, """Illegal Escape In String: "abc\\h""", 105))

    def test_106(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 106))

    def test_107(self):
        """test string"""
        inp = """
class BananaBunch extends Fruit {
    int banana_count = 12;    
    Banana[12] bananas;
}"""
        exp = """class,BananaBunch,extends,Fruit,{,int,banana_count,=,12,;,Banana,[,12,],bananas,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 107))

    def test_108(self):
        """test string"""
        inp = """
        Banana(int size) {
        this.banana := new Banana(size);
        this.banana_count := banana;
    }"""
        exp = """Banana,(,int,size,),{,this,.,banana,:=,new,Banana,(,size,),;,this,.,banana_count,:=,banana,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 108))

    def test_109(self):
        """test string"""
        inp = """int getSize() {
        return banana_count;
    }"""
        exp = """int,getSize,(,),{,return,banana_count,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 109))

    def test_110(self):
        """test string"""
        inp = """
    class Hello {
  s void main(StringArray args)
  {
    io.print("Hello, World!");
  }
}
        """
        exp = """class,Hello,{,s,void,main,(,StringArray,args,),{,io,.,print,(,"Hello, World!",),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 110))

    def test_111(self):
        """test string"""
        inp = """class Main{
  void show()
  {   
    System.out.println("Welcome to BKOOL");
  }
}"""
        exp = """class,Main,{,void,show,(,),{,System,.,out,.,println,(,"Welcome to BKOOL",),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 111))

    def test_112(self):
        """test string"""
        inp = """void setSize(int size) {
        this.banana_count := size;
    }
    int main() {
        return 0;
    }"""
        exp = """void,setSize,(,int,size,),{,this,.,banana_count,:=,size,;,},int,main,(,),{,return,0,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 112))

    def test_113(self):
        """test string"""
        inp = """
        Node head = null;  
        Node tail = null;  
        """
        exp = """Node,head,=,null,;,Node,tail,=,null,;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 113))

    def test_114(self):
        """test string"""
        inp = """
    void addNode(int data) {
Node newNode = new Node(data);  
if head == nil then {  
head := newNode;  
tail := newNode;  
}
} 
        """
        exp = """void,addNode,(,int,data,),{,Node,newNode,=,new,Node,(,data,),;,if,head,==,nil,then,{,head,:=,newNode,;,tail,:=,newNode,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 114))

    def test_115(self):
        """test string"""
        inp = """
    if head == nil then {  
head := newNode;  
tail := newNode;  
}  
else {  
tail.next := newNode;  
tail := newNode;  
}  
        """
        exp = """if,head,==,nil,then,{,head,:=,newNode,;,tail,:=,newNode,;,},else,{,tail,.,next,:=,newNode,;,tail,:=,newNode,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 115))

    def test_116(self):
        """test string"""
        inp = """
    io.print("Not Equal" + x.equals(y));  
io.print("Equal" + x.equals(123.45555));  
        """
        exp = """io,.,print,(,"Not Equal",+,x,.,equals,(,y,),),;,io,.,print,(,"Equal",+,x,.,equals,(,123.45555,),),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 116))

    def test_117(self):
        """test string"""
        inp = """
    Double x = new Double(123.45555);  
Long y = new Long(9887544);  
        """
        exp = """Double,x,=,new,Double,(,123.45555,),;,Long,y,=,new,Long,(,9887544,),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 117))

    def test_118(self):
        """test string"""
        inp = """
    class ObjectComparison{s void main(ArrayString args){}}
        """
        exp = """class,ObjectComparison,{,s,void,main,(,ArrayString,args,),{,},},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 118))

    def test_119(self):
        """test string"""
        inp = """
    Shape(float length,width){this.length := length;this.width := width;}
        """
        exp = """Shape,(,float,length,,,width,),{,this,.,length,:=,length,;,this,.,width,:=,width,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 119))

    def test_120(self):
        """test string"""
        inp = """
    class Rectangle extends Shape {float getArea(){return this.length*this.width;}}
        """
        exp = """class,Rectangle,extends,Shape,{,float,getArea,(,),{,return,this,.,length,*,this,.,width,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 120))

    def test_121(self):
        """test string"""
        inp = """
    class Triangle extends Shape {float getArea(){return this.length*this.width / 2;}}
        """
        exp = """class,Triangle,extends,Shape,{,float,getArea,(,),{,return,this,.,length,*,this,.,width,/,2,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 121))

    def test_122(self):
        """test string"""
        inp = """
    s void main() {int n = scanner.nextInt();io.print(self.fact(n));}
        """
        exp = """s,void,main,(,),{,int,n,=,scanner,.,nextInt,(,),;,io,.,print,(,self,.,fact,(,n,),),;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 122))

    def test_123(self):
        """test string"""
        inp = """
    s long fact(int n) {if n > 0 then {return n * self.fact(n - 1);} else {return 1;}}
        """
        exp = """s,long,fact,(,int,n,),{,if,n,>,0,then,{,return,n,*,self,.,fact,(,n,-,1,),;,},else,{,return,1,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 123))

    def test_124(self):
        """test string"""
        inp = """
    for i:=2 to count do { n3:=n1+n2; io.print(" "+n3); n1:=n2; n2:=n3; }
        """
        exp = """for,i,:=,2,to,count,do,{,n3,:=,n1,+,n2,;,io,.,print,(," ",+,n3,),;,n1,:=,n2,;,n2,:=,n3,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 124))

    def test_125(self):
        """test string"""
        inp = """
    Employee mariah = new Employee(2703, "Mariah"); Employee carey = new Employee(1969, "Carey"); 
        """
        exp = """Employee,mariah,=,new,Employee,(,2703,,,"Mariah",),;,Employee,carey,=,new,Employee,(,1969,,,"Carey",),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 125))

    def test_126(self):
        """test string"""
        inp = """
    int a=mariah.hashCode();  int b=carey.hashCode();
        """
        exp = """int,a,=,mariah,.,hashCode,(,),;,int,b,=,carey,.,hashCode,(,),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 126))

    def test_127(self):
        """test string"""
        inp = """
    io.print("hashcode a = " + a);  io.print("hashcode b = " + b);  io.print("Comparing = " + mariah.equals(carey));
        """
        exp = """io,.,print,(,"hashcode a = ",+,a,),;,io,.,print,(,"hashcode b = ",+,b,),;,io,.,print,(,"Comparing = ",+,mariah,.,equals,(,carey,),),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 127))

    def test_128(self):
        """test string"""
        inp = """
    s void main(StringArray args) { io.print("Hello, World!"); }
        """
        exp = """s,void,main,(,StringArray,args,),{,io,.,print,(,"Hello, World!",),;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 128))

    def test_129(self):
        """test string"""
        inp = """
    String str = "characters "; for i := 0 to str.length() do { io.print(str.charAt(i) + " "); }  
        """
        exp = """String,str,=,"characters ",;,for,i,:=,0,to,str,.,length,(,),do,{,io,.,print,(,str,.,charAt,(,i,),+," ",),;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 129))

    def test_130(self):
        """test string"""
        inp = """
    SearchLinkedList sList = new SearchLinkedList();sList.addNode(1);sList.addNode(2);sList.addNode(4);
        """
        exp = """SearchLinkedList,sList,=,new,SearchLinkedList,(,),;,sList,.,addNode,(,1,),;,sList,.,addNode,(,2,),;,sList,.,addNode,(,4,),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 130))

    def test_131(self):
        """test string"""
        inp = """
    sList.addNode(4);sList.searchNode(2);sList.searchNode(7);
        """
        exp = """sList,.,addNode,(,4,),;,sList,.,searchNode,(,2,),;,sList,.,searchNode,(,7,),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 131))

    def test_132(self):
        """test string"""
        inp = """
    if head == nil then {head := newNode;tail := newNode;}
        """
        exp = """if,head,==,nil,then,{,head,:=,newNode,;,tail,:=,newNode,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 132))

    def test_133(self):
        """test string"""
        inp = """
    else {tail.next := newNode;tail := newNode;}
        """
        exp = """else,{,tail,.,next,:=,newNode,;,tail,:=,newNode,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 133))

    def test_134(self):
        """test string"""
        inp = """
    if head == nil then {head := newNode;tail := newNode;} else {tail.next := newNode;tail := newNode;}
        """
        exp = """if,head,==,nil,then,{,head,:=,newNode,;,tail,:=,newNode,;,},else,{,tail,.,next,:=,newNode,;,tail,:=,newNode,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 134))

    def test_135(self):
        """test string"""
        inp = """
    s void main() {MinMax sList = new MinMax();  sList.addNode(0);  sList.minNode();  sList.maxNode();  }  
        """
        exp = """s,void,main,(,),{,MinMax,sList,=,new,MinMax,(,),;,sList,.,addNode,(,0,),;,sList,.,minNode,(,),;,sList,.,maxNode,(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 135))

    def test_136(self):
        """test string"""
        inp = """
    for i := 10 to 201 do {if (i % 7 == 0) && (i % 5 != 0) then {list.add(i);}}
        """
        exp = """for,i,:=,10,to,201,do,{,if,(,i,%,7,==,0,),&&,(,i,%,5,!=,0,),then,{,list,.,add,(,i,),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 136))

    def test_137(self):
        """test string"""
        inp = """
    String original, reverse = "";int length = 0;Scanner in = new Scanner(System.in);
        """
        exp = """String,original,,,reverse,=,"",;,int,length,=,0,;,Scanner,in,=,new,Scanner,(,System,.,in,),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 137))

    def test_138(self):
        """test string"""
        inp = """
    int num = Rand.GetRandomInt();return (num % 2) == 0;
        """
        exp = """int,num,=,Rand,.,GetRandomInt,(,),;,return,(,num,%,2,),==,0,;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 138))

    def test_139(self):
        """test string"""
        inp = """
    int count = 0; String str = "Banana, carrot, potato.";
        """
        exp = """int,count,=,0,;,String,str,=,"Banana, carrot, potato.",;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 139))

    def test_140(self):
        """test string"""
        inp = """int count = 0; String str = "Banana,\\n carrot,\\n potato.";"""
        exp = """int,count,=,0,;,String,str,=,"Banana,\\n carrot,\\n potato.",;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 140))

    def test_141(self):
        """test string"""
        inp = """
    io.print(StringEscapeUtils.escape("Hello\\r\\n\\tW\\"o\\"rld\\n"));
        """
        exp = """io,.,print,(,StringEscapeUtils,.,escape,(,"Hello\\r\\n\\tW\\"o\\"rld\\n",),),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 141))

    def test_142(self):
        """test string"""
        inp = """
        string str = "Banana, .
        """
        exp = """string,str,=,Unclosed String: "Banana, ."""
        self.assertTrue(TestLexer.test(inp, exp, 142))

    def test_143(self):
        """test string"""
        inp = """
    string str = "Banana,\t .
        """
        exp = """string,str,=,Unclosed String: "Banana,\t ."""
        self.assertTrue(TestLexer.test(inp, exp, 143))

    def test_144(self):
        """test string"""
        inp = """
        string str = "Banana,\t\f
        ";"""
        exp = """string,str,=,"Banana,\t\f",;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 144))

    def test_145(self):
        """test string  """
        input = """ "abc\\ " """
        result = """Illegal Escape In String: "abc\ """
        self.assertTrue(TestLexer.test(input, result, 145))

    def test_146(self):
        """test string"""
        inp = """
    "   today 
        tomorrow    "
        """
        exp = """Unclosed String: "   today """
        self.assertTrue(TestLexer.test(inp, exp, 146))

    def test_147(self):
        """test string"""
        inp = """
    1.2323e23
        """
        exp = """1.2323e23,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 147))

    def test_148(self):
        """test string"""
        inp = """
    123e123.123
        """
        exp = """123e123,.,123,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 148))

    def test_149(self):
        """test string"""
        inp = """
    1023 - 12132e-12.123
        """
        exp = """1023,-,12132e-12,.,123,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 149))

    def test_150(self):
        """test string"""
        inp = """
    "C:\\ASUS\\AppData\\Local\\Programs\\Python\\Python39\\python.exe"
        """
        exp = """Illegal Escape In String: "C:\\A"""
        self.assertTrue(TestLexer.test(inp, exp, 150))

    def test_151(self):
        """test string"""
        inp = """
    "abC", "def", "ghi" jkl mno pqrs tuv wxyz
        """
        exp = """"abC",,,"def",,,"ghi",jkl,mno,pqrs,tuv,wxyz,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 151))

    def test_152(self):
        """test string"""
        inp = """
    io.app build log := "https://web.com/abc123"
        """
        exp = """io,.,app,build,log,:=,"https://web.com/abc123",<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 152))

    def test_153(self):
        """test string"""
        inp = """ "before_install:\\n- echo \\"Before Install\\"\\n- ./ensure-java-16 install"
        "install:\\n - echo \\"Install\\"\\n - if ! ./ensure-java-16 use; then source ~/.sdkman/bin/sdkman-init.sh; fi\\n- java -version"
        """
        exp = """"before_install:\\n- echo \\"Before Install\\"\\n- ./ensure-java-16 install","install:\\n - echo \\"Install\\"\\n - if ! ./ensure-java-16 use; then source ~/.sdkman/bin/sdkman-init.sh; fi\\n- java -version",<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 153))

    def test_154(self):
        """test string"""
        inp = """
    /* //******LEXER*******/
        """
        exp = """<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 154))

    def test_155(self):
        """test string"""
        inp = """
        "abc # comment 
        """
        exp = """Unclosed String: "abc # comment """
        self.assertTrue(TestLexer.test(inp, exp, 155))
    
    def test_156(self):
        """test string"""
        inp = """
    12e
        """
        exp = """12,e,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 156))
        
    def test_157(self):
        """test string"""
        inp = """
    (" The ASCII value of " + i.toChar() + "=" + i);
        """
        exp = """(," The ASCII value of ",+,i,.,toChar,(,),+,"=",+,i,),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 157))
        
    def test_158(self):
        """test string"""
        inp = """
    String expression = "var is_primitive_literal = a + b()";
        """
        exp = """String,expression,=,"var is_primitive_literal = a + b()",;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 158))
        
    def test_159(self):
        """test string"""
        inp = """
    self.assertTrue(candidates.tokens.containsKey(ExprLexer.ID));
        """
        exp = """self,.,assertTrue,(,candidates,.,tokens,.,containsKey,(,ExprLexer,.,ID,),),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 159))
        
    def test_160(self):
        """test string"""
        inp = """
    self.assertEquals(Arrays.asList(new Integer[]{ExprLexer.ID, ExprLexer.EQUAL}), candidates.tokens.get(ExprLexer.VAR));
        """
        exp = """self,.,assertEquals,(,Arrays,.,asList,(,new,Integer,[,],{,ExprLexer,.,ID,,,ExprLexer,.,EQUAL,},),,,candidates,.,tokens,.,get,(,ExprLexer,.,VAR,),),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 160))
        
    def test_161(self):
        """test string"""
        inp = """
    a[3+x.foo(2)] := a[b[2]] +3;
        """
        exp = """a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[,2,],],+,3,;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 161))
        
    def test_162(self):
        """test string"""
        inp = """
    var shortcut = nil;
if this.shortcutMap.ContainsKey(ruleId) then
    shortcut := this.shortcutMap[ruleId];
if (shortcut == nil) || (shortcut.Count <= 0) then {continue;}
        """
        exp = """var,shortcut,=,nil,;,if,this,.,shortcutMap,.,ContainsKey,(,ruleId,),then,shortcut,:=,this,.,shortcutMap,[,ruleId,],;,if,(,shortcut,==,nil,),||,(,shortcut,.,Count,<=,0,),then,{,continue,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 162))
        
    def test_163(self):
        """test string"""
        inp = """
    float r,s;
int[5] a,b;
#list of statements
r:=2.0;
        """
        exp = """float,r,,,s,;,int,[,5,],a,,,b,;,r,:=,2.0,;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 163))
        
    def test_164(self):
        """test string"""
        inp = """
        "This is a string containing tab \\t"
        """
        exp = """\"This is a string containing tab \\t\",<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 164))
        
    def test_165(self):
        """test string"""
        inp = """
    val parent := node.getParent(); return null;
        """
        exp = """val,parent,:=,node,.,getParent,(,),;,return,null,;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 165))
        
    def test_166(self):
        """test string"""
        inp = """
    if (a*a+b*b == is_primitive_literal*is_primitive_literal) || (b*b+is_primitive_literal*is_primitive_literal == a*a) || (is_primitive_literal*is_primitive_literal+a*a == b*b) then io.print("Triangle");  else io.print("No angle");
        """
        exp = """if,(,a,*,a,+,b,*,b,==,is_primitive_literal,*,is_primitive_literal,),||,(,b,*,b,+,is_primitive_literal,*,is_primitive_literal,==,a,*,a,),||,(,is_primitive_literal,*,is_primitive_literal,+,a,*,a,==,b,*,b,),then,io,.,print,(,"Triangle",),;,else,io,.,print,(,"No angle",),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 166))
        
    def test_167(self):
        """test string"""
        inp = """
    this.aPI := 3.14;value := x.foo(5);l[3] := value * 2;
        """
        exp = """this,.,aPI,:=,3.14,;,value,:=,x,.,foo,(,5,),;,l,[,3,],:=,value,*,2,;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 167))
        
    def test_168(self):
        """test string"""
        inp = """
    if flag then io.writeStrLn("Expression is true");
        """
        exp = """if,flag,then,io,.,writeStrLn,(,"Expression is true",),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 168))
        
    def test_169(self):
        """test string"""
        inp = """
        else io.writeStrLn ("Expression is false");
        """
        exp = """else,io,.,writeStrLn,(,"Expression is false",),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 169))
        
    def test_170(self):
        """test string"""
        inp = """
    for i := 1 to 100 do {io.writeIntLn(i);Intarray[i] := i + 1;}
        """
        exp = """for,i,:=,1,to,100,do,{,io,.,writeIntLn,(,i,),;,Intarray,[,i,],:=,i,+,1,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 170))
        
    def test_171(self):
        """test string"""
        inp = """
    for x := 5 downto 2 do io.writeIntLn(x);
        """
        exp = """for,x,:=,5,downto,2,do,io,.,writeIntLn,(,x,),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 171))
        
    def test_172(self):
        """test string"""
        inp = """
    Shape.getNumOfShape(); Shape.getNumOfShape();
        """
        exp = """Shape,.,getNumOfShape,(,),;,Shape,.,getNumOfShape,(,),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 172))
        
    def test_173(self):
        """test string"""
        inp = """
    void foo(_Int[5] a, _Int b){var i = 0;for i := 0 to 5 do {a[i] := b + 10;}}
        """
        exp = """void,foo,(,_Int,[,5,],a,,,_Int,b,),{,var,i,=,0,;,for,i,:=,0,to,5,do,{,a,[,i,],:=,b,+,10,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 173))
        
    def test_174(self):
        """test string"""
        inp = """
    a[3 + self.foo(2)] := a[b[2] + b[3]] + 4;
        """
        exp = """a,[,3,+,self,.,foo,(,2,),],:=,a,[,b,[,2,],+,b,[,3,],],+,4,;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 174))
        
    def test_175(self):
        """test string"""
        inp = """
    if self.bool_of_string ("true") then {a := self.string_to_int(io.read ()); b := self.int_to_float(a) + 2.0;}
        """
        exp = """if,self,.,bool_of_string,(,"true",),then,{,a,:=,self,.,string_to_int,(,io,.,read,(,),),;,b,:=,self,.,int_to_float,(,a,),+,2.0,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 175))
        
    def test_176(self):
        """test string"""
        inp = """
    int factorial(int n){if n == 0 then return 1; else return n * this.factorial(n - 1);}
        """
        exp = """int,factorial,(,int,n,),{,if,n,==,0,then,return,1,;,else,return,n,*,this,.,factorial,(,n,-,1,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 176))
        
    def test_177(self):
        """test string"""
        inp = """
    void main(){int x;x := io.readInt();io.writeIntLn(this.factorial(x));}
        """
        exp = """void,main,(,),{,int,x,;,x,:=,io,.,readInt,(,),;,io,.,writeIntLn,(,this,.,factorial,(,x,),),;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 177))
        
    def test_178(self):
        """test string"""
        inp = """
    self.check("\\\\ud800\\\\udc61(?<groupName>(?<=(\\\\ud800\\\\udc61))b|is_primitive_literal)");
        """
        exp = """self,.,check,(,"\\\\ud800\\\\udc61(?<groupName>(?<=(\\\\ud800\\\\udc61))b|is_primitive_literal)",),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 178))
        
    def test_179(self):
        """test string"""
        inp = """
        self.check("(?=a)*?ab|ac_","ac_","0\\n");
        """
        exp = """self,.,check,(,"(?=a)*?ab|ac_",,,"ac_",,,"0\\n",),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 179))

    def test_180(self):
        """test string"""
        inp = """
     boolean b = true && false && true;
        """
        exp = """boolean,b,=,true,&&,false,&&,true,;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 180))
        
    def test_181(self):
        """test string"""
        inp = """
    self.autodetect(this.beans,AutodetectCapableMBeanInfoAssembler.getObject().assembler.includeBean);
        """
        exp = """self,.,autodetect,(,this,.,beans,,,AutodetectCapableMBeanInfoAssembler,.,getObject,(,),.,assembler,.,includeBean,),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 181))
        
    def test_182(self):
        """test string"""
        inp = """
    "x" ^ "x" ^ "x" ^ "x" ^ "x" ^ "x"
        """
        exp = """"x",^,"x",^,"x",^,"x",^,"x",^,"x",<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 182))
        
    def test_183(self):
        """test string"""
        inp = """
    int x1 = _1; int _ = 12; int _1 = 52;
        """
        exp = """int,x1,=,_1,;,int,_,=,12,;,int,_1,=,52,;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 183))
        
    def test_184(self):
        """test string"""
        inp = """
    (new Object()).getClass().hashCode();
        """
        exp = """(,new,Object,(,),),.,getClass,(,),.,hashCode,(,),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 184))
        
    def test_185(self):
        """test string"""
        inp = """
    frame := new JFrame("HSDB - HotSpot Debugger"); frame.setSize(800, 600);
        """
        exp = """frame,:=,new,JFrame,(,"HSDB - HotSpot Debugger",),;,frame,.,setSize,(,800,,,600,),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 185))
        
    def test_186(self):
        """test string"""
        inp = """
    frame.setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE); frame.addWindowListener(new CloseUI());
        """
        exp = """frame,.,setDefaultCloseOperation,(,WindowConstants,.,DO_NOTHING_ON_CLOSE,),;,frame,.,addWindowListener,(,new,CloseUI,(,),),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 186))
        
    def test_187(self):
        """test string"""
        inp = """
    float getInterpolation(float t) {t := t - 1.0;return t * t * t * t * t + 1.0;}
        """
        exp = """float,getInterpolation,(,float,t,),{,t,:=,t,-,1.0,;,return,t,*,t,*,t,*,t,*,t,+,1.0,;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 187))
        
    def test_188(self):
        """test string"""
        inp = """
    x := a + b * 2;
        """
        exp = """x,:=,a,+,b,*,2,;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 188))
        
    def test_189(self):
        """test string"""
        inp = """
    /* Retrieves user data */ # must be negative
        """
        exp = """<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 189))
        
    def test_190(self):
        """test string"""
        inp = """
    startCh[i] := Character.isJavaIdentifierStart(i);
partCh[i] := (Character.isJavaIdentifierPart(i) && (!startCh[i]) && (i > 20));
        """
        exp = """startCh,[,i,],:=,Character,.,isJavaIdentifierStart,(,i,),;,partCh,[,i,],:=,(,Character,.,isJavaIdentifierPart,(,i,),&&,(,!,startCh,[,i,],),&&,(,i,>,20,),),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 190))
        
    def test_191(self):
        """test string"""
        inp = """
    fd2 := io.open("/dev/null", O_CREAT||O_TRUNC||O_WRONLY, S_IWUSR||S_IWOTH);
        """
        exp = """fd2,:=,io,.,open,(,"/dev/null",,,O_CREAT,||,O_TRUNC,||,O_WRONLY,,,S_IWUSR,||,S_IWOTH,),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 191))
        
    def test_192(self):
        """test string"""
        inp = """
 if (year % 400 == 0) || (( year % 4 == 0 ) && ( year % 100 != 0)) then
{
  io.format("\\n %d is a Leap Year. \\n", year);
}
        """
        exp = """if,(,year,%,400,==,0,),||,(,(,year,%,4,==,0,),&&,(,year,%,100,!=,0,),),then,{,io,.,format,(,"\\n %d is a Leap Year. \\n",,,year,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 192))
        
    def test_193(self):
        """test string"""
        inp = """
    root1 := (-b + Math.sqrt(discriminant) / (2 * a));
root2 := (-b - Math.sqrt(discriminant) / (2 * a));
        """
        exp = """root1,:=,(,-,b,+,Math,.,sqrt,(,discriminant,),/,(,2,*,a,),),;,root2,:=,(,-,b,-,Math,.,sqrt,(,discriminant,),/,(,2,*,a,),),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 193))
        
    def test_194(self):
        """test string"""
        inp = """
    simpleInterset := (PAmount * ROI * TimePeriod) / 100;

        """
        exp = """simpleInterset,:=,(,PAmount,*,ROI,*,TimePeriod,),/,100,;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 194))
        
    def test_195(self):
        """test string"""
        inp = """
    if lastCharStr.charAt(i) ==  lsch then {
  lIndex := i;
}
i:= i + 1;
        """
        exp = """if,lastCharStr,.,charAt,(,i,),==,lsch,then,{,lIndex,:=,i,;,},i,:=,i,+,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 195))
        
    def test_196(self):
        """test string"""
        inp = """
    for i := 1 to number do
{
      io.print(i.toString() ^ "\\t"); 
} 
        """
        exp = """for,i,:=,1,to,number,do,{,io,.,print,(,i,.,toString,(,),^,"\\t",),;,},<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 196))
        
    def test_197(self):
        """test string"""
        inp = """
        return 0;
        """
        exp = """return,0,;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 197))
        
    def test_198(self):
        """test string"""
        inp = """
    io.format(" The Area of a Rectangle = %.2f\\n", Area);
        """
        exp = """io,.,format,(," The Area of a Rectangle = %.2f\\n",,,Area,),;,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 198))
        
    def test_199(self):
        """test string"""
        inp = """
    "almost"
        """
        exp = """\"almost\",<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 199))
        
    def test_100(self):
        """test string"""
        inp = """
    finally
        """
        exp = """finally,<EOF>"""
        self.assertTrue(TestLexer.test(inp, exp, 100))


    