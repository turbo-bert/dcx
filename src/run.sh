#!/bin/bash


#vp -m dcx "$@" --pre-bash "docker restart edge; sleep 20" --remote-edge

vp -m dcx "$@"

#vp -m dcx "$@" --log --unzip-profile testprofile1.zip
