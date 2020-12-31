#include<deque>
class RecentCounter {
    deque <int> req;
public:
    RecentCounter() {
        // init stuff
        req = {};
    }

    int ping(int t) {
        req.push_back(t); // Adding Current request
        while (req.front() < t-3000) req.pop_front(); // Removing all req that does not fall in range
        return req.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
