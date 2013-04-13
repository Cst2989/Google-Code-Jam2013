Google-Code-Jam2013
===================

My solutions to Google's Code Chalange

Here are the problems : 

1)Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.

After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning positions.

Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:

"X won" (the game is over, and X won)
"O won" (the game is over, and O won)
"Draw" (the game is over, and it ended in a draw)
"Game has not completed" (the game is not over yet)
If there are empty cells, and the game is not over, you should output "Game has not completed", even if the outcome of the game is inevitable.
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of 4 lines with 4 characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an empty line.

Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of the statuses given above. Make sure to get the statuses exactly right. When you run your code on the sample input, it should create the sample output exactly, including the "Case #1: ", the capital letter "O" rather than the number "0", and so on.

Limits

The game board provided will represent a valid state that was reached through play of the game Tic-Tac-Toe-Tomek as described above.

Small dataset

1 = T = 10.

Large dataset

1 = T = 1000.

2)Problem

Alice and Bob have a lawn in front of their house, shaped like an N metre by M metre rectangle. Each year, they try to cut the lawn in some interesting pattern. They used to do their cutting with shears, which was very time-consuming; but now they have a new automatic lawnmower with multiple settings, and they want to try it out.

The new lawnmower has a height setting - you can set it to any height h between 1 and 100 millimetres, and it will cut all the grass higher than h it encounters to height h. You run it by entering the lawn at any part of the edge of the lawn; then the lawnmower goes in a straight line, perpendicular to the edge of the lawn it entered, cutting grass in a swath 1m wide, until it exits the lawn on the other side. The lawnmower's height can be set only when it is not on the lawn.

Alice and Bob have a number of various patterns of grass that they could have on their lawn. For each of those, they want to know whether it's possible to cut the grass into this pattern with their new lawnmower. Each pattern is described by specifying the height of the grass on each 1m x 1m square of the lawn.

The grass is initially 100mm high on the whole lawn.

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing two integers: N and M. Next follow N lines, with the ith line containing M integers ai,j each, the number ai,j describing the desired height of the grass in the jth square of the ith row.

Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is either the word "YES" if it's possible to get the x-th pattern using the lawnmower, or "NO", if it's impossible (quotes for clarity only).

Limits

1 = T = 100.

Small dataset

1 = N, M = 10.
1 = ai,j = 2.
Large dataset

1 = N, M = 100.
1 = ai,j = 100.


3)Little John likes palindromes, and thinks them to be fair (which is a fancy word for nice). A palindrome is just an integer that reads the same backwards and forwards - so 6, 11 and 121 are all palindromes, while 10, 12, 223 and 2244 are not (even though 010=10, we don't consider leading zeroes when determining whether a number is a palindrome).

He recently became interested in squares as well, and formed the definition of a fair and square number - it is a number that is a palindrome and the square of a palindrome at the same time. For instance, 1, 9 and 121 are fair and square (being palindromes and squares, respectively, of 1, 3 and 11), while 16, 22 and 676 are not fair and square: 16 is not a palindrome, 22 is not a square, and while 676 is a palindrome and a square number, it is the square of 26, which is not a palindrome.

Now he wants to search for bigger fair and square numbers. Your task is, given an interval Little John is searching through, to tell him how many fair and square numbers are there in the interval, so he knows when he has found them all.

Solving this problem

Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has 1 Small input and 2 Large inputs. Once you have solved the Small input, you will be able to download any of the two Large inputs. As usual, you will be able to retry the Small input (with a time penalty), while you will get only one chance at each of the Large inputs.

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line contains two integers, A and B - the endpoints of the interval Little John is looking at.

Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of fair and square numbers greater than or equal to A and smaller than or equal to B.

Limits

Small dataset

1 ≤ T ≤ 100.
1 ≤ A ≤ B ≤ 1000.

First large dataset

1 ≤ T ≤ 10000.
1 ≤ A ≤ B ≤ 1014.

Second large dataset

1 ≤ T ≤ 1000.
1 ≤ A ≤ B ≤ 10100.
   





