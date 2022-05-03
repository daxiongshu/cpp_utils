#pragma once
#include <vector>
void split_session(const std::vector<int> session_id, 
                     const std::vector<int> item_id_viewed,
                     const std::vector<int> item_id_purchased,
                     std::vector<std::vector<int>>& X,
                     std::vector<int>& Y);