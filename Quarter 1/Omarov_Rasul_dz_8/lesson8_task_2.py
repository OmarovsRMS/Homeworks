import re
match = re.compile(r'((?:\d{1,3}[.]){3}\d{1,3})[\s-]+(.+?[]]).+?"(.+?)\s*(/.+?)\s.+?\s(.+?)\s(.).+')

parse_list = ()
with open('nginx_logs.txt', 'r') as f:
    for line in f:
        match_string = match.findall(line)
        print(match_string)
