import re
import sys

def main(inpath, outpath):
    tmp = []
    with open(inpath, "r", encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            schema = None
            # 过滤协议
            if '://' in line:
                schema = line.split('://')[0]
                line = line.split('://')[1]
            # 过滤参数
            if '?' in line:
                line = line.split('?')[0]
            # 判断是否存在目录，存在的话递归处理
            while '/' in line:
                if line.endswith('/'):
                    line = line[:-1]
                    continue
                else:
                    if '.' not in line.split('/')[-1]:
                        if schema:
                            tmp.append(f'{schema}://{line.strip()}\n')
                    line = '/'.join(line.split('/')[:-1])

    tmp = list(set(tmp))
    tmp.sort()
    with open(outpath, "w", encoding="utf-8") as fp:
        fp.writelines(tmp)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f'使用格式：python main.py in.txt out.txt')
        exit(-1)

    main(sys.argv[1], sys.argv[2])