// Problem statement: https://leetcode.com/problems/asteroid-collision/description/
// Asteroid collision problem: Chalo DSA first round (solve using stack)

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> s; // Stack to simulate collisions
        for (int asteroid : asteroids) {
            bool destroyed = false; // Track if the current asteroid gets destroyed
            // Handle collision scenarios, it will only happen if top is + and current is - 
            // else they move in opposite directions, no collision
            while (!s.empty() && asteroid < 0 && s.top() > 0) {
                if (abs(asteroid) > s.top()) {
                    // Current asteroid destroys the top of the stack
                    s.pop();
                } else if (abs(asteroid) == s.top()) {
                    // Both asteroids are destroyed
                    s.pop();
                    destroyed = true;
                    break;
                } else {
                    // Current asteroid is destroyed
                    destroyed = true;
                    break;
                }
            }
            // Push the asteroid to the stack if it wasn't destroyed
            if (!destroyed) {
                s.push(asteroid);
            }
        }
        // Extract remaining asteroids from the stack
        vector<int> res;
        while (!s.empty()) {
            res.push_back(s.top());
            s.pop();
        }
        reverse(res.begin(), res.end()); // Reverse to get the correct order
        return res;
    }
};