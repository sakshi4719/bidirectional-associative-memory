# Bidirectional Associative Memory (BAM) Implementation

**Bidirectional Associative Memory (BAM)** is a neural network with two layers, where each layer is connected to the other. It stores associations between input-output pairs, allowing pattern recall in both directions.
BAM's weight matrix is symmetric, facilitating the retrieval of the associated output when given an input and vice versa.

- The code calculates weights (`w1`, `w2`) by taking dot products between input arrays (`input1`, `input2`) and target arrays (`target1`, `target2`).
- The weight matrix `w` is the sum of `w1` and `w2`.
- The weighted sum (`y_in`) is computed using a dot product, and the `signum` function applies a step function to determine the output (`y`).
- The `tester1` function checks if the output matches `target1`, verifying the BAM's performance.

This implementation shows how BAM can retrieve patterns in both directions: input-to-output and output-to-input.
