def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def count_batteries_by_health(present_capacities):  
  battery = {
    "invalid_entry": 0, 
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  for capacity in present_capacities:
    #if string input is float, convert to float
    if(str(type(capacity)) == "<class 'str'>"):
        if(isfloat(capacity)): capacity = float(capacity)
    #proceed only if input is string
    if(str(type(capacity)) == "<class 'int'>" or str(type(capacity)) == "<class 'float'>"):
        p = int(100*float(capacity))/120
        if(p > 100 or p < 0): battery["invalid_entry"] += 1 #battery percentage > 100% or <0%
        elif(p > 80): battery["healthy"] += 1 #battery percentage > 80% and <= 100%
        elif(p > 62): battery["exchange"] += 1 #battery percentage > 62% and <= 80%
        elif(p >= 0): battery["failed"] += 1 #battery percentage >= 0% and <= 62%
    else: battery["invalid_entry"] += 1 #entry not a float
  return battery


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [150, 180, 119, 113, 101.5, 97, 96.5, 96,80, 75, 74.4, 51, -9, -17, 'o', ['a','e','i','o','u'], '110', '130.5', '20.22', '80']
  #above 120, below 0 and non float values are invalid entries
  #96 - 120 (80% - 100%) are healthy entries (including str entries in this range)
  #74.4 to 95.9999... (62% - 80%) are exchange entries (including str entries in this range)
  #0 to 74.3999... (0% - 62%) are failed entries (including str entries in this range)
  counts = count_batteries_by_health(present_capacities)
  assert(counts["invalid_entry"] == 7)
  assert(counts["healthy"] == 6)
  assert(counts["exchange"] == 4)
  assert(counts["failed"] == 3)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
