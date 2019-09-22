import sys
import time
import random

def tik(bacot):
    for meizu in bacot + '\n':
        sys.stdout.write(meizu)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)

map(tik, ['Assalamualaikum Wr.Wb','semangat pagi teman teman',
          'semoga hari anda menyenangkan','`','jangan di salah gunakan',
          'untuk Hal jahat atau berniat Semena mena',
          'mari kita Bangun Video Chanel','====> Edi Garsell <====',
          'bersama karena kebersamaan adalah kunci dari','kesuksesan',
          '`','Note :','jangan di recode BANGSAT',
          'dan jangan di jual belikan','Terima Kasih... !!'])
