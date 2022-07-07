#!/bin/bash
python test.py \
--img 640 \
--conf 0.25 \
--data ./config/fall_down.yaml \
--weights ./weights/best.pt \
--source "http://admin:admin@192.168.0.113:8081/"