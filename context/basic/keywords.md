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
**Description:** Returns the single-precision form of numeric expression. A! = CSNG(0.66666666666)
**Description:** <a id='a309005e-e387-4e35-a27b-a6ae91b2b353'></a>
**Description:** 12
**Description:** <!-- PAGE BREAK -->
**Description:** <a id='55cd82d7-4245-4e4f-a69a-b023639288d5'></a>
**Description:** DATA constant list Defines a set of constants (numeric and/or string) to be accessed by a READ command. DATA 10,25,50,15, "Probabilities", "Total"
**Description:** DATES$ Keeps track of the current date, in string form. You may access it like any string variable. PRINT DATES$            DATES$ = "11/02/82"
**Description:** DAYS$ Keeps track of the current day of the week, in string form. You may access DAY$ like any string variable. PRINT DAYS$             DAYS$ = "Fri"
**Description:** DEFDBL letter list Defines all of the variables which begin with the letters in letter list to be double precision variables. Letter list consists of individual letters and/or letter ranges of the form letter1-letter2. 100 DEFDBL D, X-Z
**Description:** DEFINT letter list Defines all of the variables which begin with the letters in letter list to be integer variables. letter list consists of individual letters and/or letter ranges of the form letter1-letter2. DEFINT D, X-Z
**Description:** DEFSNG letter list Defines all of the variables which begin with the letters in letter list to be single precision variables. letter list consists of individual letters and/or letter ranges of the form letter1-letter2. DEFSNG D, X-Z
**Description:** DEFSTR letter list Defines all of the variables which begin with the letters in letter list to be string variables. letter list consists of individual letters and/or letter ranges of the form letter1-letter2. DEFSTR D, X-Z
**Description:** DIM variable name(dimensions) list Defines variable name as an array with the given dimensions. dimensions is a list of one or more numeric expressions, defining the "length", "width", and so on for the array. DIM A$(10) BAL%(10,10)
**Description:** EDIT line number range Enter text editing mode using the given lines. EDIT 100-1000           EDIT              EDIT-200
**Description:** END Terminates execution of the BASIC program. END
**Description:** ERL Returns the line number of the last error. IF ERL = 140 THEN RESUME 150
**Description:** ERR Returns the error code number of the last error. IF ERR = 18 THEN RESUME
**Description:** <a id='f23ba006-94cc-4846-84b7-301068053b8d'></a>
**Description:** 13
**Description:** <a id='63bddb97-9bd3-4249-a781-c6a024de3ad0'></a>

### ERROR
**Syntax:** `ERROR`
**Description:** *numeric expression* Simulates the error specified by *numeric expression.* ERROR 35 ERROR ERR

### EXP
**Syntax:** `EXP`
**Description:** (*numeric expression*) Returns the exponential (antilog) of *numeric expression.* PRINT EXP(14)

