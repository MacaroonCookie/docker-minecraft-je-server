#!/bin/bash

if [ ! "${test}" ] ; then
    echo 'ERROR: No Minecraft JE version listed'
    exit 1
elif [[ "${MC_VERSION}" =~ ^b?1(\.[0-9]){1,2}$ ]] ; then

fi

function get_mc_version() {

}
