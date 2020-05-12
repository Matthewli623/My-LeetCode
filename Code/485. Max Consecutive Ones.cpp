class Solution
{
public:
    int findMaxConsecutiveOnes(vector<int> &nums)
    {
        int outsum = 0;
        int innersum = 0;
        if (nums.size() == 0)
            return 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == 1)
            {
                innersum++;
                if (innersum > outsum)
                    outsum = innersum;
            }
            if (nums[i] == 0)
            {
                innersum = 0;
            }
        }
        return outsum;
    }
};