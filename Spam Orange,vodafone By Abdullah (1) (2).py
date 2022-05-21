
from bs4 import BeautifulSoup as BS 
import sys
from time import sleep 
print ()
print ('\033[1;92mclick on this link to get password👇')
#sleep (0.1)
print ()
link1="\033[1;93m https://miklpro.com/Nm7QS"
print (link1)
#sleep (1)
print ()
password=input ('\033[1;92m》Enter Password Script :  \033[1;96m')


rrr=requests.get('https://pastelink.net/5rnzlcn8').text
soup=BS(rrr,'html.parser')
lxc=(soup.find('div',{'class':'body-display'})).text

if password in lxc:
    print ()
    print ('\033[1;96m》True Password《')
    
else:
    print ()
    print ('\033[1;91mError Password')
    exit()
