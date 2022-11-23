# Notes

## Attribute Initilization

Public attributes are visible everywhere, and class attributes are visible in class scope.
that means this can happen.

```java
class A {
    public static final int C = B.C; // = 0?!
    int cyc0 = this.cyc1 + 1;  // = 0
    int cyc1 = this.cyc0 + -1; // = -1
    /*  how this is calculated??
        init cyc0 = ... cyc1 ...
            -> cal cyc1 = cyc0 - 1
                -> cyc0 ??? default()
            cyc1 = 0 - 1
        cyc0 = 0
    */
}
class B {
    public static final int C = A.C;  // = 0 ?!
}
```

C# will throw an error. Java? Don't know.

Getters and setters doesn't count.

## Member (Instance) visibility and inheritance

Java protected members are still visible in the same package.
Let's assume all classes are in **different packages**.

```java
class SuperClass {
    protected int protectedSuper;
    void Method(SuperClass s, BaseClass b, Subclass d) { 
        int protect;

        protect = this.protectedSuper; // works

        protect = s.protectedSuper; // works
        protect = b.protectedSuper; // works
        protect = d.protectedSuper; // works
        
        protect = b.protectedBase;  // err
        protect = d.protectedBase; // err

        protect = d.protectedSub; // err
    }
}
class BaseClass extends SuperClass {
    protected int protectedBase;
    void Method(SuperClass s, BaseClass b, SubClass d) { 
        int protect;
        
        protect = this.protectedSuper; // works
        protect = this.protectedBase; // works

        protect = s.protectedSuper;  // err
        protect = b.protectedSuper; // works
        protect = d.protectedSuper;// works
        
        protect = b.protectedBase;  // works
        protect = d.protectedBase; // works
        
        protect = d.protectedSub; // err
    }
}
class SubClass extends BaseClass {
    protected int ProtectedSub;
    protected float ProtectedBase;
       void Method(SuperClass s, BaseClass b, Subclass d) { 
        int protect;
        float prfloat;
        
        protect = this.protectedSuper;  // works
        protect = super.protectedBase; // works
        prfloat = this.protectedBase; // works
        protect = this.protectedSub; // works

        protect = s.protectedSuper; // err
        protect = b.protectedSuper; // err
        protect = d.protectedSuper; // works
        
        protect = b.protectedBase; // err
        protect = d.protectedBase; // works
        
        protect = d.protectedSub; // works
    }
}
```

Read more about this and why this makes sense: CS1540.

Static method should only be accessed by the enclosing of that method itself.

## Methods

In java (or at least the jvm), methods are virtual by default and:

- Invariant on paramaters types.
- Covariant on return type.

If a subclass method and base-class method has the same name,
if there are differences between parameters, subclass one will
shadow the base one, else it will override the base.
(int and float are primitive type, and Integer does not
extend Float, instead it extends Number)

```java
class A {
    Number get0() { return Integer.valueOf(0); }
    Float get1() { return Float.valueOf(1); }
    
}
class B extends A {
    Integer get0() { return Integer.valueOf(0); } // Override
    Integer get1(int i) { return Integer.valueOf(0); } // Shadow
}
...
A a = new B(); 
a.get1(); // call A.get1
((B)a).get1(1); // call B.get1
...
```

## Sematical reachability

If we don't write code that return properly, it will come back and
bite us in code gen.
Example

```cs
class BKoolClass {
    int main() {
        int i = 0;
        if condition then
        {
            for i := 1 to 10 do
            {
                if condition then
                {
                    break;
                    _.print("Unreachable.");
                }
                else
                {
                    return 0;
                    _.print("Unreachable.");
                }
                _.print("Unreachable here, too");
            }
        }
    }
}
