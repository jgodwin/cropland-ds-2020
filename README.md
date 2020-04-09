# cropland-ds-2020
A small data science demo project that shows supervised and unsupervised classification on a small dataset using publicly available data.

This project was originally inspired by a similar project located at: https://github.com/bhavesh907/Crop-Classification, which in turn was inspired by this [paper](http://cs229.stanford.edu/proj2017/final-reports/5243811.pdf) paper by Rustowicz, which uses multiple hyperspectral images acquired over a single growing season to make better crop predictions than found in the original USDA Cropland dataset.  This intuitively makes sense, because different crops will grow at different rates over time, and have varying spectral characteristics as the season progresses, which should be easily recognizable in the temporal domain.  

My main contribution is to investigate the use of unsupervised classification to tease out the dominant temporal signal associated with some of these crops, and also to use higher dimensional (2D and 3D) convolutional neural networks to try to produce more consistent and better labels.
