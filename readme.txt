NOTE: This is a Python program. Follow this link to install python on Windows:
https://docs.python.org/3/using/windows.html

You do not need to install any additional modules to use this program. All modules are built-in to Python.


INSTRUCTIONS
1. Run "getnames.py". You can do this on the command line with "py getnames.py". You may find additional information on how to run python programs on Windows here: https://docs.python.org/3/faq/windows.html

2. Input the number of names you want into request.txt

3. Wait for the program to generate names (this shouldn't take long!)

4. Read the list of names from response.txt


ADDITIONAL NOTES:
Every time you request a list of names, it will generate names that sound similar to each other, so it sounds like they're a part of the same culture. This means that, if you want to generate names for multiple cultures, you should make multiple requests!

This service will clear request.txt after reading it - You only have to make sure it's clear before the program is started.

This service will automatically overwrite response.txt of any previous names that are stored, so your program does not have to worry about this. You should store the previous list of names before making a new request.


PSEUDOCODE FOR MAKING A SINGLE REQUEST
list_of_names = []

open request.txt
write num_names to request.txt
close request.txt

wait for response

open response.txt
for i in range(num_names)
    new_name = contents of response.txt at line i
    append new_name to list of names
close response.txt

# use the list of names as you see fit!


TROUBLESHOOTING
Problem: Program crashes with "Type object is not superscriptable"
Solution: This usually happens when something's wrong with whatever's input into request.txt. You may be able to fix this by completely clearing the contents of requests.txt

Problem: response.txt is populated with "ERROR: Too many words requested. Please choose a smaller number."
Solution: This program tries to generate entirely unique names, so this happens when the program runs out of possible words to generate. You are generally a able to generate up over 10,000 names, but if you get this message, input a smaller number.

Problem: response.txt is populated with "ERROR: Non-Number Requested"
Solution: Make sure you're inputting an integer into request.txt