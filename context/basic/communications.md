# Communications (COM + MDM)

## RS-232C Configuration
- Format: `rwpbs`
  - `r`: baud rate (1=75, 2=110, 3=300, 4=600, 5=1200, 6=2400, 7=4800, 8=9600, 9=19200, `M` = 300 baud modem)
  - `w`: word length (6–8 bits)
  - `p`: parity (`E`, `O`, `I`, `N`)
  - `b`: stop bits (1 or 2)
  - `s`: XON/XOFF status (`E` enable, `D` disable)

## TELCOM Commands

### COM ON / OFF / STOP
**Syntax:** `COM ON` / `COM OFF` / `COM STOP`

**Description:** Enables or disables the COM interrupt.

### CLOSE file number list
**Syntax:** `CLOSE file number list`

**Description:** Closes communications buffers.

### EOF (file number)
**Syntax:** `EOF (file number)`

**Description:** Returns `true` when the communication buffer is at end-of-file.

### INPUT#
**Syntax:** `INPUT #file number, variable list`

**Description:** Reads data from the communications file sequentially.

### INPUT$ (numeric expression, file number)
**Syntax:** `INPUT$ (numeric expression, file number)`

**Description:** Reads a fixed-length string from the communications buffer.

### LOAD "COM:configuration", R
**Syntax:** `LOAD "COM:<configuration>", R`

**Description:** Loads a BASIC program via communications. `R` runs the program after loading.

### MAXFILES
**Syntax:** `MAXFILES`

**Description:** Controls the number of simultaneous open communication buffers.

### MERGE "COM:configuration"
**Syntax:** `MERGE "COM:<configuration>"`

**Description:** Merges incoming lines from communications into the current program.

### ON COM GOSUB
**Syntax:** `ON COM GOSUB line number`

**Description:** Defines a routine triggered by incoming RS-232C data.

### OPEN "COM:configuration" FOR mode AS file number
**Syntax:** `OPEN "COM:<configuration>" FOR INPUT/OUTPUT AS file number`

**Description:** Allocates a buffer for communications. Mode selects transmission direction.

### PRINT # commands
**Syntax:** `PRINT #file number, expression list` / `PRINT #file number, USING "format"; expression list`

**Description:** Sends raw or formatted data out the communications buffer.

### RUN "COM:configuration", R
**Syntax:** `RUN "COM:<configuration>", R`

**Description:** Loads and runs a BASIC program from communications.

### SAVE "COM:configuration"
**Syntax:** `SAVE "COM:<configuration>"`

**Description:** Transmits the current BASIC program over the communication link in ASCII.

### TELCOM AUTO CONFIG EXAMPLES
- `88E1E`: 9600 baud, 8 bits, even parity, 1 stop bit, XON/XOFF enabled (RS-232C)
- `M7N2D`: 300 baud, 7 bits, no parity, 2 stop bits, XON/XOFF disabled (modem)

## Modem Configuration
- Format: `wpbs` (baud is fixed at 300)
  - `w`: word length (6–8)
  - `p`: parity (`E`, `O`, `I`, `N`)
  - `b`: stop bits (1 or 2)
  - `s`: XON/XOFF status (`E`/`D`)

## Modem Commands

### CLOSE file number list
**Syntax:** `CLOSE file number list`

**Description:** Closes modem buffers.

### EOF (file number)
**Syntax:** `EOF (file number)`

**Description:** Detects end-of-file condition for modem transfers.

### INPUT #
**Syntax:** `INPUT #file number, variable list`

**Description:** Reads data sequentially from the modem file.

### INPUT$ (numeric expression, file number)
**Syntax:** `INPUT$ (numeric expression, file number)`

**Description:** Reads a fixed-length string from the modem buffer.

### LINE INPUT #
**Syntax:** `LINE INPUT #file number, string variable`

**Description:** Reads a line of text from the modem buffer.

### LOAD "MDM:configuration", R
**Syntax:** `LOAD "MDM:<configuration>", R`

**Description:** Loads a BASIC program from the modem.

### MAXFILES
**Syntax:** `MAXFILES`

**Description:** Same as COM, but scoped to modem buffers.

### MDM ON / OFF / STOP
**Syntax:** `MDM ON` / `MDM OFF` / `MDM STOP`

**Description:** Controls the modem interrupt.

### MERGE "MDM:configuration"
**Syntax:** `MERGE "MDM:<configuration>"`

**Description:** Merges incoming modem program lines.

### ON MDM GOSUB
**Syntax:** `ON MDM GOSUB line number`

**Description:** Interrupt routine triggered by incoming modem data.

### OPEN "MDM:configuration" FOR mode AS file number
**Syntax:** `OPEN "MDM:<configuration>" FOR INPUT/OUTPUT AS file number`

**Description:** Allocates a buffer for modem transfers.

### PRINT # commands
**Syntax:** `PRINT #file number, expression list` / `PRINT #file number, USING "format"; expression list`

**Description:** Sends data to the modem buffer.

### RUN "MDM:configuration", R
**Syntax:** `RUN "MDM:<configuration>", R`

**Description:** Loads and executes a program transmitted via modem.

### SAVE "MDM:configuration"
**Syntax:** `SAVE "MDM:<configuration>"`

**Description:** Sends the current BASIC program out the modem.

### TAB (numeric expression)
**Syntax:** `TAB (numeric expression)`

**Description:** Inserts spacing before the next data item transmitted over the modem.
