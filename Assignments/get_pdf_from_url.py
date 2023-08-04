import os
import requests

def download_pdf_from_url(url, output_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, "wb") as file:
            file.write(response.content)
        print(f"PDF downloaded successfully and saved to {output_path}")
    else:
        print("Failed to download the PDF.")

def main():
    url = "https://example.com/sample.pdf"  # Replace with the URL of the PDF you want to download
    output_path = "downloaded_pdf.pdf"

    download_pdf_from_url(url, output_path)

if __name__ == "__main__":
    main()
