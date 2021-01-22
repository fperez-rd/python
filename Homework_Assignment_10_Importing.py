"""

programmer: Felix Perez

Homework Assignment #10: Importing

Details:
 
Pick any library that come with Python (https://docs.python.org/3/library/) that we haven't covered in the course already.

Learn how to use the library extensively, then prepare a code sample that showcases what you've learned. This can take any form you wish. You
could create an application with the library, or just show examples of how to use its methods.

Extra Credit:

Share your knowledge with the community by writing a blog post instead of just uploading a code sample! You don't need to mention this
class at all, just share what you've learned about that library. If you've been meaning to start a coding blog, now you have a reason
to do it! If you take this route, just send us the link to the post instead of to your Github code,

"""
import statistics as stat, tkinter, os, datetime

#statistics

    #mean example:
resultMean = stat.mean([1,2,3,4,4])
print(resultMean)

    #median examle:
resultMedian = stat.median([1,2,5])
print(resultMedian)

    #mode example:
resultMode = stat.mode([1,1,2,3,3,3,3,4])
print(resultMode)

#tkinter

    #window example:
window = tkinter.Tk()
testWindow = tkinter.Frame(window)
testWindow.mainloop()

#os

    #getcwd example:
currentDirectory = os.getcwd()
print(currentDirectory)

    #date.today example:
currentDate = datetime.date.today()
print(currentDate)