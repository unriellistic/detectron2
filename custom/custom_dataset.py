from detectron2.data.datasets import register_coco_instances
from detectron2.data import MetadataCatalog

register_coco_instances("car_damage_train", {}, "car_damage_dataset/train/COCO_mul_train_annos.json", "car_damage_dataset/train")
register_coco_instances("car_damage_val", {}, "car_damage_dataset/val/COCO_mul_val_annos.json", "car_damage_dataset/val")

MetadataCatalog.get("car_damage_train").thing_classes = ["headlamp", "rear_bumper", "door", "hood", "front_bumper"]
MetadataCatalog.get("car_damage_val").thing_classes = ["headlamp", "rear_bumper", "door", "hood", "front_bumper"]