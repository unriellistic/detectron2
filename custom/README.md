### Use the container

```
cd docker/
# Build:
docker build --build-arg USER_ID=1000 -t detectron2:v0 .
# Launch (require GPUs):
docker run --gpus all -it --shm-size 8gb --env "DISPLAY" --volume "C:\Users\HTX CBRNE\Documents\charles\detectron2\custom:/home/appuser/custom:" --name detectron2 detectron2:v0
```

### Demo script
Output folder must be created first.
- Instance Segmentation
    ```
    python demo.py --config-file ~/detectron2_repo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml --input car_damage_dataset/train/10.jpg --output demo_output --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl
    ```
- Object Detection
    ```
    python demo.py --config-file ~/detectron2_repo/configs/COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml --input car_damage_dataset/train/10.jpg --output demo_output --opts MODEL.WEIGHTS detectron2://COCO-Detection/faster_rcnn_R_50_FPN_3x/137849458/model_final_280758.pkl
    ```

### Custom dataset training
- Create your own config file. Inherit from one of the given ones and add an entry for `DATASETS.TRAIN` and `DATASETS.TEST`
- Modify train_net.py to set up the config for your custom dataset
```
./train_net.py --config-file config.yaml --num-gpus 1 SOLVER.IMS_PER_BATCH 2 SOLVER.BASE_LR 0.0025
```
- Evaluation:
```
./train_net.py --config-file config.yaml --eval-only MODEL.WEIGHTS output/model_final.pth
```

### Inferences using custom trained model
```
python demo.py --config-file config.yaml --input car_damage_dataset/val/*.jpg --output demo_output --opts MODEL.WEIGHTS output/model_final.pth
```