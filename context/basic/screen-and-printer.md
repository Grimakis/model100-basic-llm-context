# The Screen (LCD)

The LCD consists of 15,360 dots (240 x 64) that you can set on/off via BASIC (`PSET`/`PRESET`). These dots map to 320 printable-character positions (40 x 8).

## Screen Commands

### CLS
**Syntax:** `CLS`

**Description:** Clears the LCD, turning off every pixel and moving the cursor to the upper-left corner.

### CLOSE file number list
**Syntax:** `CLOSE file number list`

**Description:** Closes the named buffer(s) opened via `OPEN`.

**Examples:** `CLOSE 1,2,3` or `CLOSE`

### CSRLIN
**Syntax:** `CSRLIN`

**Description:** Returns the vertical cursor position (0 at top, 7 at bottom). Example: `A% = CSRLIN`.

### LCOPY
**Syntax:** `LCOPY`

**Description:** Sends the LCD screen text to the printer, ignoring non-text data.

### LINE / B / BF
**Syntax:** `LINE (x1,y1)-(x2,y2), color switch`, optionally followed by `B` or `BF`

**Description:** Draws a line (`LINE`), a box (`B`), or a filled box (`BF`). The `color switch` sets or unsets pixels depending on whether it is odd (set) or even (reset).

**Examples:** `LINE (0,0)-(239,63),1`, `LINE (0,0)-(239,63),1,BF`

### LIST line number range
**Syntax:** `LIST line number range`

**Description:** Lists the specified lines of the current BASIC program on the screen.

### MAXFILES
**Syntax:** `MAXFILES`

**Description:** Returns or sets the current maximum number of files. Example: `10 MAXFILES = 5` followed by `PRINT MAXFILES`.

### OPEN "LCD:" FOR OUTPUT AS file number
**Syntax:** `OPEN "LCD:" FOR OUTPUT AS <file number>`

**Description:** Allocates a buffer for a screen file and ties it to the given file number.

### POS
**Syntax:** `POS(dummy numeric expression)`

**Description:** Returns the current cursor position (`R% = POS(0)`).

### PRESET
**Syntax:** `PRESET (x-coordinate, y-coordinate)`

**Description:** Turns off the pixel at the given coordinates (x: 0-239, y: 0-63).

### PRINT expression list
**Syntax:** `PRINT` followed by an expression list

**Description:** Prints text/data at the current cursor position. Example: `PRINT "Menu #"; PRINT I%, J%, K%`.

### PRINT @screen position
**Syntax:** `PRINT @<position>, expression list`

**Description:** Sends output to an absolute screen position, such as `PRINT @140, TIMES$`.

### PRINT USING
**Syntax:** `PRINT USING "format"; expression list`

**Description:** Formats the expression list using the template. Format specifiers include:
- `"I"`: first string character
- `"#"`: digit placeholder
- `"+"`/`"-"`: insert sign
- `$`, `"**S###"`, decimal point, exponential markers, etc.

### PRINT # file number, expression list
**Syntax:** `PRINT #<file number>, expression list`

**Description:** Writes formatted output to the LCD file opened via `OPEN`.

### PRINT #file number, USING
**Syntax:** `PRINT #<file number>, USING "format"; expression list`

**Description:** Formats and writes data to the opened LCD file, using the same format specifiers as `PRINT USING`.

### PSET
**Syntax:** `PSET (x-coordinate, y-coordinate)`

**Description:** Sets (turns on) the LCD pixel at the given coordinates.

### SAVE "LCD:"
**Syntax:** `SAVE "LCD:"`

**Description:** Lists the current BASIC program to the screen. Pressing `PAUSE` has no effect during this command.

### SCREEN on/off
**Syntax:** `SCREEN 0,1` to show the Label line, `SCREEN 0,0` to hide it

**Description:** Toggles the LABEL line (bottom of the display) on or off.

### TAB
**Syntax:** `TAB (numeric expression)`

**Description:** Skips the specified number of spaces before printing the next field (`numeric expression` ranges 0-255). Example: `PRINT TAB(30); "Table 1"`.

# Printer (LPT)

## Printer Commands and Functions

### CLOSE file number list
**Syntax:** `CLOSE file number list`

**Description:** Closes one or more printer buffers.

### LCOPY
**Syntax:** `LCOPY`

**Description:** Prints the LCD screen contents on the printer.

### LLIST line number range
**Syntax:** `LLIST line number range`

**Description:** Lists the specified program lines on the printer.

### LPOS
**Syntax:** `LPOS (dummy numeric expression)`

**Description:** Returns the print head position within the printer buffer.

### LPRINT expression list
**Syntax:** `LPRINT` followed by an expression list

**Description:** Sends the values to the printer.

### LPRINT USING
**Syntax:** `LPRINT USING "format string"; expression list`

**Description:** Formats the data before printing. Format specifiers mirror those used by `PRINT USING` (`!`, `#`, `+`, `$`, `.`, `,`, etc.).

### MAXFILES
**Syntax:** `MAXFILES`

**Description:** Controls how many files can be open simultaneously at the printer device level.

### OPEN "LPT:" FOR OUTPUT AS file number
**Syntax:** `OPEN "LPT:" FOR OUTPUT AS <file number>`

**Description:** Allocates a buffer file number for printing.

### PRINT # commands
**Syntax:** `PRINT #<file number>, expression list` or `PRINT #<file number>, USING "format"; expression list`

**Description:** Sends either raw or formatted data to the opened printer file (mirrors `PRINT` behavior but targets the printer buffer).

### SAVE "LPT:"
**Syntax:** `SAVE "LPT:"`

**Description:** Sends the current BASIC program to the printer.

### TAB (numeric expression)
**Syntax:** `TAB (numeric expression)`

**Description:** Inserts spaces before the next data item, with the numeric expression limited to 0-255.
