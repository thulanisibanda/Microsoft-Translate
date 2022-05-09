<html>

<body lang=EN-GB link=blue vlink="#954F72" style='word-wrap:break-word'>

<div class=WordSection1>

<p class=MsoNormal><b><span style='font-size:16.0pt;line-height:107%'>Set up</span></b></p>

<p class=MsoListParagraphCxSpFirst>&nbsp;</p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-18.0pt'>1.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Download
and install python version 3.8.2 from <a
href="https://www.python.org/downloads/">https://www.python.org/downloads/</a> making
sure to check the “add python to PATH” box </p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-18.0pt'>2.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Verify
install by opening command line and checking the python version by running “python
--version” which should return “Python 3.8.2”</p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-18.0pt'>3.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Follow
instructions from <a
href="https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip">https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip</a>
on how to install pip. </p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-18.0pt'>4.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Verify
pip install by running command “pip --version” which should return something
like “pip 19.2.3 from c:\users\sibandat\appdata\local\programs\python\etc”</p>

<p class=MsoListParagraphCxSpMiddle style='text-indent:-18.0pt'>5.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Run
command “pip install pandas requests pybase64 openpyxl asyncio aiohttp xlrd”</p>

<p class=MsoListParagraphCxSpLast style='text-indent:-18.0pt'>6.<span
style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Update
UserAuthentication, portalTranslateUrl and microsoftTranslateUrl variables to
your own</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal><b><span style='font-size:16.0pt;line-height:107%'>Instructions</span></b></p>

<p class=MsoNormal>This script will translate all excel (.xlsx) files in the
same folder and store in a new folder called “processed” with the filename
“YYYY_MM_DD_HH_original filename”. In the newly generated file there will be a
new column called Result Translation Type. This column lets you know where the
translated text came from within Service Now or will show Microsoft Translate
Service.</p>

<p class=MsoNormal>The easiest way to run the script is navigate to the folder
in which it is stored. Hold shift and right click in that folder, making sure
you’re not right clicking on any file, and open your terminal here. If using
Powershell click on “Open PowerShell window from here”</p>

<p class=MsoNoSpacing>In Powershell run the command “python '.\microsoft
translate.py'” and the script should run.</p>

</div>

</body>

</html>
