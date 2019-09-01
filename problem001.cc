// 2019-08-25
//
// Given a list of numbers and a number k, return whether any two numbers from
// the list add up to k.
// 
// For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is
// 17.
// 
// Bonus: Can you do this in one pass?

#include <assert.h>
#include <unordered_set>
#include <vector>

bool has_sum(const std::vector<int> &nums, const int sum)
{
    for (size_t i = 0; i < nums.size() - 1; i++)
    {
        for (size_t j = i + 1; j < nums.size(); j++)
        {
            if (nums[i] + nums[j] == sum) return true;
        }
    }
    return false;
}

bool has_sum_one_pass(const std::vector<int> &nums, const int sum)
{
    std::unordered_set<int> candidates;
    for (const auto &n : nums)
    {
        if (candidates.count(n)) return true;
        candidates.insert(sum - n);
    }
    return false;
}

int main()
{
    std::vector<int> nums = {10, 15, 3, 7};
    assert(has_sum(nums, 17));
    assert(has_sum_one_pass(nums, 17));

    return 0;
}
