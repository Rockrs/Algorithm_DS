class Solution {
public:
    int longestValidParentheses(string s) {
        vector<char> vect;
        int n  = s.length();
        for (int i=0;i<n;i++){
            vect.push_back(s[i]);
        }

        for (int i=0;i<n;i++){
            if (vect[i]==')' && i!=0){
                if (vect[i-1]=='(' || vect[i-1]=='0'){
                    int j=i-1;
                    while(j>=0){
                        if (vect[j]=='('){
                            vect[j]='0';
                            vect[i]='0';
                            break;
                        }
                        j-=1;
                    }
                }
            }
        }

        for (auto it=vect.begin();it!=vect.end();++it){
            cout<<*it;
        }
        int g_max=0,l_max=0;
        for (auto it=vect.begin();it!=vect.end();++it){
            if (*it!='0'){
                g_max = max(g_max,l_max);
                l_max=0;
            }
            else{
                l_max+=1;
            }
        }
        g_max = max(l_max,g_max);
       return g_max;
    }
};
