# coding:utf8
import sys

import easyquotation

if sys.version_info[:2] < (3, 5):
    raise Exception('Python版本需要3.5或以上, 请升级Python.')


def main():
    quotation = easyquotation.use('sina')
    data = quotation.real('162411')
    print(data)


if __name__ == '__main__':
    main()
