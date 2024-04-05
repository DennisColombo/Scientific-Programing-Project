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

Tasks for the day (April 3rd, 2024):
    Write code to graph data from the rangefinder against time (DONE)
    Get rangefinder data into the code (DONE)
    Assemble a structure so I don't have to hold everything while using the device (PARTLY DONE)

Tasks for the day (April 5th, 2024):
    Create a plan to test the rangefinder against the physics app on my iPad (DONE)
        ~Plan:
            ~Step 1: Lay one of the portable whiteboards in the room flat on a table, this whiteboard will be called the 'track'
                ~I need to make a mark on the beginning point and ending point so that way I know the distace I am measuring which will help ensure accuracy
            ~Step 2: Get a large, flat object, which will be called the 'target object' from here on, and move it alongside the edge of the whiteboard from one end to the other
                ~I will use another one of the portable whiteboards as it is pretty much impossible for the rangefinder to miss it and I will be able to easily ensure that the target object's face is perpendicular to the sides of the track
                ~In order to make sure that the rangefinder isn't at an angle relative to the target, which would increase the distance and reduce accuracy, I will hold the rangefinder against one of the sides in order to keep it at the correct angle
            ~Step 3: Move the target object on the track between the starting mark and ending mark and record the data using the rangefinder and Video Physics at the same time
                ~Manually moving the target object, while inconvient, allows complete control over what the data looks like, at least theoretically
                ~The iPad will be off to the side, recording video while the rangefinder records real-time data
                ~The Video Physics app can keep track of time, and it can also allow to rewind to see what was going on at any given moment
            ~Step 4: Compare data from each run, and record it in a google document
                ~The graph from the data collected with the rangefinder vs. the graph from the points I manually plotted with the Video Physics app
                ~The percent difference of a few points in time between the two methods of collecting data
                    ~As expected, the lower the better...
            ~Step 5: Repeat experiment in order to ensure that the results are good
                ~Each time the experiment is repeated move the target object in a slightly different way to make sure that the rangefinder can handle more complex motion
    Figure out a method of making the starting and ending marks on the track (DONE)
        ~Ask for a dry erase marker when getting ready to run the tests, there are plenty available!
    Write down the name of the physics app for clarity's sake (DONE)
        ~Name of physics app: Video Physics
    Clean up long term objectives section to remove unneeded clutter and make goals more accurate (DONE)
    Ask GITHUB COPILOT if there is a better method of getting the derivative at a point from a scatter plot (PARTLY DONE)
        ~I got some results but I didn't have time to actually refine the results that the AI spat out
        ~I will keep working at it and remove the flawed plan I made from the long term objectives section
        ~I will add this to long term objectives

Long term objectives:
    Improve the code which graphs the data from the rangefinder (NOT DONE)
    Ask GITHUB COPILOT if there is a better method of getting the derivative at a point from a scatter plot (CONTINUE)
        ~Code must have a derivative funtion, this is VERY different from a line of best fit
            ~Until this is done, I can't compare the velocity or the acceleration of Video Physics and my device
    Determine potential sources of error for my rangefinder, and determine if there are ways to address them (NOT DONE)
    Improve the structure holding the instrument (NOT DONE)
    Make getting data from the rangefinder quick and easy (NOT DONE)
    Test data gathered from my rangefinder against data from Video Physics (NOT DONE)
    Remember to pull source code once per week (DO ON FRIDAY)

Note: Password for rasberry pi is: robots1234

Handy command to remember: (This command can pull the data after it is recorded)
scp pi@10.10.71.136:Documents/test.py /Users/denniscolombo/Documents
    ~Note: IP Address is incorrect!
Get the IP on the raspberry pi:
run 'ifconfig' in the terminal on the raspberry pi, IP is in the 'wlan0' section labeled 'inet'
Doing this will give us the IP Address of the raspberry pi and allow us to get data from it.