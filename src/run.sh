#!/bin/bash


#vp -m dcx "$@" --pre-bash "docker restart edge; sleep 20" --remote-edge
vp -m dcx "$@" --remote-firefox
