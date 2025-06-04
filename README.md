# Rayyan Decision Resolution Script

This repository contains a Python script to identify **true disagreements** between individual reviewer votes and final decisions made by a designated reviewer in a Rayyan systematic review export.

## Purpose

In our systematic review, we resolved conflicting inclusion/exclusion decisions through final arbitration by one reviewer (Opeyemi). To support transparency and reproducibility, we developed this script to:

- Extract all reviewer votes from the Rayyan export `notes` column
- Compare each reviewer’s vote to Opeyemi’s final decision
- Output only **true disagreements** — where both Opeyemi and the reviewer have voted, and their decisions differ

Each reviewer receives a CSV file listing only the articles they need to revisit and update in Rayyan.

## What it does

- Parses the `notes` column of a Rayyan CSV export
- Extracts decisions from Opeyemi and other reviewers (e.g. Fabian, Lauren, Jackeline, Oshani)
- Filters for rows where both Opeyemi **and** the reviewer voted, and their decisions differ
- Outputs one file per reviewer with:
  - Rayyan article ID (`key`)
  - Title, year, journal, authors, abstract
  - Opeyemi’s decision
  - Reviewer’s decision

## How to use

1. Place your Rayyan export file (CSV) in your working directory.
2. Ensure your terminal is in the same directory.
3. Run the script:

```bash
python generate_reviewer_disagreements.py
```

You will receive separate CSV files for each reviewer with true disagreements.

## Customisation

To use this script with your own Rayyan review, adjust the following:

### CSV filename  
Change the filename in the script from `Conflicts_YemiVotes_04062025.csv` to your own export file name.

### Reviewer names  
Update the list of reviewers in the script to match the names used in the `notes` column of your CSV. For example:

```python
reviewers = ['Opeyemi', 'Reviewer1', 'Reviewer2']
```

### Working directory  
Run the script from the same folder where your CSV file is stored, or adjust the file path in the script accordingly.

💡 **Note:** Reviewer names must match exactly (including capitalization and spelling) with how they appear in the `notes` column.

## Requirements

- Python 3.8 or higher  
- `pandas` library

Install the required library using:

```bash
pip install pandas
```

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this code with attribution.

## Citation (Optional)

If you use or adapt this script in a published review or project, please consider citing:

```bibtex
@misc{hookham2025rayyan,
  author = {Hookham, Lauren},
  title = {Rayyan Decision Resolution Script},
  year = {2025},
  howpublished = {\url{https://github.com/lafhlafh/rayyan-decision-resolution}},
  note = {Version 1.0}
}
```

## Author

Lauren Hookham  
lauren.hookham@ouh.nhs.uk

## Project Links (Optional)

- GitHub: [https://github.com/lafhlafh/rayyan-decision-resolution](https://github.com/lafhlafh/rayyan-decision-resolution)
- OSF Project: [https://osf.io/ae7v4/] (https://osf.io/ae7v4/)
