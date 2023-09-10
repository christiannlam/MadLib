#Display MadLib paragraph
def madLib(adj,v1,name):
  madLib = f" Today was such a {adj} day.\n All I did today was {v1}.\n I guess {name} was right when they said,'Make every day and exciting day.'"
  return madLib

def main():
  #User gives words for madlib
  while True:
    adj = input("Adjective: ")
    verb = input("Verb: ")
    name = input("Name of a Celebrity: ")
    print(madLib(adj,verb,name))
    return False
    
if __name__ == "__main__":
  main()

  

