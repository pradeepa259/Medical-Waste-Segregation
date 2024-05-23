from pyzbar.pyzbar import decode
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def get_QR_Data(ip_frame):
    try:
        return decode(ip_frame)
    except:
        return []

def draw_poly(INframe, QRobj):
    if len(QRobj) == 0:
        return INframe
    else:
        for obj in QRobj:
            text = obj.data.decode('utf-8')
            pts = obj.polygon
            pts = np.array([pts], np.int32)
            pts = pts.reshape((4,1,2))
            print("Decoded Output:", text)
            cv2.polylines(INframe, [pts], True, (255,55,5), 2)
            cv2.putText(INframe, text, (50,50), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,200,1), 2)
            return INframe

while True:
    _, frame = cap.read()

    QRobj = get_QR_Data(frame)
    frame = draw_poly(frame, QRobj)

    cv2.imshow("QR", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()