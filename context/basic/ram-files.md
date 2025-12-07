# RAM Files (RAM)

## Filenames and Extensions
- RAM filenames are 1–6 characters long and must start with a letter.
- Common extensions:
  - `.BA` – BASIC program file
  - `.DO` – ASCII formatted file (data or Text Editor)
  - `.CO` – machine-language command file
- Most commands that accept a device default to RAM, and BASIC often infers the extension.

## RAM I/O Commands and Functions

### CLOSE file number list
**Syntax:** `CLOSE file number list`

**Description:** Closes the specified RAM buffers (e.g., `CLOSE 1,2,3`).

### EOF
**Syntax:** `EOF (file number)`

**Description:** Tests whether the RAM file has reached end-of-file (`IF EOF(1) THEN GOTO 1000`). Returns `-1` (true) at EOF, `0` otherwise.

### INPUT #
**Syntax:** `INPUT #file number, variable list`

**Description:** Reads data sequentially from the RAM file into the variables (e.g., `INPUT #1, A, B, C$`).

### INPUTS
**Syntax:** `INPUTS (length, file number)`

**Description:** Reads `length` characters from the RAM file and returns them as a string (e.g., `A$ = INPUTS(5.1)`).

### IPL
**Syntax:** `IPL "filename"`

**Description:** Designates the RAM program as the warm-start routine that runs immediately after powering on.

### KILL
**Syntax:** `KILL "filename"

**Description:** Deletes the RAM file (must specify extension, e.g., `KILL "MSGS.DO"`).

### LINE INPUT #
**Syntax:** `LINE INPUT #file number, string variable`

**Description:** Reads a line of text from the RAM buffer.

### LOAD
**Syntax:** `LOAD "RAM:filename", R`

**Description:** Loads a BASIC program from RAM; `R` runs it immediately afterward (e.g., `LOAD "TIMSET", R`).

### LOADM
**Syntax:** `LOADM "RAM:filename"`

**Description:** Loads a machine-language module from RAM at the address recorded when it was saved.

### MAXFILES
**Syntax:** `MAXFILES`

**Description:** Controls the maximum number of files that can be open simultaneously. Example: `10 MAXFILES = 5` then `?MAXFILES`.

### MERGE
**Syntax:** `MERGE "RAM:filename"`

**Description:** Merges lines from an ASCII-formatted RAM file into the current program (e.g., `MERGE "RAM ACT.DO"`).

### NAME
**Syntax:** `NAME "RAM:old filename" AS "RAM:new filename"`

**Description:** Renames a RAM file while keeping the extension.

### OPEN
**Syntax:** `OPEN "RAM:filename" FOR mode AS file number`

**Description:** Allocates a buffer for the RAM file. Mode can be `OUTPUT`, `INPUT`, or `APPEND`.

### PRINT #
**Syntax:** `PRINT #file number, expression list`

**Description:** Sends data to the RAM file buffer.

### PRINT # USING
**Syntax:** `PRINT #file number, USING "format"; expression list`

**Description:** Formats the output before writing to RAM, using the same format specifiers as `PRINT USING`.

### RUN
**Syntax:** `RUN "RAM:filename", R`

**Description:** Loads and runs the BASIC program from RAM. If `R` is present, open files stay open.

### RUNM
**Syntax:** `RUNM "RAM:filename"`

**Description:** Loads and executes a machine-language program stored in RAM. The target must be a standalone executable.

### SAVE
**Syntax:** `SAVE "RAM:filename", A`

**Description:** Saves the current BASIC program to RAM. `A` saves in ASCII; otherwise a compressed binary copy is written.

### SAVEM
**Syntax:** `SAVEM "RAM:filename", start address, end address, entry address`

**Description:** Saves a block of memory as a machine-language program. Entry address defaults to start if omitted.

### TAB
**Syntax:** `TAB (numeric expression)`

**Description:** Inserts spaces before the next output when writing to a RAM file.
