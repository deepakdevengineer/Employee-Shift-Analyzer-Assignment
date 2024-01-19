# Employee Shift Analyzer

## Overview

Welcome to the Employee Shift Analyzer tool! This Python-based program is designed to automate the analysis of employee shift data from a CSV file, helping you identify specific patterns and conditions related to employee work schedules.

## Features

- **Consecutive Days Analysis:** Identify employees who have worked for 7 consecutive days.
- **Shift Gap Detection:** Recognize employees with less than 10 hours of break between shifts but greater than 1 hour.
- **Long Shift Alert:** Detect employees who have worked for more than 14 hours in a single shift.

## Getting Started

### Prerequisites

- Python 3
- Pandas library

### Installation

1. **Clone the repository:**

       ```bash
       git clone <repository_url>
       cd employee-shift-analyzer
  ### Install dependencies:
      ```bash
      pip install -r requirements.txt

  ## Usage
  
  1. **Place your CSV file:**
     - Ensure your CSV file containing employee shift data is located in the project directory.

  2. **Run the analyzer:**
     ```bash
     python analyze_file.py
  3. Review the detailed results generated in the output directory.

## Results
The program generates a comprehensive output file (output/output.txt) providing information about employees who meet specific conditions. The results include employee names, position IDs, and relevant shift details.

## Contributing
If you're interested in contributing to this project, please follow the guidelines outlined in CONTRIBUTING.md. We welcome your insights, suggestions, and improvements!

## License
This project is licensed under the MIT License.

Feel free to explore, use, and enhance the Employee Shift Analyzer tool. We appreciate your efforts and contributions to making this tool more valuable for analyzing employee work patterns.

