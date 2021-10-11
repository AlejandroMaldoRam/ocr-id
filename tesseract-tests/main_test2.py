# Programa principal para pruebas con Tesseract y Pytesseract

import cv2
import pytesseract
import marker_utils as mu
import getopt
import sys

def parse_options(argv):
    """Parse the arguments of this program"""
    image_file = ''
    if len(argv) == 0:
        print("get_marker_pose.py -i <image>")
        sys.exit(2)
    try:
        opts, _ = getopt.getopt(argv, 'hi:', ['image='])
    except getopt.GetoptError:
        print("get_marker_pose.py -i <image>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("get_marker_pose.py -i <image>")
            sys.exit()
        elif opt in ("-i", "--image"):
            image_file = arg
    print("Image file: ", image_file)

    return image_file


def main1():
    # leemos imagen
    im = cv2.resize(cv2.imread("../images/codigo8.jpg"),dsize=None, fx=0.125, fy=0.125)
    print(im.shape)
    #im = cv2.imread("../images/prueba4.jpg")
    #cv2.imshow("Imagen", im)

    # Preprocesamos la imagen (Para un mejor funcionamiento se pueden realizar las siguientes operaciones: opening, closing, eroding, gray conversion, homographies)
    
    # Preprocesamiento
    # Aplicamos la detección de marcador
    corners, detected_markers, all_detected_markers, text_boxes = mu.detect_id_plates(im, min_area=100)
    print(corners)
    cv2.imshow("Marcador", detected_markers)
    cv2.imshow("Marcador", all_detected_markers)
    #cv2.imshow("Rectangulo", text_boxes[0])

    # Recorremos cada caja candidata con texto
    for i in range(len(text_boxes)):
        box = text_boxes[i]

        # Extraemos el texto identificado en cada caja
        box = mu.thresholding(box)
        #box = mu.remove_noise(box)
        #box = mu.opening(box)
        cv2.imshow("Caja_{}".format(i), box)
        output_text = pytesseract.image_to_string(box)
        print(output_text)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()