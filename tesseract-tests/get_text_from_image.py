# Programa principal para pruebas con Tesseract y Pytesseract

import cv2
import pytesseract
import marker_utils as mu
import getopt
import sys

# TODO: Train Tesseract with our own data (https://towardsdatascience.com/simple-ocr-with-tesseract-a4341e4564b6)

# Other configuration options
#custom_config = r'--oem 1 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#output_text = pytesseract.image_to_string(box, config=custom_config)

def parse_options(argv):
    """Parse the arguments of this program"""
    image_file = ''
    size_reduction = 1
    if len(argv) == 0:
        print("get_text_from_image.py -i <image> -s <reduction factor>")
        sys.exit(2)
    try:
        opts, _ = getopt.getopt(argv, 'his:', ['image=', 'size='])
    except getopt.GetoptError:
        print("get_text_from_image.py -i <image> -s <reduction factor>")
        sys.exit(2)
    #print(opts)
    for opt, arg in opts:
        #print(opt)
        if opt == '-h':
            print("get_text_from_image.py -i <image> -s <reduction factor>")
            sys.exit()
        elif opt in ("-i", "--image"):
            image_file = arg 
        elif opt in ("-s", '--size'):
            size_reduction = float(arg)
    #print("Image file: ", image_file)

    return image_file, size_reduction


def main():
    # Read image
    im_address, fs = parse_options(sys.argv[1:])
    print("Image: ", im_address)
    print("Resizing factor: ", fs)
    im = cv2.resize(cv2.imread(im_address),dsize=None, fx=fs, fy=fs)
    print(im.shape)
    
    # Detección de texto
    texts = []
    boxes = []
    confidences = []
    output_info = pytesseract.image_to_data(im)
    print(output_info)
    for line in output_info.split('\n')[1:]:
        features = line.split('\t')
        if len(features)==12:
            #print(features)
            texts.append(features[11])
            confidences.append(features[10])
            boxes.append([features[6], features[7], features[8], features[9]]) 
    #print(output_info)
    print(texts)
    print(confidences)
    print(boxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()