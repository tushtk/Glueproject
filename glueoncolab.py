# most of this code is NOT made by me, it's only an updated version from this Gist: https://gist.github.com/yahwang/c41b2558372c386a6b9d3fe0c701f335
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-common/apache-maven-3.6.0-bin.tar.gz
!tar xvf apache-maven-3.6.0-bin.tar.gz -C /bin/ > /dev/null
!wget -q https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-3.0/spark-3.1.1-amzn-0-bin-3.2.1-amzn-3.tgz
!tar xvf spark-3.1.1-amzn-0-bin-3.2.1-amzn-3.tgz -C /bin/ > /dev/null
!pip install -q findspark

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["PATH"] += ":/bin/apache-maven-3.6.0/bin"
os.environ["SPARK_HOME"] = "/bin/spark-3.1.1-amzn-0-bin-3.2.1-amzn-3"
os.environ["SPARK_CONF_DIR"] = "/bin/aws-glue-libs/conf"

!git clone -b glue-3.0 https://github.com/awslabs/aws-glue-libs.git /bin/aws-glue-libs
!chmod +x /bin/aws-glue-libs/bin/glue-setup.sh
!bash /bin/aws-glue-libs/bin/glue-setup.sh > /dev/null
!cp -r /bin/spark-3.1.1-amzn-0-bin-3.2.1-amzn-3/jars/netty-all-4.1.51.Final.jar /bin/aws-glue-libs/jarsv1/


import sys
sys.path.extend(["/bin/spark-3.1.1-amzn-0-bin-3.2.1-amzn-3/python","/bin/spark-3.1.1-amzn-0-bin-3.2.1-amzn-3/python/lib/py4j-0.10.9-src.zip","/bin/aws-glue-libs/PyGlue.zip"])

import findspark   # this step is very important to make sure that the language is set to pyspark and not python
findspark.init()


from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session


df = spark.createDataFrame([{"hello": "world"} ,{"my dear": "wrong number"},{"Joe": "Black"} ]) #--for x in range(1000)])
dyf_test = DynamicFrame.fromDF(df, glueContext, 'dyf_test')
dyf_test.toDF().show()
