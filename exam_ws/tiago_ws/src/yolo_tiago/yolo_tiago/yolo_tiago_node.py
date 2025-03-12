import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point  # Usiamo Point per inviare le coordinate
from cv_bridge import CvBridge
import cv2
import torch

class YOLONode(Node):
    def __init__(self):
        super().__init__('yolo_node')
        self.subscription = self.create_subscription(
            Image,
            '/head_front_camera/rgb/image_raw',  # Topic dell'immagine della camera
            self.image_callback,
            10)
        self.bridge = CvBridge()
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Carica il modello YOLOv5

        # Publisher per le coordinate del centro della bounding box del truck
        self.bbox_center_publisher = self.create_publisher(Point, '/truck_bounding_box_center', 10)

    def image_callback(self, msg):
        # Converti l'immagine ROS in formato OpenCV
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Esegui YOLO sull'immagine
        results = self.model(cv_image)

        # Trova la bounding box del truck
        truck_box = None
        truck_label = None

        for *box, conf, cls in results.xyxy[0]:
            class_id = int(cls)
            class_name = self.model.names[class_id]  # Ottieni il nome della classe

            if class_name == "truck":  # Filtra solo i truck
                x_min, y_min, x_max, y_max = map(int, box)
                truck_box = (x_min, y_min, x_max, y_max)
                truck_label = class_name
                break  # Prendi solo il primo truck rilevato

        if truck_box:
            x_min, y_min, x_max, y_max = truck_box
            center_x = (x_min + x_max) // 2
            center_y = (y_min + y_max) // 2

            # Pubblica le coordinate del centro come un messaggio Point
            bbox_center_msg = Point()
            bbox_center_msg.x = float(center_x)
            bbox_center_msg.y = float(center_y)
            bbox_center_msg.z = 0.0  # Non usato
            self.bbox_center_publisher.publish(bbox_center_msg)

            # Disegna la bounding box del truck con un bordo più spesso
            cv2.rectangle(cv_image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 4)

            # Aggiungi un'ombra alla bounding box
            shadow_offset = 5
            cv2.rectangle(cv_image, (x_min + shadow_offset, y_min + shadow_offset), 
                          (x_max + shadow_offset, y_max + shadow_offset), (0, 0, 0), 4)

            # Disegna il puntino al centro della bounding box
            cv2.circle(cv_image, (center_x, center_y), 8, (0, 0, 255), -1)  # Cerchio rosso

            # Aggiungi l'etichetta della classe con sfondo
            label = f"{truck_label} ({center_x}, {center_y})"
            (label_width, label_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv2.rectangle(cv_image, (x_min, y_min - label_height - 10), 
                          (x_min + label_width, y_min - 10), (0, 255, 0), -1)
            cv2.putText(cv_image, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            # Disegna una linea tratteggiata per il centro
            cv2.line(cv_image, (center_x, y_min), (center_x, y_max), (0, 0, 255), 2, cv2.LINE_AA)
            cv2.line(cv_image, (x_min, center_y), (x_max, center_y), (0, 0, 255), 2, cv2.LINE_AA)

        # Visualizza l'immagine con la bounding box del truck, il puntino e l'etichetta
        cv2.imshow('YOLO', cv_image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    yolo_node = YOLONode()
    rclpy.spin(yolo_node)
    yolo_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
