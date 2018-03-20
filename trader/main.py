# coding:utf8
import sys

if sys.version_info[:2] < (3, 6):
    raise Exception('Python版本需要3.5或以上, 请升级Python.')

def main():
    print("hello world.")


if __name__ == '__main__':
    main()
