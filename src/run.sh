#!/bin/bash

# Данные
docker cp ~/Desktop/TAD2/log_2.txt hadoop-lab:/tmp/log_2.txt
docker exec hadoop-lab hdfs dfs -mkdir -p /home/input
docker exec hadoop-lab hdfs dfs -put -f /tmp/log_2.txt /home/input/
docker exec hadoop-lab hdfs dfs -ls -h /home/input/

# Скрипты
docker exec hadoop-lab mkdir -p /root/scripts
docker cp ~/Desktop/TAD2/scripts/. hadoop-lab:/root/scripts/
docker exec hadoop-lab sh -c "rm -f /root/scripts/.DS_Store"
docker exec hadoop-lab sh -c "chmod +x /root/scripts/*.py && ls -la /root/scripts/ && head -1 /root/scripts/mapper1.py"