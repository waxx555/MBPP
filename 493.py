'''
Write a function to calculate a grid of hexagon coordinates where function returns a list of lists containing 6 tuples of x, y point coordinates.
'''


import math
def calculate_polygons(startx, starty, endx, endy, radius):
    sl = (2 * radius) * math.tan(math.pi / 6)
    p = sl * 0.5
    b = sl * math.cos(math.radians(30))
    w = b * 2
    h = 2 * sl   
    startx = startx - w
    starty = starty - h
    endx = endx + w
    endy = endy + h
    origx = startx
    origy = starty
    xoffset = b
    yoffset = 3 * p
    polygons = []
    row = 1
    counter = 0
    while starty < endy:
        if row % 2 == 0:
            startx = origx + xoffset
        else:
            startx = origx
        while startx < endx:
            p1x = startx
            p1y = starty + p
            p2x = startx
            p2y = starty + (3 * p)
            p3x = startx + b
            p3y = starty + h
            p4x = startx + w
            p4y = starty + (3 * p)
            p5x = startx + w
            p5y = starty + p
            p6x = startx + b
            p6y = starty
            poly = [
                (p1x, p1y),
                (p2x, p2y),
                (p3x, p3y),
                (p4x, p4y),
                (p5x, p5y),
                (p6x, p6y),
                (p1x, p1y)]
            polygons.append(poly)
            counter += 1
            startx += w
        starty += yoffset
        row += 1
    return polygons


assert calculate_polygons(1,1, 4, 4, 3)==[[(-5.0, -4.196152422706632), (-5.0, -0.7320508075688767), (-2.0, 1.0), (1.0, -0.7320508075688767), (1.0, -4.196152422706632), (-2.0, -5.928203230275509), (-5.0, -4.196152422706632)], [(1.0, -4.196152422706632), (1.0, -0.7320508075688767), (4.0, 1.0), (7.0, -0.7320508075688767), (7.0, -4.196152422706632), (4.0, -5.928203230275509), (1.0, -4.196152422706632)], [(7.0, -4.196152422706632), (7.0, -0.7320508075688767), (10.0, 1.0), (13.0, -0.7320508075688767), (13.0, -4.196152422706632), (10.0, -5.928203230275509), (7.0, -4.196152422706632)], [(-2.0, 1.0000000000000004), (-2.0, 4.464101615137755), (1.0, 6.196152422706632), (4.0, 4.464101615137755), (4.0, 1.0000000000000004), (1.0, -0.7320508075688767), (-2.0, 1.0000000000000004)], [(4.0, 1.0000000000000004), (4.0, 4.464101615137755), (7.0, 6.196152422706632), (10.0, 4.464101615137755), (10.0, 1.0000000000000004), (7.0, -0.7320508075688767), (4.0, 1.0000000000000004)], [(-5.0, 6.196152422706632), (-5.0, 9.660254037844387), (-2.0, 11.392304845413264), (1.0, 9.660254037844387), (1.0, 6.196152422706632), (-2.0, 4.464101615137755), (-5.0, 6.196152422706632)], [(1.0, 6.196152422706632), (1.0, 9.660254037844387), (4.0, 11.392304845413264), (7.0, 9.660254037844387), (7.0, 6.196152422706632), (4.0, 4.464101615137755), (1.0, 6.196152422706632)], [(7.0, 6.196152422706632), (7.0, 9.660254037844387), (10.0, 11.392304845413264), (13.0, 9.660254037844387), (13.0, 6.196152422706632), (10.0, 4.464101615137755), (7.0, 6.196152422706632)], [(-2.0, 11.392304845413264), (-2.0, 14.85640646055102), (1.0, 16.588457268119896), (4.0, 14.85640646055102), (4.0, 11.392304845413264), (1.0, 9.660254037844387), (-2.0, 11.392304845413264)], [(4.0, 11.392304845413264), (4.0, 14.85640646055102), (7.0, 16.588457268119896), (10.0, 14.85640646055102), (10.0, 11.392304845413264), (7.0, 9.660254037844387), (4.0, 11.392304845413264)]]
assert calculate_polygons(5,4,7,9,8)==[[(-11.0, -9.856406460551018), (-11.0, -0.6188021535170058), (-3.0, 4.0), (5.0, -0.6188021535170058), (5.0, -9.856406460551018), (-3.0, -14.475208614068023), (-11.0, -9.856406460551018)], [(5.0, -9.856406460551018), (5.0, -0.6188021535170058), (13.0, 4.0), (21.0, -0.6188021535170058), (21.0, -9.856406460551018), (13.0, -14.475208614068023), (5.0, -9.856406460551018)], [(21.0, -9.856406460551018), (21.0, -0.6188021535170058), (29.0, 4.0), (37.0, -0.6188021535170058), (37.0, -9.856406460551018), (29.0, -14.475208614068023), (21.0, -9.856406460551018)], [(-3.0, 4.0), (-3.0, 13.237604307034012), (5.0, 17.856406460551018), (13.0, 13.237604307034012), (13.0, 4.0), (5.0, -0.6188021535170058), (-3.0, 4.0)], [(13.0, 4.0), (13.0, 13.237604307034012), (21.0, 17.856406460551018), (29.0, 13.237604307034012), (29.0, 4.0), (21.0, -0.6188021535170058), (13.0, 4.0)], [(-11.0, 17.856406460551018), (-11.0, 27.09401076758503), (-3.0, 31.712812921102035), (5.0, 27.09401076758503), (5.0, 17.856406460551018), (-3.0, 13.237604307034012), (-11.0, 17.856406460551018)], [(5.0, 17.856406460551018), (5.0, 27.09401076758503), (13.0, 31.712812921102035), (21.0, 27.09401076758503), (21.0, 17.856406460551018), (13.0, 13.237604307034012), (5.0, 17.856406460551018)], [(21.0, 17.856406460551018), (21.0, 27.09401076758503), (29.0, 31.712812921102035), (37.0, 27.09401076758503), (37.0, 17.856406460551018), (29.0, 13.237604307034012), (21.0, 17.856406460551018)], [(-3.0, 31.712812921102035), (-3.0, 40.95041722813605), (5.0, 45.569219381653056), (13.0, 40.95041722813605), (13.0, 31.712812921102035), (5.0, 27.09401076758503), (-3.0, 31.712812921102035)], [(13.0, 31.712812921102035), (13.0, 40.95041722813605), (21.0, 45.569219381653056), (29.0, 40.95041722813605), (29.0, 31.712812921102035), (21.0, 27.09401076758503), (13.0, 31.712812921102035)]]
assert calculate_polygons(9,6,4,3,2)==[[(5.0, 2.5358983848622456), (5.0, 4.8452994616207485), (7.0, 6.0), (9.0, 4.8452994616207485), (9.0, 2.5358983848622456), (7.0, 1.3811978464829942), (5.0, 2.5358983848622456)], [(7.0, 6.0), (7.0, 8.309401076758503), (9.0, 9.464101615137753), (11.0, 8.309401076758503), (11.0, 6.0), (9.0, 4.8452994616207485), (7.0, 6.0)]]
