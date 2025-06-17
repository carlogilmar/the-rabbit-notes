def make_point(x, y):
    return (x, y)

def x_of(point):
    return point[0]

def y_of(point):
    return point[1]

def add_vectors(v1, v2):
    return (x_of(v1) + x_of(v2), y_of(v1) + y_of(v2))

def sub_vectors(v1, v2):
    return (x_of(v1) - x_of(v2), y_of(v1) - y_of(v2))

def scale_vector(scalar, v):
    return (scalar * x_of(v), scalar * y_of(v))

######################################################## 1st part
# -- Coordinate system basics ---
# Creates a point with x=10 and y=8
point = make_point(10, 8)
print(f"Point: {point}")  # → (10, 8)

# Extract X coordinate
x = x_of(point)
print(f"X: {x}")  # → 10

# Extract Y coordinate
y = y_of(point)
print(f"Y: {y}")  # → 8

# Create two points for vector math
point1 = make_point(10, 8)
point2 = make_point(1, 2)

# Add the two vectors (element-wise addition)
add_vector = add_vectors(point1, point2)
print(f"Add vector: {add_vector}")  # → (11, 10)

# Subtract point2 from point1 (element-wise subtraction)
sub_vectors = sub_vectors(point1, point2)
print(f"Sub vectors: {sub_vectors}")  # → (9, 6)

# Scale point1 by a factor of 10 (multiply both x and y by 10)
scale_vector_1 = scale_vector(10, point1)
print(f"Scale vector: {scale_vector_1}")  # → (100, 80)

########################################################
def make_frame(origin, edge1, edge2):
    return {
        "origin": origin,
        "edge1": edge1,
        "edge2": edge2
    }

def origin_of(frame):
    return frame["origin"]

def edge1_of(frame):
    return frame["edge1"]

def edge2_of(frame):
    return frame["edge2"]

def frame_coord_map(frame):
    def mapper(v):
        # v is a point like (0.5, 0.5)
        scaled_edge1 = scale_vector(x_of(v), edge1_of(frame))
        scaled_edge2 = scale_vector(y_of(v), edge2_of(frame))
        return add_vectors(origin_of(frame), add_vectors(scaled_edge1, scaled_edge2))
    return mapper

######################################################## 2nd part
origin = (0, 0)
edge1 = (1, 0)  # x-direction
edge2 = (0, 1)  # y-direction
frame = make_frame(origin, edge1, edge2)
mapper = frame_coord_map(frame)

print(mapper((0.5, 0.5)))  # Should return (0.5, 0.5)

print(f"Complete Frame: {frame}")
print(f"Origin: {origin}")
print(f"Edge1: {edge1}")
print(f"Edge2: {edge2}")

######################################################## 3rd Part

def segments_painter(segments):
    def painter(frame):
        mapper = frame_coord_map(frame)
        transformed_segments = []
        for seg in segments:
            start, end = seg
            transformed_segments.append((mapper(start), mapper(end)))
        return transformed_segments
    return painter

######################################################## 4th Part

def beside(painter1, painter2):
    def combined(frame):
        # Edges of the original frame
        origin = origin_of(frame)
        e1 = edge1_of(frame)
        e2 = edge2_of(frame)

        # Left sub-frame (0.0 to 0.5 on x-axis)
        left = make_frame(origin, scale_vector(0.5, e1), e2)

        # Right sub-frame (0.5 to 1.0 on x-axis)
        new_origin = add_vectors(origin, scale_vector(0.5, e1))
        right = make_frame(new_origin, scale_vector(0.5, e1), e2)

        # Apply painters to each half
        return painter1(left) + painter2(right)
    return combined

def below(painter1, painter2):
    def combined(frame):
        origin = origin_of(frame)
        e1 = edge1_of(frame)
        e2 = edge2_of(frame)

        # Bottom half
        bottom = make_frame(origin, e1, scale_vector(0.5, e2))

        # Top half
        new_origin = add_vectors(origin, scale_vector(0.5, e2))
        top = make_frame(new_origin, e1, scale_vector(0.5, e2))

        return painter1(bottom) + painter2(top)
    return combined

######################################################## 5th Part
def right_split(painter, n):
    if n == 0:
        return painter
    else:
        smaller = right_split(painter, n - 1)
        return beside(painter, smaller)

######################################################## 6th Part
def square_of_four(tl, tr, bl, br):
    top = beside(tl, tr)
    bottom = beside(bl, br)
    return below(bottom, top)

diag1 = segments_painter([((0, 0), (1, 1))])
diag2 = segments_painter([((0, 1), (1, 0))])
vline = segments_painter([((0.5, 0), (0.5, 1))])
hline = segments_painter([((0, 0.5), (1, 0.5))])

composite = square_of_four(diag1, diag2, vline, hline)
frame = make_frame((0, 0), (1, 0), (0, 1))
result = composite(frame)
print("Exercise")
print(result)

######################################################

def make_canvas(width, height):
    return [[" " for _ in range(width)] for _ in range(height)]

def to_grid_coords(x, y, width, height):
    gx = int(x * (width - 1))
    gy = int((1 - y) * (height - 1))  # Flip y for terminal orientation
    return gx, gy

def draw_point(canvas, x, y):
    width = len(canvas[0])
    height = len(canvas)
    gx, gy = to_grid_coords(x, y, width, height)
    if 0 <= gx < width and 0 <= gy < height:
        canvas[gy][gx] = "█"

def draw_segment(canvas, start, end, steps=100):
    x0, y0 = start
    x1, y1 = end
    for i in range(steps):
        t = i / steps
        x = x0 + t * (x1 - x0)
        y = y0 + t * (y1 - y0)
        draw_point(canvas, x, y)

def render_canvas(canvas):
    for row in canvas:
        print("".join(row))

def render_segments(segments, width=40, height=20):
    canvas = make_canvas(width, height)
    for start, end in segments:
        draw_segment(canvas, start, end)
    render_canvas(canvas)

segments = square_of_four(vline, hline, diag1, diag2)(frame)
render_segments(segments)

