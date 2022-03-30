from collections import Counter
parse_list = []
with open('nginx_logs.txt', 'r') as f:
    for line in f:
        ip_address = line.split()[0]
        parse_list.append(ip_address)


count_dict = Counter(parse_list)
print(count_dict)

