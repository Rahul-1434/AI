class Solution:
	def is_possible_to_get_seats(n, m, seats):
		available_seats = 0
		for i in range(m):
			prev = seats[i - 1] if i != 0 else 0
			next = seats[i + 1] if i != m - 1 else 0
			if prev + next + seats[i] == 0:
				available_seats += 1
				if available_seats == n:
					return True
				i += 1
		return False
	    
n = 2
m = 7
seats = [0, 0, 1, 0, 0, 0, 1]
if Solution.is_possible_to_get_seats(n, m, seats):
	print("Yes")
else:
	print("No")
