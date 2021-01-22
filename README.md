# Tool to extract one big picture from videos

I am trying to learn to play keyboard.
I watch the videos of Rousseau on Youtube.
To avoid having to jump back and forth between seconds, the idea was to save the running keys as one big picture. That's what this tool is for.

The video is loaded and each image is processed individually.
Since the pixels shift by a certain length per frame, a threshhold was built in. With this and the number of images the total height of the image is calculated.
