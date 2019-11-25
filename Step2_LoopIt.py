#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""
#%% Required set up
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window
# so that you can still see your console
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging
from psychopy.hardware import keyboard

#gui
theGui = gui.Dlg()
theGui.addText('Welcome :)')
theGui.show()

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height')
win.recordFrameIntervals = True
win.refreshThreshold = 1/60 + 0.004
logging.console.setLevel(logging.WARNING)

# uncomment if you use a clock. Optional because we didn't cover timing this week,
# but you can find examples in the tutorial code
#trialClock = core.Clock()


#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things
thePic = visual.ImageStim(win,image='sin',pos=(0,0),units='pix',size=(800,600))
theText = visual.TextStim(win,color='black',text='Z or M?',
    alignHoriz='center',pos=(0,-0.5))

# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
# e.g. stim = ['1.jpg','2.jpg','3.jpg']
trialInfo = pd.read_csv('pics.csv')
trialInfo = trialInfo.sample(frac=1)
trialInfo = trialInfo.reset_index()
nTrials = len(trialInfo)

# make your loop
expClock = core.Clock() # won't reset
trialClock = core.Clock() # will reset at the beginning of each trial
stimClock = core.Clock() # will reset when stim are presented
for t in np.arange(0,nTrials):

    trialClock.reset()

    thePic = visual.ImageStim(win, image=trialInfo.loc[t,'img'],pos=(0,0),units='pix',size=(800,600))
    theText = visual.TextStim(win,color='white',text='Z or M?',
        alignHoriz='center',pos=(0,-0.5))
    thePic.draw()
    theText.draw()

    win.flip()
    stimClock.reset()

    keys = event.waitKeys(keyList=('z','m'))
    event.clearEvents()

win.flip()
core.wait(1)

win.close()
core.quit()
