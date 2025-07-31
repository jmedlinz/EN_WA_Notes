from calendar import monthrange

import note


class Document:

    def __init__(self, year, month):

        HEADER = '<?xml version="1.0" encoding="UTF-8"?>\n'
        HEADER += '<!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export4.dtd">\n'
        HEADER += '<en-export export-date="20250731T220000Z" application="Evernote" version="10.147.1">\n'

        FOOTER = "</en-export>\n"

        # Create a list of notes, one for each day of the month.
        notes = [note.Note(year, month, i + 1).content() for i in range(monthrange(year, month)[1])]

        # Assemble the header, notes, and footer into a document.
        self.__doc = HEADER + "".join(notes) + FOOTER

    def content(self):
        return self.__doc

    def __repr__(self):
        return self.__doc
