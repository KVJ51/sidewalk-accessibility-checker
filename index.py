import json
import os

def convert_coco_to_yolo(json_path, images_folder, output_folder, classes):
    with open(json_path, 'r') as f:
        data = json.load(f)

    for image in data['images']:
        image_id = image['id']
        filename = image['file_name']
        width, height = image['width'], image['height']

        annotations = [ann for ann in data['annotations'] if ann['image_id'] == image_id]

        label_file = os.path.join(output_folder, filename.replace('.jpg', '.txt'))
        with open(label_file, 'w') as f:
            for ann in annotations:
                category_id = ann['category_id']
                bbox = ann['bbox']  # COCO format: [x_min, y_min, width, height]

                # Convert to YOLO format
                x_center = (bbox[0] + bbox[2] / 2) / width
                y_center = (bbox[1] + bbox[3] / 2) / height
                bbox_width = bbox[2] / width
                bbox_height = bbox[3] / height

                f.write(f"{category_id} {x_center} {y_center} {bbox_width} {bbox_height}\n")

# Define paths
json_path = "path/to/mapillary_annotations.json"
images_folder = "path/to/images"
output_folder = "path/to/labels"

# Define class names
classes = ["pedestrian", "bicycle", "vehicle", "sidewalk obstruction", "ramp"]

# Convert dataset
convert_coco_to_yolo(json_path, images_folder, output_folder, classes)
