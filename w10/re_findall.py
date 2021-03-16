import re
#https://scccd.instructure.com/courses/63347/assignments/1423373?module_item_id=2636128
#Findall funtion

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume= """
Never use your work phone number on your resume –– that's the quickest way to make your confidential job search not-so-confidential. Instead, include your personal cell phone number. That way, you have control over the voicemail message, who answers the phone, and when it is answered. When setting up your voicemail, be sure to include your name in the message so employers know they have called the right person.

When it comes to listing your phone number on your resume, there are a number of different formats that are considered acceptable:

    555-567-7309 | 855-868-5909 | 505-867-5309

You can also choose to put a label in front of your phone number such as “Tel:”, “Ph:”, “Phone:”, “C:”, or “M:” (for mobile).
"""
print('Printing the first phone')
mp = phoneRegex.search(resume)
print(mp.group())

print('\nPrinting all phone #s')
mp = phoneRegex.findall(resume)
print(mp)

#character classes
digitRegex = re.compile(r'\d')

lyrics = """
1 note, 2 notes, 3 notes, 4 notes, 5 notes, 10 notes, etc.
"""

print('\nfinding numbers')
xmasregex= re.compile(r'\d+')
print(xmasregex.findall(lyrics))

print('Finding more chars')
vowelRegex = re.compile(r'[aeiouAEIOU]')  #ginding all the vowels
print(vowelRegex.findall('Robocop eats baby food.'))
vowelRegex = re.compile(r'[aeiouAEIOU]{2}') #vowels in pair
print(vowelRegex.findall('Robocop eats baby food.'))
vowelRegex = re.compile(r'[^aeiouAEIOU]')  #finding what is not in
print(vowelRegex.findall('Robocop eats baby food.'))
