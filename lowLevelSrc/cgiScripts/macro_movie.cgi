#!/bin/bash
irsend SEND_ONCE TV KEY_CHANNELUP
sleep 0.5
irsend SEND_ONCE TV KEY_SOURCE
sleep 0.5
irsend SEND_ONCE TV KEY_DOWN
sleep 0.3
irsend SEND_ONCE TV KEY_DOWN
sleep 0.3
irsend SEND_ONCE TV KEY_DOWN
sleep 0.5
irsend SEND_ONCE TV KEY_ENTER
sleep 0.5
irsend SEND_ONCE STERIO KEY_POWER
sleep 0.5
irsend SEND_ONCE STERIO KEY_RECEIVER_TV_SOUND

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
