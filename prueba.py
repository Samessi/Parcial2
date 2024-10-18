from prettytable import PrettyTable


Tabla = PrettyTable()

Tabla.field_names=["Nombre","Edad"]
Tabla.add_row(["Samuel",19])
Tabla.add_row(["Jona",20])
Tabla.add_row(["Messi",37])


Filas = [["Emilio",20],["Ronaldo",39]]
Tabla.add_rows(Filas)
Tabla.del_row(1)
Tabla.del_column("Edad")
print(Tabla)
