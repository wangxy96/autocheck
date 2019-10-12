#!/usr/bin/env python3
# *-* coding:utf8 *-*
# sky

from core import host, tomcat, redis, mysql
import os

def main():
    #host.info()
    tomcat.stats()
    redis.stats()
    mysql.stats()

    
if __name__ == "__main__":
    if os.path.exists("check.info"):
        os.remove("check.info")
    main()
