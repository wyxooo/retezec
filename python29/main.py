jmeno = " Vojtěch"
prijmeni = " Dokoupil"
celek = jmeno + prijmeni
print (celek)
print (len(celek))
print (celek.upper())
print (celek.lower())
print (celek.count("o"))


print (celek.index("o"))
print (celek.index("o", 1))
print (celek.lstrip())
print (celek.rstrip())
print (celek.strip())
print (celek.replace('o', 'f'))
print (celek.startswith('p'))
print (celek.endswith('l'))
print ('{0} !!!'.format(celek))

