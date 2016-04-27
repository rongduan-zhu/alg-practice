#!/usr/bin/env python

# https://code.google.com/codejam/contest/32001/dashboard

OR = 0
CHANGABLE = 1
IMPOSSIBLE = 5000

def main():
  tests = input()

  for test in xrange(tests):
    nodes_count, desired = map(int, raw_input().split(' '))
    nodes = []
    dp = [0] * ((nodes_count - 1) / 2)
    nodes_val = [0] * nodes_count

    for i in xrange(nodes_count):
      nodes.append(map(int, raw_input().split(' ')))

    for i in xrange((nodes_count - 1) / 2, nodes_count):
      nodes_val[i] = nodes[i][0]
      dp.append(0 if nodes[i][0] == desired else IMPOSSIBLE)

    for i in xrange((nodes_count - 1) / 2 - 1, -1, -1):
      if desired == 1:
        dp[i] = desire_1(
          nodes,
          nodes_val,
          dp,
          i,
          2 * (i + 1) - 1,
          2 * (i + 1),
          nodes[i][1] == CHANGABLE
        )
      else:
        dp[i] = desire_0(
          nodes,
          nodes_val,
          dp,
          i,
          2 * (i + 1) - 1,
          2 * (i + 1),
          nodes[i][1] == CHANGABLE
        )

      nodes_val[i] = desired if dp[i] < IMPOSSIBLE else desired ^ 1

    print 'CASE #{}: {}'.format(test + 1, dp[0] if dp[0] < IMPOSSIBLE else 'IMPOSSIBLE')

def desire_1(nodes, nodes_val, dp, p, lc, rc, changable):
  if get_val(nodes_val, lc, rc, nodes[p][0]):
    if nodes[p][0] == OR:
      return min(dp[lc], dp[rc])
    elif changable:
      return min(dp[lc] + dp[rc], 1 + min(dp[lc], dp[rc]))
    else:
      return dp[lc] + dp[rc]
  elif nodes[p][0] != OR and changable and nodes_val[lc] | nodes_val[rc]:
    return 1 + min(dp[lc], dp[rc])
  return IMPOSSIBLE

def desire_0(nodes, nodes_val, dp, p, lc, rc, changable):
  if get_val(nodes_val, lc, rc, nodes[p][0]) == 0:
    if nodes[p][0] != OR:
      return min(dp[lc], dp[rc])
    elif changable:
      return min(dp[lc] + dp[rc], 1 + min(dp[lc], dp[rc]))
    else:
      return dp[lc] + dp[rc]
  elif nodes[p][0] == OR and changable and nodes_val[lc] & nodes_val[rc] == 0:
    return 1 + min(dp[lc], dp[rc])
  return IMPOSSIBLE

def get_val(nodes_val, l, r, op):
  if op == OR:
    return nodes_val[l] | nodes_val[r]
  else:
    return nodes_val[l] & nodes_val[r]

if __name__ == '__main__':
  main()
