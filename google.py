import os 
import urllib 
google = os.popen('zenity --entry --text="Enter what you want to google: " --title="google.py"').read() 
google = urllib.quote(google) 
os.system('www.google.com/search?q= %s' % (google))  