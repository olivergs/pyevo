# -*- coding: utf-8 -*-
"""
PyEVO PIL image manipulation tools
===============================================

.. module:: pyevo.images
    :platform: Unix, Windows
    :synopsis: PIL image manipulation tools
.. moduleauthor:: (C) 2013 Oliver Gutiérrez
"""

from PIL import Image, ImageEnhance, ImageStat, ImageFont, ExifTags

def opacity(im,alpha):
    """
    Returns an image with reduced opacity
    """
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alphachannel = im.split()[3]
    alphachannel = ImageEnhance.Brightness(alphachannel).enhance(alpha)
    im.putalpha(alphachannel)
    return im

def average_brightness(im):
    """
    Return average brightness for an image
    """
    imcopy = im.copy().convert('L')
    stat = ImageStat.Stat(imcopy)
    return stat.mean[0]

def watermark(im, mark, position=None, adjust='tile', alpha=1):
    """
    Adds a watermark to an image
    """
    # Check input
    assert alpha >= 0 and alpha <= 1

    # Set watermark alpha
    if alpha < 1:
        mark = opacity(mark, alpha)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    # Draw watermark in a transparent layer
    layer = Image.new('RGBA', im.size, (0,0,0,0))
    if adjust == 'tile':
        for y in range(0, im.size[1], mark.size[1]):
            for x in range(0, im.size[0], mark.size[0]):
                layer.paste(mark, (x, y))
    elif adjust == 'scale':
        # Scale preserving the aspect ratio
        ratio = min(
            float(im.size[0]) / mark.size[0], float(im.size[1]) / mark.size[1])
        w = int(mark.size[0] * ratio)
        h = int(mark.size[1] * ratio)
        mark = mark.resize((w, h))
        layer.paste(mark, ((im.size[0] - w) / 2, (im.size[1] - h) / 2))
    else:
        layer.paste(mark, position)
    # Composite watermark with layer
    return Image.composite(layer, im, layer)

def get_optimal_font_size(fontfile,text,maxwidth,maxheight):
    """
    Get optimal font size for given max width and height
    """
    fontsize = 1
    font = ImageFont.truetype(fontfile, fontsize)
    while font.getsize(text)[0] < maxwidth and font.getsize(text)[1] < maxheight:
        fontsize += 1
        font = ImageFont.truetype(fontfile, fontsize-1)
    return font

#def crop_image(imagefile,rect,size=None,format='JPEG',filename='cropped.jpg'):
#    """
#    Crops an image at given rectangle and returns a InMemoryUploadedFile instance for use in django
#    """
#    # Create a file-like object to write cropped data
#    fd = StringIO.StringIO()
#    # Load image
#    im=Image.open(imagefile)
#    cropped=im.crop(rect)
#    if size:
#        cropped.resize(size)
#    cropped.save(fd,format=format)
#    # Create django file upload object and return it
#    return InMemoryUploadedFile(fd, None, filename,'image/%s' % format.lower(), fd.len, None) 
#
#
#def resize(path,outpath,width,height,format='JPEG'):
#    """
#    Resizes an image to the specified width and height
#    
#    :param path: Path to input image file
#    :type path: String
#    :param outpath: Path to output image file
#    :type outpath: String
#    :param width: Desired width
#    :type width: Integer
#    :param height: Desired height
#    :type height: Integer
#    :param format: Output image format
#    :type format: String
#    :returns: True or False on any error
#    :rtype: Boolean
#    """
#    try:
#        imgsize=(width,height)
#        th=Image.open(path)
#        if th.size!=imgsize:
#            th.thumbnail(imgsize)
#            th.save(outpath,format=format)
#        return True
#    except:
#        return False

def extract_exif_data(image):
    """
    Return a dictionary with EXIF data from an image
    """
    if isinstance(image,(str,unicode,file)):
        # Open image
        im=Image.open(image)
    else:
        im=image
    # Get EXIF numeric tags info
    exif_data = im._getexif()
    data={}
    if exif_data is not None:
        data={ 
            ExifTags.TAGS[k]: v
            for k, v in exif_data.items()
            if k in ExifTags.TAGS
        }
    return data
