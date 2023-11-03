
def count_batteries_by_health(present_capacities):  
  battery = {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  for i in present_capacities:
    p = 100*int(i)/120
    if(p >= 80): battery["healthy"] += 1
    elif(p >= 62): battery["exchange"] += 1
    else: battery["failed"] += 1
  return battery


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
