import numpy as np

def is_segments_intersect(p1, p2, p3, p4):
    """
    Check whether line segments p1p2 and p3p4 intersect in three-dimensional space
    """
    if np.allclose(p1, p3) or np.allclose(p1, p4) or np.allclose(p2, p3) or np.allclose(p2, p4):
        return False
    
    v1 = p2 - p1
    v2 = p4 - p3
    
    r = p3 - p1
    
    v1xv2 = np.cross(v1, v2)
    rxv1 = np.cross(r, v1)
    rxv2 = np.cross(r, v2)
    
    if np.abs(np.dot(r, v1xv2)) > 1e-10:
        return False 
    
    v1xv2_squared = np.dot(v1xv2, v1xv2)
    
    if v1xv2_squared < 1e-10:
        if np.linalg.norm(rxv1) > 1e-10:
            return False
        
        t0 = np.dot(r, v1) / np.dot(v1, v1)
        t1 = t0 + np.dot(v2, v1) / np.dot(v1, v1)
        
        if (t0 <= 0 <= t1) or (t0 <= 1 <= t1) or (0 <= t0 <= 1) or (0 <= t1 <= 1):
            return True
        return False
    
    t = np.dot(np.cross(r, v2), v1xv2) / v1xv2_squared
    s = np.dot(np.cross(r, v1), v1xv2) / v1xv2_squared
    
    return (0 <= t <= 1) and (0 <= s <= 1)

def check_quadrilateral_intersections(A, B, C, D):
    """
    Check whether the four sides of quadrilateral ABCD intersect
    """
    A = np.array(A)
    B = np.array(B)
    C = np.array(C)
    D = np.array(D)

    AB_CD = is_segments_intersect(A, B, C, D)
    BC_DA = is_segments_intersect(B, C, D, A)

    return AB_CD or BC_DA

if __name__ == "__main__":
    A = [0, 0, 0]
    B = [1, 0, 0]
    C = [0, 1, 0]
    D = [1, 1, 0]

    result = check_quadrilateral_intersections(A, B, C, D)
    print(result)
