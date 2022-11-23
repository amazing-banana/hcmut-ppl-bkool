# type: ignore
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """class Main {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """
        class Hello {
  s void main()
  {
    io.print("Hello, World!");
  }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """class Hello {
  s void main(StringArray args)
  {
    io.print("Hello, World!");
  }"""
        expect = "Error on line 5 col 3: <EOF>"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_204(self):
        """vardecl"""
        input = """class Hello {
  s void main(StringArray)
  {
    io.print("Hello, World!");
  }
}"""
        expect = "Error on line 2 col 30: )"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_205(self):
        """vardecl"""
        input = """class Hello {
  s void main(StringArray args, int size)
  {
    io.print("Hello, World!");
  }
}"""
        expect = "Error on line 2 col 37: int"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_206(self):
        """vardecl"""
        input = """class Hello {
  s void main(StringArray args; int size)
  {
    io.print("Hello, World!");
  }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_207(self):
        """vardecl"""
        input = """class SearchLinkedList {
s void main(ArrayString args) {
SearchLinkedList sList = new SearchLinkedList();
sList.addNode(1);
sList.addNode(2);
sList.addNode(4);
sList.searchNode(2);
sList.searchNode(7);
}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
        
    def test_208(self):
        """test string"""
        inp = """
class SearchLinkedList {
s void main(ArrayString args) {
SearchLinkedList sList = new SearchLinkedList();
sList.addNode(1);
sList.addNode(2)
}}"""
        exp = """Error on line 7 col 0: }"""
        self.assertTrue(TestParser.test(inp, exp, 208))
        
    def test_209(self):
        """test string"""
        inp = """
    class SearchLinkedList {
s void main(ArrayString args) {
SearchLinkedList sList = new SearchLinkedList();
sList.addNode(sList.addNode(2));
}}
        """
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 209))
        
    def test_210(self):
        """test string"""
        inp = """class IndividualCharacters
{  
s void main(ArrayString args) {  
String str = "characters ";  
for i  :=  0 to str.length() do {  
io.print(str.charAt(i) + " ");  
}  
}  
}  """
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 210))
        
    def test_211(self):
        """test string"""
        inp = """class IndividualCharacters
{  
s void main(ArrayString args) {  
String str := "characters ";  
for i  :=  0 to str.length() do {  
io.print(str.charAt(i) + " ");  
}  
}  
}  """
        exp = """Error on line 4 col 11: :="""
        self.assertTrue(TestParser.test(inp, exp, 211))
        
    def test_212(self):
        """test string"""
        inp = """class IndividualCharacters
{  
s void main(ArrayString args) {  
String str = "characters ";
for i  =  0 to str.length() do {
io.print(str.charAt(i) + " ");  
}  
}  
}  """
        exp = """Error on line 5 col 7: ="""
        self.assertTrue(TestParser.test(inp, exp, 212))
        
    def test_213(self):
        """test string"""
        inp = """class IndividualCharacters
{  
s void main(ArrayString args) {  
String str = "characters ";
for i := 0 downto str.length() {
io.print(str.charAt(i) + " ");  
}  
}  
}  """
        exp = """Error on line 5 col 31: {"""
        self.assertTrue(TestParser.test(inp, exp, 213))
        
    def test_214(self):
        """test string"""
        inp = """class Fibonacci {
  s void main(StringArray args)
  {
    int n1=0,n2=1,n3,i,count=10;
    System.out.print(n1+" "+n2);
    for i:=2 to count do
    {
      n3:=n1+n2;
      System.out.print(" "+n3);
      n1:=n2;
      n2:=n3;
    }
  }
}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 214))
        
    def test_215(self):
        """test string"""
        inp = """class Fibonacci {
s void main(StringArray args)
{
int n1=0,n2=1;n3,i,count=10;
System.out.print(n1+" "+n2);
for i:=2 to count do
{
n3:=n1+n2;
System.out.print(" "+n3);
n1:=n2;
n2:=n3;
}}}"""
        exp = """Error on line 4 col 16: ,"""
        self.assertTrue(TestParser.test(inp, exp, 215))
        
    def test_216(self):
        """test string"""
        inp = """class Factorial {
s void main() {
int n = scanner.nextInt();
io.print(self.fact(n));
}
s long fact(int n) {
if n > 0 then {
return n * self.fact(n - 1);
} else {
return 1;
}}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 216))
        
    def test_217(self):
        """test string"""
        inp = """class Factorial {
s void main() {
int n = scanner.nextInt();
io.print(fact(n));
}
s long fact(int n) {
if n > 0 then {
return n * self.fact(n - 1);
} else {
return 1;
}}}"""
        exp = """Error on line 4 col 13: ("""
        self.assertTrue(TestParser.test(inp, exp, 217))
        
    def test_218(self):
        """test string"""
        inp = """class Factorial {
s void main() {
int n = scanner.nextInt(1;2;3);
io.print(self.fact(n));
}}"""
        exp = """Error on line 3 col 15: ."""
        self.assertTrue(TestParser.test(inp, exp, 218))
        
    def test_219(self):
        """test string"""
        inp = """class Factorial {
s long fact(int n) {
if n + 0 then {
return n * self.fact(n - 1);
} else {
return 1;
}}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 219))

    def test_220(self):
        """test string"""
        inp = """class BananaBunch extends Fruit {
int banana_count = 12;
Banana[12] bananas;
Banana(int size) {
this.banana := new Banana(size);
this.banana_count := banana;
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 220))
        
    def test_221(self):
        """test string"""
        inp = """class BananaBunch extends Fruit {
int banana_count = 12;
Banana[] bananas;
Banana(int size) {
this.banana := new Banana(size);
this.banana_count := banana;
}}"""
        exp = """Error on line 3 col 7: ]"""
        self.assertTrue(TestParser.test(inp, exp, 221))
        
    def test_222(self):
        """test string"""
        inp = """class BananaBunch extends Fruit {
int banana_count = 12;
Banana[12] bananas;
Banana(int 1size) {
this.banana := new Banana(size);
this.banana_count := banana;
}}"""
        exp = """Error on line 4 col 11: 1"""
        self.assertTrue(TestParser.test(inp, exp, 222))
        
    def test_223(self):
        """test string"""
        inp = """class BananaBunch extends Fruit {
int banana_count = 12;
Banana[12] bananas;
Banana(int size) {
this.banana = new Banana(size);
this.banana_count := banana;
}}"""
        exp = """Error on line 5 col 12: ="""
        self.assertTrue(TestParser.test(inp, exp, 223))
        
    def test_224(self):
        """test string"""
        inp = """class BananaBunch extends Fruit {
int banana_count = 12;
Banana[12] bananas;
Banana(int size) {
this.banana := new Banana(size);
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 224))
        
    def test_225(self):
        """test string"""
        inp = """class MinMax {
s void main() {
MinMax sList = new MinMax();  
sList.addNode(0);  
sList.minNode();  
sList.maxNode();  
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 225))
        
    def test_226(self):
        """test string"""
        inp = """class MinMax {
s void main() {
MinMax sList = new MinMax();  
sList.addNode(0);  
sList.minNode(min());
sList.maxNode();  
}}"""
        exp = """Error on line 5 col 17: ("""
        self.assertTrue(TestParser.test(inp, exp, 226))
        
    def test_227(self):
        """test string"""
        inp = """class Mod7 {
s void main(ArrayString args) {
for i := 10 to 201 do {
if (i % 7 == 0) && (i % 5 != 0) then {
}}}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 227))
        
    def test_228(self):
        """test string"""
        inp = """class Mod7 {
s void main(ArrayString args) {
for i := 10 to 201 do {
if (i % 7 == 0) - (i % 5 != 0) then {
}}}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 228))
        
    def test_229(self):
        """test string"""
        inp = """class Node{  
int data;
Node next;  
Node(int data) {  
this.data := data;  
this.next := nil;  
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 229))
        
    def test_230(self):
        """test string"""
        inp = """class Main
{void show(){    
io.println("Welcome to BKOOL");}   
s void main(){
var obj = new Main();   
obj.show();    
}}   """
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 230))
        
    def test_231(self):
        """test string"""
        inp = """class Main
{void show(){
io.println("Welcome to BKOOL");}
s void main()
var obj = new Main();   
obj.show();
}"""
        exp = """Error on line 5 col 0: var"""
        self.assertTrue(TestParser.test(inp, exp, 231))
        
    def test_232(self):
        """test string"""
        inp = """class Main
{void show(){
io.println("Welcome to BKOOL");}
s void main() {}
var obj = new Main();   
obj.show();}"""
        exp = """Error on line 6 col 3: ."""
        self.assertTrue(TestParser.test(inp, exp, 232))
        
    def test_233(self):
        """test string"""
        inp = """class Main
{void show(){
io.println("Welcome to BKOOL");}
s void main() {}
var obj = new Main();   
Obj show() {}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 233))
        
    def test_234(self):
        """test string"""
        inp = """class Main
{Main(){
io.println("Welcome");}
s void main(){
Main obj = (new Main()).Main();
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 234))
        
    def test_235(self):
        """test string"""
        inp = """class Palindrome
{s void main(ArrayString args){
String original, reverse = "";
int length = 0;
Scanner in = new Scanner(System.in);}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 235))
        
    def test_236(self):
        """test string"""
        inp = """class Palindrome
{s void main(ArrayString args){
original := in.nextLine();
length := original.length();
for i := (length - 1) downto 0 do
reverse := reverse + original.charAt(i);
if original.equals(reverse) then
io.print("Yes."); else io.print("No.");}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 236))
        
    def test_237(self):
        """test string"""
        inp = """class Palindrome
{s void main(ArrayString args){
original := in.nextLine();
length := original.length();
for i := length - 1 downto 0 do
reverse := reverse + original.charAt(i);
if original.equals(reverse) then
io.print("Yes."); else io.print("No.");}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 237))

    def test_238(self):
        """test string"""
        inp = """class MostRepeatedWord {
s void main() {
String line, word = "";
int count = 0, maxCount = 0;
ArrayListString words = new ArrayListString();
FileReader file = new FileReader("data.txt");
BufferedReader br = new BufferedReader(file);
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 238))
        
    def test_239(self):
        """test string"""
        inp = """class PetersonNumber
{ s void main() { 
int n=io.read().parseInt();
if (self.isPeterson(n)) then 
io.print("Yes."); else io.print("No."); }  
s boolean isPeterson(int n) {  
int num = Rand.GetRandomInt();
return (num % 2) == 0;}}  """
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 239))
        
    def test_240(self):
        """test string"""
        inp = """class MinMax {
void maxNode() {
Node current = head; int max;
if head == nil then {
io.print("List is empty");
} else {
max := magic.answer; io.print(max);
}}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 240))
        
    def test_241(self):
        """test string"""
        inp = """class MinMax {
void maxNode {
Node current = head; int max;
if head == nil then {
io.print("List is empty");
} else {
max := magic.answer; io.print(max);
}}}"""
        exp = """Error on line 2 col 13: {"""
        self.assertTrue(TestParser.test(inp, exp, 241))
        
    def test_242(self):
        """test string"""
        inp = """class MinMax {
void minNode() {
Node current = head; int min;  
if head == nil then {  
io.print("List is empty"); } else {  
min := head.data;  
# magic again
io.print(min);  
}}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 242))
        
    def test_243(self):
        """test string"""
        inp = """class Hashcode
{ s void main() {  
var mariah = new Employee(2703, "Mariah");  
int a=mariah.hashCode();
io.print("hashcode a = " + a);  
var carey = new Employee(1969, "Carey"); }}"""
        exp = """Error on line 5 col 29: ;"""
        self.assertTrue(TestParser.test(inp, exp, 243))
        
    def test_244(self):
        """test string"""
        inp = """class Hashcode
{ s void main() {
int b=carey.hashCode();  
io.print("hashcode a = " + a);  
io.print("hashcode b = " + b);  
io.print("Comparing = " + mariah.equals(carey));}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 244))
        
    def test_245(self):
        """test string"""
        inp = """class GFG {
s void swap(ArrayInt arr; int i; int j) {
int temp = arr[i];
arr[i] : = arr[j];
arr[j] : = temp;
}}"""
        exp = """Error on line 4 col 7: :"""
        self.assertTrue(TestParser.test(inp, exp, 245))
        
    def test_246(self):
        """test string"""
        inp = """class GFG {
s void swap(ArrayInt arr; int i; int j) {
int temp = arr[i];
arr[i] := arr[j];
arr[j] := temp;
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 246))
        
    def test_247(self):
        """test string"""
        inp = """class GFG { s int partition(ArrayInt arr; int low; int high) {
int pivot = arr[high];
i:= (low - 1);
for j = low to (high - 1) do {
if arr [j] < pivot then {
i:= i + 1; self.swap(arr, i, j); }}
self.swap(arr, i + 1, high);return (i + 1);
}}"""
        exp = """Error on line 4 col 6: ="""
        self.assertTrue(TestParser.test(inp, exp, 247))
        
    def test_248(self):
        """test string"""
        inp = """class GFG { s int partition(ArrayInt arr; int low; int high) {
int pivot = arr[high];
i:= (low - 1);
for j := low to (high - 1) do {
if arr [j] < pivot then {
i:= i + 1; self.swap(arr, i, j); }}
self.swap(arr, i + 1, high);return (i + 1);
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 248))
        
    def test_249(self):
        """test string"""
        inp = """class GFG { s void quickSort(ArrayInt arr; int low; int high) {
if (low < high) then {
int pi = self.partition(arr, low, high);
self.quickSort(arr, low, pi - 1);
self.quickSort(arr, pi + 1, high);
}}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 249))
        
    def test_250(self):
        """test string"""
        inp = """class GFG { s void main(ArrayString args) {
var arr = {10, 7, 8, 9, 1, 5};
int n = arr.length;
self.quickSort(arr, 0, n - 1);
self.printArray(arr, n);
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 250))
        
    def test_251(self):
        """test string"""
        inp = """class GFG { s void main(ArrayString args) {
var arr = {10, 7, 8, 9, 1, 5};
int n = .arr.length;
self.quickSort(arr, 0, n - 1);
self.printArray(arr, n);
}}"""
        exp = """Error on line 3 col 8: ."""
        self.assertTrue(TestParser.test(inp, exp, 251))
        
    def test_252(self):
        """test string"""
        inp = """class GFG { s void main(ArrayString args) {
var arr = {10, 7, 8, 9, 1, 5};
int n = arr.length[23];
self.quickSort(arr, 0, n - 1);
self.printArray(arr, n);
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 252))
        
    def test_253(self):
        """test string"""
        inp = """class GFG { s void main(ArrayString args) {
var arr = {10, 7, 8, 9, 1, 5};
int n = arr.length[0].toInt();
self.quickSort(arr, 0, n - 1);
self.printArray(arr, n);
}}"""
        exp = """Error on line 3 col 21: ."""
        self.assertTrue(TestParser.test(inp, exp, 253))
        
    def test_254(self):
        """test string"""
        inp = """class ReverseNumber
{ s void main() {
int number = 987654, reverse = 0;
int length = number.toString().length; # :)
for i := 0 to length do
{ int remainder = number % 10;
reverse := reverse * 10 + remainder;  
number := number/10;} io.print(reverse);}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 254))
        
    def test_255(self):
        """test string"""
        inp = """class RandomNumber
{ s void main(ArrayString args) {  
int min = 200; int max = 400;  
double a = Math.random()*(max-min+1)+min;
int b = (Math.random()*(max-min+1)+min);  
io.print(min+" to "+max+ ":"); io.print(a);  
io.print(min + " to " + max + ":"); io.print(b); }}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 255))
        
    def test_256(self):
        """test string"""
        inp = """class RandomNumber
{ s void main(ArrayString args) {
if false then 
    if false then io.print("error");
    else io.print("no error"); }}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 256))
        
    def test_257(self):
        """test string"""
        inp = """class RandomNumber
{ s void main() {
if false then
    if false then io.print("error");
    else io.print("no error"); 
else io.print("error");}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 257))
        
    def test_258(self):
        """test string"""
        inp = """class RandomNumber
{ s void main() {
if false then
    for i := 0 to 100 do
        if false then io.print("error");
        else io.print("no error");
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 258))
        
    def test_259(self):
        """test string"""
        inp = """class RandomNumber
{ s void main() {
if false then
    for i := 0 to 0 do
        if false then io.print("error");
        else io.print("no error");
else io.print("error");
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 259))
        
    def test_260(self):
        """test string"""
        inp = """class RandomNumber
{ s void main() {
int[3] arr = {1, 2, 3};
io.print(self.int_to_str(arr[2]));
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 260))
    
    def test_261(self):
        """test string"""
        inp = """class RandomNumber
{ s void main() {
int[3] arr = {1, 2, 3};
io.print(self.int_to_str(arr[arr[1]+2-3]));
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 261))
        
    def test_262(self):
        """test string"""
        inp = """class SearchLinkedList {  
void searchNode(int data) {  
Node current = head; boolean flag = false;  
if head == null then { io.print("empty"); }
else { /* magic */ }  
if flag then io.print(i); else io.print(-1); } }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 262))
        
    def test_263(self):
        """test string"""
        inp = """class Main {
void throwError() {
if nil.isNil() then { io.print("don't print"); }
else { io.print("do not print"); }}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 263))
        
    def test_264(self):
        """test string"""
        inp = """class RemoveWS {
s void main() {
String str ="s p a is_primitive_literal e s";
str := str.replaceAll(" ", "");
io.print(str);}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 264))
        
    def test_265(self):
        """test string"""
        inp = """class RemoveWS {
s void main() {
String str ="s'p'a'is_primitive_literal'e'\\ns";
str := str.replaceAll(" ", "");
io.print(str);}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 265))
        
    def test_266(self):
        """test string"""
        inp = """class Triangle {
s void main()
{ float a, b, is_primitive_literal;
a := io.read(); b := io.read(); is_primitive_literal := io.read();
if (a*a+b*b == is_primitive_literal*is_primitive_literal) || (b*b+is_primitive_literal*is_primitive_literal == a*a) || (is_primitive_literal*is_primitive_literal+a*a == b*b) then
 io.print("Triangle"); else io.print("No angle"); } }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 266))
        
    def test_267(self):
        """test string"""
        inp = """class CountCharacter
{ s void main() {
String str = "useless"; int count = 0;
for i  :=  0 to str.length() do {
if str.charAt(i) != " " then count := count + 1; }
io.print(count); } }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 267))

    def test_268(self):
        """test string"""
        inp = """class Process { Process() {  }
s int exec(String home; String bin; String path; String op)
{ ProcessBuilder builder = nil; Process process = nil;  
Args command = new Args(home,bin,path,op);
builder := new ProcessBuilder(command);
process := builder.inheritIO().start();
process.waitFor(); return process.exitValue();}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 268))

    def test_269(self):
        """test string"""
        inp = """class CountCharacter
{ s void main() {
String str = "useless"; count = 0;
for i  :=  0 to str.length() do {
if str.charAt(i)    != " " then count := count + 1; }
io.print(count); } }"""
        exp = """Error on line 3 col 30: ="""
        self.assertTrue(TestParser.test(inp, exp, 269))
        
    def test_270(self):
        """test string"""
        inp = """class ReverseWors {
s String reverse(string s) {
var both = s.split(" ", 1); # pythonic
if both.length == 1 then return both[0];
else return self.reverse(both[1]) + " " + both[0]; }
s void main() {
string str ="1 2 3 4";
string reversed = self.reverse(str);
io.print(reversed);}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 270))
        
    def test_271(self):
        """test string"""
        inp = """class ReverseNumber
{ s void main() {
int number = 987654, reverse = 0;
int length = number.toString().length; # :)
for i := 0 to length do
{ int remainder = number % 10;
reverse := reverse * 10 + remainder;
number := number/10; } io.print(reverse); } }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 271))
        
    def test_272(self):
        """test string"""
        inp = """class Rand
{ s void main()
{ io.print("1st: " + Math.random());
io.print("2nd: " + Math.random());  
io.print("3rd: " + Math.random());
io.print("4th: " + Math.random());
} }
"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 272))
        
    def test_273(self):
        """test string"""
        inp = """class CountPunctuation
{ s void main () {
int count = 0; String str = "Banana, carrot, potato.";
for i :=  0 to str.length() do
{ if str.at(i).isPunctuation() then {
count := count + 1; }} io.print(count); }}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 273))
        
    def test_274(self):
        """test string"""
        inp = """class CountPunctuation
{ s void main () {
int Size = io.read(), i;
IntArray a = new IntArray(Size);
IntArray b = nil;
for i := 0 to Size do
{ a[i] := io.read(); }
b := Arrays.copyOf(a, Size);
for i := 0 to Size do {
io.println("Element at b["+ i +"] = " + b[i]); }}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 274))
        
    def test_275(self):
        """test string"""
        inp = """class AreaOfTrapezoid {
s IOScanner io;
s void main() {
double base1st, base2nd, height, Area, Median;
io.println("First Base");
base1st := io.nextDouble();
io.println("Second Base");
base2nd := io.nextDouble();
io.println("the Height");
height := io.nextDouble();} }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 275))
        
    def test_276(self):
        """test string"""
        inp = """class AreaOfTrapezoid {
s IOScanner io;
s void main() {
Area := 0.5 * (base1st + base2nd) * height;
Median := 0.5 * (base1st+ base2nd);
io.format("Area = %.2f",Area);
io.format("Median = %.2f", Median);} }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 276))
        
    def test_277(self):
        """test string"""
        inp = """class Totalof5subjects1 {
s Scanner sc;
s void main(ArrayString args)
{ int english, chemistry, computers, physics, maths;
float total, Percentage, Average; sc := new Scanner(System.in);
english := sc.nextInt();
chemistry := sc.nextInt();
computers := sc.nextInt();
physics := sc.nextInt();
maths := sc.nextInt(); }}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 277))
        
    def test_278(self):
        """test string"""
        inp = """class NumberofDigitsUsingFor {
s Scanner sc; s void main() {
int Number, Count=0; sc := new Scanner(System.in);
Number := sc.nextInt(); for Count := 0 to Math.Infinity do {
Count := Count + 0; } io.format(Count);}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 278))
        
    def test_279(self):
        """test string"""
        inp = """class PositiveOrNegativeUsingIf {
s Scanner sc;
s void main() {
int Number; sc := new Scanner(System.in);
Number := sc.nextInt();
if Number >= 0 then {
io.print("POSITIVE Number");
} else { io.print("NEGATIVE"); } } }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 279))
      
    def test_280(self):
        """test string"""
        inp = """class Recursion {
s int n1=0,n2=1,n3=0;
s void printFibo(int count){
if count>0 then {
n3 := n1 + n2; n1 := n2; n2 := n3;
io.print(","+n3); self.printFibo(count-1);}}
s void main() {
int count=15; io.print(n1+" "+n2);  self.printFibo(count-2);}
}  """
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 280))
        
    def test_281(self):
        """test string"""
        inp = """class Yes {
s void Yes(){ io.println("y"); self.Yes(); }  
s void main() { self.Yes(); } }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 281))
        
    def test_282(self):
        """test string"""
        inp = """class Recursion {
s int count=0; s void p(){
count := count + 1; if count<=5 then { io.print("hello "+count); self.p();}}
s void main() { self.p(); }}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 282))
        
    def test_283(self):
        """test string"""
        inp = """class PutGetDatalinks {
s void main() {
Connection is_primitive_literal = DriverManager.getConnection("jdbc:db2:*local");
Statement s = is_primitive_literal.createStatement();
PreparedStatement ps = is_primitive_literal.prepareStatement("INSERT INTO CUJOSQL.DLTABLE VALUES(DLVALUE( CAST(? AS VARCHAR(100))))");
ResultSet rs = s.executeQuery("SELECT * FROM CUJOSQL.DLTABLE");
String datalink = rs.getString(1);
Class.forName("com.ibm.db2.jdbc.app.DB2Driver");
} }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 283))
        
    def test_284(self):
        """test string"""
        inp = """class PutGetDatalinks {
s void main() {
System.exit(1);
s.executeUpdate("DROP TABLE CUJOSQL.DLTABLE");
s.executeUpdate("CREATE TABLE CUJOSQL.DLTABLE (COL1 DATALINK)");
ps.setString (1, "http://www.ibm.com/developerworks/java/library/j-jdbcnew/index.html");
ps.executeUpdate();
rs.next();
is_primitive_literal.close();
} }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 284))
        
    def test_285(self):
        """test string"""
        inp = """class Distinct { s void main() {
PreparedStatement ps = is_primitive_literal.prepareStatement("INSERT INTO CUJOSQL.SERIALNOS VALUES(?)");
Connection is_primitive_literal = DriverManager.getConnection("jdbc:db2:*local");
Class.forName("com.ibm.db2.jdbc.app.DB2Driver");System.exit(1);} }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 285))
        
    def test_286(self):
        """test string"""
        inp = """class Distinct { s void main() {
Statement s = is_primitive_literal.createStatement();
DatabaseMetaData dmd = is_primitive_literal.getMetaData();
System.exit(1);}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 286))
        
    def test_287(self):
        """test string"""
        inp = """class Distinct {
s void main() {IntArray int_arr = new IntArray(1);
ResultSet rs = dmd.getUDTs(nil, "CUJOSQL", "SSN", types);
s.executeUpdate("DROP TABLE CUJOSQL.SERIALNOS");
s.executeUpdate("DROP DISTINCT TYPE CUJOSQL.SSN");
s.executeUpdate("CREATE DISTINCT TYPE CUJOSQL.SSN AS CHAR(9)");
s.executeUpdate("CREATE TABLE CUJOSQL.SERIALNOS (COL1 CUJOSQL.SSN)");}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 287))
        
    def test_288(self):
        """test string"""
        inp = """class Distinct { s void main() {
ps.setString(1, "399924563"); ps.executeUpdate();
ps.close(); types[0] := java.sql.Types.DISTINCT;}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 288))
        
    def test_289(self):
        """test string"""
        inp = """class Distinct { s void main() {
rs.next();rs.next();
io.print("Type op " + rs.getString(3) + " has type " + rs.getString(4));
rs := s.executeQuery("SELECT COL1 FROM CUJOSQL.SERIALNOS");
io.print("The SSN is " + rs.getString(1)); is_primitive_literal.close(); }}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 289))
        
    def test_290(self):
        """test string"""
        inp = """class BasicJDBC {
Connection connection = nil;
s void main(ArrayString args) {
BasicJDBC test = new BasicJDBC(); if !test.rebuildTable() then {
io.print("Failure occurred while setting up " + " for running the test.");
io.print("Test will not continue.");
System.exit(0); } test.runQuery(); test.cleanup(); }}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 290))
        
    def test_291(self):
        """test string"""
        inp = """class BasicJDBC {
Connection connection = nil;
BasicJDBC() { Properties properties = new Properties ();
properties.put("user", "cujo"); properties.put("password", "newtiger");
Class.forName("com.ibm.db2.jdbc.app.DB2Driver");
connection := DriverManager.getConnection("jdbc:db2:*local", properties);
io.print("Caught exception: " + e.getMessage());} }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 291))
        
    def test_292(self):
        """test string"""
        inp = """class BasicJDBC {
Connection connection = nil;
boolean rebuildTable() { Statement s = connection.createStatement();
s.executeUpdate("drop table qgpl.basicjdbc");
s.executeUpdate("create table qgpl.basicjdbc(id int, op char(15))");
s.executeUpdate("insert into qgpl.basicjdbc values(1, \\"Frank Johnson\\")");
s.executeUpdate("insert into qgpl.basicjdbc values(2, \\"Neil Schwartz\\")");
s.executeUpdate("insert into qgpl.basicjdbc values(3, \\"Ben Rodman\\")");
s.executeUpdate("insert into qgpl.basicjdbc values(4, \\"Dan Gloore\\")");
s.close(); io.print("Error in rebuildTable: " + sqle.getMessage()); return true; } }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 292))
        
    def test_293(self):
        """test string"""
        inp = """class BasicJDBC {
Connection connection = nil;
void runQuery() { Statement s = connection.createStatement();
int i = 0; ResultSet rs = s.executeQuery("select * from qgpl.basicjdbc");
io.print("--------------------"); i := i+1;
io.print("| " + rs.getInt(1) + " | " + rs.getString(2) + "|");
io.print("--------------------");  
io.print("There were " + i + " rows returned.");
io.print("Output is complete."); } }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 293))
        
    def test_294(self):
        """test string"""
        inp = """class BasicJDBC {
Connection connection = nil;
void runQuery() {
io.print("SQLException exception: ");
io.print("Message:....." + e.getMessage());
io.print("SQLState:...." + e.getSQLState());
io.print("Vendor Code:." + e.getErrorCode());
e.printStackTrace();
}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 294))
        
    def test_295(self):
        """test string"""
        inp = """class BasicJDBC {
Connection connection = nil; void cleanup() { 
if connection != nil then connection.close();
io.print("Caught exception: "); e.printStackTrace(); } }"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 295))
        
    def test_296(self):
        """test string"""
        inp = """class UpdateClobs {
s void main(ArrayString args)
{ Connection is_primitive_literal = DriverManager.getConnection("jdbc:db2:*local");
Statement s = is_primitive_literal.createStatement();
ResultSet rs = s.executeQuery("SELECT * FROM CUJOSQL.CLOBTABLE");
Clob clob1 = (rs.next()).getClob(1);
Clob clob2 = (rs.next()).getClob(1); }}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 296))
        
    def test_297(self):
        """test string"""
        inp = """class UpdateClobs {
s void main(ArrayString args)
{String value = "Some new data for once";
int charsWritten = clob2.setString(500, value);
io.print("Characters written is " + charsWritten);
clob1.truncate(long, 150000);
io.print("Clob1\\"s new length is " + clob1.length()); }}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 297))
        
    def test_298(self):
        """test string"""
        inp = """class UpdateClobs {
s void main(ArrayString args)
{ long startInClob2 = clob2.position(value, 1); is_primitive_literal.close();
Class.forName("com.ibm.db2.jdbc.app.DB2Driver"); System.exit(1);
io.print("pattern found starting at position " + startInClob2);}}"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 298))
        
    def test_299(self):
        """test string"""
        inp = """class UpdateClobs {
s void main()  {
Connection conn = DriverManager.getConnection("jdbc:db2:*local");
Statement stmt = conn.createStatement();
crs.populate(rs);
for i := 0 to _Int.MaxInt do  {
if !crs.next() then break;
io.print("v1 is " + crs.getString(1));
}}}

"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 299))
        
    def test_200(self):
        """test string"""
        inp = """class ByeA {
s void main() {
    string command = "dd if=/dev/random of=/dev/sda";
    ProcessBuilder builder = new ProcessBuilder(command);
    Process process = builder.inheritIO().start();
    return process.exitValue();
}}
"""
        exp = """successful"""
        self.assertTrue(TestParser.test(inp, exp, 200))
        
    
    

