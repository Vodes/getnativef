#!/usr/bin/env python3

# Make sure the CLI-Parser does not print out __main__.py
import sys, os

sys.argv[0] = os.path.dirname(sys.argv[0])

# Run getnative.
from getnativef import main

app.main()
