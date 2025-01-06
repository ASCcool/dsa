#include <bits/stdc++.h>
using namespace std;

# This code also takes care of cases where numbers are repeated in the array, returns unique top k

int main()
{
    vector<int> arr = {1, 2, 3, 4, 6, 5, 5, 5, 6, 1, 3};
    int k = 3;
    priority_queue<int, vector<int>, greater<int>> pq;
    unordered_set<int> st;
    for(int x : arr){
        if(st.find(x) == st.end()){
	        pq.push(x);
	        st.insert(x);
        }
	    if(pq.size() > k){
		    pq.pop();
	    }
    }
    while(!pq.empty()){
        cout<<pq.top()<<" ";
        pq.pop();
    }
    return 0;
}