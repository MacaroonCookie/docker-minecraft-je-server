#!/bin/bash

if [ ! "${MCVERSION}" ] ; then
  echo "No Minecraft JE Server version provided"
  exit 1
fi

mc_prefix="/minecraft"
mc_file="${mc_prefix}/$(mcmeta --download-version ${MCVERSION} | cut -d' ' -f1)"
if [ $? -ne 0 ] || [ ! "${mc_file}" ] ; then
  echo "Minecraft JE Server version provided is invalid. Please visit https://mcversions.net for a list of valid versions"
  exit 1
fi

mc_url=$(mcmeta --download-version ${MCVERSION} | cut -d' ' -f2)

if [ ! -f "${mc_file}" ] ; then
  # Download MC JE Server
  curl -o "${mc_file}" "${mc_url}"
  if [ $? -ne 0 ] || [ ! -f "${mc_file}" ] ; then
    echo Minecraft JE Server failed to download
    exit 1
  fi

  echo "eula=true" > ${mc_prefix}/eula.txt
fi

cd $mc_prefix
java -server -Xmx2048M -Xms256M -XX:+UseG1GC -XX:+CMSIncrementalPacing -XX:+CMSClassUnloadingEnabled -XX:ParallelGCThreads=2 -XX:MinHeapFreeRatio=5 -XX:MaxHeapFreeRatio=10 -jar ${mc_file} nogui

echo Minecraft JE Server stopped
exit 0
