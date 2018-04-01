"""
Varias formas de hacerlo toma una cerveza y tirala a la pare, va disminuyendo
"""
def sing(b,end):
    print(b or 'No more', 'bottle' + ('s' if b-1 else ''), end)

verse = """\
{some} bottles of beer  on the walt
{some} bottles of beer
Take one down, pass it around
{less} bottles of beer on the wall

"""

for bottles in range(99,0,-1):
    print (verse.format(some=bottles, less=bottles-1 ))