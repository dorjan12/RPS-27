def vnos(s:list):
  while True:
    izdelek = input("Vnesi: ").lower()
    if izdelek == "":
      break
    s.append(izdelek)
def izpis(s:list):
  print("----------------")
  for index in range(len(s)):
    print(f"({index}) {s[index]}")
    
def briši(s:list):
  briši = input("Briši: ").lower()
  while briši in s:
    s.remove(briši)
    print("*", end="")
print()
    
def posodobi(s:list):
  stara = input("Posodobi":).lower()
  nova = input("Novo":).lower()
  for index in range(len(s)):
    if stara == s[index]:
        s[index] = nova

if __name__=="__main__":
  s = []
  vnos(s)
  izpis(s)
  briši(s)
  izpis(s)
  posodobi(s)
  izpis(db)




