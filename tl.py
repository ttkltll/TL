import sys

from interpreter import evaluate
from myParser import parse
from scanner3 import scanTokens


def runFile(path):
    try:
        with open(path, 'rb') as file:
            code = file.read().decode('utf-8')
            run(code)

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def split_list_by_separator(original_list, delimiter=";"):
    # 存储子列表的结果
    result = []
    current_sublist = []

    # 遍历原始列表
    for item in original_list:
        if item.lexeme == delimiter:
            result.append(current_sublist)
            current_sublist = []
        else:
            current_sublist.append(item)

    # 添加最后一个子列表
    result.append(current_sublist)
    return result


def run(line):
    tokens = scanTokens(line)
    tokens_splited = split_list_by_separator(tokens)
    for statement_tokens in tokens_splited:
        expression = parse(statement_tokens)
        evaluate(expression)



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
        runFile(args[0])
    else:
        runPrompt()

if __name__ == "__main__":
    main()