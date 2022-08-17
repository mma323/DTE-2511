#Hentet fra løsningsforslag, modifisert i ettertid
import math

# Return the points that form a convex hull 
def get_convex_hull(my_points):   
    # Step 1
    h0 = get_right_most_lowest_point(my_points)
    
    H = [h0]    
    t0 = h0
        
    # Step 2 and Step 3
    while True:   
        t1 = my_points[0]
        for i in range(1, len(my_points)):
            status = which_side(
                t0[0], t0[1], t1[0], t1[1], my_points[i][0], my_points[i][1]
            )
        
            if status < 0:  # Right side of the line
                t1 = my_points[i]
            elif status == 0:
                if distance(my_points[i][0], my_points[i][1], t0[0], t0[1]) > \
                   distance(t1[0], t1[1], t0[0], t0[1]):
                    t1 = my_points[i]
      
        if t1[0] == h0[0] and t1[1] == h0[1]: 
            break; # A convex hull is found
        else:
            H.append(t1)
            t0 = t1
    
    return H
  
# Return the rightmost lowest point in S 
def get_right_most_lowest_point(points):
    right_most_index = 0;
    right_most_x = points[0][0];
    right_most_y = points[0][1];
    
    for i in range(1, len(points)):
        if right_most_y > points[i][1]:
            right_most_y = points[i][1]
            right_most_x = points[i][0]
            right_most_index = i
        elif right_most_y == points[i][1] and right_most_x < points[i][0]:
            right_most_x = points[i][0]
            right_most_index = i   
    
    return points[right_most_index]
  
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
  
# Is (x2, y2) on the right side of [x0, y0] and [x1, y1]  
def which_side(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)


def main():
    coordinates = input("Enter the points in one line separated by space: ")
    coordinates = coordinates.split()
    print(coordinates)
    points = [
        [float(coordinates[i]), float(coordinates[i + 1])] 
        for i in range(0, len(coordinates) - 2, 2)
    ]
    print(points)

    convex_hull = get_convex_hull(points)   
    print("The convex hull is ")
    print(convex_hull)

if __name__ == "__main__":
    main()
