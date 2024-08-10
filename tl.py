import sys

from scanner import scanTokens

had_error = False

def runFile():
    print('file')
    pass


def run(line):
    tokens = scanTokens(line)
    print(tokens)


def runPrompt():
    global had_error
    while True:
        try:
            line = input("> ")
            if line == "":  # 模拟EOF的效果
                break
            run(line)  # 调用run函数处理输入
            had_error = False
        except EOFError:
            break
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    """
    这个方法主要实现：根据参数的长度决定是用文件还是从命令行输入
    :return:
    """
    args = sys.argv[1:]
    if len(args)>1:
        print("usage:python ")
    elif len(args)==1:
        runFile()
    else:
        runPrompt()

if __name__ == "__main__":
    main()