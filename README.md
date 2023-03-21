INTRODUCTION

Project overview

Diabetic retinopathy is an eye condition that can cause vision loss and blindness in people who have diabetes. It affects blood vessels in the retina (the light-sensitive layer of tissue in the back of the eye). For patients with diabetes, it is important to get a comprehensive dilated eye exam at least once a year. There are five stages of DR that is 0, 1, 2, 3, and 4.
0 - No DR
1 - Mild
2 - Moderate
3 - Severe
4 - Proliferative DR

PROBLEM STATEMENT

Detecting the stage of Diabetic retinopathy using Fundus photograph images with help of deep learning model. The main objective of the project is to detect diabetic retinopathy to stop blindness before it is too late. we detect by classifying the images of retina of patient into five labels numbered from 0 to 4 where each label named as Normal, Mild DR, Moderate DR, Severe DR, Prolific DR respectively represents the Complication of the disease using Deep transfer learning and classification techniques. From these 5 stages one stages is observed as an output label for the given input fundus image.

Proposed Solution

STEP 1-Collected dataset of colored fundus Eye images from Kaggle.
STEP 2-Preprocessing like highlighting important features , resizing , cleaning ,conversion to NumPy array will be done.
STEP 3-After preprocessing, for prediction we will be using VGG16 architecture or transfer learning.
STEP 4-At last, the trained model will be used for Making user interface or GUI.(frontend).
