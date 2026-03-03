# EN_WA_Notes

A Python utility that generates monthly Work Activity notes for Evernote. This tool creates a complete set of daily notes for a specified month, formatted as an Evernote export file (.enex) ready for import.

## Description

This script automatically generates a month's worth of daily work activity notes with customized templates for weekdays and weekends. Each note includes sections for daily notes, meetings, and hours worked, helping you maintain consistent work activity tracking in Evernote.

## Features

- **Automated Monthly Note Generation**: Creates a note for every day in a specified month
- **Day-Based Templates**: Different note templates for weekdays (with meetings section) and weekends
- **Ready for Import**: Generates .enex files that can be directly imported into Evernote
- **Customizable Date Range**: Choose any year and month for note generation
- **Pre-formatted Sections**: Each note includes:
  - 📝 Notes section
  - 🤝 Meetings Today (weekdays only)
  - ⏳ Hours Worked tracker

## Prerequisites

- Python 3.11 or higher
- Poetry (for dependency management)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/jmedlinz/EN_WA_Notes.git
   cd EN_WA_Notes
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

## Usage

Run the script with Poetry:

```bash
poetry run python create_WA_notes_import_file.py
```

The script will prompt you for:
- **Year**: Enter a 4-digit year (press ENTER to use current year)
- **Month**: Enter a 2-digit month (press ENTER to use current month)

Example interaction:
```
This script will generate a months worth of Work Activity notes
into a .enex file that can be imported into Evernote.

What year? (Format: ####.  ENTER for 2026) 2026
What month? (Format: ##.  ENTER for March) 3
```

## Output

The script generates a file named `WA_notes.YYYYMM.enex` in `c:\temp\`. For example:
- March 2026 → `WA_notes.202603.enex`

Import this file into Evernote through:
1. File → Import → Evernote Export files
2. Select your generated .enex file
3. All notes will be imported with the "Today" tag

## Project Structure

- `create_WA_notes_import_file.py` - Main script entry point
- `document.py` - Document class that assembles the complete .enex file
- `note.py` - Note class that generates individual daily notes
- `pyproject.toml` - Poetry configuration and dependencies

## Development

Run pre-commit checks:
```bash
poetry run pre-commit run --all-files
```

Run tests:
```bash
poetry run pytest
```

## License

See [LICENSE](LICENSE) file for details.
