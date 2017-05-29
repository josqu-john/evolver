#!/usr/bin/python
import os
import time

log_txt = "Unkown"
def make_log(ex_name, f = log_txt):
    date = give_date()
    file_name = '%s' % (date)
    file_location = 'log/%s' % (file_name)
    touch('log/%s' % (file_name))
    set_file(open(file_location, 'a'))
    write_('/<--- BEGIN LOG AT %s: --->' % (date))

def set_file(var):
    global log_txt
    log_txt = var
def give_file():
    return log_txt
def write_only(var):
    global log_txt
    log_txt.write('\n')
    log_txt.write('%s: %s' % (give_time(), var))
def show(var):
    print var
def write_(var):
    write_only(var)
    show(var)
def close_log():
    global log_txt
    write_('>--- END LOG AT %s: ---</' % (give_date()))
    log_txt.close()

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def give_date():
    date = time.strftime("%c")
    return date
def give_time():
    t = time.strftime("%X")
    return t