### FIX
**Syntax:** `FIX`
**Description:** (*numeric expression*) Returns the whole number portion of *numeric expression.* 10 A% = FIX(A2#)

### FOR
**Syntax:** `FOR`
**Description:** *counter variable* = *initial value* **TO** *final value* **STEP** *increment* ...**NEXT** *counter variable* Executes the commands between the FOR command and the NEXT command repetitively, varying counter variable from initial value to final value, adding increment to it each time BASIC ends the loop. FOR I = 1 TO 100 STEP 4: (): NEXT I

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

### IF
**Syntax:** `IF`
**Description:** *relational or logical expression* **THEN** *command(s)*1 **ELSE** *command(s)*2 Tests the logical "truth" of relational or logical expression. If the expression is "true", then BASIC executes command(s)1. If the expression is "false", BASIC executes command(s)2. IF A > B THEN GOTO 100 ELSE INPUT A,B

### INP
**Syntax:** `INP`
**Description:** (*port number*) Returns a byte from the specified CPU port *number.* A% = INP(5)
**Description:** <a id='30a1631b-147d-493e-a594-8ed15c358a0f'></a>
**Description:** 14
**Description:** <!-- PAGE BREAK -->
**Description:** <a id='00f2b352-78c9-4993-8435-2474eaae4f5c'></a>
**Description:** INSTR (start position, search string, match string) Searches search string for the first occurrence of match string, beginning at start position. If the string is found, INSTR returns the position in the string where it occurs. If the string isn't found, then INSTR returns a zero. PRINT INSTR(1,"dimenthylsulfate","sulfate")
**Description:** INT(numeric expression) Returns the whole number representation of numeric expression not greater than numeric expression. A# = INT(-214.995)
**Description:** LEFT$(string expression,length) Returns the first length characters of string expression. DAY$ = LEFT$("THURSDAY",3)
**Description:** LEN(string expression) Returns the number of characters in string expression. A% = LEN("February")
**Description:** LET variable = expression Assign value of expression to variable. variable must be of the same data type as expression (that is, numeric or string). The word LET is optional. LET A$ = "The" A$ = "The"
**Description:** LOG (numeric expression) Returns the natural logarithm (base "e") of numeric expression. numeric expression must be greater than zero. A = LOG(10)
**Description:** MENU Exits BASIC and returns you to the Model 100 Menu. MENU
**Description:** MID$(string expression,position,length) Returns length characters from string expression starting at position. 10 HASH$ = MID$(A$,2,2)
**Description:** MID$(string expression 1,position,length)=string expression2 Replaces characters of string expression 1 starting at position with string expression 2. length and position are numeric expressions. length is optional and if present is ignored. MID$(A$,5) = "FF"
**Description:** NEW Erases the current program, sets numeric variables equal to zero, and sets string variables equal to null (""). NEW
**Description:** ON ERROR GOTO line number Defines an error trapping interrupt. ON ERROR GOTO 1000
**Description:** <a id='9081036c-37bb-4683-840f-1c9e613f9aee'></a>
**Description:** 15
**Description:** <a id='ae330c50-1464-4631-a595-0d219c9d836b'></a>
**Description:** ON TIMES = "time" GOSUB line number Defines an interrupt for a clock condition. time is a string expression in the form HH:MM:SS. ON TIMES = "14 20 00" GOSUB 1000
**Description:** ON numeric expression GOTO line number list Evaluates numeric expression to an integer n, and then branches to the nth line number in the list. ON X GOTO 100,200,300
**Description:** ON numeric expression GOSUB line number list Evaluates numeric expression to an integer n, and then calls the subroutine beginning at the nth line number in the list. ON X GOSUB 100,200,300
**Description:** OUT port number, byte value Outputs byte value to the CPU port number. OUT 55.100
**Description:** PEEK (memory address) Returns the byte value stored at memory address. A% = PEEK(16999)
**Description:** POKE memory address, byte value Loads memory address with byte value. POKE 62000.104
**Description:** POWER numeric expression Sets the automatic power down period. numeric expression has a range of 10 to 255. The Model 100 will automatically turn off after a period of numeric expression times 0.1 minutes if you are neither running a program nor entering commands. POWER 10
**Description:** POWER CONT Disables the automatic power down feature of the Model 100. POWER CONT
**Description:** POWER OFF, RESUME Turns off the power to the Model 100 immediately. If RESUME is present, upon turning the power back on, the Model 100 resumes execution of the program at the statement following the POWER OFF. RESUME, if not present, then the Model 100 returns to the Menu upon power up. IF TIMES > "11:30:00" THEN POWER OFF POWER OFF, RESUME
**Description:** READ variable list Reads an appropriate number of values from a DATA statement and stores the values in the variables of variable list. 120 READ A,B%, C$
**Description:** <a id='0e2b5ef0-cd3d-4e6a-8fea-180064360679'></a>
**Description:** 16
**Description:** <!-- PAGE BREAK -->
**Description:** <a id='ad946c5f-7149-46f6-b930-57262ca865c3'></a>

### REM comment statement
**Syntax:** `REM comment statement`
**Description:** Signifies to the BASIC interpreter that the remainder of the line as comment. You may abbreviate REM with an apostrophe.
**Description:** 90REM This program finds the standard deviation 100 AVE = SUM/TT "Calculate the average
**Description:** <a id='ab5fc5fc-bd23-414c-b644-87764ab3d414'></a>
**Description:** RESTORE line number Resets the DATA statement pointer to the first item in the DATA statement on line number so that a READ command can access the same values more than once. 600 RESTORE 100
**Description:** <a id='d1f291cd-5a00-405a-8dc9-28f660e193e5'></a>
**Description:** RESUME line number Ends an error handling routine by branching to line number where BASIC begins normal execution. If line number is null or 0, then BASIC returns to the line which caused the error. 1010 RESUME
**Description:** <a id='8ab44798-39d6-466e-ae31-1f1ee4f44f0d'></a>
**Description:** RETURN Ends a subroutine by branching back to the command immediately following the corresponding GOSUB. RETURN
**Description:** <a id='101035dd-3287-425a-84f4-849b8459c4ce'></a>
**Description:** RIGHTS$ (string expression,count) Returns the rightmost count characters of string expression. 10 SEC$ = RIGHTS$(TIME$,2)
**Description:** <a id='bd5da5cc-76b5-4ba2-b609-784b49ca16d3'></a>
**Description:** RND (numeric expression) Returns a pseudo-random number between 0 and 1. If numeric expression is non-zero, then RND returns a new random number. If numeric expression equals 0, then AND returns the last random number generated. PRINT RND(1) PRINT RND(0)
**Description:** <a id='8f72902d-6fd0-4d3a-b98b-9a36ad11f403'></a>
**Description:** RUN line number Clears all variables and executes the current program starting at line number. line number is optional if omitted, BASIC begins execution at the first line of the program. RUN 100 RUN
**Description:** <a id='328f2c69-921f-4ea1-9bf8-20068b0d1f3b'></a>
**Description:** SGN(numeric expression) Returns a -1 for negative, 0 for zero, and 1 for positive values of numeric expression. TTL = 10 * SGN(CR)
**Description:** <a id='ffc5b28f-227c-4fc4-9ff2-e8dcef4499c0'></a>
**Description:** SIN (numeric expression) Returns the trigonometric sine of numeric expression. The numeric expression must be in radians. Y = SIN(1.5)
**Description:** <a id='3f526769-9d2c-48df-b15c-726dbf99897f'></a>
**Description:** SPACES$ (length) Returns a string of length spaces. BS = SPACES(20) + A$
**Description:** <a id='e991f008-c925-4ce4-b42e-bcfb71dd853a'></a>
**Description:** SQR(numeric expression) Returns the square root of numeric expression. C2 = SQR(A2 + B2)
**Description:** <a id='124adbfb-ec52-4c41-8124-9aa70fdb2072'></a>
**Description:** STOP Stops execution of a BASIC program at some point other than the physical end. STOP
**Description:** STR$(numeric expression) Converts numeric expression to its string representation. B$ = "$" + STR$(BAL) + "00"
**Description:** STRING$ (length, character) Returns a string of the given length composed of character. length may range from 0 to 255. character is either a string expression or numeric expression—if it is a string expression, only the first character of the string is duplicated. If it is a numeric expression, it must evaluate to a number between 0 and 255. PRINT STRING$(20,"*") PRINT STRING$(40,239)
**Description:** <a id='d9b64e29-9c52-478e-9127-018e74f924ed'></a>

### TAN (numeric expression)
**Syntax:** `TAN (numeric expression)`
**Description:** Returns the tangent of numeric expression. numeric expression must be in radians.
**Description:** SLOPE = TAN(THETA)
**Description:** <a id='6adbddfc-813b-44bc-80e9-aa8da201d2d8'></a>
**Description:** TIMES Keeps track of the current time, in the form of a string variable. You may access it like any string variable. PRINT TIME$ TIMES$ = "10:00:00"
**Description:** <a id='7f4e4a99-193b-477b-a318-538113b34dd0'></a>
**Description:** TIME ON or OFF or STOP Enables or disables ON TIMES interrupting. TIMES ON
**Description:** <a id='3e339f92-c238-417e-a54c-2c1fcbdcc307'></a>
**Description:** VAL (string expression) Converts string expression to a numeric representation of the string. If string expression contains non-numeric characters, VAL returns only the value of the leading number, if any. A = VAL(B$)
**Description:** <a id='e99225bc-c991-4e89-ba51-4ce33ec05939'></a>
**Description:** VARPTR (variable name) Returns the memory address of variable name. LINK(1) = VARPTR(B$)
**Description:** <a id='cbbbca97-91cc-4b5c-8a59-7ec28f51b9fc'></a>
**Description:** 17
**Description:** <a id='4aa51e78-ba7b-4bd8-afec-f402f8d0237d'></a>
**Description:** 18
**Description:** <!-- PAGE BREAK -->
**Description:** <a id='ab35c934-2326-4b6b-abbc-0d0175830c53'></a>
**Description:** Keyboard Input
**Description:** <a id='bd371f41-25e0-4ee4-b378-5aef57007621'></a>

