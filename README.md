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

Long term objectives:
    Determine what scientific instrument I want to build (DONE)
    Determine which sensors I will need to build said instrument (NOT DONE)
    Investigate sensors to determine what we want our instrument to measure (NOT DONE)
    Integrate Grove-LCD RGB Backlight in order to have a display for the Raspberry Pi (DONE)
    Fix the toggle button by ensuring that the backlight doesn't flip back to the first screen the moment the user stops holding down the button (NOT DONE)
    Remember to pull source code once per week (DO ON FRIDAY)

Note: Password for rasberry pi is: robots1234

Handy command to remember: (This command can pull the data after it is recorded)
scp pi@10.10.71.136:Documents/test.py /Users/denniscolombo/Documents