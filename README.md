Concept: Huffman encoding uses a bottom-up approach to build a binary tree based on symbol frequencies, i.e., we keep on
combining the letters instead of dividing them.
Algorithm Steps:
Combine Lowest Frequencies: Pair the two symbols with the lowest frequencies and combine them into a new node.
Repeat: Continue combining the lowest frequency nodes until only one node (the root) remains.
Generate Codes: Assign ’0’ to left edges and ’1’ to right edges as you traverse the tree from the root.
Efficiency and Accuracy: This coding gives a very high efficiency as compared to using ASCII codes or defining custom
fixed-length codes. Also note that there can be no ambiguity while decoding a binary string since we read the string, go step
by step (left or right according to 0 or 1) through the tree, until we strike a character. And then we go back to the top and
continue reading the binary string.# Huffman-Encoding
