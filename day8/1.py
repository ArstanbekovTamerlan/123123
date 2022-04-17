import re
arraychik = open('input1.txt', 'r')
file = open('output1.txt', 'w+')
cod = 0
pamyat = 0
a = 0
def memory(string):
    mem = string[1:-1]
    mem = mem.replace("\\\\", "x")
    mem = mem.replace("\\\"", "x")
    mem, _  = re.subn('\\\\x..', 'x', mem)
    return len(mem)
def esc(string):
    escaped = string
    escaped = escaped.replace("\\", "\\\\")
    escaped = escaped.replace('"', '\\"')
    escaped = '"' + escaped + '"'
    return len(escaped)
for line in arraychik:
    chars = len(line)
    mem = memory(line)
    escaped = esc(line)
    cod += len(line)
    pamyat += memory(line)
    a += escaped
file.write(str(cod - pamyat))
file.close()