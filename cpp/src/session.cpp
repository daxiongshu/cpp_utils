#include "session.h"
#include <cassert> 
#include <cstdio>

void split_session(const std::vector<int> session_id, 
                     const std::vector<int> item_id_viewed,
                     const std::vector<int> item_id_purchased,
                     std::vector<std::vector<int>>& X,
                     std::vector<int>& Y)
{
    assert(session_id.size() == item_id_viewed.size());
    assert(session_id.size() == item_id_purchased.size());

    int s = session_id[0];
    int y = item_id_purchased[0];
    std::vector<int> x_tmp;

    for(unsigned int i = 0; i < session_id.size(); i++){
        if (s!=session_id[i]){
            std::vector<int> x_tmp2(x_tmp);
            X.push_back(x_tmp2);
            x_tmp.clear();
            Y.push_back(y);
        }
        s = session_id[i];
        x_tmp.push_back(item_id_viewed[i]);
        y = item_id_purchased[i];
    }

    X.push_back(x_tmp);
    Y.push_back(y);
}