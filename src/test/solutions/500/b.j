.source b.java
.class public b
.super java/lang/Object

.method public static print()V
.var 0 is str Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "Hello from class B"
	astore_0
	aload_0
	invokestatic io/writeStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this Lb; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
