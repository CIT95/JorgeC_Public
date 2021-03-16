"""
Video 29 https://www.udemy.com/course/automate/learn/lecture/3470534#overview

"""
import re
import pyperclip

re.compile(r'''
#415-555-5563, 555-0000, (415) 5656-3656, 555-0000 ext 12345, ext.9635, x12345
((\d\d\d)|(\(\d\d\d\)))? #area code optional
(\s|-) #first separator
\d\d\d #first 3 digits
-      #separator
\d\d\d\d #last 4 digits
(((ext(\.)?\s)|x) #extension word-part (optional)
  (\d{2,5}))     #extension optional
''',re.VERBOSE)

mytext = """
Foglio, Dan 559-365-6558 dan@fresnocity.edu	CTC 	CTC 	5781 	DAILY 2-2:50
Lum, Rick 559-33-6698	rick33@fresnocity.edu CTC 	CTC H 	5779 	M T W TH F 8-9am
Putman, Dale 522-365-0698 putman.dale@fresnocity.edu	CTC 	CTC N/L 	5782 	M T W TH F 9-10am
See, Charles 549-365-6098 see.charles@fresnocity.edu	CTC 	CTC B 	5767 	M T W TH F 2-2:50pm
"""
phonereg=re.compile(r'((\d\d\d)|(\(\d\d\d\)))?(\s|-)\d\d\d-\d\d\d\d(((ext(\.)?\s)|x)(\d{2,5}))''',re.VERBOSE)
extractPhone = phonereg.findall(mytext)
print(extractPhone)

emailRegex=re.compile(r'''
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+
''',re.VERBOSE)
extractEmail= emailRegex.findall(mytext)
print(extractEmail)

allphonenumbers = []
for phonenumber in extractPhone:
    allphonenumbers.append(phonenumber[0])
results = '\n'.join(allphonenumbers)+'\n'+'\n'.join(extractEmail)
print(allphonenumbers)
pyperclip.copy(results)