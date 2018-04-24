donors = [('Donor A', [50, 100, 25, 100]),
          ('Donor B', [100, 25]),
          ('Donor C', [300])
          ]

def totaldonations(donations):
    return donations[1]

def report():
    report = []
    for (donor, amounts) in donors:
        report.append((donor, sum(amounts), len(amounts), sum(amounts)/len(amounts)))
    report.sort(key = totaldonations, reverse = True)
    print('Donor Name',' '*10, '|  Total Given  |', ' Num Gifts ', '|  Average Gift  |')
    print('-'*70)
    for (donor, total, num, avg) in report:
        print(donor, ' '*(21 - len(str(donor))), #print donor
              '$', ' '*(12 - len(str(total))), total, #print sum
              ' '*(12 - len(str(num))), num, #print num
              ' $', ' '*(12 - len(str(avg))), avg, #print avg
             )
