class Solution
{
public:
    bool isHappy(int n)
    {
        if (n == 0)
            return 0;
        vector<int> a;
        int i = 0;
        while (n != 1)
        {
            int temp = n;
            a.push_back(temp);
            n = 0;

            while (temp > 0)
            {
                int dig = 0;
                dig = temp % 10;
                temp = temp / 10;
                n = n + (dig * dig);
            }
            if (find(a.begin(), a.end(), n) != a.end())
            {
                return false;
            }
        }
        return true;
    }
};