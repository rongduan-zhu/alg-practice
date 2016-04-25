#!/usr/bin/env python

# https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493

def main():
  nums = map(int, raw_input().split(','))
  longest = [(1, 0) for i in xrange(len(nums))]

  longest[0] = (1, 0)

  for i in xrange(1, len(nums)):
    current_longest = 0

    for j in xrange(0, i):
      diff = nums[i] - nums[j]

      if diff > 0 and longest[j][1] <= 0 or diff < 0 and longest[j][1] >= 0:
        if longest[j][0] + 1 > longest[i][0]:
          longest[i] = (longest[j][0] + 1, diff)

  print max(map(lambda x: x[0], longest))

if __name__ == '__main__':
  main()
