def count_batteries_by_health(present_capacities):  
  battery = {
    "invalid_entry": 0, 
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  for i in present_capacities:
    if(str(type(i)) == "<class 'int'>" or str(type(i)) == "<class 'float'>"):
        p = int(100*float(i))/120
        if(p > 100 or p < 0): battery["invalid_entry"] += 1
        elif(p > 80): battery["healthy"] += 1
        elif(p > 62): battery["exchange"] += 1
        elif(p >= 0): battery["failed"] += 1
    else: battery["invalid_entry"] += 1
  return battery


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [150, 180, 119, 113, 101.5, 97, 96.5, 96,80, 75, 74.4, 51, -9, -17, 'o', ['a','e','i','o','u']]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["invalid_entry"] == 6)
  assert(counts["healthy"] == 5)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 2)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
