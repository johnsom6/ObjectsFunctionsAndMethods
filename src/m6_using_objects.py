"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Madi Johnson
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------
    window = rg.RoseWindow()

    cp1 = rg.Point(50,50)
    cp2 = rg.Point(100,100)

    circle = rg.Circle(cp1,25)
    circle2 = rg.Circle(cp2,10)

    circle.attach_to(window)
    circle2.attach_to(window)

    circle.fill_color = 'Cyan'

    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------

window = rg.RoseWindow()

cp3 = rg.Point(50, 50)
cp4 = rg.Point(100, 100)
cp5 = rg.Point(250,200)

circle3 = rg.Circle(cp3, 25)
rectangle = rg.Rectangle(cp4,cp5)

circle3.attach_to(window)
rectangle.attach_to(window)

circle3.fill_color = 'blue'

window.render()
window.close_on_mouse_click()

print(circle3.outline_thickness)
print(circle3.fill_color)
print(circle3.center)
print(cp3.x)
print(cp3.y)

print(rectangle.outline_thickness)
print(rectangle.fill_color)

# here are the corners, not sure if the center is a thing

print(cp4)
print(cp5)


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------
    window = rg.RoseWindow()

    start1 = rg.Point(10,10)
    end1 = rg.Point(50,50)
    start2 = rg.Point(60,60)
    end2 = rg.Point(250,250)

    line1 = rg.Line(start1,end1)
    line2 = rg.Line(start2,end2)

    line2.thickness = 20

    line1.attach_to(window)
    line2.attach_to(window)


    window.render()
    window.close_on_mouse_click()

    mp2 = line2.get_midpoint()

    print(mp2)
    print(mp2.x)
    print(mp2.y)




# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
