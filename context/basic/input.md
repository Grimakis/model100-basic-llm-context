## Keyboard Input Commands and Functions

### INKEY$
**Syntax:** `INKEY$`

**Description:** Returns the string value of the key currently pressed without pausing execution. If no key is pressed, it returns a null character (`" ").

**Example:** `A$ = INKEY$`

### INPUT "prompt"; variable list
**Syntax:** `INPUT "prompt"; variable list`

**Description:** Displays the prompt, halts execution, and waits for the user to enter data for the specified variables.

**Example:** `INPUT "X, Y Values"; X, Y`

### INPUT$ (numeric expression)
**Syntax:** `INPUT$ (numeric expression)`

**Description:** Reads exactly `numeric expression` characters from the keyboard without echoing them; all keys except `(BREAK)` are accepted.

**Example:** `A$ = INPUT$(5)`

### KEY function key number, string expression
**Syntax:** `KEY function key number, string expression`

**Description:** Redefines the specified function key so that pressing it injects the provided string expression.

**Example:** `KEY 6, "?TIMES" + CHR$(13)`

### KEY LIST
**Syntax:** `KEY LIST`

**Description:** Lists the current function key definitions on the screen.

### KEY (function key number) ON/OFF/STOP
**Syntax:** `KEY (function key number) ON` / `OFF` / `STOP`

**Description:** Enables or disables the interrupt for the given function key.

**Example:** `KEY (2) ON`, `KEY (4) OFF`

### LINE INPUT "prompt"; string variable
**Syntax:** `LINE INPUT "prompt"; string variable`

**Description:** Displays the prompt, waits for a line of text, and assigns it to the string variable (including blanks).

**Example:** `LINE INPUT "Enter Name and Address"; NA$`

### ON KEY GOSUB line number list
**Syntax:** `ON KEY GOSUB line number list`

**Description:** Assigns a GOSUB routine to a list of function keys; pressing the nth function key jumps to the nth line number.

**Example:** `ON KEY GOSUB 1000, 2000, 3000, 5000`
