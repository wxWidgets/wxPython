import unittest
import wx

"""
This file contains classes and methods for unit testing the API of wx.Color
(as well as wx.Colour, because they're the same thing)

IDEA: implement all the tests for just wx.Color, then abstract the tests
        to run against a particular symbol that can be substituted into.
        then sub both wx.Color and wx.Colour into it.
        (yes i know that they refer to the same thing.  but let's be thorough.)
        
Methods yet to test:
Alpha, GetPixel, GetRGB, SetFromName, SetRGB
"""

RED = wx.Colour(255,0,0)
GREEN = wx.Colour(0,255,0)
BLUE = wx.Colour(0,0,255)

def getColourData():
    return (
            (wx.Color(255,0,0), RED), (wx.Color(0,255,0), GREEN), (wx.Color(0,0,255), BLUE),
            ('RED', RED), ('GREEN', GREEN), ('BLUE', BLUE),
            ('#FF0000', RED), ('#00FF00', GREEN), ('#0000FF', BLUE),
            ((255,0,0), RED), ((0,255,0), GREEN), ((0,0,255), BLUE)
        )

# -----------------------------------------------------------

class ColorTest(unittest.TestCase):
    #####################
    ## Fixture Methods ##
    #####################
    def setUp(self):
        self.app = wx.PySimpleApp()
        
    ##################
    ## Test Methods ##
    ##################
    
    def testConstructor(self):
        """__init__"""
        self.assertRaises(OverflowError, wx.Colour, -1)
        self.assertRaises(OverflowError, wx.Colour, 256)
        
    def testSingleAccessors(self):
        """Red, Green, Blue, Alpha"""
        for i in range(256):
            colour = wx.Colour(i,i,i,i)
            self.assertEquals(i, colour.Red())
            self.assertEquals(i, colour.Green())
            self.assertEquals(i, colour.Blue())
            self.assertEquals(i, colour.Alpha())
    
    def testMultipleAccessors(self):
        """Get, Set"""
        for i in range(256):
            color = wx.Color()
            color.Set(i,i,i,i)
            self.assertEquals((i,i,i), color.Get())
            self.assertEquals(i, color.Alpha())
    
    def testStringRepresentation(self):
        """GetAsString"""
        for i in range(256):
            tup = (i,i,i,i)
            col_tup = (i,i,i)
            color = wx.Colour(i,i,i,i)
            self.assertEquals(str(tup), str(color))
            self.assertEquals('rgb'+str(col_tup), 
                                color.GetAsString(wx.C2S_CSS_SYNTAX))
            # TODO: implement tests for below flags
            # wx.C2S_NAME 	return colour name, when possible
            # wx.C2S_CSS_SYNTAX 	return colour in rgb(r,g,b) syntax
            # wx.C2S_HTML_SYNTAX 	return colour in #rrggbb syntax
    
    def testOk(self):
        """IsOk, Ok"""
        c1 = wx.Colour(255,255,255,255)
        c2 = wx.Colour(0,0,0,0)
        c3 = wx.Colour()
        for color in (c1, c2, c3):
            self.assert_(color.IsOk())
            self.assert_(color.Ok())

def suite():
    suite = unittest.makeSuite(ColorTest)
    return suite
    
if __name__ == '__main__':
    unittest.main(defaultTest='suite')
