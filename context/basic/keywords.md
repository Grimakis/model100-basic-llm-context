# BASIC Keywords (except for Input/output)

### ABS(numeric expression)
**Syntax:** `ABS(numeric expression)`
**Description:** Returns the absolute value of numeric expression. A! = ABS(BAL) B = ABS(-100)

### ASC(string expression)
**Syntax:** `ASC(string expression)`
**Description:** Returns the ASCII code for the first character of string expression. A% = ASC(MN$) PRINT ASC(MN$)

### ATN(numeric expression)
**Syntax:** `ATN(numeric expression)`
**Description:** Returns the arctangent (in radians) of numeric expression. AN = ATN(TH) PC = ATN(3.14)

### CALL address, expression1, expression2
**Syntax:** `CALL address, expression1, expression2`
**Description:** Calls a machine level subroutine beginning at address. Upon entry to the subroutine, the A register contains the value of expression1 and the HL register contains the value of expression2. CALL 60000, 10 VARPTR(A%)

### CDBL(numeric expression)
**Syntax:** `CDBL(numeric expression)`
**Description:** Converts the value of numeric expression to a double-precision number. A# = CDBL(A%)

### CHR$(numeric expression)
**Syntax:** `CHR$(numeric expression)`
**Description:** Returns the ASCII character for the value of numeric expression. PRINT CHR$(65) PRINT "He said ";CHR$(34);"Hello";CHR$(34)

