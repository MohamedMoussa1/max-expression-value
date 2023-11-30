# Max-Expression-Value Algorithm

This document outlines the implementation of an algorithm by Roozbeh Yadollahi and Mohamed Moussa designed to find the maximum value of a given expression using dynamic programming. The expression follows a specific format as described below.

## Expression Format

The expression is structured in the following form:


Where:
- `ai` represents a number.
- `bi` represents an operator, which can be either `+` (plus) or `-` (minus).

## Algorithm Overview

The primary goal of this algorithm is to compute the maximum possible value of the expression by appropriately combining the numbers (`ai`) with the given operators (`bi`). The use of dynamic programming is crucial in optimizing the computation, especially for longer expressions. This approach helps in breaking down the problem into smaller sub-problems and storing their results to avoid redundant calculations.

## Implementation Details

- **Dynamic Programming Approach**: The algorithm stores the results of sub-expressions in a table, facilitating efficient computation of larger expressions by reusing these precomputed values.
- **Handling Operators**: Special attention is given to the way plus and minus operators are handled to ensure that the maximum possible value is achieved.
- **Optimization Techniques**: Various optimization techniques are employed to minimize the time and space complexity of the algorithm.

## Example

Consider the expression `3+2-4+5`. The algorithm will evaluate this expression in different combinations using dynamic programming to find the maximum value that can be obtained, which in this case would be `6`.

## Conclusion

The max-expression-value algorithm effectively finds the maximum value of a given expression with numbers and plus/minus operators, leveraging the power of dynamic programming for optimized performance.
