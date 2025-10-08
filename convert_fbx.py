#!/usr/bin/env python3
"""
Convenience script to convert ASCII FBX to Binary FBX
"""

import sys
import os

# Add scripts directory to path
scripts_dir = os.path.join(os.path.dirname(__file__), 'scripts')
sys.path.insert(0, scripts_dir)

# Import and run the converter
from ascii_to_binary_fbx import *

if __name__ == '__main__':
    # Re-run main from ascii_to_binary_fbx
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python convert_fbx.py <input.fbx> [output.fbx]")
        print("  python convert_fbx.py <directory>  # Convert all FBX in directory")
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    
    if input_path.is_dir():
        # Convert all FBX files in directory
        print(f"Scanning directory: {input_path}")
        converted = convert_all_fbx_in_directory(input_path)
        print(f"\nConverted {len(converted)} file(s)")
    elif input_path.is_file():
        # Convert single file
        output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.with_name(input_path.stem + '_binary.fbx')
        
        print(f"Converting: {input_path}")
        print(f"Output: {output_path}")
        
        try:
            convert_ascii_to_binary(str(input_path), str(output_path))
            print("[OK] Conversion successful!")
        except Exception as e:
            print(f"[ERROR] Conversion failed: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    else:
        print(f"Error: {input_path} not found")
        sys.exit(1)

