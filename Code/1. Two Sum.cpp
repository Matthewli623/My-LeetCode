class Solution
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        map<int, int> a;
        vector<int> result;
        for (int i = 0; i < numbers.size(); i++)
        {
            a[numbers[i]] = i;
        }
        for (int t = 0; t < numbers.size(); t++)
        {
            int k = target - numbers[t];

            if (a.find(k) != a.end() && a[k] > t)
            {
                result.push_back(t);
                result.push_back(a[k]);
            }
        }
        return result;
    }
};