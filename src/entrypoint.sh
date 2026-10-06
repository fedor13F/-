#!/bin/bash
set -e

if [ ! -d /tmp/hadoop-root/dfs/name/current ]; then
  echo ">>> Formatting NameNode..."
  hdfs namenode -format -force -nonInteractive
fi

service ssh start

echo ">>> Starting HDFS..."
start-dfs.sh

echo ">>> Starting YARN..."
start-yarn.sh

echo ">>> Hadoop is up. Web UIs:"
echo "    NameNode:  http://localhost:9870"
echo "    YARN:      http://localhost:8088"

tail -f $HADOOP_HOME/logs/*.log
