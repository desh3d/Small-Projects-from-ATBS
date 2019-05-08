import shutil, os, re


myregx = re.compile(r'''
                   (\d\d\d,)(\d)?(\d\d)?        #anything
                                          #seperator
                                              #anything 
                    ''', re.VERBOSE)     #year

mo1 = myregx.findall('11 222 33,333 444,444,444 555,5555,5555,5555,555  ')
mo2= '454'
print(mo1)
