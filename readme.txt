NOTE: This is a Python program. Follow this link to install python:
https://docs.python.org/3/using/windows.html

You do not need to install any additional modules to use this program. All modules are built-in to Python.

INSTRUCTIONS
1. Run "getnames.py". You can do this on the command line with "py getnames.py". You may find additional information on how to run python programs here: https://docs.python.org/3/faq/windows.html

2. Input the number of names you want into request.txt

3. Wait for the program to generate names (this shouldn't take long!)

4. Read the list of names from response.txt

ADDITIONAL NOTES

This program automatically clears request.txt after reading. It also automatically clears response.txt before writing its new list of names. This is meant to minimize the amount of work your program has to do - However, it also means you should store your list of names somewhere before making a new request.

Every time you request a list of names, it will generate names that sound similar to each other, so it sounds like they're a part of the same culture. This means that, if you want to generate names for multiple cultures, you should make multiple requests!

ERROR HANDLING:

If you input a request with a number that's too large (<5000), your name file will be populated with ERROR text.

If you input a request with something that's not a number, your name file will be populated with 20 ERROR messages.