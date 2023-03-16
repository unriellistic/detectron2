### Demo script
- Instance Segmentation
    ```
    python ../demo/demo.py --config-file ../configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml --input image1.jpg image2.jpg image3.jpg --output outputs --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl
    ```
- Object Detection
    ```
    python ../demo/demo.py --config-file ../configs/COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml --input image1.jpg image2.jpg image3.jpg --output outputs --opts MODEL.WEIGHTS detectron2://COCO-Detection/faster_rcnn_R_50_FPN_3x/137849458/model_final_280758.pkl
    ```

### Custom dataset training
- Create your own config file. Inherit from one of the given ones and add an entry for `DATASETS.TRAIN` and `DATASETS.TEST`
- Modify train_net.py to set up the config for your custom dataset
```
./train_net.py --config-file config.yaml --num-gpus 1 SOLVER.IMS_PER_BATCH 2 SOLVER.BASE_LR 0.0025
```