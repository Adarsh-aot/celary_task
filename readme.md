# PDF to JSON Data Extraction using Donut Transformer

This project demonstrates how to process PDF files by splitting them into pages, extracting data using a transformer model (Donut Transformer), and saving the extracted data as JSON files in the same directory as the original PDFs.

## Features

- Split PDF files into individual pages (PNG images).
- Extract data from each page using a transformer model (e.g., Donut Transformer).
- Save extracted data in JSON format alongside the original PDF files.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Adarsh-aot/quipo-oscar.git
```
```bash
cd pdf-to-json
```


Install the required Python packages:
```bash 
pip install -r requirements.txt
```

Run code 

```bash
python main.py
```


Usage
Running the PDF to JSON Conversion
Place your PDF files in the pdf_files directory.
Run the pdf_to_json.py script to process the PDF files:
bash
Copy code
python pdf_to_json.py
Output
For each input PDF file (example.pdf), the script will:
Split the PDF into individual pages (PNG images) stored in the output_images directory.
Use the Donut Transformer model to extract data from each page and save the extracted data as example_page1.json, example_page2.json, etc. in the output_json directory.
Configuration
Customize the configuration settings (e.g., model parameters, output directories) in config.py before running the script.
Requirements
Python 3.x
Donut Transformer model (pre-trained or custom)

License
This project is licensed under the MIT License - see the LICENSE file for details.



- **Project Overview:** The README provides an overview of the project, explaining its purpose and key features related to PDF processing and data extraction using a transformer model.
  
- **Installation:** Instructions for cloning the repository and installing the required Python packages using pip.

- **Usage:** Detailed instructions on how to run the `pdf_to_json.py` script to process PDF files and convert them into JSON format. It includes information about input/output directories and running the script.

- **Configuration:** Guidance on customizing configuration settings (e.g., model parameters, output directories) in the `config.py` file.

- **Requirements:** List of software requirements and dependencies needed to run the project, including Python version and Donut Transformer model.

- **Directory Structure:** Description of the directory structure used in the project, including directories for input PDF files, output PNG images, output JSON files, and main script files.

- **Contributing:** Encouragement for contributions from the community, with instructions on how to submit issues or pull requests on GitHub.

- **License:** Information about the project's license (in this case, the MIT License) for users and contributors.

You can customize this README.md template by replacing placeholders (e.g., `yourusernam