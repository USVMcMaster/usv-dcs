import sys
import subprocess
import os

prog = r
#include<stdio.h>
int main(){
//My first Quora answer.
printf("Hello Quora! Is this Python code or C code?\n");
return 0;
}


if not os.path.exists('foo'):
    f = open('foo.c', 'w')
    f.write(prog)
    f.close()
    subprocess.call(["gcc", "foo.c", "-ofoo", "-std=c99", '-w', '-Ofast'])
subprocess.call(["./foo"], stdin = sys.stdin)
