# WSPLIN
pytorch implementation of [Weakly Supervised Patch Label Inference Networks for Efficient Pavement Distress Detection and Recognition in the Wild](https://arxiv.org/abs/2203.16782)

For more details of this task, See [Pavement Distress Classification](https://github.com/DearCaat/Pavement-Distress-Classification).

## Usage
### Crack500-PDD

#### Train IOPLIN

```shell
# IOPLIN use the pretrained efficientnet_b3 weight to init the model
python3 main.py --data-path=$DATA_PATH --output=$OUTPUT_PATH --project=wsplin --cfg ../configs/crack500/crack500_effi_b3.yaml ../configs/crack500/crack500_ioplin.yaml --title=ioplin_crack500 --opts MODEL.BACKBONE_INIT $PRETRAINED_WEIGHT_PATH
```

#### Train STN

```shell
python3 main.py --data-path=$DATA_PATH --output=$OUTPUT_PATH --project=wsplin --cfg ../configs/crack500/crack500_effi_b3.yaml ../configs/stn_effi_b3.yaml --title=stn_crack500
# you can change the $STN_NAME to train different stn
# $STN_NAME = {stn_1_bn,stn_1,stn_2,stn_3}
python3 main.py --data-path=$DATA_PATH --output=$OUTPUT_PATH --project=wsplin --cfg ../configs/crack500/crack500_effi_b3.yaml ../configs/stn_effi_b3.yaml --title=stn_crack500 --opts MODEL.NAME $STN_NAME
```

#### Train Other Baselines

```shell
# you can change the config file to train different baselines
python3 main.py --data-path=$DATA_PATH --output=$OUTPUT_PATH --project=wsplin --cfg ../configs/crack500/crack500_effi_b3.yaml --title=effi_b3_crack500
```

#### Train WSPLIN-IP

```shell
# WSPLIN use the pretrained efficientnet_b3 weight to init the model
python3 main.py --data-path=$DATA_PATH --output=$OUTPUT_PATH --project=wsplin --cfg ../configs/crack500/crack500_effi_b3.yaml ../configs/crack500/crack500_wsplin.yaml --title=wsplin_ip_crack500 --opts MODEL.BACKBONE_INIT $PRETRAINED_WEIGHT_PATH
```

### CQU-BPDD

These examples are in the **I-DET** setting. For other settings, please change the config file.

#### Train IOPLIN

```shell
# IOPLIN use the pretrained efficientnet_b3 weight to init the model
python3 main.py --data-path=$DATA_PATH --output=$OUTPUT_PATH --project=wsplin --cfg ../configs/baseline/effi_b3_1det.yaml ../configs/ioplin.yaml --title=ioplin --opts MODEL.BACKBONE_INIT $PRETRAINED_WEIGHT_PATH
```

#### Train STN

```shell
python3 main.py --data-path=$DATA_PATH --output=$OUTPUT_PATH --project=wsplin --cfg ../configs/baseline/effi_b3_1det.yaml ../configs/stn_effi_b3.yaml --title=stn 
# you can change the $STN_NAME to train different stn
# $STN_NAME = {stn_1_bn,stn_1,stn_2,stn_3}
python3 main.py --data-path=$DATA_PATH --output=$OUTPUT_PATH --project=wsplin --cfg ../configs/baseline/effi_b3_1det.yaml ../configs/stn_effi_b3.yaml --title=stn --opts MODEL.NAME $STN_NAME
```

#### Train Other Baselines

```shell
# effi_b3
python3 main.py --data-path=$DATA_PATH --output=$OUTPUT_PATH --project=wsplin --cfg ../configs/baseline/effi_b3_1det.yaml --title=effi_b3 
# you can change the model name $MODEL_NAME_TIMM to train different baselines. the model name can be referd to timm repo
python3 main.py --data-path=$DATA_PATH --output=$OUTPUT_PATH --project=wsplin --cfg ../configs/baseline/effi_b3_1det.yaml --title=other_baseline --opts MODEL.NAME $MODEL_NAME_TIMM
```

#### Train WSPLIN-IP

```shell
# WSPLIN use the pretrained efficientnet_b3 weight to init the model
python3 main.py --data-path=$DATA_PATH --output=$OUTPUT_PATH --project=wsplin --cfg ../configs/baseline/effi_b3_1det.yaml ../configs/wsplin_1det.yaml --title=wsplin --opts MODEL.BACKBONE_INIT $PRETRAINED_WEIGHT_PATH
```

#### Train WSPLIN-SW

```shell
# WSPLIN use the pretrained efficientnet_b3 weight to init the model
python3 main.py --data-path=$DATA_PATH --output=$OUTPUT_PATH --project=wsplin --cfg ../configs/baseline/effi_b3_1det.yaml .../configs/wsplin_1det.yaml --title=wsplin --opts MODEL.BACKBONE_INIT $PRETRAINED_WEIGHT_PATH DATA.IS_IP False NUM_PATCHES 12
```

#### Train WSPLIN-SS

```shell
# WSPLIN use the pretrained efficientnet_b3 weight to init the model
python3 main.py --data-path=$DATA_PATH --output=$OUTPUT_PATH --project=wsplin --cfg ../configs/baseline/effi_b3_1det.yaml ../configs/wsplin_1det.yaml --title=wsplin --opts MODEL.BACKBONE_INIT $PRETRAINED_WEIGHT_PATH WSPLIN.SPARSE_RATIO 0.5
```
