#let me know if any mistakes # 75days <br>
from pypdf import PdfMerger

def merge_pdfs(input_files, output_filename):

  merger = PdfMerger()

  for file in input_files:
    merger.append(file)

  merger.write(output_filename)
  merger.close()

# Example usage:
input_files = ["21.pdf", "22.pdf"] # enter you Pdf name want to Merge
output_filename = "merged.pdf"     # enter your Merged PDF name (desired name)
merge_pdfs(input_files, output_filename)
