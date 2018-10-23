#- * - coding : utf-8 - * -


from site import addsitedir
from sys import executable
from os import path
interpreter = executable
print executable
sitepkg = path.dirname(interpreter) + "\\site-packages"
print sitepkg

print addsitedir(sitepkg)