### CINT(numeric expression)
**Syntax:** `CINT(numeric expression)`
**Description:** Returns the largest integer not greater than the numeric expression. A% = CINT(45.67) B = CINT(B#)/CINT(A!)

### CLEAR string space, high memory
**Syntax:** `CLEAR string space, high memory`
**Description:** Clears the values in all numeric and string variables, closes all open files, allocates string space bytes for string storage, and sets the end of BASIC memory to high memory. CLEAR 100,50000 CLEAR 500 CLEAR 0,MAXRAM

### CONT
**Syntax:** `CONT`
**Description:** Resumes execution of a program after you have pressed BREAK or else after BASIC has encountered a STOP command in the program. CONT

### COS(numeric expression)
**Syntax:** `COS(numeric expression)`
**Description:** Returns the cosine of the radian angle given by numeric expression. Y = COS(60*0.01745329)

### CSNG(numeric expression)
**Syntax:** `CSNG(numeric expression)`
**Description:** Returns the single-precision form of numeric expression. A! = CSNG(0.66666666666) </a> 12 <!-- PAGE BREAK --> </a> DATA constant list Defines a set of constants (numeric and/or string) to be accessed by a READ command. DATA 10,25,50,15, "Probabilities", "Total" DATES$ Keeps track of the current date, in string form. You may access it like any string variable. PRINT DATES$ DATES$ = "11/02/82" DAYS$ Keeps track of the current day of the week, in string form. You may access DAY$ like any string variable. PRINT DAYS$ DAYS$ = "Fri" DEFDBL letter list Defines all of the variables which begin with the letters in letter list to be double precision variables. Letter list consists of individual letters and/or letter ranges of the form letter1-letter2. 100 DEFDBL D, X-Z DEFINT letter list Defines all of the variables which begin with the letters in letter list to be integer variables. letter list consists of individual letters and/or letter ranges of the form letter1-letter2. DEFINT D, X-Z DEFSNG letter list Defines all of the variables which begin with the letters in letter list to be single precision variables. letter list consists of individual letters and/or letter ranges of the form letter1-letter2. DEFSNG D, X-Z DEFSTR letter list Defines all of the variables which begin with the letters in letter list to be string variables. letter list consists of individual letters and/or letter ranges of the form letter1-letter2. DEFSTR D, X-Z DIM variable name(dimensions) list Defines variable name as an array with the given dimensions. dimensions is a list of one or more numeric expressions, defining the "length", "width", and so on for the array. DIM A$(10) BAL%(10,10) EDIT line number range Enter text editing mode using the given lines. EDIT 100-1000 EDIT EDIT-200 END Terminates execution of the BASIC program. END ERL Returns the line number of the last error. IF ERL = 140 THEN RESUME 150 ERR Returns the error code number of the last error. IF ERR = 18 THEN RESUME </a> 13 </a>

### ERROR
**Syntax:** `ERROR`
**Description:** *numeric expression* Simulates the error specified by *numeric expression.* ERROR 35 ERROR ERR

### EXP
**Syntax:** `EXP`
**Description:** (*numeric expression*) Returns the exponential (antilog) of *numeric expression.* PRINT EXP(14)

### FIX
**Syntax:** `FIX`
**Description:** (*numeric expression*) Returns the whole number portion of *numeric expression.* 10 A% = FIX(A2#)

### STEP
**Syntax:** `STEP`
**Description:** *increment* ...

### NEXT
**Syntax:** `NEXT`
**Description:** *counter variable* Executes the commands between the FOR command and the NEXT command repetitively, varying counter variable from initial value to final value, adding increment to it each time BASIC ends the loop. FOR I = 1 TO 100 STEP 4: (): NEXT I

### FRE
**Syntax:** `FRE`
**Description:** (*expression*) Returns the current amount of unused numeric memory in bytes when expression is numeric and the current total amount of unused string space when expression is string-type. ?FRE(0) ?FRE("")

### GOSUB
**Syntax:** `GOSUB`
**Description:** *line number* Transfers program control to the subroutine beginning at *line number.* GOSUB 1000

### GOTO
**Syntax:** `GOTO`
**Description:** *line number* Branches program control to the specified line *number.* GOTO 1000

### HIMEM
**Syntax:** `HIMEM`
**Description:** Returns the top address of memory available to BASIC. ?HIMEM

### ELSE
**Syntax:** `ELSE`
**Description:** *command(s)*2 Tests the logical "truth" of relational or logical expression. If the expression is "true", then BASIC executes command(s)1. If the expression is "false", BASIC executes command(s)2. IF A > B THEN GOTO 100 ELSE INPUT A,B

### INP
**Syntax:** `INP`
**Description:** (*port number*) Returns a byte from the specified CPU port *number.* A% = INP(5) </a> 14 <!-- PAGE BREAK --> </a> INSTR (start position, search string, match string) Searches search string for the first occurrence of match string, beginning at start position. If the string is found, INSTR returns the position in the string where it occurs. If the string isn't found, then INSTR returns a zero. PRINT INSTR(1,"dimenthylsulfate","sulfate") INT(numeric expression) Returns the whole number representation of numeric expression not greater than numeric expression. A# = INT(-214.995) LEFT$(string expression,length) Returns the first length characters of string expression. DAY$ = LEFT$("THURSDAY",3) LEN(string expression) Returns the number of characters in string expression. A% = LEN("February") LET variable = expression Assign value of expression to variable. variable must be of the same data type as expression (that is, numeric or string). The word LET is optional. LET A$ = "The" A$ = "The" LOG (numeric expression) Returns the natural logarithm (base "e") of numeric expression. numeric expression must be greater than zero. A = LOG(10) MENU Exits BASIC and returns you to the Model 100 Menu. MENU MID$(string expression,position,length) Returns length characters from string expression starting at position. 10 HASH$ = MID$(A$,2,2) MID$(string expression 1,position,length)=string expression2 Replaces characters of string expression 1 starting at position with string expression 2. length and position are numeric expressions. length is optional and if present is ignored. MID$(A$,5) = "FF" NEW Erases the current program, sets numeric variables equal to zero, and sets string variables equal to null (""). NEW ON ERROR GOTO line number Defines an error trapping interrupt. ON ERROR GOTO 1000 </a> 15 </a> ON TIMES = "time" GOSUB line number Defines an interrupt for a clock condition. time is a string expression in the form HH:MM:SS. ON TIMES = "14 20 00" GOSUB 1000 ON numeric expression GOTO line number list Evaluates numeric expression to an integer n, and then branches to the nth line number in the list. ON X GOTO 100,200,300 ON numeric expression GOSUB line number list Evaluates numeric expression to an integer n, and then calls the subroutine beginning at the nth line number in the list. ON X GOSUB 100,200,300 OUT port number, byte value Outputs byte value to the CPU port number. OUT 55.100 PEEK (memory address) Returns the byte value stored at memory address. A% = PEEK(16999) POKE memory address, byte value Loads memory address with byte value. POKE 62000.104 POWER numeric expression Sets the automatic power down period. numeric expression has a range of 10 to 255. The Model 100 will automatically turn off after a period of numeric expression times 0.1 minutes if you are neither running a program nor entering commands. POWER 10 POWER CONT Disables the automatic power down feature of the Model 100. POWER CONT POWER OFF, RESUME Turns off the power to the Model 100 immediately. If RESUME is present, upon turning the power back on, the Model 100 resumes execution of the program at the statement following the POWER OFF. RESUME, if not present, then the Model 100 returns to the Menu upon power up. IF TIMES > "11:30:00" THEN POWER OFF POWER OFF, RESUME READ variable list Reads an appropriate number of values from a DATA statement and stores the values in the variables of variable list. 120 READ A,B%, C$ </a> 16 <!-- PAGE BREAK --> </a>

### REM comment statement
**Syntax:** `REM comment statement`
**Description:** Signifies to the BASIC interpreter that the remainder of the line as comment. You may abbreviate REM with an apostrophe. 90REM This program finds the standard deviation 100 AVE = SUM/TT "Calculate the average </a> RESTORE line number Resets the DATA statement pointer to the first item in the DATA statement on line number so that a READ command can access the same values more than once. 600 RESTORE 100 </a> RESUME line number Ends an error handling routine by branching to line number where BASIC begins normal execution. If line number is null or 0, then BASIC returns to the line which caused the error. 1010 RESUME </a> RETURN Ends a subroutine by branching back to the command immediately following the corresponding GOSUB. RETURN </a> RIGHTS$ (string expression,count) Returns the rightmost count characters of string expression. 10 SEC$ = RIGHTS$(TIME$,2) </a> RND (numeric expression) Returns a pseudo-random number between 0 and 1. If numeric expression is non-zero, then RND returns a new random number. If numeric expression equals 0, then AND returns the last random number generated. PRINT RND(1) PRINT RND(0) </a> RUN line number Clears all variables and executes the current program starting at line number. line number is optional if omitted, BASIC begins execution at the first line of the program. RUN 100 RUN </a> SGN(numeric expression) Returns a -1 for negative, 0 for zero, and 1 for positive values of numeric expression. TTL = 10 * SGN(CR) </a> SIN (numeric expression) Returns the trigonometric sine of numeric expression. The numeric expression must be in radians. Y = SIN(1.5) </a> SPACES$ (length) Returns a string of length spaces. BS = SPACES(20) + A$ </a> SQR(numeric expression) Returns the square root of numeric expression. C2 = SQR(A2 + B2) </a> STOP Stops execution of a BASIC program at some point other than the physical end. STOP STR$(numeric expression) Converts numeric expression to its string representation. B$ = "$" + STR$(BAL) + "00" STRING$ (length, character) Returns a string of the given length composed of character. length may range from 0 to 255. character is either a string expression or numeric expression—if it is a string expression, only the first character of the string is duplicated. If it is a numeric expression, it must evaluate to a number between 0 and 255. PRINT STRING$(20,"*") PRINT STRING$(40,239) </a>

### TAN (numeric expression)
**Syntax:** `TAN (numeric expression)`
**Description:** Returns the tangent of numeric expression. numeric expression must be in radians. SLOPE = TAN(THETA) </a> TIMES Keeps track of the current time, in the form of a string variable. You may access it like any string variable. PRINT TIME$ TIMES$ = "10:00:00" </a> TIME ON or OFF or STOP Enables or disables ON TIMES interrupting. TIMES ON </a> VAL (string expression) Converts string expression to a numeric representation of the string. If string expression contains non-numeric characters, VAL returns only the value of the leading number, if any. A = VAL(B$) </a> VARPTR (variable name) Returns the memory address of variable name. LINK(1) = VARPTR(B$) </a> 17 </a> 18 <!-- PAGE BREAK --> </a> Keyboard Input </a>

