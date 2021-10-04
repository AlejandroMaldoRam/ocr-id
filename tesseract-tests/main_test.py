# Programa principal para pruebas con Tesseract y Pytesseract

import cv2
import pytesseract

# TODO: Necesitamos hacer letreros de pruebas que combinen marcadores que podamos encontrar con qr-recognizer y que nos sirvan para
# aplicar la homografía necesaria para mejorar la detección de texto con Tesseract. 

def main1():
    # leemos imagen
    im = cv2.imread("../images/placa1.jpg")
    cv2.imshow("Imagen", im)

    # Preprocesamos la imagen (Para un mejor funcionamiento se pueden realizar las siguientes operaciones: opening, closing, eroding, gray conversion, homographies)
    
    # Conversión a escala de grises
    im_g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Imagen Gris", im_g)
    
    # Aplicación de Tesseract para extraer texto
    output_text = pytesseract.image_to_string(im_g, lang='eng+spa')
    print(output_text)

    # Generamos rectángulos donde encontro texto
    output_info = pytesseract.image_to_data(im_g)
    print(output_info)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    print("Pruebas")
    main1()