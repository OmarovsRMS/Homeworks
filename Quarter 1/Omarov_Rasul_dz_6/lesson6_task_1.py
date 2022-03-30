parse_list = []
with open('nginx_logs.txt', 'r') as f:
    for line in f:
        ip_address = line.split()[0]
        send_method = line.split()[5].lstrip('"')
        content = line.split()[6]
        my_turple = (ip_address, send_method, content)
        parse_list.append(my_turple)

print(parse_list)
