# GoogleFormAutoFillCodeTemplate
This is a code template program that can be used to auto-fill the Google form (Only choice questions)

Test link: https://docs.google.com/forms/d/e/1FAIpQLSf3cpgt4hddwYXDNbFUOlVfZKDp2gEsDCat56_g3OVLgzQXcQ/viewform
**Note that this is a template code, You might need to modify some part to make it working in your own google form.

## Requirements
1) A Chrome driver that matches your Chrome version, you can check the driver version by going to your Chrome -> setting -> about Chrome. then you'll need to download a driver at this link https://chromedriver.chromium.org/downloads after you download you'll need to extract the zip then open the driver once then we're all done.
(In this project I also add the Chome driver version 111.0.5 if you using the same version as me then you can skip the download part, but do not forget to open the driver once and put it somewhere else not in the project directory)
2) Selenium library for Python, you can install it by using this command `pip install selenium` in your terminal.

## How to use it?
1) After you have the Chrome driver, when you run the program, it will ask you how many times you want to loop doing the form, I suggest putting 1 for the first time, then paste the Google form link into it.
2) Since this is a code template, you might need to change the element according to your Google form by inspecting the element, finding the class then using it instead of mine.
