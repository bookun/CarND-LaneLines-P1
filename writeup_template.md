# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. First, I converted the images to grayscale, then I converted the images to gaussian_blue.

Next, I have detected edges by using canny (low_threshold=50, high_threshold=150) , then I declared the vertices. By using the vertices, I masked edges and executed hough transfer.


In order to draw a single line on the left and right lanes, I modified the draw_lines() function by calculating slope( (y2 - y1) / (x2 - x1) ).

if slope > 0, the line is a right edge. If slope < 0, that is a left edge.

Finally, I draw approximation straight lines in right and left side.

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![gray image](https://github.com/bookun/CarND-LaneLines-P1/blob/master/sample_images/gray.png?raw=true)

![blur_gaussian image](https://github.com/bookun/CarND-LaneLines-P1/blob/master/sample_images/blur_gaussian.png?raw=true)

![canny image](https://github.com/bookun/CarND-LaneLines-P1/blob/master/sample_images/canny.png?raw=true)

![my region image](https://github.com/bookun/CarND-LaneLines-P1/blob/master/sample_images/my_region.png?raw=true)

![maked image](https://github.com/bookun/CarND-LaneLines-P1/blob/master/sample_images/masked_edge.png?raw=true)

![hough transfer](https://github.com/bookun/CarND-LaneLines-P1/blob/master/sample_images/hough.png?raw=true)

![result image](https://github.com/bookun/CarND-LaneLines-P1/blob/master/sample_images/result.png?raw=true)



### 2. Identify potential shortcomings with your current pipeline

My pipline has a shortcomming.
Shadow have a bad influence on detecting line.
For examle, in `test_viedeos_output/challenge.mp4`, lines drew by my pipeline is not  on target when shadow appered.


### 3. Suggest possible improvements to your pipeline

Color detection will improve to my pipeline.
I want to mask shadow. 
By detecting white and yellow,  it will not be affected by shadows.
