import sys

from lark import Lark, Transformer, v_args


toml_parser = Lark.open('lark_grammar/toml.lark',parser='lalr', **kwargs)
parse = toml_parser.parse


def test():
    test_toml = '''
        #
    '''

    j = parse(test_toml)
    print(j)


if __name__ == '__main__':
    # test()
    with open(sys.argv[1]) as f:
        print(parse(f.read()))
