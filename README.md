Wake Up!
========

Wake your target PC up with a single click!

Concepts
--------

I personally have two PC set here at home. A Windows
All-In-One and a RaspberryPi running Raspbian.

It occurred to me that if I can use the RaspberryPi to wake up
the All-In-One remotely using Wake On Lan so that I can have
full access to my powerful Windows PC anywhere away from
home and at the same time save some energy by turn my
Windows PC into sleep/hibernate mode when I finished my work
with it.

By using `Wake Up!`, the Windows PC is defined as a `target`
computer, while my RaspberryPi as a `server`. Simply run
`./run_target.py` on `target` and `./run_server.py` on
`server`, I can achieve the goal.

Usage
-----

Firstly, as always, you should have Python 3 installed.
Then

    pip install -r requirements.txt

Next, copy the file `./wakeup/config.py.example` to
`./wakeup/config.py` and set all the configuration
variables as you desired.

Finally, copy and run the code seperately on `target` and
`server`.

Navigate to your `server`'s HTTP server and login use the
token specified in `./wakeup/config.py`. Done!

