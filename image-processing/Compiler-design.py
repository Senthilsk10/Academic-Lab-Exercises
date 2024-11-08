import matplotlib.pyplot as plt
import numpy as np

# Define drawing functions
def draw_star(ax, x1, y1, x2, y2):
    """Draws a star-like pattern."""
    middle_x = (x1 + x2) / 2
    radius = (x2 - x1) / 2

    # Draw the ellipse
    ellipse = plt.Circle((middle_x, y2 - 10), radius, color='black', fill=False)
    ax.add_patch(ellipse)
    
    # Draw the lines
    ax.plot([x1 - 2, middle_x], [y2 - 17, y2], color='black')
    ax.plot([x2 + 10, x2 + 30], [y2, y2], color='black')
    ax.plot([x1 - 30, x1 - 10], [y2, y2], color='black')
    ax.plot([x2 + 10, x2 + 40], [y2, y2], color='black')

    # Draw text
    ax.text(x1 - 15, y1 - 3, ">", fontsize=12, ha='center')
    ax.text(x2 + 25, y2 - 3, ">", fontsize=12, ha='center')
    
    # Draw circles
    ax.add_patch(plt.Circle((x1 - 40, y1), 10, color='black', fill=False))
    ax.add_patch(plt.Circle((x1 - 80, y1), 10, color='black', fill=False))
    ax.add_patch(plt.Circle((x2 + 40, (y2 - y1) / 2 + y1), 10, color='black', fill=False))
    ax.add_patch(plt.Circle((x2 + 40, (y2 - y1) / 2 + y1), 10, color='black', fill=False))

    # Draw arrows
    ax.text(middle_x, y1 - 30, "^", fontsize=12, ha='center')
    ax.text(middle_x, y1 + 30, "^", fontsize=12, ha='center')
    
    # Update min values
    global minx, miny
    if x1 - 40 < minx:
        minx = x1 - 40
    miny = y1

def draw_basis(ax, x1, y1, char):
    """Draws a basic element with circles and lines."""
    ax.add_patch(plt.Circle((x1, y1), 10, color='black', fill=False))
    ax.plot([x1 + 30, x1 + 10], [y1, y1], color='black')
    ax.text(x1 + 20, y1 - 10, char, fontsize=12, ha='center')
    ax.text(x1 + 23, y1 - 3, ">", fontsize=12, ha='center')

    # Update min values
    global minx, miny
    if x1 < minx:
        minx = x1
    miny = y1

def draw_slash(ax, x1, y1, x2, y2, x3, y3, x4, y4):
    """Draws a slash pattern."""
    c1 = max(x1, x3)
    c2 = max(x2, x4)
    
    ax.plot([x1 - 10, c1 - 40], [(y3 - y1) / 2 + y1 - 10], color='black')
    ax.plot([x2 + 10, c2 + 40], [(y4 - y2) / 2 + y2 - 10], color='black')
    ax.plot([x3 - 10, c1 - 40], [(y3 - y1) / 2 + y1 + 10], color='black')

    # Draw circles and text
    ax.add_patch(plt.Circle((c1 - 40, (y4 - y2) / 2 + y2), 10, color='black', fill=False))
    ax.add_patch(plt.Circle((c2 + 40, (y4 - y2) / 2 + y2), 10, color='black', fill=False))
    
    ax.text(c2 + 35, (y4 - y2) / 2 + y2 - 15, "^", fontsize=12, ha='center')
    ax.text(c1 + 35, (y4 - y2) / 2 + y2 + 10, "^", fontsize=12, ha='center')
    
    # Update min values
    global minx, miny
    minx = c1 - 40
    miny = (y4 - y2) / 2 + y2

# Initialize global variables
minx = 1000
miny = 0

def main():
    """Main function to read input and generate graphical output."""
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    
    # Example inputs
    input_str = input("Enter the regular expression: ")
    x1, y1 = 200, 200
    pos = 0
    stx, endx, sty, endy = [], [], [], []
    
    for i, char in enumerate(input_str):
        if char.isalpha():
            if i + 1 < len(input_str) and input_str[i + 1] == '*':
                x1 += 40
            draw_basis(ax, x1, y1, char)
            stx.append(x1)
            endx.append(x1 + 40)
            sty.append(y1)
            endy.append(y1)
            x1 += 40
            pos += 1
        elif char == '*':
            draw_star(ax, stx[-1], sty[-1], endx[-1], endy[-1])
            stx[-1] -= 40
            endx[-1] += 40
            x1 += 40
        elif char == '/':
            # Further implementation needed for handling '/'
            pass

    # Draw final elements
    ax.add_patch(plt.Circle((x1, y1), 13, color='black', fill=False))
    ax.plot([minx - 30, minx - 10], [miny, miny], color='black')
    ax.text(minx - 100, miny - 10, "start", fontsize=12, ha='center')
    ax.text(minx - 15, miny - 3, ">", fontsize=12, ha='center')

    plt.xlim(minx - 200, x1 + 200)
    plt.ylim(miny - 200, y1 + 200)
    plt.show()

if __name__ == "__main__":
    main()
