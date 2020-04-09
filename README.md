# cropland-ds-2020
A small data science demo project that shows supervised and unsupervised classification on a small dataset using publicly available satellite imagery that was found here: [Kaggle Dataset](https://www.kaggle.com/bhavesh907/crop-classificationcs2292017usgscroplanddata)

This dataset was used for a similar project located at: https://github.com/bhavesh907/Crop-Classification, which in turn was inspired by this [paper](http://cs229.stanford.edu/proj2017/final-reports/5243811.pdf) by Rustowicz, which uses multiple hyperspectral images acquired over a single growing season to make better crop predictions than possible using only a single image acquired during the growing season.  This intuitively makes sense, because different crops will grow at different rates over time, and have varying spectral characteristics as the season progresses, which should be easily recognizable in the temporal domain.  In general, it looks like the predictions from the multi-temporal approach are more consistent spatially than those found in the original USDA Cropland dataset. 

My main contribution is to investigate the use of unsupervised classification, and also to use higher dimensional (2D and 3D) convolutional neural networks to try to produce more consistent and better labels.

In this case, a 2D-convolutional neural network treats each of the temporal images as an additional set of channels, and then runs the convolution over the spatial dimensions of the "hyper" image. This has an advantage over the 1D convolutional neural network used by Rustowicz and bhaevesh in that it should allow for more spatial continuity in the predicted labels, as the 1D convolution does not take into account the spatial autocorrelation between nearby samples.  

A 3D convolutional neural network takes things one step further by also allowing us to use convolutional filters across the temporal domain instead of treating each temporal image as a separate set of channels.
