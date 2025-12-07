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
**Description:** Converts a value to single-precision floating point (`A! = CSNG(0.66666666666)`).

### DATA constant list
**Syntax:** `DATA constant list`
**Description:** Defines a block of constants accessed by `READ` statements.
**Example:** `DATA 10,25,50,15,"Probabilities","Total"`

### DATES$
**Syntax:** `DATES$`
**Description:** Holds the current date as a string.
**Example:** `PRINT DATES$` or `DATES$ = "11/02/82"`

### DAYS$
**Syntax:** `DAYS$`
**Description:** Keeps the current day of the week as a string.
**Example:** `DAYS$ = "Fri"`

### DEFDBL letter list
**Syntax:** `DEFDBL letter list`
**Description:** Declares variables beginning with the listed letters as double precision.
**Example:** `100 DEFDBL D, X-Z`

### DEFINT letter list
**Syntax:** `DEFINT letter list`
**Description:** Declares variables beginning with the letters in the list as integers.
**Example:** `DEFINT D, X-Z`

### DEFSNG letter list
**Syntax:** `DEFSNG letter list`
**Description:** Declares listed letters as single precision variables.
**Example:** `DEFSNG D, X-Z`

### DEFSTR letter list
**Syntax:** `DEFSTR letter list`
**Description:** Declares listed letters as string variables.
**Example:** `DEFSTR D, X-Z`

### DIM variable name(dimensions) list
**Syntax:** `DIM variable name(dimensions) list`
**Description:** Defines `variable` as an array with the specified dimensions.
**Example:** `DIM A$(10)` or `BAL%(10,10)`

### EDIT line number range
**Syntax:** `EDIT line number range`
**Description:** Enters text-editing mode bounded by the given lines.
**Example:** `EDIT 100-1000`, `EDIT` (current), or `EDIT-200` to go back.

### END
**Syntax:** `END`
**Description:** Terminates program execution.

### ERL
**Syntax:** `ERL`
**Description:** Returns the line number of the last error (`IF ERL = 140 THEN RESUME 150`).

### ERR
**Syntax:** `ERR`
**Description:** Returns the error number of the last error.
**Example:** `IF ERR = 18 THEN RESUME`

### ERROR
**Syntax:** `ERROR`
**Description:** Simulates the runtime error specified by the numeric expression.
**Example:** `ERROR 35`

### EXP
**Syntax:** `EXP(numeric expression)`
**Description:** Returns the exponential (antilog) of the numeric expression.
**Example:** `PRINT EXP(14)`

### FIX
**Syntax:** `FIX(numeric expression)`
**Description:** Returns the whole number portion of a numeric expression.
**Example:** `10 A% = FIX(A2#)`

### FOR
**Syntax:** `FOR counter = start TO end [STEP increment]`
**Description:** Executes the loop body while varying `counter` from `start` up to `end`, optionally adjusting by `increment`.
**Example:** `FOR I = 1 TO 100 STEP 4` … `NEXT I`

### FRE
**Syntax:** `FRE(expression)`
**Description:** Returns unused numeric memory in bytes for numeric expressions or unused string space for string expressions.
**Example:** `?FRE(0)` and `?FRE("")`

### GOSUB
**Syntax:** `GOSUB line number`
**Description:** Transfers control to the subroutine beginning at `line number`.
**Example:** `GOSUB 1000`

### GOTO
**Syntax:** `GOTO line number`
**Description:** Branches directly to the specified line number.
**Example:** `GOTO 1000`

### HIMEM
**Syntax:** `HIMEM`
**Description:** Returns the top address of memory available to BASIC. ?HIMEM

### IF
**Syntax:** `IF`
**Description:** *relational or logical expression* **THEN** *command(s)*1 **ELSE** *command(s)*2 Tests the logical "truth" of relational or logical expression. If the expression is "true", then BASIC executes command(s)1. If the expression is "false", BASIC executes command(s)2. IF A > B THEN GOTO 100 ELSE INPUT A,B

### INP
**Syntax:** `INP`
**Description:** (*port number*) Returns a byte from the specified CPU port *number.* A% = INP(5) 

### INSTR (start position, search string, match string)
**Syntax:** `INSTR (start position, search string, match string)`
**Description:** Searches `search string` for `match string` starting at `start position`; returns the match position or zero if not found.

### INT(numeric expression)
**Syntax:** `INT(numeric expression)`
**Description:** Returns the largest integer not greater than the argument (e.g., `A# = INT(-214.995)`).

### LEFT$(string expression,length)
**Syntax:** `LEFT$(string expression,length)`
**Description:** Extracts the first `length` characters from `string expression` (e.g., `DAY$ = LEFT$("THURSDAY",3)`).

### LEN(string expression)
**Syntax:** `LEN(string expression)`
**Description:** Returns the number of characters in a string (`A% = LEN("February")`).

### LET variable = expression
**Syntax:** `LET variable = expression`
**Description:** Assigns `expression` to `variable`; the keyword is optional (`LET A$ = "The"` or `A$ = "The"`).

### LOG (numeric expression)
**Syntax:** `LOG (numeric expression)`
**Description:** Returns the natural logarithm (base e) of the argument, which must be positive (`A = LOG(10)`).

### MENU
**Syntax:** `MENU`
**Description:** Exits BASIC and returns to the Model 100 Menu.

### MID$(string expression,position,length)
**Syntax:** `MID$(string expression,position,length)`
**Description:** Returns `length` characters from `string expression` starting at `position`; also supports assignment (`MID$(A$,5)="FF"`).

