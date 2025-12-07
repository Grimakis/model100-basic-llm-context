# BASIC Interpreter Overview

## Starting the BASIC Interpreter
From the Menu, highlight `BASIC` or a BASIC program file and press ENTER. The interpreter loads and runs the selected program or opens the prompt for editing.

### LABEL
**Syntax:** `LABEL`

**Description:** Displays the LABEL line so you can verify the current function-key assignments.

### PRINT / SHIFT PRINT
**Syntax:** `PRINT` / `SHIFT PRINT`

**Description:** `PRINT` mimics `LCOPY` (ENTER) and sends the screen contents to the printer. `SHIFT PRINT` behaves like `LLIST` (ENTER) to list the program on the printer.

### F1–F6
**Syntax:** `F1` … `F6`

**Description:** Each function key is tied to the menu commands `Files`, `Load`, `Save`, `Run`, `List`, and `Menu`. You can redefine these keys inside BASIC via the `KEY` command (see Keyboard Input).

## Special Keys in Execute Mode

### BREAK
**Syntax:** `BREAK`

**Description:** Stops the current BASIC command. You can resume many interrupted commands by typing `CONT` followed by ENTER.

### PAUSE
**Syntax:** `PAUSE`

**Description:** Temporarily halts execution until you press `PAUSE` again, which is useful during fast screen updates such as `LIST`.

## Numeric and String Operators
- `+`: addition or unary plus for numeric expressions, concatenation for strings.
- `-`: subtraction or unary minus.
- `*`: multiplication.
- `/`: division.
- `\`: integer division.
- `^`: exponentiation.
- `MOD`: modulus arithmetic.

### Relational Operators
- `<`: less than
- `>`: greater than
- `=`: equal
- `<=` or `=<`: less than or equal
- `>=` or `=>`: greater than or equal
- `<>` or `><`: not equal

### Logical Operators
- `AND`: logical AND
- `OR`: logical OR
- `XOR`: exclusive OR
- `EQV`: equivalence
- `IMP`: implication
- `NOT`: logical negation

### Operator Hierarchy
1. Parentheses `()`
2. Unary `+` and `-`
3. `*`, `/`
4. `MOD`
5. `+`, `-`
6. Relational operators (`<`, `>`, `=` etc.)
7. `NOT`
8. `AND`
9. `OR`
10. `XOR`
11. `EQV`
12. `IMP`

**Note:** Operators on the same level evaluate left to right, except parentheses, which evaluate from inside out.

## Data Ranges
- **Integers:** -32,768 to 32,767
- **Single precision:** 10^-64 to 10^62 (6 significant digits)
- **Double precision:** 10^-64 to 10^62 (14 significant digits)
- **Strings:** 0 to 255 characters
- Unless declared otherwise, BASIC treats constants, variables, and numeric functions as double precision.

## Declaration Tags
- `%`: declare an integer variable.
- `!`: declare a single-precision variable.
- `#`: declare a double-precision variable.
- `$`: declare a string variable.
