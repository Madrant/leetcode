#include <iostream>
#include <assert.h>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        int i = 0;

        while (i < nums.size() - 1)
        {
            if (nums[i] + nums[i + 1] == target)
            {
                break;
            }
        }

        vector<int> v{i, i + 1};

        return v;
    }
};

int main(int argc, char **argv)
{
    cout << "Hello"  << endl;

    vector<int> test_set { 2, 7, 11, 15 };

    Solution s;
    auto result = s.twoSum(test_set, 9);

    auto it = result.begin();

    cout << "Results: " << result.size() << endl;

    while (it != result.end())
    {
        cout << *it << endl;
        it++;
    }

    assert(result[0] == 0);
    assert(result[1] == 1);
}
