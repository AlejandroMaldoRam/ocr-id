# Introduction

Programs that use Tesseract OCR for identifying plates or tags on warehouses.

# Requeriments

- Install Tesseract for the corresponding OS.
- Create a conda environment with pytesseract.

# References

- PyTesseract[https://pypi.org/project/pytesseract/]

# Usage

get_id_from_plate.py -i <image> -s <reduction factor>

* image: "Image address"
* reduction factor: Scale for changing size of the image, fo example, s = 0.25 will reduce image 4 times.