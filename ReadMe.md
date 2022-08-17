# Project Implementation Instructions


This document explains how to implement a feature flag from LaunchDarkly using the Python SDK. 

This feature flag turns an image on and off on a HTML page. Feature flag targeting has also been implemented in this solution to determine which image exactly to display to the user depending on the country they are from (country variable is hard-coded in the python script). 

The steps below will show you how to implement the feature flag and the targeting functions within it and also how to run the Python script locally on your computer. Mac and Windows instructions written below.


## Prerequisites - Building the Feature Flag in LaunchDarkly 

1. Start a free trial with LaunchDarkly at https://launchdarkly.com/start-trial/

2. Create a feature flag called "launch_region_flag"

3. Select 'SDKs using Client-side ID'

4. Set the flag variation to type 'String'

5. Create 5 Variations for this feature flag:

		Variation 1 : ireland.png
		Variation 2 : france.png
		Variation 3 : spain.png
		Variation 4 : portugal.png
		Variation 5 : null.png

6. Set the Default ON to Variation 1

7. Set the Default OFF to Variation 5

8. Save the flag

9. Click on the feature flag you just created and go to the targetting menu. We are going to create 4 targetting rules.

10. Under the 'Target users who match these rules' section, click 'Add Rule'

11. Create a rule where 'IF country contains value Ireland', Serve ireland.png.

12. Repeat step 11 three more times for Spain, France and Portugal for thier associating image variations referenced above.

13. You should now have 4 rules in total whereby if the country is X then the rule will serve x.png

14. At the bottom of the targeting page, set the Default Rule to serve null.png and if targeting is off, serve null.png as well.





#### Running the program - Mac Users


1. Click the 'Code' button in Github and download the ZIP file 'Assignment-ArmanH-main'

2. Unzip the file where you would like to store it.

3. Edit assignment.py and replace the SDK key in line 18 with the key generated in your own LaunchDarkly environment and save it.

4. Open Terminal on your Mac and navigate to the folder you unzipped using the `cd` command. You should be within the 'Assignment-ArmanH-main' directory now within Terminal

5. Next, we need to setup a virtual environment within this folder. We can do so by running the command `python3 -m venv fl_venv` and click enter. Next we need to activate it by typing : `. fl_venv/bin/activate`. You should see the name fl_venv before the Command Prompt now which means it is activated.

6. Next we need to install Flask in the virtual environment. To do this type : `pip install Flask` and hit enter. Flask should be installed successfully in the virtual environment.

7. If step 6 didn't work, you may need to install Pip. To install Pip type `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` and click enter. After that executes type `python3 get-pip.py` to run the program. Pip should be installed successfully now. Repeat step 6.

8. Next we need to install the LaunchDarkly SDK. Again within the virtual environment type : `pip install -r requirements.txt` and hit enter. You have now installed the LaunchDarkly Server SDK.

9. If you type : `pip list` and hit enter, you will see Flask and the SDK installed in the virtual environment now.

10. You can now run the python program by typing : `python assignment.py` and hit enter.

11. Copy and paste the URL `http://127.0.0.1:5000` into a web browser to display the HTML page.

12. In LaunchDarkly, turn the feature flag on, refresh the page and you should see the Irish flag displayed. 

13. Turn the feature flag off, refresh the page and you will see a 'null' image displayed.

14. If you are interested in testing the targeting settings you created, exit the python program in terminal by pressing CTRL+C to quit.

15. Edit assignment.py again but this time edit line 11 and change country to "Spain" instead of "Ireland" and save.

16. Jump back into the terminal again. You should still be within your virtual environment, if not refer to step 5 to activate it again. Run the python program again by typing : `python assignment.py` and hit enter.

17. Refresh the url page `http://127.0.0.1:5000` and you should see the Spanish flag displayed instead. This is because we are using targetting rules to first identify the user's country and based off this information, we are displaying the relavant image to them. If you are still seeing the null image, your feature flag may be turned off so turn this back on in LaunchDarkly.




#### Running the program - Windows Users


1. Click the 'Code' button in Github and download the ZIP file 'Assignment-ArmanH-main'

2. Unzip the file where you would like to store it.

3. Edit assignment.py and replace the SDK key in line 18 with the key generated in your own LaunchDarkly environment and save it.

4. If you don't have Python or Pip installed on your machine you can install it from here: https://www.python.org/downloads/

5. Open cmd on your desktop and navigate to the folder you unzipped using the `cd` command. You should be within the 'Assignment-ArmanH-main' directory now within cmd

6. Next we need to install Flask if you do not have it installed already. To do this type : `pip install Flask` and hit enter. Flask should be installed successfully.

7. Next we need to install the LaunchDarkly SDK. Again within cmd type : `pip install -r requirements.txt` and hit enter. You have now installed the LaunchDarkly Server SDK.

8. If you type : `pip list` and hit enter, you will see Flask and the SDK installed now.

9. You can now run the python program by typing : `python assignment.py` and hit enter.

10. Copy and paste the URL `http://127.0.0.1:5000` into a web browser to display the HTML page.

11. In LaunchDarkly, turn the feature flag on, refresh the page and you should see the Irish flag displayed. 

12. Turn the feature flag off, refresh the page and you will see a 'null' image displayed.

13. If you are interested in testing the targeting settings you created, exit the python program in cmd by pressing CTRL+C to quit.

14. Edit assignment.py again but this time edit line 11 and change country to "Spain" instead of "Ireland" and save.

15. Jump back into the cmd again. Run the python program again by typing : `python assignment.py` and hit enter.

16. Refresh the url page `http://127.0.0.1:5000` and you should see the Spanish flag displayed instead. This is because we are using targetting rules to first identify the user's country and based off this information, we are displaying the relavant image to them. If you are still seeing the null image, your feature flag may be turned off so turn this back on in LaunchDarkly.














