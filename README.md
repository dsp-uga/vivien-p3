# vivien-p3
## Fluctuation Variance
Implemented by using: Python 3 with OpenCV and NumPy modules

#### Input arguments:
1 - text file of hashes
2 - directory of data .tar files
3 - directory of mask images
4 - directory to output prediction masks

#### Summary:
This script does the following:
 - Extract tar archives of images
 - Decode images into NumPy with OpenCV
 - Calculate variance of pixels across images
 - Test different threshold values for fluctuation variances
 - Calculate IoU accuracy
 - Export predicted mask images

#### Notes: 
Average accuracy for the test set of 211 videos were around 29%. Additionally, median filter has been implemented however, performed worse. Ways to explore more: FFT and optical flow.

#### References:
https://docs.opencv.org/master/

## Pyramid Scene Parsing Network

Pyrammid Scene Parsing Network(PSPNet) is used here for deep learning based segmentation. Implemented by using M2Lab open library.

The model is pretrained on VOC 12 dataset with augmentation. And the model is modified and further trained on Cilia dataset for 5k epochs. The final performance is listed below.

+------------+-------+-------+
| Class      | IoU   | Acc   |
+------------+-------+-------+
| background | 97.72 | 98.72 |
| cell       | 96.15 | 98.07 |
| cilia      | 82.87 | 91.4  |
+------------+-------+-------+

+--------+-------+-------+-------+
| Scope  | mIoU  | mAcc  | aAcc  |
+--------+-------+-------+-------+
| global | 92.25 | 96.06 | 97.94 |
+--------+-------+-------+-------+

On Autolab, it reached 44 mIOU score





