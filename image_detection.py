from imageai.Detection import ObjectDetection
import os

execution_path_input = os.path.abspath("./temp")
execution_path_output = os.path.abspath("./temp_output")
execution_path_model = os.path.abspath("./models")
print(execution_path_model)

input_file_path = [os.path.join(execution_path_input, file) for file in os.listdir(execution_path_input)]
print(input_file_path)
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path_model , "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=input_file_path[0], output_image_path=os.path.join( execution_path_output , "imagenew.jpg"), minimum_percentage_probability=30)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")
