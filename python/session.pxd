from libcpp.vector cimport vector

cdef extern from "session.h":
    void split_session(const vector[int] session_id, 
                     const vector[int] item_id_viewed,
                     const vector[int] item_id_purchased,
                     vector[vector[int]]& X,
                     vector[int]& Y);