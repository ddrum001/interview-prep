# program to count the inversions in a text file i n*log(n) time
# using the merge-sort algorithm

# create an empty array to hold the unsorted elements from the file
unsorted = []

# open the file, read each line, and push to the array
f = File.open("IntegerArray.txt", "r")
#f = File.open("test.txt", "r")
f.each_line do |line|
	unsorted.push(line.to_i)
end
f.close	#close the array

# the algorithm works by using the divide and conquer method to
# split the array into log(n) sub-arrays and recursively solve those
# the critical part of the algorithm occurs when the sorted sub-arrays
# are merged together using the fact that the minimum must be the first
# entry of either of the sub-arrays, requiring only linear comparisons
#
# to find the inversions we use the fact that the sorted sub-array have
# no internal inversions so the inversion will be found in the merge step.
# In particular, when the first entry of the right sub-array is less than
# the first entry of the left sub-array then it must be less than all the
# remainging entries of the first sub-array, which are inversions that can
# be easily counted.

# we start by defining our recursive function merge_and_count
# which takes in two sorted sub-arrays and returns one sorted array
# the counting is done by adding to a global variable

$count = 0

# the merge and count function works by comparing the first entries from
# the sub-arrays L and R and pushing the smaller entry, counting the
# inversion when the smaller entry belongs to R

# the base case is when one of the sub-arrays has size 0, in which case the
# non-zero sub-array is returned

# the comparisons will be done by iterating thru each array with iterators
# l and r, which both start at 0.  We push the smaller of left[l] and right[r]
# to the array sorted.  If it is from left we simply increment l.  If it is
# from right we increment r and add (left.size - l) to count to account for the 
# inversions.  If either l or r reaches the end of their sub-array,
# indexed at size, the other arrays first entry will be pushed until
# both l and r are at size

def merge_and_count(arr)
#   puts "merge called"
    return arr if arr.size == 1 # checks base case
    cut = arr.size / 2   # cuts roughly in half
    left = merge_and_count(arr[0..cut-1]) # recursive call to sort left sub-array
    right = merge_and_count(arr[cut..-1]) # recursive call to sort right sub-array
	sorted = [] # create an empty array to place the sorted entries in
	l=0	# iterator for left
	r=0	# iterator for right
	while l < left.size or r < right.size
		if l == left.size
			sorted.push(right[r])
#			puts "#{right[r]} pushed"
			r += 1
		elsif r == right.size
            sorted.push(left[l])
#            puts "#{left[l]} pushed"
            l += 1
        elsif left[l] < right[r]
            sorted.push(left[l])
#            puts "#{left[l]} pushed"
            l += 1
        else
            sorted.push(right[r])
#            puts "#{right[r]} pushed"
            r += 1
            $count += left.size - l
        end
#		puts "l=#{l}, r=#{r}, count=#{$count}"
#		puts sorted
#		puts "sub-array sorted"	
	end
	return sorted
end

# test case of [2, 3, 6, 7, 1, 4, 5, 8] with 8 inversions
# (2,1) (3,1) (6,1) (7,1) (2,4) (3,4) (6,4) (7,4)
#test_left = [2, 3, 6, 7]
#test_right = [1, 4, 5, 8]

#test_array = [3, 2, 6, 7, 4, 1, 5, 8]

#merge_and_count([5,4,3,2,1])
merge_and_count(unsorted)
puts "Final count = #{$count}"
