def number(lines):
    return [''.join(str(i+1))+f": {lines[i]}" if len(lines) > 1 else lines for i in range(len(lines))]
