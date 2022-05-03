cimport session
from libcpp.vector cimport vector

def split_session(session_id, 
                  item_id_viewed,
                  item_id_purchased):
    cdef vector[vector[int]] X;
    cdef vector[int] Y;
    session.split_session(session_id,
                          item_id_viewed,
                          item_id_purchased,
                          X, Y)
    return X, Y