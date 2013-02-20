import subprocess
import os
import re
import time
def extract_url_from_html(f_name):
    n = open(f_name)
    s = n.read()
    m = re.findall('href=[^>]*pdf', s)
    for w in set(m):
        '''
        if "help" not in w:
            return w
        '''
        yield w
#extract_url_from_html("title1.php?offset=10")


def extract_delhi_hc():
    offset = 360
    while offset < 500:
        bashCommand = 'wget http://lobis.nic.in/dhc/title1.php?offset=%s --header Cookie:PHPSESSID=t1mpajp0f0c0h3tk37uvl7qdq5'%offset
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]

        for url in extract_url_from_html("title1.php?offset=%s"%offset):
            bashCommand = 'wget http://lobis.nic.in%s --header Cookie:PHPSESSID=t1mpajp0f0c0h3tk37uvl7qdq5'% url[6:]
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output = process.communicate()[0]
            tok = url[6:].split('/')
            '''
            bash_comm = 'pdftotext %s' % tok.pop()
            process = subprocess.Popen(bash_comm.split(), stdout=subprocess.PIPE)
            output = process.communicate()[0]
            '''
        offset = offset + 10
        time.sleep(5)

extract_delhi_hc()

def run():
    f = open('test')
    line = f.readline()
    for line in f:
        bashCommand = 'wget http://164.100.9.38%s --header Cookie:JSESSIONID=E0CCF9F835812D869B820082155518E0' % line.strip()
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        tok = line.strip().split('/')
        f = tok.pop()
        pdf = extract_url_from_html(f)
        bashCommand = 'wget http://164.100.9.38%s --header Cookie:JSESSIONID=E0CCF9F835812D869B820082155518E0' % pdf[6:]
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        tok = pdf[6:].split('/')
        bash_comm = 'pdftotext %s' % tok.pop()
        process = subprocess.Popen(bash_comm.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]


