# AUTONOMUS-LANDING-ZONE-DETECTION-FOR-QUADROTOR-TYPE-UAV
Image Processing based autonomous landing zone detection detection for quadrotor-type UAV in emergency situation 

The object detection starts with converting the FOV image into a grayscale image.  This is necessary for preparing the image for canny operator which is a method for edge detection to find objects on image. The Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images. The advantage of using Canny Edge detection technique over other well-known edge detection algorithms is that it gives better results even in noisy conditions.  

The edge detection operator has four steps. 
•	Smooth an image with Gaussian filter.
•	Calculate gradient magnitude and gradient direction.
•	“Non - maximum suppression” to ensure the desired edge with one single pixel width.
•	Determine two threshold values, and then select possible edge points and trace edges.


In a typical emergency landing scenario, a maximum altitude of 5 meters is appropriate for initialization of image processing tasks. Therefore, we used the same altitude value for our analysis as well. In case of triggering the emergency landing at a higher altitude, the UAV is brought to 5-meter height first, then the image processing is activated. 

After determining the optimal dimensions for landing, an available space for these dimensions is searched in the FOV image. The availability of a spot in the image is defined as the area in which no object is present. In order to check the availability, a binary mask is created. In this binary mask, an area with the optimal dimensions is made “1”, and all the remaining area is left as “0”. The area with “1” values in the binary image is the proposed region and we check the availability of that region. By observing the output of the logical AND operation between the binary mask and the objects image, it is possible to determine if a spot is available or not. If the logical AND operation returns “1” value, then it means that there is an overlap between any of the objects and the proposed region in the binary mask. Therefore, this proposed region is labeled as “negative”. On the other hand, if a value of “0” is returned from the AND operation, then no overlap is present, hence the proposed region is labeled as “positive”. 

When a proposed region is labeled as “negative”, another region should be proposed immediately until a “positive” label is achieved. Since this work concerns only with the emergency situations, the location of the first proposed region is the middle of the FOV image which is the spot that is closest to UAV. If this spot is not available then a circular vicinity of the middle point is searched for availability, and the radius of the circle is gradually increased until an available spot is found. 

