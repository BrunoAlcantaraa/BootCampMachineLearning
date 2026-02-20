lockdown = False
grana = 30

status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu'

print(status)

# Outras linguagens: cond == true ? sim : não