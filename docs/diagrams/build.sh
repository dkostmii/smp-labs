#!/bin/sh

java -jar $PUML_JAR **.pu -progress -checkmetadata -tpng -failfast
