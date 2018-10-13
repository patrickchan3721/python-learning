#!/usr/bin/python

def checkip (ip):
   import re
   if re.match("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip):
      for octet in ip.split("."):
         if int(octet) > 255:
            print "This is invalid ip"
            return False
      print "This is valid ip"
      return True
   else:
      print "This is invalid ip"
      return False

print "Please enter IP: "
ip = raw_input() 
checkip(ip)
