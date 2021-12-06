a= {
    'Ari' : '081267888',
    'Dina' : '087677776'
}
print("Kontak Ari : ",a['Ari'])
print("Kontak Dina Sebelum Diganti: ", a['Dina'])
a['Riko'] = '087654544'
print(a)
a['Dina'] = '088999776'
print("Kontak Dina Sesudah ganti, ",a['Dina'])
print(a.keys())
print(a.values())
print(a)
del a['Dina']
print(a)