### NEW
**Syntax:** `NEW`
**Description:** Erases the current program and resets numeric variables to zero and string variables to null.
**Example:** Run `NEW` before loading a fresh program.

### ON ERROR GOTO line number
**Syntax:** `ON ERROR GOTO line number`
**Description:** Sets an error-trapping interrupt that jumps to `line number` when a runtime error occurs.
**Example:** `ON ERROR GOTO 200`

### ON TIMES = "time" GOSUB line number
**Syntax:** `ON TIMES = "time" GOSUB line number`
**Description:** Defines a clock-based interrupt that GOSUBs to `line number` when the clock matches `time`.
**Example:** `ON TIMES = "12:00:00" GOSUB 100`

### ON numeric expression GOTO line number list
**Syntax:** `ON numeric expression GOTO line number list`
**Description:** Evaluates the expression to `n` and branches to the nth line number in the list.
**Example:** `ON A% GOTO 100,200,300`

### ON numeric expression GOSUB line number list
**Syntax:** `ON numeric expression GOSUB line number list`
**Description:** Calls the nth subroutine when the expression evaluates to `n`.
**Example:** `ON A% GOSUB 100,200,300`

### OUT port number, byte value
**Syntax:** `OUT port number, byte value`
**Description:** Writes a byte to the specified CPU port.
**Example:** `OUT 55,100`

### PEEK (memory address)
**Syntax:** `PEEK(memory address)`
**Description:** Reads the byte stored at the specified address.
**Example:** `A% = PEEK(16999)`

### POKE memory address, byte value
**Syntax:** `POKE memory address, byte value`
**Description:** Stores a byte at the given memory address (`POKE 62000.104`).

### POWER numeric expression
**Syntax:** `POWER numeric expression`
**Description:** Sets the auto power-off period (10–255 → 0.1-minute ticks); use `POWER CONT` to disable.

### POWER OFF, RESUME
**Syntax:** `POWER OFF, RESUME`
**Description:** Turns the Model 100 off immediately; `RESUME` continues execution after power-up.

### READ variable list
**Syntax:** `READ variable list`
**Description:** Reads values from a `DATA` statement into the specified variables (`120 READ A,B%, C$`).

### REM comment statement
**Syntax:** `REM comment statement`
**Description:** Treats the remainder of the line as a comment; you can abbreviate `REM` with an apostrophe. Example: `90REM This program...`.

### RESTORE line number
**Syntax:** `RESTORE line number`
**Description:** Resets the `DATA` pointer to the specified line so `READ` can reconsume values (`600 RESTORE 100`).

### RESUME line number
**Syntax:** `RESUME line number`
**Description:** After an error, branches to the specified line number (the default is the line that caused the error).

### RETURN
**Syntax:** `RETURN`
**Description:** Ends a subroutine and continues execution after the corresponding `GOSUB`.

### RIGHTS$ (string expression,count)
**Syntax:** `RIGHTS$(string expression,count)`
**Description:** Extracts the rightmost `count` characters of a string (`SEC$ = RIGHTS$(TIME$,2)`).

### RND (numeric expression)
**Syntax:** `RND (numeric expression)`
**Description:** Produces a random value between 0 and 1; supply zero to reuse the previous random number.

### RUN line number
**Syntax:** `RUN line number`
**Description:** Clears variables and runs the program starting at the given line; the line is optional (defaults to the first line).

### SGN(numeric expression)
**Syntax:** `SGN(numeric expression)`
**Description:** Returns `-1`, `0`, or `1` when the argument is negative, zero, or positive (`TTL = 10 * SGN(CR)`).

### SIN (numeric expression)
**Syntax:** `SIN (numeric expression)`
**Description:** Returns the sine of the angle given in radians (`Y = SIN(1.5)`).

### SPACES$ (length)
**Syntax:** `SPACES$ (length)`
**Description:** Returns a string composed of `length` spaces (`BS = SPACES$(20) + A$`).

### SQR(numeric expression)
**Syntax:** `SQR(numeric expression)`
**Description:** Returns the square root of the expression (`C2 = SQR(A2 + B2)`).

### STOP
**Syntax:** `STOP`
**Description:** Halts execution before the end of the program.

### STR$(numeric expression)
**Syntax:** `STR$(numeric expression)`
**Description:** Converts a numeric expression into its string representation (`B$ = "$" + STR$(BAL) + "00"`).

### STRING$ (length, character)
**Syntax:** `STRING$ (length, character)`
**Description:** Creates a string of the given length by repeating the specified character; numeric input must be within 0–255.

### TAN (numeric expression)
**Syntax:** `TAN (numeric expression)`
**Description:** Returns the tangent of the radian angle (`SLOPE = TAN(THETA)`).

### TIMES
**Syntax:** `TIMES`
**Description:** Tracks the current time as a string variable (`PRINT TIME$`; `TIMES$ = "10:00:00"`).

### TIME ON or OFF or STOP
**Syntax:** `TIME ON` / `TIME OFF` / `TIME STOP`
**Description:** Enables/disables or stops the `ON TIMES` interrupt mechanism.

### VAL (string expression)
**Syntax:** `VAL (string expression)`
**Description:** Converts the leading numeric portion of a string into a number (`A = VAL(B$)`).

### VARPTR (variable name)
**Syntax:** `VARPTR (variable name)`
**Description:** Returns the memory address of the named variable (`LINK(1) = VARPTR(B$)`).

