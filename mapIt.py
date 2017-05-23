#10 REM
""" This is from the How To Automate the Boring Stuff book, Chapter 11 (IIRC)
It pulls an address from the command line and searches google maps for the address."""
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address form command line.
	address = ' '.join(sys.argv[1:])
	
else:
    #get address for clipboard.
	address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)


