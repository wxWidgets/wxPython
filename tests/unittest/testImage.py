import unittest
import wx

"""
This file contains classes and methods for unit testing the API of 
wx.Image

Methods yet to test:
__del__, __nonzero__, AddHandler, Blur, BlurHorizontal, BlurVertical, CanRead,
CanReadStream, ComputeHistogram, ConvertAlphaToMask, ConvertColourToAlpha,
ConvertToBitmap, ConvertToGreyscale, ConvertToMono, ConvertToMonoBitmap, Copy,
CountColours, Create, Destroy, FindFirstUnusedColour, GetAlphaBuffer, GetAlphaData,
GetData, GetDataBuffer, GetHandlers, GetImageCount, GetImageExtWildcard, GetMaskBlue,
GetMaskGreen, GetMaskRed, GetOption, GetOptionInt, GetOrFindMaskColour, GetSubImage,
HasOption, HSVtoRGB, InsertHandler, LoadFile, LoadMimeFile, LoadMimeStream, LoadStream,
Mirror, Paste, RemoveHandler, Replace, ResampleBicubic, ResampleBox, Rescale, Resize,
RGBtoHSV, Rotate, Rotate90, RotateHue, SaveFile, SaveMimeFile, Scale, SetAlphaBuffer,
SetAlphaData, SetData, SetDataBuffer, SetMaskColour, SetMaskFromImage, SetOption,
SetOptionInt, SetRGBRect, ShrinkBy, Size

TODO: I don't understand why all the Mask-related methods are implemented within
    the wxImage class.  Wouldn't it be better to abstract it into wx.Mask?
    Revisit this later.
"""


class ImageTest(unittest.TestCase):
    def setUp(self):
        self.app = wx.PySimpleApp()
        self.size = wx.Size(10,10)
        self.testControl = wx.EmptyImage(*self.size)
    
    def tearDown(self):
        self.testControl.Destroy()
        self.app.Destroy()
    
    def testAlpha(self):
        """SetAlpha, GetAlpha"""
        self.testControl.InitAlpha() # needs to have Alpha
        for a in range(0,255,5):
            self.testControl.SetAlpha(0,0,a)
            self.assertEquals(a, self.testControl.GetAlpha(0,0))
        
    def testAlphaExists(self):
        """InitAlpha, HasAlpha"""
        self.assert_(not self.testControl.HasAlpha())
        self.testControl.InitAlpha()
        self.assert_(self.testControl.HasAlpha())
    
    def testAlphaFails(self):
        """SetAlpha
        Not all wx.Images have alpha channels"""
        self.assertRaises(wx.PyAssertionError, self.testControl.SetAlpha,0,0,0)
    
    def testAlphaInitFails(self):
        """InitAlpha
        'It is an error to call it if the image already has alpha data.'"""
        self.testControl.InitAlpha()
        self.assertRaises(wx.PyAssertionError, self.testControl.InitAlpha)
    
    def testConstructor(self):
        """__init__"""
        self.testControl = wx.Image('')
        self.assert_(isinstance(self.testControl, wx.Image))
    
    def testHeight(self):
        """GetHeight"""
        self.assertEquals(self.size.GetHeight(), self.testControl.GetHeight())
    
    def testImageSize(self):
        """GetSize"""
        self.assertEquals(self.size, self.testControl.GetSize())
    
    def testIsOk(self):
        """IsOk, Ok"""
        self.assert_(self.testControl.IsOk())
        self.assert_(self.testControl.Ok())
        self.testControl = wx.Image('')
        self.assert_(not self.testControl.IsOk())
        self.assert_(not self.testControl.Ok())
    
    def testMask(self):
        """SetMask, HasMask"""
        self.testControl.SetMask()
        self.assert_(self.testControl.HasMask())
        self.testControl.SetMask(False)
        self.assert_(not self.testControl.HasMask())
        self.testControl.SetMask(True)
        self.assert_(self.testControl.HasMask())
    
    def testSetColours(self):
        """SetRGB, GetRed, GetGreen, GetBlue"""
        for c in range(0,255,5):
            self.testControl.SetRGB(0,0,c,c,c)
            self.assertEquals(c, self.testControl.GetRed(0,0))
            self.assertEquals(c, self.testControl.GetGreen(0,0))
            self.assertEquals(c, self.testControl.GetBlue(0,0))
    
    def testTransparent(self):
        """IsTransparent"""
        self.testControl.InitAlpha()
        self.testControl.SetAlpha(0,0,wx.IMAGE_ALPHA_THRESHOLD)
        self.testControl.SetAlpha(1,1,wx.IMAGE_ALPHA_THRESHOLD-1)
        self.assert_(not self.testControl.IsTransparent(0,0))
        self.assert_(self.testControl.IsTransparent(1,1))
        threshold = 55
        self.testControl.SetAlpha(2,2,threshold)
        self.testControl.SetAlpha(3,3,threshold-1)
        self.assert_(not self.testControl.IsTransparent(2,2,threshold))
        self.assert_(self.testControl.IsTransparent(3,3,threshold))
    
    def testWidth(self):
        """GetWidth"""
        self.assertEquals(self.size.GetWidth(), self.testControl.GetWidth())
        

if __name__ == '__main__':
    unittest.main()