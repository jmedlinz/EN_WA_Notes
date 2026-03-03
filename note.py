import calendar
from datetime import date


class Note:

    def __init__(self, year, month, day):
        self.__date = date(year, month, day)

        # Some of the days have similar but slightly different content.
        # Choose the correct version of the content for this note.
        if calendar.weekday(year, month, day) in (calendar.SATURDAY, calendar.SUNDAY):
            content = """<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd"><en-note><div style="display:none;--en-chs:&quot;eyJpc0VtcHR5IjpmYWxzZSwiaDEiOnsiZm9udEZhbWlseSI6ImluaGVyaXQiLCJmb250U2l6ZSI6IjI1cHgiLCJjb2xvciI6ImluaGVyaXQiLCJmb250V2VpZ2h0IjoiNjAwIiwiZm9udFN0eWxlIjoiaW5oZXJpdCIsInRleHREZWNvcmF0aW9uIjoiaW5oZXJpdCJ9LCJoMiI6eyJmb250RmFtaWx5IjoiaW5oZXJpdCIsImZvbnRTaXplIjoiMjBweCIsImNvbG9yIjoiaW5oZXJpdCIsImZvbnRXZWlnaHQiOiI2MDAiLCJmb250U3R5bGUiOiJpbmhlcml0IiwidGV4dERlY29yYXRpb24iOiJpbmhlcml0In0sImgzIjp7ImZvbnRGYW1pbHkiOiJpbmhlcml0IiwiZm9udFNpemUiOiIxOHB4IiwiY29sb3IiOiJpbmhlcml0IiwiZm9udFdlaWdodCI6IjYwMCIsImZvbnRTdHlsZSI6ImluaGVyaXQiLCJ0ZXh0RGVjb3JhdGlvbiI6ImluaGVyaXQifSwicCI6eyJmb250RmFtaWx5IjoiaW5oZXJpdCIsImZvbnRTaXplIjoiaW5oZXJpdCIsImNvbG9yIjoiaW5oZXJpdCIsImZvbnRXZWlnaHQiOiJpbmhlcml0IiwiZm9udFN0eWxlIjoiaW5oZXJpdCIsInRleHREZWNvcmF0aW9uIjoiaW5oZXJpdCJ9fQ==&quot;"> </div><div><br/></div><hr/><div><span style="font-size: 16px;">📝 Notes:</span></div><ul><li><div>Weekend</div></li></ul><hr/><div><span style="font-size: 12pt;">⏳ Hours Worked:</span></div><div><span style="font-family: Consolas;"><span style="font-size: 11pt;">Enter_time</span></span></div><hr/><div><br/></div></en-note>      ]]>"""
        else:  # Monday-Friday
            content = """<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd"><en-note><div style="display:none;--en-chs:&quot;eyJpc0VtcHR5IjpmYWxzZSwiaDEiOnsiZm9udEZhbWlseSI6ImluaGVyaXQiLCJmb250U2l6ZSI6IjI1cHgiLCJjb2xvciI6ImluaGVyaXQiLCJmb250V2VpZ2h0IjoiNjAwIiwiZm9udFN0eWxlIjoiaW5oZXJpdCIsInRleHREZWNvcmF0aW9uIjoiaW5oZXJpdCJ9LCJoMiI6eyJmb250RmFtaWx5IjoiaW5oZXJpdCIsImZvbnRTaXplIjoiMjBweCIsImNvbG9yIjoiaW5oZXJpdCIsImZvbnRXZWlnaHQiOiI2MDAiLCJmb250U3R5bGUiOiJpbmhlcml0IiwidGV4dERlY29yYXRpb24iOiJpbmhlcml0In0sImgzIjp7ImZvbnRGYW1pbHkiOiJpbmhlcml0IiwiZm9udFNpemUiOiIxOHB4IiwiY29sb3IiOiJpbmhlcml0IiwiZm9udFdlaWdodCI6IjYwMCIsImZvbnRTdHlsZSI6ImluaGVyaXQiLCJ0ZXh0RGVjb3JhdGlvbiI6ImluaGVyaXQifSwicCI6eyJmb250RmFtaWx5IjoiaW5oZXJpdCIsImZvbnRTaXplIjoiaW5oZXJpdCIsImNvbG9yIjoiaW5oZXJpdCIsImZvbnRXZWlnaHQiOiJpbmhlcml0IiwiZm9udFN0eWxlIjoiaW5oZXJpdCIsInRleHREZWNvcmF0aW9uIjoiaW5oZXJpdCJ9fQ==&quot;"> </div><div><br/></div><hr/><div><span style="font-size: 16px;">📝 Notes:</span></div><ul><li><div><br/></div></li></ul><hr/><div><span style="font-size: 16px;">🤝 Meetings Today:</span></div><ul><li><div><br/></div></li></ul><hr/><div><span style="font-size: 12pt;">⏳ Hours Worked:</span></div><div><span style="font-family: Consolas;"><span style="font-size: 11pt;">Enter_time</span></span></div><hr/><div><br/></div></en-note>      ]]>"""

        # Assemble the note.
        # The data and the content are unique for each note.
        self.__content = "  <note>\n"
        self.__content += "    <title>" + self.__date.strftime("%B %#d, %Y - %A") + "</title>\n"
        self.__content += "    <created>" + self.__date.strftime("%Y%m%d") + "T060100Z</created>\n"
        self.__content += "    <updated>" + self.__date.strftime("%Y%m%d") + "T060100Z</updated>\n"
        self.__content += "    <tag>Today</tag>\n"
        self.__content += "    <note-attributes>\n"
        self.__content += "      <author>James Medlin</author>\n"
        self.__content += "    </note-attributes>\n"
        self.__content += "    <content>\n"
        self.__content += '      <![CDATA[<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
        self.__content += content + "\n"
        self.__content += "    </content>\n"
        self.__content += "  </note>\n"

    def content(self):
        return self.__content

    def __repr__(self):
        return f"Work Activity note for {str(self.__date)}."
