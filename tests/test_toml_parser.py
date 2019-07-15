import sys

from lark import Lark, Transformer, v_args


toml_parser = Lark.open('../lark_grammar/test.lark',parser='lalr')
parse = toml_parser.parse


def test():
    test_toml = '''#'''

    j = parse(test_toml)
    print(j)


test()
