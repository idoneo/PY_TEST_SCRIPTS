#phone and email scraper
!# python3

import re
import pyperclip

#TODO: Create a regex object for phone numbers the entire list of groups
#has to be enclosed in () otherwise findall will return a list of tuples for each match and each
#tuple will have several strings in it, by wrapping the whole regex in () group 0 will cover
#the entire matched text

phoneRegex = re.compile (r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?  #area code (optional)
(\s|-)                    #first separator
\d\d\d                    #first 3 digits  
-                         #separator
\d\d\d\d                  #last 4 digits
(((ext(\.)?|s)|x)         #extension word-part (optional)
(\d{2,5}))?               #extension number-part (optional)
) 
''',re.VERBOSE)


#create a regex for email
emailRegex = re.compile(r'''
                          #some.+_name@something.com
[a-zA-Z0-9_.+]            #name part (you dont have to escape characters, you are creating a class)
 @                         # @symbol
 [a-zA-Z0-9_.+]            #domain name


''',re.VERBOSE)
#get text off clipboard

text = pyperclip.paste()
#extract email phone from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers[]
for phoneNUmber in extractedPhone:
	allPhoneNumbers.append(phoneNumber[0])
print(allPhoneNumbers)
	
#copy this to clipboard
results = '\n'.join(allPhoneNumbers) + 'n\' + '\n'.join(extractedEmail)
pyperclip.copy(results)

#note
#os.unlink() will delete a file
#os.rmdir() will remove and EMPTY directory ( folder)
#shutil.rmtrr() will delete a folder and all its contents
# send2trash,send2trash() will send to recycle  PIP install send2trash
