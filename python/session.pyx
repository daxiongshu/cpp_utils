cimport session

def split_session(session_id, 
                  item_id_viewed,
                  item_id_purchased):
    X = []
    Y = []
    session.split_session(session_id,
                          item_id_viewed,
                          item_id_purchased,
                          X, Y)
    return X, Y