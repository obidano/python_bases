menus = ['RDC', "Cameroun", "Gabon"]

"""
i=1
for m in menus:
    print(f"{i}. {m}")
    i=i+1
"""

"""
for i, m in enumerate(menus):
    print(f"{i+1}. {m}")
"""
affichage=""
for i, m in enumerate(menus):
    a=f"{i+1}. {m}\n"
    affichage+=a
print(affichage)