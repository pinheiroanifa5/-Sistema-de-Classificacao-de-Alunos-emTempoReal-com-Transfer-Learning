import cv2

video = cv2.VideoCapture(0)

# classificador Haar Cascade para detecção de rostos
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Detecta rostos no frame
    faces = faceDetect.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)

    # Desenha retângulos e linhas ao redor dos rostos detectados
    for x, y, w, h in faces:
        x1, y1 = x + w, y + h

        # Desenha o retângulo em volta do rosto
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)

        # Desenha linhas nos lados do retângulo
        cv2.line(frame, (x, y), (x, y + 30), (255, 0, 255), 6)    # left
        cv2.line(frame, (x, y), (x + 30, y), (255, 0, 255), 6)    # top-left

        cv2.line(frame, (x1, y), (x1 - 30, y), (255, 0, 255), 6)  # right
        cv2.line(frame, (x1, y), (x1, y + 30), (255, 0, 255), 6)  # top-right

        cv2.line(frame, (x, y1), (x, y1 - 30), (255, 0, 255), 6)  # bottom-left
        cv2.line(frame, (x, y1), (x + 30, y1), (255, 0, 255), 6)  # bottom

        cv2.line(frame, (x1, y1), (x1 - 30, y1),
                 (255, 0, 255), 6)  # bottom-right
        cv2.line(frame, (x1, y1), (x1, y1 - 30),
                 (255, 0, 255), 6)  # right-bottom

    # Exibe o frame com as detecções
    cv2.imshow("Frame", frame)

    # Aguarda pela tecla 'q' para sair do loop
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

# Libera os recursos da câmera e fecha todas as janelas abertas
video.release()
cv2.destroyAllWindows()
