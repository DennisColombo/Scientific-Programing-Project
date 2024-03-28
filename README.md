# MY project...

some descriptive text

github workflow:

git add .  
git commit -m "Text describing what I did"  
git push  

Got the Rasberry Pi to do something today, I can get data on the other computer and my next step I need to take is to get the data onto a graph

Tasks for the day (Febuary 9th, 2024):
    Write down the orignial function on the side of the graph (DONE)
    Make the graph look better (DONE)
    Figure how to make a scatter plot (DONE)
        ~To build on this, get a line of best fit for your plot (DONE)
        ~Display the function and derivative of line of best fit (DONE)

Tasks for the day (Febuary 23rd, 2024):
    Collect data from the rasberry pi and plot it (DONE)
    Figure out how to calculate the line of best fit for the data (DONE)
    Come up with a plan for tasks I need to accomplish in the future (DONE)
    Add some labels to help future me figure out what to do (DONE)

Tasks for the day (Febuary 29th, 2024):
    Figure out how to get a timestamp (DONE)
    Figure out how to make the file clear itself after I run the program again (DONE)
        ~Note: You have to close the file to get it to update or else it will just display the same text
    Pull source code from the Pi so that I have a second copy just in case (DONE)

Tasks for the day (March 4th, 2024):
    Pull up grove_rotary_angle_sensor.py in /home/pi/Desktop/GrovePi/Software/Python (DONE)
    Make the rotary angle sensor work in a graphable way (DONE)
    Figure out how to get the line of best fit to not be super short, it just doesn't make any sense at all (DONE)
    Figure out proper units for my axis, especially time (DONE)

Tasks for the day (March 6th, 2024):
    Work on long term objectives (NOT DONE)

Tasks for the day (March 20th, 2024):
    Add a display sensor to the rotation graphing program to figure out how that works (DONE)
        ~I created a program which displays the degree value every 100 miliseconds
    Add a way to toggle the display sensor with a button (NOT DONE)

Tasks for the day (March 22nd, 2024):
    Work on the toggle button I failed to finish last class period (DONE)
        ~It works, but it isn't perfect (more detail in long term objectives section)
    Figure out how to display different graphs on different tabs (DONE)
        ~Look in RotationGraphing.py to see how it works (plt.figure('some number here'))

Tasks for the day (March 26th, 2024):
    Determine which sensor(s) needed to build the sensor to bare minimum functionality (DONE)
        ~Rangefinder (to measure distance)
    Add rangefinder to raspberry pi and get it to work (NOT DONE)
    Determine how to create an if statement with two requirements in python (DONE)
    Remove clutter (completed objectives) from long term objectives list (DONE)

Tasks for the day (March 28th, 2024):
    Add rangefinder to raspberry pi and get it to work (DONE)
    Test rangefinder against a ruler (DONE)
        ~The rangefinder is within a few centimeters of the tape measurer, good enough for me
    Make the rangefinder code actually go to the correct file (DONE) *Priority*
    Make decision on whether or not the backlight will actually be helpful (DONE)
        ~After significant work with it, I just don't see it being useful
    Figure out the units for the rangefinder (DONE)
        ~The rangefinder is measured in centimeters
    Remove irrelevant and completed long term objectives (DONE)
    Pull source code to make sure that nothing is lost (NOT DONE)

Long term objectives:
    Write code to graph data from the rangefinder (NOT DONE)
    Test data gathered from my rangefinder against one of the physics apps I have (NOT DONE)
    Assemble a structure so that I don't have to hold everything (NOT DONE)
    Remember to pull source code once per week (DO ON FRIDAY)

Note: Password for rasberry pi is: robots1234

Handy command to remember: (This command can pull the data after it is recorded)
scp pi@10.10.71.136:Documents/test.py /Users/denniscolombo/Documents