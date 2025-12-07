# Telecommunications (TELCOM) Quick Reference

## Entering TELCOM
From the Menu, position the cursor on `TELCOM` and press ENTER to launch the Telecommunications Program.

## Special Commands and Keys in TELCOM
When TELCOM displays `TELCOM:`, you can use these commands:
- `(F1) Find string`: Search `ADRS.DO` for the target string. Within Find mode:
  - `(F2) CALL`: dial the currently found number.
  - `(F3) MORE`: find the next match.
  - `(F4) QUIT`: stop the search.
- `(F2) Call number`: Dial a number. If a number was just found with (F1), TELCOM auto-calls that entry.
- `(F3) Stat config`: Show or change the current communications configuration. Without arguments it displays the configuration.
- `(F4) Term`: Enter Terminal Mode, where you can:
  - `(F1)`: display the previous received page.
  - `(F2)`: save incoming data to a RAM file.
  - `(F3)`: transmit a file to the host.
  - `(F4)`: toggle between full and half duplex.
  - `(F5)`: echo incoming data to the printer.
  - `(F8)`: exit Terminal Mode and return to TELCOM.
- `FB Menu`: Exit TELCOM and return to the Menu.

## Communications Configuration
RS-232C configuration is a five-character string `rwpbs`:
- `r` (Baud Rate): 1=75, 2=110, 3=300, 4=600, 5=1200, 6=2400, 7=4800, 8=9600, 9=19200. `M` selects the built-in modem at 300 baud.
- `w` (Word Length): 6, 7, or 8 bits.
- `p` (Parity): `E` (Even), `O` (Odd), `N` (None), `I` (Ignore).
- `b` (Stop Bits): `1` or `2`.
- `s` (XON/XOFF Status): `E` (Enable) or `D` (Disable).

Modem configuration uses `wpbs` (same definitions), with baud fixed at 300 by TELCOM.

### Examples
- `88E1E`: 9600 baud, 8-bit words, Even parity, 1 stop bit, XON/XOFF enabled (RS-232C port).
- `M7N2D`: 300 baud, 7-bit words, No parity, 2 stop bits, XON/XOFF disabled (built-in modem).

## Auto Log-on Commands
Store host phone numbers and log-on sequences in `ADRS.DO`. Inside an auto-dial entry, characters enclosed in `<` and `>` are sent verbatim as the log-on sequence. Special sequences:
- `?c`: wait for character `c` from the host.
- `=`: pause 2.0 seconds.
- `!c`: treat `c` as a literal character instead of a command.
- `^c`: send the CTRL-`c` control character (where `c` is A–Z).

### Example
`<="C?U9857,756"M?PMICRO!?\'M>`
This waits 2 seconds, sends BREAK (`C`), waits for `U`, sends `9857,756` + carriage return (`M`), waits for `P`, sends `MICRO?`, and sends carriage return (the `!?` ensures the `?` is literal). Auto-dialed phone numbers start with `:` and end with a second `:` (e.g., `CIS:555-1234:`).
