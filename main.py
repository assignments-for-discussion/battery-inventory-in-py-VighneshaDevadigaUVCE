
def count_batteries_by_usage(cycles):
  low_batteries_count=0
  medium_batteries_count=0
  high_batteries_count=0
  
  for i in cycles:
    if i<=0: #Base case
      continue
    elif i<410:
      low_batteries_count+=1
    elif i>=410 and i<950:
      medium_batteries_count+=1
    else:
      high_batteries_count+=1
  return {
    "lowCount": low_batteries_count,
    "mediumCount": medium_batteries_count,
    "highCount": high_batteries_count
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
