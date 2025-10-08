#!/usr/bin/env python3
"""
Convenience script to start the FBX Exporter Server
"""

import sys
import os

# Add scripts directory to path
scripts_dir = os.path.join(os.path.dirname(__file__), 'scripts')
sys.path.insert(0, scripts_dir)

# Change to scripts directory so relative imports work
os.chdir(scripts_dir)

# Import and run the server
import FbxExporterServer

