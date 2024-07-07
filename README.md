# Fruits Classification using CNN Models

This repository contains code for training Convolutional Neural Network (CNN) models to classify images of fruits into different categories. Three CNN architectures were implemented and evaluated: EfficientNetB3, VGG16, and Vision Transformer (ViT). Below are the final accuracies achieved on the validation set for each model:

- EfficientNetB3: 90%
- VGG16: 84%
- Vision Transformer (ViT): 62%

## Dataset

The dataset used consists of images divided into training, validation, and test sets. The dataset is organized with class directories where each directory corresponds to a different fruit category.

## Data Preprocessing

- The training data was augmented using various techniques such as random flips, rotations, crops, zooms, contrast adjustments, and rescaling.

## Model Architectures

### EfficientNetB3

- EfficientNetB3 architecture was employed with custom modifications for the task. It includes:
  - Stem convolution layers
  - Multiple blocks with depthwise separable convolutions and Squeeze-and-Excitation (SE) blocks
  - Global average pooling and dense layers for classification

### VGG16

- VGG16 architecture adapted for fruit classification:
  - Several convolutional blocks with batch normalization and max-pooling
  - Global average pooling and fully connected layers for classification

### Vision Transformer (ViT)

- Vision Transformer architecture:
  - Patch extraction and encoding layers
  - Transformer encoder blocks with multi-head attention and MLPs
  - Global average pooling and classification MLP

## Training

- Each model was trained using the Adam optimizer with a custom learning rate scheduler.
- Early stopping was employed to prevent overfitting, and the best weights were restored based on validation loss.

## Usage

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>

 
