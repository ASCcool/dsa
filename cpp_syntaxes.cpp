#include <iostream> // for cout etc
#include <string> // for string
#include <cctype> // for tolower and isalnum
#include <algorithm> // for sort

/********** STRING **********/

// Use of isalnum and tolower
string filtered;
for (char c : s) {
    if (isalnum(c)) {  // Keep only alphanumeric characters
        filtered += tolower(c);  // Convert to lowercase
    }
}

// Length of string
int len = s.length()

// Substring: Extract substring from index <start> of length <length>
string sub = s.substr(start, length);

// Find a Substring
int pos = s.find(substring);
if (pos != string::npos) {
    cout << "Substring found at index: " << pos;
}

// Erase substring from index <start> of length <length>: s.erase(index, length);
string s = "abcdef";
s.erase(2, 3);  // s = "abf"

// Insert character or substring
string s = "abcdef";
s.insert(3, "XYZ");  // s = "abcXYZdef"

// Replace substring: s.replace(start, length, "new_substring");
string s = "abcdef";
s.replace(2, 3, "XYZ");  // s = "abXYZf"

// Count occurances of a character
int count = count(s.begin(), s.end(), 'a');

/********** VECTOR **********/

// Declaration
vector<vector<int>> v2d;
vector<int> nums = {5, 2, 9, 1, 5, 6};

// Size of vector
int size = nums.size();

//********** 1. Adding Elements **********//

// push_back(value): Adds an element to the end of the vector.
vector<int> v;
v.push_back(10);  // v = {10}

// emplace_back(value): Constructs and adds an element at the end of the vector in place (avoids copying).
v.emplace_back(20);  // v = {10, 20}

//********** 2. Removing Elements **********//

// pop_back(): Removes the last element of the vector.
v.pop_back();  // Removes 20, v = {10}

// erase(iterator): Removes an element at a specific position.
v.erase(v.begin());  // Removes the first element, v = {}

// erase(iterator, iterator): Removes elements in a range.
v = {1, 2, 3, 4};
v.erase(v.begin(), v.begin() + 2);  // Removes 1 and 2, v = {3, 4}

// clear(): Removes all elements from the vector.
v.clear();  // v = {}

//********** 3. Accessing Elements **********//

// operator[] or at(index): Access elements by index. at(index) performs bounds checking; operator[] does not.
v[0];      // Access first element
v.at(0);   // Access first element with bounds checking

// front() and back(): ********** Access the first and last elements of the vector.  
v.front();  // First element
v.back();   // Last element

//********** 4. Capacity and Size **********//

// empty(): Checks if the vector is empty.
if (v.empty()) "Empty!";

// capacity(): Returns the current capacity of the vector.
v.capacity();

// reserve(n): Reserves capacity for at least n elements, minimizing reallocations during push_back.
v.reserve(10);  // Reserve space for 10 elements

// resize(n): Changes the size of the vector. If the new size is greater, new elements are default-initialized.
v.resize(5);  // v = {10, 0, 0, 0, 0}

//********** 5. Iterators **********//

// begin() and end(): Returns iterators to the start and end of the vector.
for (auto it = v.begin(); it != v.end(); ++it) {
    *it;
}

// rbegin() and rend(): Returns reverse iterators (iterate from end to start).
for (auto it = v.rbegin(); it != v.rend(); ++it) {
    *it;
}

//********** 6. Searching and Sorting **********//

// find (with std::find): Find an element in the vector.
auto it = find(v.begin(), v.end(), 3);
if (it != v.end()) "Found!";

// sort (with std::sort): Sort the vector in ascending order. 
sort(v.begin(), v.end());

// Descending order
sort(nums.begin(), nums.end(), greater<int>()); 

// reverse (with std::reverse): Reverse the elements of the vector.
reverse(v.begin(), v.end());

//********** 7. Modifying Elements **********//

// assign(n, value): Assigns n elements of value to the vector.
v.assign(5, 10);  // v = {10, 10, 10, 10, 10}

// insert(iterator, value): Inserts value at the specified position.
v.insert(v.begin(), 15);  // v = {15, 10, 10, 10, 10, 10}

// insert(iterator, n, value): Inserts n copies of value at the specified position.
v.insert(v.begin(), 3, 20);  // v = {20, 20, 20, 15, 10, ...}

//********** 8. Swapping **********//

// swap(): Swaps the contents of two vectors.
vector<int> v1 = {1, 2, 3}, v2 = {4, 5, 6};
v1.swap(v2);  // v1 = {4, 5, 6}, v2 = {1, 2, 3}

//********** 9. Copying **********//

// Copy Constructor: Create a copy of a vector.
vector<int> v1 = {1, 2, 3};
vector<int> v2(v1);  // v2 = {1, 2, 3}

/********** SET **********/

unordered_set<int> visited;

// Insert in a set
visited.insert(top->left->val)

// Find element in a set
visited.find(top->left->val) != visited.end()

// Count occurances of element in a set
visited.count(key)

/********** MAP **********/

// Almost works same as set commands
unordered_map<TreeNode*, TreeNode*> parentMap;

/********** QUEUE **********/

queue<TreeNode*> q;

// size
q.size()

// front
q.front() -> int

// pop
q.pop() -> NULL

// push
q.push(value)

// empty check
q.empty()

/********** STACK **********/

stack<TreeNode*> s;

// size
s.size()

// top
s.top() -> int

// pop
s.pop() -> NULL

// push
s.push(value)

// empty check
s.empty()