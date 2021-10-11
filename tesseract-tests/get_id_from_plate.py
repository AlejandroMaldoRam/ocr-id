# Programa principal para pruebas con Tesseract y Pytesseract

import cv2
import pytesseract
import marker_utils as mu
import getopt
import sys

# TODO: Train Tesseract with our own data (https://towardsdatascience.com/simple-ocr-with-tesseract-a4341e4564b6)
# TODO: Reeimprimir etiquetas con bordes más grandes y contrastantes

def parse_options(argv):
    """Parse the arguments of this program"""
    image_file = ''
    size_reduction = 1
    if len(argv) == 0:
        print("get_id_from_plate.py -i <image> -s <reduction factor>")
        sys.exit(2)
    try:
        opts, _ = getopt.getopt(argv, 'his:', ['image=', 'size='])
    except getopt.GetoptError:
        print("get_id_from_plate.py -i <image> -s <reduction factor>")
        sys.exit(2)
    #print(opts)
    for opt, arg in opts:
        #print(opt)
        if opt == '-h':
            print("get_id_from_plate.py -i <image>")
            sys.exit()
        elif opt in ("-i", "--image"):
            image_file = arg 
        elif opt in ("-s", '--size'):
            size_reduction = float(arg)
    #print("Image file: ", image_file)

    return image_file, size_reduction


def main():
    # leemos imagen
    im_address, fs = parse_options(sys.argv[1:])
    print("Imagen: ", im_address)
    print("Reducción: ", fs)
    im = im = cv2.resize(cv2.imread(im_address),dsize=None, fx=fs, fy=fs)
    print(im.shape)
    
    # Preprocesamiento
    # Aplicamos la detección de marcador
    corners, detected_markers, text_boxes = mu.detect_id_plates(im, min_area=100, min_error_poly=20)
    #print(corners)
    cv2.imshow("Marcador final", detected_markers)
    #cv2.imshow("Rectangulo", text_boxes[0])

    # Recorremos cada caja candidata con texto
    ids = []
    for i in range(len(text_boxes)):
        box = text_boxes[i]

        # Extraemos el texto identificado en cada caja
        box = mu.thresholding(box)
        box = mu.remove_noise(box)
        box = mu.opening(box)
        cv2.imshow("Caja_{}".format(i), box)
        custom_config = r'--oem 1 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        output_text = pytesseract.image_to_string(box, config=custom_config)

        # TODO: Aplicar búsqueda por Regex para dicernir entre patrones
        print(output_text)
        ids.append(output_text.replace("\n\x0c", ''))
    print(ids)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()