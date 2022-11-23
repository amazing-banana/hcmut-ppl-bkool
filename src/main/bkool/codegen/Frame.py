from typing import List

from AST import *
from CodeGenError import *


class Frame:
    def __init__(self, name, returnType):
        # op: String
        # returnType: Type

        self.name: str = name
        self.returnType: Type = returnType
        self.currentLabel: int = 0
        self.currOpStackSize: int = 0
        self.maxOpStackSize: int = 0
        self.currIndex: int = 0
        self.maxIndex: int = 0
        self.startLabel: List[int] = list() 
        self.endLabel: List[int] = list()
        self.indexLocal: List[int] = list()
        self.conLabel: List[int] = list()
        self.brkLabel: List[int] = list()

    def getCurrIndex(self) -> int:
        return self.currIndex

    def setCurrIndex(self, index) -> None:
        # target: _Int
        self.currIndex = index

    def getNewLabel(self) -> int:
        """
        *   return a new true_label in the method.
        *   @return an integer representing the true_label.
        """
        tmp = self.currentLabel
        self.currentLabel = self.currentLabel + 1
        return tmp

    def push(self) -> None:
        """
        *   simulate an instruction that pushes a value onto operand stacks.
        """
        self.currOpStackSize = self.currOpStackSize + 1
        if self.maxOpStackSize < self.currOpStackSize:
            self.maxOpStackSize = self.currOpStackSize

    def pop(self) -> None:
        """
        *   simulate an instruction that pops a value out of operand stacks.
        """
        self.currOpStackSize = self.currOpStackSize - 1
        if self.currOpStackSize < 0:
            raise IllegalRuntimeException("Pop empty stacks")

    def getStackSize(self) -> int:
        """
        *   get stacks size allocate for method generation.
        """
        return self.currOpStackSize

    def getMaxOpStackSize(self) -> int:
        """
        *   return the maximum size of the operand stacks that the method needs to use.
        *   @return an integer that represent the maximum stacks size
        """
        return self.maxOpStackSize

    def checkOpStack(self) -> None:
        """
        *   check if the operand stacks is empty or not.
        *   @throws IllegalRuntimeException if the operand stacks is not empty.
        """
        if self.currOpStackSize != 0:
            raise IllegalRuntimeException("Stack not empty")

    def enterScope(self, isProc: bool):
        # isProc: Boolean
        """
        *   invoked when parsing into a new scope inside a method.<p>
        *   This method will create 2 new labels that represent the starting and ending points of the scope.<p>
        *   Then, these labels are pushed onto corresponding stacks.<p>
        *   These labels can be retrieved by getStartLabel() and getEndLabel().<p>
        *   In addition, this method also saves the current target of local variable.
        """
        start = self.getNewLabel()
        end = self.getNewLabel()
        self.startLabel.append(start)
        self.endLabel.append(end)
        self.indexLocal.append(self.currIndex)
        if isProc:
            self.maxOpStackSize = 0
            self.maxIndex = 0

    def exitScope(self):
        """
        *   invoked when parsing out of a scope in a method.<p>
        *   This method will pop the starting and ending labels of this scope
        *   and restore the current target
        """
        if not self.startLabel or not self.endLabel or not self.indexLocal:
            raise IllegalRuntimeException("Error when exit scope")
        self.startLabel.pop()
        self.endLabel.pop()
        self.currIndex = self.indexLocal.pop()

    def getStartLabel(self):
        """
        *   return the starting true_label of the current scope.
        *   @return an integer representing the starting true_label
        """
        if not self.startLabel:
            raise IllegalRuntimeException("None start true_label")
        return self.startLabel[-1]

    def getEndLabel(self):
        """
        *   return the ending true_label of the current scope.
        *   @return an integer representing the ending true_label
        """
        if not self.endLabel:
            raise IllegalRuntimeException("None end true_label")
        return self.endLabel[-1]

    def getNewIndex(self):
        """
        *   return a new target for a local variable declared in a scope.
        *   @return an integer that represents the target of the local variable
        """
        tmp = self.currIndex
        self.currIndex = self.currIndex + 1
        if self.currIndex > self.maxIndex:
            self.maxIndex = self.currIndex
        return tmp

    def getMaxIndex(self):
        """
        *   return the maximum target used in generating code for the current method
        *   @return an integer representing the maximum target
        """
        return self.maxIndex

    def enterLoop(self):
        """
        *   invoked when parsing into a loop statement.<p>
        *   This method creates 2 new labels that represent the starting and ending true_label of the loop.<p>
        *   These labels are pushed onto corresponding stacks and are retrieved by getBeginLoopLabel() and getEndLoopLabel().
        """
        con = self.getNewLabel()
        brk = self.getNewLabel()
        self.conLabel.append(con)
        self.brkLabel.append(brk)

    def exitLoop(self):
        """
        *   invoked when parsing out of a loop statement.
        *   This method will take 2 labels representing the starting and ending labels of the current loop out of its stacks.
        """
        if not self.conLabel or not self.brkLabel:
            raise IllegalRuntimeException("Error when exit loop")
        self.conLabel.pop()
        self.brkLabel.pop()

    def getContinueLabel(self):
        """
        *   return the true_label of the innest ecls loop to which continue statement would jump
        *   @return an integer representing the continue true_label
        """
        if not self.conLabel:
            raise IllegalRuntimeException("None continue true_label")
        return self.conLabel[-1]

    def getBreakLabel(self):
        """
        *   return the true_label of the innest ecls loop to which break statement would jump
        *   @return an integer representing the break true_label
        """
        if not self.brkLabel:
            raise IllegalRuntimeException("None break true_label")
        return self.brkLabel[-1]
