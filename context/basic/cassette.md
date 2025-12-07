# Cassette Recorder/Player (CAS)

## Cassette Filenames
- Names are 1–6 characters long and must begin with a letter.
- No extension is required; examples include `ACCTM`, `MEMTST`, `CLK100`.

## Cassette Commands

### CLOAD "filename", R
**Syntax:** `CLOAD "filename", R`

**Description:** Clears the current BASIC program and loads one from cassette. Include `R` to run immediately after loading.

### CLOAD?
**Syntax:** `CLOAD? filename`

**Description:** Compares the cassette file with the currently loaded BASIC program; prints `OK` if they match.

### CLOADM
**Syntax:** `CLOADM "filename"`

**Description:** Loads a machine-language program from cassette into memory using the previously stored address.

### CLOSE file number list
**Syntax:** `CLOSE file number list`

**Description:** Closes cassette buffers (`CLOSE 1,2,3`).

### CSAVE "filename", A
**Syntax:** `CSAVE "filename", A`

**Description:** Stores the current BASIC program to cassette. Use `A` for ASCII; omit it for binary.

### CSAVEM
**Syntax:** `CSAVEM "filename", start address, end address, entry address`

**Description:** Saves a machine-language block to cassette along with its entry point.

### EOF
**Syntax:** `EOF (file number)`

**Description:** Tests for end of the cassette file (`IF EOF(1) THEN GOTO 1000`). Returns `-1` when reached.

### INPUT #
**Syntax:** `INPUT #file number, variable list`

**Description:** Reads sequential data from the cassette buffer.

### INPUTS$
**Syntax:** `INPUTS$ (numeric expression, file number)`

**Description:** Returns a string of the specified length from cassette.

### LINE INPUT #
**Syntax:** `LINE INPUT #file number, string variable`

**Description:** Reads a line of text from the cassette buffer.

### LOAD "CAS:filename", R
**Syntax:** `LOAD "CAS:filename", R`

**Description:** Loads a BASIC program from cassette; `R` runs it after loading.

### LOADM "CAS:filename"
**Syntax:** `LOADM "CAS:filename"`

**Description:** Loads a machine-language module from cassette.

### MAXFILES
**Syntax:** `MAXFILES`

**Description:** Sets or queries the maximum open file count for cassette devices.

### MERGE "CAS:filename"
**Syntax:** `MERGE "CAS:filename"`

**Description:** Merges the ASCII-formatted cassette file into the current BASIC program.

### MOTOR ON/OFF
**Syntax:** `MOTOR ON` / `MOTOR OFF`

**Description:** Starts or stops the cassette motor.

### OPEN "CAS:filename" FOR mode AS file number
**Syntax:** `OPEN "CAS:filename" FOR OUTPUT/INPUT AS file number`

**Description:** Allocates a buffer for cassette input or output.

### PRINT #
**Syntax:** `PRINT #file number, expression list`

**Description:** Writes data to the open cassette buffer.

### PRINT # ... USING
**Syntax:** `PRINT #file number, USING "format"; expression list`

**Description:** Formats values before writing to cassette.

### RUN "CAS:filename", R
**Syntax:** `RUN "CAS:filename", R`

**Description:** Loads and executes a BASIC program from cassette; `R` keeps files open.

### RUNM "CAS:filename"
**Syntax:** `RUNM "CAS:filename"`

**Description:** Loads and executes a machine-language program from cassette.

### SAVE "CAS:filename", A
**Syntax:** `SAVE "CAS:filename", A`

**Description:** Saves the current BASIC program to cassette, optionally in ASCII.

### SAVEM
**Syntax:** `SAVEM "CAS:filename", start address, end address, entry address`

**Description:** Saves machine-language data to cassette, including the optional entry address.

### TAB (numeric expression)
**Syntax:** `TAB (numeric expression)`

**Description:** Inserts spaces before the next data item when printing to cassette (range 0–255).
