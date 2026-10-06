FROM eclipse-temurin:8-jdk-jammy

ENV HADOOP_VERSION=3.3.6
ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
ENV JAVA_HOME=/opt/java/openjdk

RUN apt-get update && apt-get install -y \
    ssh rsync python3 python3-pip curl wget vim net-tools \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir mrjob

COPY hadoop-3.3.6.tar.gz /tmp/
RUN tar -xzf /tmp/hadoop-3.3.6.tar.gz -C /opt \
    && mv /opt/hadoop-3.3.6 $HADOOP_HOME \
    && rm /tmp/hadoop-3.3.6.tar.gz

# SSH без пароля (Hadoop требует для запуска демонов)
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa \
    && cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
    && chmod 0600 ~/.ssh/authorized_keys

COPY core-site.xml $HADOOP_CONF_DIR/core-site.xml
COPY hdfs-site.xml $HADOOP_CONF_DIR/hdfs-site.xml
COPY mapred-site.xml $HADOOP_CONF_DIR/mapred-site.xml
COPY yarn-site.xml $HADOOP_CONF_DIR/yarn-site.xml
COPY hadoop-env.sh $HADOOP_CONF_DIR/hadoop-env.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 9870 8088 9000
ENTRYPOINT ["/entrypoint.sh"]