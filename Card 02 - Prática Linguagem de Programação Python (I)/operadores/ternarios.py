lockdown = False
grana = 30

# Se lockdown ser true ou grana menor que 100, em caso, se não uhuuu
status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu'

print(status)

# Outras linguagens: cond == true ? sim : não