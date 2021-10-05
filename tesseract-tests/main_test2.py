# Programa principal para pruebas con Tesseract y Pytesseract

import cv2
import pytesseract
import marker_utils as mu

# TODO: Necesitamos hacer letreros de pruebas que combinen marcadores que podamos encontrar con qr-recognizer y que nos sirvan para
# aplicar la homografía necesaria para mejorar la detección de texto con Tesseract. 

def main1():
    # leemos imagen
    im = cv2.resize(cv2.imread("../images/codigo5.jpg"),dsize=None, fx=0.125, fy=0.125)
    #im = cv2.imread("../images/prueba4.jpg")
    cv2.imshow("Imagen", im)

    # Preprocesamos la imagen (Para un mejor funcionamiento se pueden realizar las siguientes operaciones: opening, closing, eroding, gray conversion, homographies)
    
    # Preprocesamiento
    # Aplicamos la detección de marcador
    corners, detected_markers, text_boxes = mu.detect_rectangles(im)
    print(corners)
    cv2.imshow("Marcador", detected_markers)
    #cv2.imshow("Rectangulo", text_boxes[0])
    im_g = text_boxes[0]
    im_g = mu.thresholding(im_g)
    im_g = mu.remove_noise(im_g)
    im_g = mu.opening(im_g)
    cv2.imshow("Preprocesada", im_g)
    
    # Aplicación de Tesseract para extraer texto
    #output_text = pytesseract.image_to_string(im_g)
    #custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    custom_config = r'--oem 3 --psm 6'
    output_text = pytesseract.image_to_string(im_g, config=custom_config)
    print(output_text)

    # Generamos rectángulos donde encontro texto
    #output_info = pytesseract.image_to_data(im_g)
    #print(output_info)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    print("Pruebas")
    main1()