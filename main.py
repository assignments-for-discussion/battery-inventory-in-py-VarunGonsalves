def count_batteries_by_health(present_capacities):  
  battery = {
    "invalid": 0, 
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  for i in present_capacities:
    p = int(100*float(i))/120
    if(p > 100 or p < 0): battery["invalid"] += 1
    elif(p > 80): battery["healthy"] += 1
    elif(p > 62): battery["exchange"] += 1
    else: battery["failed"] += 1
  return battery


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [150, 180, 119, 113, 101.5, 97, 96.5, 96,80, 75, 74.4, 51, -9, -17]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["invalid"] == 4)
  assert(counts["healthy"] == 5)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 2)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
