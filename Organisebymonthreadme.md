
# README for Organizing by File Type and Month

# Automated File Organizer by Type and Month

## Overview

This project expands upon a basic file organization system by categorizing files based on **file type** and **creation month**. It not only organizes files by type but also creates subfolders by month and year, allowing for an organized and time-based structure. The system continuously monitors the specified directory to auto-sort new files as they arrive.

## Features

1. **Automatic Sorting by Type and Month**:
   - Creates a main folder for each file type (e.g., `PDF Files`, `JPEG Files`).
   - Within each file type, files are organized by the month and year they were created (e.g., `2023_January`).

2. **Real-Time Monitoring**:
   - The system watches the specified directory and categorizes any new files by type and creation month as they are added.

3. **Duplicate Detection**:
   - Checks for duplicate files based on file content and size to keep only unique files.

## Tools and Libraries Used

- **Python**: Core language for creating the organization script.
- **Watchdog**: Library for monitoring the file system to trigger automatic sorting.
- **Pillow** and **pdf2image**: For optional file previews if needed.

## Setup Instructions

### Requirements

1. **Python 3.x**
2. Install dependencies:

   ```bash
   pip install watchdog pillow pdf2image