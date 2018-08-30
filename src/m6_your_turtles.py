"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.
"""
###############################################################################
# TODO: 1.
#   On Line 5 above, replace  Thomas Nandola  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.

import rosegraphics as rg
window = rg.TurtleWindow()

size = 300

thomas = rg.SimpleTurtle('circle')
thomas.Pen = rg.Pen('midnightblue',15)
thomas.Speed = 15

for k in range(20):
    thomas.right(45)
    thomas.forward(50)
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
