# Image Automation - Fullstack UI Automation Program

## Project Overview
- This project automates UI interactions (mouse clicks, keyboard input) by detecting screen elements based on image templates.  
Also, enhanced with a **frontend UI** for scenario management, monitoring, and configuration.

## Tech Stack

### Backend
- **Language**: Python
- **Libraries**: OpenCV, PyAutoGUI

### Frontend

## Features
- Image-based screen element matching
- Mouse/Keyboard automation via PyAutoGUI

## Development Environment Setup

## Project Structure
```
image_automation/
├── backend/
│   ├── action/                     # Handles input actions like mouse/keyboard
│   │   └── __init__.py
│   │
│   ├── api/                     
│   │   └── __init__.py
│   │
│   ├── detector/                   # Logic for detecting images on screen
│   │   └── __init__.py
│   │
│   ├── runners/                    # Scenario executor
│   │   └── __init__.py
│   │
│   ├── db/                         # Database connections
│   │   └── __init__.py
│   │
│   ├── utils/                      # Utility helper functions
│   │   └── __init__.py
│   │
│   ├── config/                     # Global config settings
│   │   └── config.yaml
│   │
│   ├── assets/                     # Image templates used for matching
│   │
│   │
│   ├── main.py                     # Flask app entry point
│
├── frontend/                       
│
└── README.md
```

## Build & Run

## License
MIT License

Copyright (c) 2025 Image Automation

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Third-Party Licenses
- pyautogui: BSD License
- numpy: BSD License
- opencv-python: Apache License 2.0

## Commit Style
- feat: Add new feature
- fix: Fix a bug
- docs: Documentation changes
- test: Add or update test code
- refactor: Code refactoring
- build: Modify build files
- chore: Minor changes
- rename: Rename file
- remove: Delete file
- release: Version release

## Project Purpose

## Key Features

## Example Usage

## Debugging