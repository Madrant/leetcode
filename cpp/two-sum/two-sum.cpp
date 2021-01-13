#include <iostream>
#include <assert.h>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        assert(nums.size() >= 2);

        int i = 0;

        while (i < nums.size() - 1)
        {
            if (nums[i] + nums[i + 1] == target)
            {
                break;
            }

            i++;
        }

        vector<int> result{i, i + 1};

        return result;
    }
};

void print_vector(string prefix, vector<int>& v, bool noendl = true)
{
    auto it = v.begin();

    cout << prefix << "size: " << v.size() << ": [";

    while (it != v.end())
    {
        cout << *it;
        it++;

        if (it != v.end())
        {
            cout << ", ";
        }
    }

    cout << "] ";

    if (!noendl)
    {
        cout << endl;
    }
}

inline bool result_is_correct(vector<int>& result, vector<int>& answer)
{
    return result == answer;
}

bool run_test(vector<int> test_set, int target, vector<int> answer)
{
    assert(test_set.size() >= 2);

    Solution s;
    auto result = s.twoSum(test_set, target);

    cout << "Target: " << target << " ";
    print_vector("Data: ", test_set);
    print_vector("Result: ", result);

    bool solution_correct = result_is_correct(result, answer);

    cout << ": " << (solution_correct ? "Correct" : "Incorrect") << endl;

    return solution_correct;
}

int main(int argc, char **argv)
{
    run_test({2, 7, 11, 15}, 9, {0, 1});
    run_test({3, 2, 4}, 6, {1, 2});
    run_test({3, 3}, 6, {0, 1});
}
