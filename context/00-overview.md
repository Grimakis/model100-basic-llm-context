# TRS-80 Model 100 Quick Reference

## Introduction
In this Quick Reference Guide you will find most of what you need to run your Model 100: basic startup and power information, application program overviews, and handy tables covering keyboard-to-ASCII mappings and BASIC error messages.

## How to Use the Guide
The first part of the book covers general machine information such as power sources and menu navigation. After that come descriptions of each onboard application program, outlining the purpose, entry method, and command set for TEXT, SCHEDL, ADDRSS, TELCOM, and BASIC. The back section holds the tables and quick-reference alerts (ASCII codes, error codes, etc.) that are useful when writing programs or debugging behavior.

## Notation Used in This Guide
- **BOLDFACE CAPS**: type the command exactly as shown.
- *boldface italics*: insert a suitable argument.
- KEY: press the labeled key.
- CTRL KEY: hold CTRL and the labeled key.
- CODE KEY: hold CODE and the labeled key.
- GRPH KEY: hold GRPH and the labeled key.
- expression / string expression / numeric expression / list / range: insert a value described by the label.

## Function Key Definitions (F1–F8)
| Program | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BASIC | Files | Load | Save | Run | List | — | — | Menu |
| TEXT | Find | Load | Save | — | Copy | Cut | Sel | Menu |
| TELCOM | Find | Call | Stat | Term | Echo | Wait | — | Menu |
| ADDRSS | Find | — | — | — | Lfnd | — | — | Menu |
| SCHDL | Find | horizontal line | horizontal line | horizontal line | Lfnd | — | — | Menu |

## Using the Model 100
- **Power sources:** Four size-AA alkaline manganese batteries or 120VAC adapter (Catalog 26-3804).
- **Turning on:** Move the right-side Power Switch to `ON`; the Main Menu appears.
- **Setting date/time:** Enter BASIC and run commands such as `DAYS="Mon"`, `DATES="03/18/83"`, `TIMES="13:45.25"` (followed by ENTER).
- **Selecting menu options:** Use the arrow keys to highlight a file or application; pressing ENTER opens a text file in TEXT, runs a BASIC program, or launches the selected built-in application (BASIC interpreter, TEXT, etc.) depending on the target.
- **Turning off:** Set the Power Switch to `OFF`. RAM files are preserved when you power down from the Menu or while the cursor is blinking. Do not power-off while the machine is busy writing unless you accept potential data loss.
- **Auto power-off:** After 10 minutes of no keyboard input or running programs, the computer shuts down automatically. To restart, flip the switch to `OFF` briefly, then back to `ON`.
