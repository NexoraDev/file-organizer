# file-organizer by File Type only
Automation scripts for file organization and management in Python."
# Automated File Organizer by Type

## Overview

This project is a simple yet powerful file organization system that categorizes files within a specified directory based on **file type**. The system continuously monitors the directory and automatically sorts files as they are added, keeping it organized without manual intervention.

## Features

1. **Automatic File Sorting by Type**:
   - Organizes files based on their extension (e.g., `PDF`, `JPEG`, `DOCX`).
   - Creates folders for each file type and moves files into their respective folders.
   
2. **Real-Time Monitoring**:
   - The system continuously monitors the specified directory and organizes new files by type as they are added.

3. **Duplicate Detection**:
   - Checks for duplicate files based on content and size, ensuring only unique files are retained in each folder.

## Tools and Libraries Used

- **Python**: Core language for scripting the organization.
- **Watchdog**: Library for monitoring file system changes to trigger automatic sorting.

## Setup Instructions

### Requirements

1. **Python 3.x**
2. Install dependencies:
   ```bash
   pip install watchdog
