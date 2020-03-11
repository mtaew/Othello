from unittest import TestCase
from othello.create import _create as create

class CreateTest(TestCase):
    #    Desired level of confidence: boundary value analysis
    #    Input-output analysis
    #        inputs:    light -> integer .GE. 0, .LE. 9, Optional (Integer 1), unvalidated
    #                   dark -> integer .GE. 0, .LE. 9, Optional (Integer 2), unvalidated
    #                   blank -> integer .GE. 0, .LE. 9, Optional (Integer 0), unvalidated
    #                   size -> integer .GE. 6, .LE. 16, Optional (Integer 8), unvalidated
    #        ouputs:    board -> dictionary .GE.0 .LE.9,
    #                   tokens -> dictionary value specified by light, dark, and blank
    #                   integrity -> dictionary value is sha256 hash hexdigest of the strin
    #                   status -> dictionary string associating that the board is created
    #    Happy path analysis
    #        light:    low value    light = 0
    #                  high value    light = 9
    #                  missing light    light = 1
    #        dark:     low value    dark = 0
    #                  high value    dark = 9
    #                  missing dark    dark= 2
    #        blank:    low value    blank = 0
    #                  high value    blank = 9
    #                  missing blank    blank = 0
    #        size:    low value    size = 6
    #                  high value    size = 16
    #                  missing size    size = 8
    #    
    #    Sad path analysis
    #        light:    above boundary    light = 10
    #                  below boundary    light = -1
    #                  non integer        light = w
    #                  null                light =
    #        dark:    above boundary    dark = 10
    #                  below boundary    dark = -1
    #                  non integer        dark = d
    #                  null                dark =
    #        blank:    above boundary    blank = 10
    #                  below boundary    blank = -1
    #                  non integer        blank = b
    #                  null                blank =
    #        size:    above boundary    size = 17
    #                  below boundary    size = 5
    #                  odd number         size = 9
    #                  non integer        size = 1.2
    #                  null                size = 
    #    light=dark:    same value as light and dark    light = 5 & dark = 5
    #    light=blank:    same value as ligth and blank    light = 5 & blank = 5
    #    blank=dark:    same value as blank and dark    blank = 2 & dark = 2
    
    #900 Sad Path
    def test900_AboveBoundLight(self):
        light = 10
        errorDict = {'status':'error: Above bound light integer'}
        actual = create(light)
        expected = errorDict
        self.assertEqual(actual, expected)
        