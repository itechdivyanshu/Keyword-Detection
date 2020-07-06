# Python Always Listening Keyword Detection

This project provides example code for device that can trigger off of a keyword that is always listening using Python. This can be used for to augment any project that requires the user to initiate any action. As an example, the phrase "Jarvis" can trigger a call to the [SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition) library, where the users next sentence can be captured and parsed.

## Requirements

- [Python 3.4+](https://www.python.org/)
	- #### [pyaudio](https://people.csail.mit.edu/hubert/pyaudio/)`
	
	```javascript
	sudo apt-get install python3-pyaudio
	```
	
	- #### [pocketsphinx](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pocketsphinx)
	
	```javascript
	sudo apt-get install python3 python3-all-dev python3-pip build-essential swig git libpulse-dev libasound2-dev
	```
	```javascript
	pip3 install pocketsphinx
	```
	
	
- [Microphone](http://amzn.to/1rvSxuS)

## Using CMU Sphinx

The code in this repository is based on an example in the pocketsphinx GitHub repository. 

[pocketsphinx/swig/python/test/kws_test.py](https://github.com/cmusphinx/pocketsphinx/blob/master/swig/python/test/kws_test.py)

- To use this repository just run [always_listening.py](./always_listening.py)
    ```javascript
    python3 always_listening.py
    ```

## Cross-Platform

This code has only been tested on Windows. The final goal is for this project to work out of the box on a Raspberry Pi and on Windows.

## Bugs

If you run into any bugs, please create an issue on GitHub. Don't hesitate to submit bugs for the README as well! I can't promise that I will get to it quickly, but I will do my best to keep this project as bug free as possible.

## License
MIT - [See LICENSE](./LICENSE)

## Change Log
* Version 0.1 - Initial commit

## Contributing


If you're new to contributing to Open Source on Github, [this guide](https://guides.github.com/activities/contributing-to-open-source/) can help you get started. We're a warm and welcoming community of open source contributors. Please join. All types of contribution are welcome.

###### This repository is just a small subset of work put together by a much larger pool of voluntary efforts contributed by generous people all around the world. Reach out to us through itechindrustries@gmail.com
