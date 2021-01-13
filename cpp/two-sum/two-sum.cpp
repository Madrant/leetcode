#include <iostream>
#include <assert.h>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        vector<int> result;

        auto first = nums.begin();

        // Take first number
        while (first != nums.end())
        {
            auto second = first;

            // Check it with each second
            while (second++ != nums.end())
            {
                if (*first + *second == target)
                {
                    result.push_back(distance(nums.begin(), first));
                    result.push_back(distance(nums.begin(), second));

                    return result;
                }
            }

            first++;
        }

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

    cout << "Target: " << target << " ";
    print_vector("Data: ", test_set);

    Solution s;
    auto result = s.twoSum(test_set, target);

    print_vector("Result: ", result);

    bool solution_correct = result_is_correct(result, answer);

    cout << ": " << (solution_correct ? "Correct" : "Incorrect") << endl;

    return solution_correct;
}

int main(int argc, char **argv)
{
    // Leetcode test cases:
    run_test({2, 7, 11, 15}, 9, {0, 1});
    run_test({3, 2, 4}, 6, {1, 2});
    run_test({3, 3}, 6, {0, 1});

    // Additional test cases:
    run_test({3, 2, 3}, 6, {0, 2});
    run_test({1, 2, 3, 4, 5}, 10, {});
}
