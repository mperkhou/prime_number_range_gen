# Instructions

---

*Notice: Python must be installed on the system to run this app.*

---

Option 1: Using app.zip

*Note: after compiling the algorithm module, this will still run the pre-compiled version. You can*
*use this to compare runtimes againt the compiled version*

Make sure 'app.zip' is located in your working directory.


From your working directory (in commandline or terminal):

` > python app.zip `

or:

` > python3 app.zip `

---

Option 2: Using app directory

From the project directory (in commandline or terminal):

` > python app `

or:

` > python3 app `

---

Option 3: Optimize speed (2x more effecient)

First, install Cython

` > pip install cython`

Next, from the app directory run the compile.py script.
*note 1, uncomment line 8 if running on linux*
*note 2, it may require installing Microsoft Visual C++ 14.0* 

change to app directory:

` > cd app `

run compile.py

` > python compile.py build_ext --inplace `

or

` > python3 compile.py build_ext --inplance `

Finally to run the app, return to app root directory

` > cd .. `

and

` >  python app `

or 

` > python3 app `

*Note: in my environment, compiling improved execution runtime by half. My test case was the range from 1 to 10,000, which initially*
*had a runtime of 0.45s (on avg) and after compiling it averaged at around 0.24s.*

---

---
To run tests:

First change into the /app directory

` > cd ./app `

and then run the test.py file

` > python test.py `

or:

` > python3 test.py `

