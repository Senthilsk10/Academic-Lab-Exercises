import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_star(ax, x1, y1, x2, y2):
    width = x2 - x1
    ellipse = patches.Ellipse(((x1 + x2) / 2, y2 - 10), width, 70, angle=0, color='black', fill=False)
    ax.add_patch(ellipse)
    ax.text(x1 - 2, y2 - 17, 'v', fontsize=12)
    ax.plot([x2 + 10, x2 + 30], [y2, y2], 'k-')
    ax.text(x1 - 15, y1 - 3, '>', fontsize=12)
    ax.add_patch(patches.Circle((x1 - 40, y1), 10, color='black', fill=False))
    ax.add_patch(patches.Circle((x1 - 80, y1), 10, color='black', fill=False))
    ax.plot([x1 - 30, x1 - 10], [y2, y2], 'k-')
    ax.text(x2 + 25, y2 - 3, '>', fontsize=12)
    ax.text(x2 + 15, y2 - 9, chr(238), fontsize=12)
    ax.text(x1 - 25, y1 - 9, chr(238), fontsize=12)
    ax.text((x2 - x1) / 2 + x1, y1 - 30, chr(238), fontsize=12)
    ax.text((x2 - x1) / 2 + x1, y1 + 30, chr(238), fontsize=12)
    ax.add_patch(patches.Ellipse(((x1 + x2) / 2, y2 + 10), width + 80, 70, angle=180, color='black', fill=False))
    ax.text(x2 + 37, y2 + 14, '^', fontsize=12)
    return x1 - 40, y1

def draw_basis(ax, x1, y1, label):
    ax.add_patch(patches.Circle((x1, y1), 10, color='black', fill=False))
    ax.plot([x1 + 30, x1 + 10], [y1, y1], 'k-')
    ax.text(x1 + 20, y1 - 10, label, fontsize=12)
    ax.text(x1 + 23, y1 - 3, '>', fontsize=12)

def draw_slash(ax, x1, y1, x2, y2, x3, y3, x4, y4):
    c1 = max(x1, x3)
    c2 = max(x2, x4)
    ax.plot([x1 - 10, c1 - 40], [y1, (y3 - y1) / 2 + y1 - 10], 'k-')
    ax.text(x1 - 15, y1 - 3, '>', fontsize=12)
    ax.text(x3 - 15, y4 - 3, '>', fontsize=12)
    ax.add_patch(patches.Circle((c1 - 40, (y4 - y2) / 2 + y2), 10, color='black', fill=False))
    ax.text(c1 - 40, (y4 - y2) / 2 + y2 + 25, chr(238), fontsize=12)
    ax.text(c1 - 40, (y4 - y2) / 2 + y2 - 25, chr(238), fontsize=12)
    ax.plot([x2 + 10, c2 + 40], [y2, (y4 - y2) / 2 + y2 - 10], 'k-')
    ax.plot([x3 - 10, c1 - 40], [y3, (y3 - y1) / 2 + y2 + 10], 'k-')
    ax.add_patch(patches.Circle((c2 + 40, (y4 - y2) / 2 + y2), 10, color='black', fill=False))
    ax.text(c2 + 40, (y4 - y2) / 2 + y2 - 25, chr(238), fontsize=12)
    ax.text(c2 - 40, (y4 - y2) / 2 + y2 + 25, chr(238), fontsize=12)
    ax.text(c2 + 35, (y4 - y2) / 2 + y2 - 15, '^', fontsize=12)
    ax.text(c1 + 35, (y4 - y2) / 2 + y2 + 10, '^', fontsize=12)

def draw_nfa(regex):
    x1, y1 = 200, 200
    stx, endx, sty, endy = [], [], [], []
    pos = 0
    i = 0
    len_regex = len(regex)
    
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    
    while i < len_regex:
        if regex[i].isalpha():
            if i + 1 < len_regex and regex[i + 1] == '*':
                x1 += 40
            draw_basis(ax, x1, y1, regex[i])
            stx.append(x1)
            endx.append(x1 + 40)
            sty.append(y1)
            endy.append(y1)
            x1 += 40
            pos += 1
        elif regex[i] == '*':
            x1, y1 = draw_star(ax, stx[pos - 1], sty[pos - 1], endx[pos - 1], endy[pos - 1])
            x1 += 40
        elif regex[i] == '/':
            cx1, cy1 = stx[pos - 1], sty[pos - 1]
            cx2, cy2 = endx[pos - 1], endy[pos - 1]
            i += 1
            while i < len_regex and regex[i] in ' ()':
                i += 1
            cx3, cy3 = stx[pos - 1], sty[pos - 1]
            cx4, cy4 = endx[pos - 1], endy[pos - 1]
            draw_slash(ax, cx1, cy1, cx2, cy2, cx3, cy3, cx4, cy4)
            x1 += 40
        i += 1
    
    ax.add_patch(patches.Circle((x1, y1), 13, color='black', fill=False))
    ax.plot([x1 - 30, x1 - 10], [y1, y1], 'k-')
    ax.text(x1 - 100, y1 - 10, 'start', fontsize=12)
    ax.text(x1 - 15, y1 - 3, '>', fontsize=12)
    
    plt.show()

# Example usage
regex = input("Enter the regular expression: ")
draw_nfa(regex)
