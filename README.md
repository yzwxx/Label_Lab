# Label_Lab
It is a tool to create labels for images with an index-based name, written in Python and PyQt4 for graphical interface.  
Currently, it supports two image formats, which are jpeg and png, respectively. The outputs are stored in a json line file for easy access.

<div align="center">
    <img src="https://github.com/yzwxx/Label_Lab/blob/master/demo_lablab.png?raw=true"/>  
    <br>  
    <em align="center">”demo screenshot</em>
</div>

## Usage
git clone the repository to your file directory and use the command below to run it:
```python
python lablab.py
```
### hot keys
key-combo | functionalty 
------------ | -------------  
Alt+1 | select image source file
Alt+2 | select result file
Alt+3 | clear the input label entry
Alt+a | move to previous image
Alt+d | move to next image
Alt+s | save the current labels
Alt+q | exit the program

### workflow
1.select the image source file containing all the images to be labelled
2.select the result json line file 
3.type the label for current image, press 'Enter' to create a new label;If the search bar auto-tip gives what we want just click it and press 'Enter' or just press 'Enter'.Remember to use 'Alt+3' to clear the entry when necessary. 
4.after creating all the labels,then save them using 'Alt+s'
5.move to next image and repeat the procedure from 3~5 untill  all images are labelled.
6.if we want to update old labels of one previous image,first move to it and then create and save new labels.The new labels will overwrite the old

