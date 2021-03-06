'''
    Created on Mar 8, 2020
    
    @author:    Tae Myles
'''
from unittest import TestCase
from othello.create import _create as create

class CreateTest(TestCase):
    #    Desired level of confidence: boundary value analysis
    #    Input-output analysis
    #        inputs:    light -> dictionary string key, value .GE. 0, .LE. 9, Optional (Integer 1), unvalidated
    #                   dark -> dictionary string key, value .GE. 0, .LE. 9, Optional (Integer 2), unvalidated
    #                   blank -> dictionary string key, value .GE. 0, .LE. 9, Optional (Integer 0), unvalidated
    #                   size -> dictionary string key, value .GE. 6, .LE. 16, Optional (Integer 8), unvalidated
    #        outputs:    board -> dictionary string key, list of integer value .GE.0 .LE.9,
    #                   tokens -> dictionary string key, value specified by light, dark, and blank
    #                   integrity -> dictionary string key, value is sha256 hash hex digest of the strin
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
    #        default:    light = 1, dark = 2, blank = 0, size = 8
    #        extraneous output:    'extra' = 1234
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
    #    light=blank:    same value as light and blank    light = 5 & blank = 5
    #    blank=dark:    same value as blank and dark    blank = 2 & dark = 2
    
    def setUp(self):
        self.parms = {'op': 'create', 'light': '1', 'dark': '2', 'blank': '0', 'size': '8'}
    
    def tearDown(self):
        self.parms = {'op': 'create', 'light': '1', 'dark': '2', 'blank': '0', 'size': '8'}  
        
    #1000 _create development
    def test1000_DefaultLightValue(self):
        self.setUp()
        expected = 1
        del self.parms['light']
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['tokens']['light'])
        self.tearDown()
        
    def test1001_DefaultDarkValue(self):
        self.setUp()
        expected = 2
        del self.parms['dark']
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['tokens']['dark'])
        self.tearDown()
        
    def test1002_DefaultBlankValue(self):
        self.setUp()
        expected = 0
        del self.parms['blank']
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['tokens']['blank'])
        self.tearDown()
        
    def test1003_DefaultSizeValue(self):
        self.setUp()
        defaultSize = 8
        del self.parms['size']
        self.actual = create(self.parms)
        expected = int(defaultSize ** 2)
        self.assertEqual(expected, len(self.actual['board']))
        self.tearDown()
        
    def test1004_SizeSixBoard(self):
        self.parms['size'] = 6
        expected = [0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0,
                    0, 0, 1, 2, 0, 0,
                    0, 0, 2, 1, 0, 0,
                    0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0]
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['board'])
        self.tearDown()
    
    def test1005_SizeEightBoard(self):
        self.setUp()
        self.parms['size'] = 8
        expected = [0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 1, 2, 0, 0, 0,
                    0, 0, 0, 2, 1, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0]
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['board'])
        self.tearDown()

    def test1005_SizeTenBoard(self):
        self.setUp()
        self.parms['size'] = 10
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 1, 2, 0, 0, 0, 0,
                    0, 0, 0, 0, 2, 1, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['board'])
        self.tearDown()
        
    def test1006_SizeTwelveBoard(self):
        self.setUp()
        self.parms['size'] = 12
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['board'])
        self.tearDown()
    
    def test1007_SizeFourteenBoard(self):
        self.setUp()
        self.parms['size'] = 14
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['board'])
        self.tearDown()

    def test1008_SizeSixteenBoard(self):
        self.setUp()
        self.parms['size'] = 16
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['board'])
        self.tearDown()
        
    def test1009_DefaultSha256HexDigest(self):
        self.setUp()
        expected = 'b11fcf5f9ac9d3b8cea8085208e210182a8d6b73a84028562ab2c87d190b9ada'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['integrity'])
        self.tearDown()
    
    #000 Happy path
    def test010_NominalLightDarkBlankSize(self):
        self.setUp()
        self.parms['light'] = 6
        self.parms['dark'] = 5
        self.parms['blank'] = 1
        self.parms['size'] = 10
        expected = {'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 6, 5, 1, 1, 1, 1,
                              1, 1, 1, 1, 5, 6, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    'tokens': {'light': 6, 'dark': 5, 'blank': 1},
                    'status': 'ok',
                    'integrity': 'd0f18c5b412ab1dbf89da19baa33cc35f4a7dd0619ce7b7dcb2381d2cb14a412'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
    
    def test020_HighBoundLightNominalDarkBlankSize(self):
        self.setUp()
        self.parms['light'] = 9
        self.parms['dark'] = 5
        self.parms['blank'] = 1
        self.parms['size'] = 10
        expected = {'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 9, 5, 1, 1, 1, 1,
                              1, 1, 1, 1, 5, 9, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    'tokens': {'light': 9, 'dark': 5, 'blank': 1},
                    'status': 'ok',
                    'integrity': '723c769319c6529cf8520336232a9e5d281be77df1455c6ceb10a5d1d4733236'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test021_LowBoundLightNominalDarkBlankSize(self):
        self.setUp()
        self.parms['light'] = 0
        self.parms['dark'] = 5
        self.parms['blank'] = 1
        self.parms['size'] = 10
        expected = {'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 0, 5, 1, 1, 1, 1,
                              1, 1, 1, 1, 5, 0, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    'tokens': {'light': 0, 'dark': 5, 'blank': 1},
                    'status': 'ok',
                    'integrity': '4bd2efa7e0d5f13551f7277950e45b6fcfe7d5159b80823a5dcbdf57abb4d83a'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test022_MissingLightNominalDarkBlankSize(self):
        self.setUp()
        self.parms['dark'] = 5
        self.parms['blank'] = 3
        self.parms['size'] = 10
        expected = {'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                              3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                              3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                              3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                              3, 3, 3, 3, 1, 5, 3, 3, 3, 3,
                              3, 3, 3, 3, 5, 1, 3, 3, 3, 3,
                              3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                              3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                              3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                              3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                    'tokens': {'light': 1, 'dark': 5, 'blank': 3},
                    'status': 'ok',
                    'integrity': 'f211a92f576794a821bb24f359739b8b42a6a16634005a1e4b32313a6575e2be'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test030_HighBoundDarkNominalLightDarkBlankSize(self):
        self.setUp()
        self.parms['light'] = 3
        self.parms['dark'] = 9
        self.parms['blank'] = 4
        self.parms['size'] = 10
        expected = {'board': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 3, 9, 4, 4, 4, 4,
                              4, 4, 4, 4, 9, 3, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    'tokens': {'light': 3, 'dark': 9, 'blank': 4},
                    'status': 'ok',
                    'integrity': 'a3718ffbc2f822320ee4db10c269a9749859b9952db13ff6b289a6ebd6ce42c6'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test031_LowBoundDarkNominalLightDarkBlankSize(self):
        self.setUp()
        self.parms['light'] = 3
        self.parms['dark'] = 0
        self.parms['blank'] = 4
        self.parms['size'] = 10
        expected = {'board': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 3, 0, 4, 4, 4, 4,
                              4, 4, 4, 4, 0, 3, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    'tokens': {'light': 3, 'dark': 0, 'blank': 4},
                    'status': 'ok',
                    'integrity': '7bf98e8385a158097f52361dac139bb5882f3eaa48e8146d72d65de5981d2e5e'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test032_MissingDarkNominalLightDarkBlankSize(self):
        self.setUp()
        self.parms['light'] = 3
        self.parms['blank'] = 4
        self.parms['size'] = 10
        expected = {'board': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 3, 2, 4, 4, 4, 4,
                              4, 4, 4, 4, 2, 3, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                              4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    'tokens': {'light': 3, 'dark': 2, 'blank': 4},
                    'status': 'ok',
                    'integrity': '71f91a7d487c9e9ad69a43269c6a90c449f97fd93848b8493e47a2f6054e7c82'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test040_HighBoundBlankNominalLightDarkSize(self):
        self.setUp()
        self.parms['light'] = 3
        self.parms['dark'] = 4
        self.parms['blank'] = 9
        self.parms['size'] = 10
        expected = {'board': [9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                              9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                              9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                              9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                              9, 9, 9, 9, 3, 4, 9, 9, 9, 9,
                              9, 9, 9, 9, 4, 3, 9, 9, 9, 9,
                              9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                              9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                              9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                              9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                    'tokens': {'light': 3, 'dark': 4, 'blank': 9},
                    'status': 'ok',
                    'integrity': '5b4c82af0cf6a72ab1938b8e5a3c1ce413b9db583d0f974703954427413021d0'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test041_LowBoundBlankNominalLightDarkSize(self):
        self.setUp()
        self.parms['light'] = 3
        self.parms['dark'] = 4
        self.parms['blank'] = 0
        self.parms['size'] = 10
        expected = {'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 3, 4, 0, 0, 0, 0,
                              0, 0, 0, 0, 4, 3, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    'tokens': {'light': 3, 'dark': 4, 'blank': 0},
                    'status': 'ok',
                    'integrity': 'eeaa1d4229234a1453901319e7f584a337595d6d332a22a76c4aae8888cde9d6'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test042_missingBlankNominalLightDarkSize(self):
        self.setUp()
        self.parms['light'] = 3
        self.parms['dark'] = 4
        self.parms['size'] = 10
        expected = {'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 3, 4, 0, 0, 0, 0,
                              0, 0, 0, 0, 4, 3, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    'tokens': {'light': 3, 'dark': 4, 'blank': 0},
                    'status': 'ok',
                    'integrity': 'eeaa1d4229234a1453901319e7f584a337595d6d332a22a76c4aae8888cde9d6'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test050_HighBoundSizeNominalLightDarkBlank(self):
        self.setUp()
        self.parms['light'] = 3
        self.parms['dark'] = 4
        self.parms['blank'] = 5
        self.parms['size'] = 16
        expected = {'board': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 3, 4, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 4, 3, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                    'tokens': {'light': 3, 'dark': 4, 'blank': 5},
                    'status': 'ok',
                    'integrity': '682b1bac788017f23b846862ce44f2c3efe03a22f49de36085e0e57fc6957416'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
     
    def test051_LowBoundSizeNominalLightDarkBlank(self):
        self.setUp()
        self.parms['light'] = 3
        self.parms['dark'] = 4
        self.parms['blank'] = 5
        self.parms['size'] = 6
        expected = {'board': [5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5,
                              5, 5, 3, 4, 5, 5,
                              5, 5, 4, 3, 5, 5,
                              5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5],
                    'tokens': {'light': 3, 'dark': 4, 'blank': 5},
                    'status': 'ok',
                    'integrity': 'b87b212e557d1dc1080f1c6e380bab404ae8cffa048b86e649e54c620f0d9c6a'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test052_MissingSizeNominalLightDarkBlank(self):
        self.setUp()
        self.parms['light'] = 3
        self.parms['dark'] = 4
        self.parms['blank'] = 5
        expected = {'board': [5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 3, 4, 5, 5, 5,
                              5, 5, 5, 4, 3, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5,
                              5, 5, 5, 5, 5, 5, 5, 5],
                    'tokens': {'light': 3, 'dark': 4, 'blank': 5},
                    'status': 'ok',
                    'integrity': '306a2474c8f8b41c9e31af0fe360f9fcaf3531b3b4a1c3624acd8fbc2530b02e'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
         
    def test060_AllDefaultParameter(self):
        self.setUp()
        expected = {'board': [0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 1, 2, 0, 0, 0,
                              0, 0, 0, 2, 1, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0],
                    'tokens': {'light': 1, 'dark': 2, 'blank': 0},
                    'status': 'ok',
                    'integrity': 'b11fcf5f9ac9d3b8cea8085208e210182a8d6b73a84028562ab2c87d190b9ada'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    def test070_ExtraneousParameterIgnored(self):
        self.setUp()
        self.parms['extra'] = 1234
        expected = {'board': [0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 1, 2, 0, 0, 0,
                              0, 0, 0, 2, 1, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0],
                    'tokens': {'light': 1, 'dark': 2, 'blank': 0},
                    'status': 'ok',
                    'integrity': 'b11fcf5f9ac9d3b8cea8085208e210182a8d6b73a84028562ab2c87d190b9ada'}
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual)
        self.tearDown()
        
    #900 Sad Path
    def test900_AboveBoundLight(self):
        self.setUp()
        self.parms['light'] = '10'
        expected = 'error: above bound light value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test901_BelowBoundLight(self):
        self.setUp()
        self.parms['light'] = '-1'
        expected = 'error: below bound light value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test902_NonIntegerLight(self):
        self.setUp()
        self.parms['light'] = 'w'
        expected = 'error: non-integer light value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test903_NullLight(self):
        self.setUp()
        self.parms['light'] = None
        expected = 'error: Null light value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test910_AboveBoundDark(self):
        self.setUp()
        self.parms['dark'] = '10'
        expected = 'error: above bound dark value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test911_BelowBoundDark(self):
        self.setUp()
        self.parms['dark'] = '-1'
        expected = 'error: below bound dark value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test912_NonIntegerDark(self):
        self.setUp()
        self.parms['dark'] = 'd'
        expected = 'error: non-integer dark value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test913_NullDark(self):
        self.setUp()
        self.parms['dark'] = None
        expected = 'error: Null dark value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test920_AboveBoundBlank(self):
        self.setUp()
        self.parms['blank'] = '10'
        expected = 'error: above bound blank value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test921_BelowBoundBlank(self):
        self.setUp()
        self.parms['blank'] = '-1'
        expected = 'error: below bound blank value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test922_NonIntegerBlank(self):
        self.setUp()
        self.parms['blank'] = 'b'
        expected = 'error: non-integer blank value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test923_NullBlank(self):
        self.setUp()
        self.parms['blank'] = None
        expected = 'error: Null blank value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test930_AboveBoundSize(self):
        self.setUp()
        self.parms['size'] = '17'
        expected = 'error: above bound size value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test931_BelowBoundSize(self):
        self.setUp()
        self.parms['size'] = '5'
        expected = 'error: below bound size value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test932_NonIntegerSize(self):
        self.setUp()
        self.parms['size'] = '1.2'
        expected = 'error: non-integer size value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test933_NullSize(self):
        self.setUp()
        self.parms['size'] = None
        expected = 'error: Null size value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
        
    def test934_OddSize(self):
        self.setUp()
        self.parms['size'] = 9
        expected = 'error: Odd size value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
    
        
    def test940_LightEqualsDark(self):
        self.setUp()
        self.parms['light'] = 5
        self.parms['dark'] = 5
        expected = 'error: light is equal to dark value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()

    def test941_BlankEqualsLight(self):
        self.setUp()
        self.parms['light'] = 5
        self.parms['blank'] = 5
        expected = 'error: blank is equal to light value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()
    
    def test942_DarkEqualsBlank(self):
        self.setUp()
        self.parms['dark'] = 2
        self.parms['blank'] = 2
        expected = 'error: dark is equal to blank value'
        self.actual = create(self.parms)
        self.assertEqual(expected, self.actual['status'])
        self.tearDown()