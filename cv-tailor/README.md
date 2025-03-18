# CV Tailor

CV Tailor is a Python application designed to help users customize their CVs according to specific job specifications. The application includes features for scraping job specifications, loading CVs from Google Docs, tailoring the CV using a locally hosted open-source language model, viewing changes as diffs, and saving the tailored CV in various formats.

## Features

1. **Job Specification Scraping**: Extract job specifications from a provided URL or PDF document.
2. **CV Loading**: Load CVs directly from Google Docs using document IDs.
3. **CV Tailoring**: Utilize an open-source language model to modify the CV based on the job specification.
4. **Diff Viewing**: Present changes between the original and tailored CVs in a Markdown format for easy review and editing.
5. **CV Saving**: Save the tailored CV as a PDF or update it in Google Docs.

## Project Structure

```
cv-tailor
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── scraper
│   │   ├── __init__.py
│   │   └── scraper.py
│   ├── cv_loader
│   │   ├── __init__.py
│   │   └── google_docs_loader.py
│   ├── tailor
│   │   ├── __init__.py
│   │   └── llm_tailor.py
│   ├── diff_viewer
│   │   ├── __init__.py
│   │   └── markdown_diff.py
│   ├── saver
│   │   ├── __init__.py
│   │   └── save_as.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/cv-tailor.git
   cd cv-tailor
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Follow the prompts to scrape a job specification, load your CV, tailor it, view the changes, and save the new version.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.