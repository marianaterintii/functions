#HW Argumenti si valori returnate
from os import system
system ("cls")

def wrap_brackets( text ):
  return "(" + text + ")"

def wrap_brackets1( text ):
  return ( "[" + text + "]")


def wrap_brackets2( text ):
  return  "<" + text + ">"


print (wrap_brackets2 (wrap_brackets1 (wrap_brackets("12345"))))

print()

