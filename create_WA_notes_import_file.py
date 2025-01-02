import os
from datetime import datetime

import document


def main():

    FOLDER = r"c:\temp"

    print(
        "This script will generate a month"
        "s worth of Work Activity notes \ninto a .enex file that can be imported into Evernote.\n"
    )

    # Ask the user which month and user they'd like to use.
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_month_string = datetime.now().strftime("%B")
    year = int(input(f"What year? (Format: ####.  ENTER for {current_year}) ") or current_year)
    month = int(input(f"What month? (Format: ##.  ENTER for {current_month_string}) ") or current_month)

    # Creating a document of WA notes for the chosen month and year.
    doc = document.Document(year, month)

    # Write the new document to a file
    # WA_notes.YYYYMM.enex
    filename = f"WA_notes.{year}{str(month).zfill(2)}.enex"
    fullpath = os.path.join(FOLDER, filename)
    f = open(fullpath, "w")
    f.write(doc.content())
    f.close()

    print(f'\nThe file was saved in the file "{fullpath}".')


main()
