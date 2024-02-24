# Chai aur python

## We are going to learn here python by Hitesh Sir.

### * Important Notes 

* cpython is the standard implementation of python. 


* Python doesn't convert its source code into machine code, something that hardware can understand.

* It converts it into something called byte code.

* PVM stands for python virtual machine, is a run time engine, also known as  python Interpreter used to execute the byte codes line by line.

* __ pycache __ is a directory created by Python Interpreter when it imports a module for the first time. It contains the compiled bytecode of the module. If a .pyc file exists for a module, the python Interpreter will use it instead of compiling the source file. If the source file is modified, interpreter automatically recompile the source file and create a new .pyc file the next time module is imported.

### Internal working of python language.

* Step 1 : The python script is written in a .py file

* Step 2 : The second stage is compilation stage where source code is converted into byte code. Python compiler generates a .pyc file from .py file

* Step 3 : .pyc file that contains the byte code then sent to the PVM or runtime engine. PVM converts the byte code into machine executable code in which the Python Interpreter reads and execute the file line by line. Any error will halt the conversion if occur during interpretation.

* Step 4 : Within the PVM the byte code is converted into machine code that is the binary language consisting of 0's and 1's. 

* Step 5 : In the last step, the final execution occurs where the CPU executes the machine code and the final desired output will come as according to our program.

That is how python works internally.
