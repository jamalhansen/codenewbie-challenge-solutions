# The challenge starts with a list of numbers, for this challenge let us say that the list starts with one and goes to 100.  Your solution will look at each number in this list and do one of the following.
#
#
#
# If the number is divisible by 3, output “Fizz”
#
# If the number is divisible by 5, output “Buzz”
#
# If the number is divisible by both 3 and 5, output “FizzBuzz”
#
# Otherwise, output the number

# Create a list from 1 to 100 and loop through it
(1..100).each do |i|

    # find when divisible by 3
    fizz = "fizz" if i % 3 == 0

    # find when divisible by 5
    buzz = "buzz" if i % 5 == 0

    if fizz || buzz then
        puts "#{fizz}#{buzz}"
    else
        puts i
    end
end
