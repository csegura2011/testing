#!/usr/bin/python2

import argparse
import cslSSHTools


def main(arg):
    print "Inside main() function"
    #cslSSHTools.remote_exec('localhost', 'csl', 'kaned2345', 'echo $HOSTNAME')
    print arg

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='cslSSH usage example')
    parser.add_argument('-host', action="ssh_hostname", Required=True)
    main(parser.host)




# References
# https://docs.python.org/2/howto/argparse.html
# https://pymotw.com/2/argparse/