## Predict The Attributes of the Animal

This project is about predicting attributes of an animal given a image.
The first intent to do the job was to train InceptionV3 model using Keras and
pretrained model, after 8 hours of finetuning the best accuracy was 0.97.
This code can be found in `zoo_attributes_inception.ipynb`.

The next intent was to extract features from a more recent deep network in this case
using TensorFlowHub I've extracted features (bottleneck) from both train and test images
using Progressive Neural Architecture Search (PNASNet-5) architecture.

The features were extracted using `retrain.py` script that can be found in tensorflow hub repository
and th command to extract features is as follows 
```
python retrain.py \
    --image_dir ./DL3Dataset \
    --tfhub_module https://tfhub.dev/google/imagenet/pnasnet_large/feature_vector/1
```

it will create text file for each image under train and test_img directories. Having this features
the next step was to train a simple keras model to predict the 85 attributes.
After 30 epochs of training a model with lower validation loss and near from the best train loss 
was choose. to make the predictions the code for this can be found in this notebook `bottles.ipynb`

I've use sklearn f1 score metrics to go further and evaluate different trained models. finding
the same model I've choosed as the best perfomer in this metric. The predictions was generated and
stored in a csv file using pandas.