#!/bin/bash
mkdir -p models &&
python download.py 1REga1z1rKezQtBebIZ86_iNR-mxum-KB models/models.tar.gz &&
tar -xvzf models/* &&
rm models/models.tar.gz &&
mkdir -p images/content &&
mkdir -p images/style &&
mkdir -p samples