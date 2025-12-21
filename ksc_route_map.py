#!/usr/bin/env python3
"""
Kennedy Space Center Visitor Complex - Tour Route Map
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(16, 11))
ax.set_xlim(0, 100)
ax.set_ylim(0, 75)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('#e8f4e8')

# Title
ax.text(50, 72, 'Kennedy Space Center Visitor Complex', fontsize=20, fontweight='bold',
        ha='center', va='center', color='#1a237e')
ax.text(50, 68, 'Recommended Tour Route Map', fontsize=14, ha='center', va='center', color='#1a237e')

# ============ Define locations ============
locations = {
    'entrance': (10, 50, 'ENTRANCE', '#4CAF50'),
    'heroes': (25, 50, 'Heroes &\nLegends', '#2196F3'),
    'rocket_garden': (40, 50, 'Rocket\nGarden', '#FF9800'),
    'gateway': (55, 50, 'Gateway\nBuilding', '#9C27B0'),
    'bus_station': (70, 50, 'Bus Tour\nStation', '#F44336'),
}

# Bus tour destinations
bus_destinations = {
    'gantry': (88, 38, 'The Gantry\nat LC-39', '#00BCD4'),
    'apollo': (88, 22, 'Apollo/Saturn V\nCenter', '#E91E63'),
}

# ============ Draw main area ============
main_area = FancyBboxPatch((5, 38), 75, 22, boxstyle="round,pad=0.02,rounding_size=2",
                            facecolor='#fff3e0', edgecolor='#ff9800', linewidth=3, alpha=0.7)
ax.add_patch(main_area)
ax.text(42.5, 58, 'MAIN VISITOR COMPLEX (Walking Area)', fontsize=13, ha='center',
        fontweight='bold', color='#e65100')

# Bus tour area
bus_area = FancyBboxPatch((80, 14), 18, 32, boxstyle="round,pad=0.02,rounding_size=2",
                           facecolor='#e3f2fd', edgecolor='#2196f3', linewidth=3, alpha=0.7)
ax.add_patch(bus_area)
ax.text(89, 44, 'BUS TOUR\nAREA', fontsize=12, ha='center',
        fontweight='bold', color='#1565c0')

# ============ Draw locations ============
# Main complex locations
for i, (key, (x, y, label, color)) in enumerate(locations.items(), 1):
    circle = Circle((x, y), 4.5, facecolor=color, edgecolor='white', linewidth=2.5, alpha=0.9)
    ax.add_patch(circle)
    ax.text(x, y, str(i), fontsize=16, ha='center', va='center', color='white', fontweight='bold')
    ax.text(x, y-9, label, fontsize=10, ha='center', va='center', color='#333', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=color, alpha=0.95, linewidth=2))

# Bus tour destinations
for i, (key, (x, y, label, color)) in enumerate(bus_destinations.items(), 6):
    circle = Circle((x, y), 4.5, facecolor=color, edgecolor='white', linewidth=2.5, alpha=0.9)
    ax.add_patch(circle)
    ax.text(x, y, str(i), fontsize=16, ha='center', va='center', color='white', fontweight='bold')
    ax.text(x, y-8, label, fontsize=10, ha='center', va='center', color='#333', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=color, alpha=0.95, linewidth=2))

# ============ Draw route arrows ============
arrow_style = "Simple, tail_width=2, head_width=8, head_length=5"

# Walking route (green arrows)
walking_coords = [((14.5, 50), (20.5, 50)), ((29.5, 50), (35.5, 50)),
                  ((44.5, 50), (50.5, 50)), ((59.5, 50), (65.5, 50))]
for (x1, y1), (x2, y2) in walking_coords:
    arrow = FancyArrowPatch((x1, y1), (x2, y2), connectionstyle="arc3,rad=0",
                            arrowstyle=arrow_style, color='#4CAF50', lw=2)
    ax.add_patch(arrow)

# Bus route (blue dashed arrows)
bus_arrow1 = FancyArrowPatch((74.5, 48), (84, 42), connectionstyle="arc3,rad=0.2",
                              arrowstyle=arrow_style, color='#2196F3', lw=2)
ax.add_patch(bus_arrow1)

bus_arrow2 = FancyArrowPatch((88, 33.5), (88, 26.5), connectionstyle="arc3,rad=0",
                              arrowstyle=arrow_style, color='#2196F3', lw=2)
ax.add_patch(bus_arrow2)

# Return route (orange arrow)
return_arrow = FancyArrowPatch((82, 20), (72, 46), connectionstyle="arc3,rad=-0.35",
                                arrowstyle=arrow_style, color='#FF5722', lw=2)
ax.add_patch(return_arrow)

# ============ Legend ============
legend_y = 10
ax.text(5, legend_y + 2, 'LEGEND:', fontsize=12, fontweight='bold', color='#333')

# Walking route
ax.plot([5, 18], [legend_y - 2, legend_y - 2], color='#4CAF50', linewidth=4, solid_capstyle='round')
ax.text(20, legend_y - 2, 'Walking Route', fontsize=11, va='center', color='#333')

# Bus route
ax.plot([5, 18], [legend_y - 5, legend_y - 5], color='#2196F3', linewidth=4)
ax.text(20, legend_y - 5, 'Bus Tour Route', fontsize=11, va='center', color='#333')

# Return route
ax.plot([5, 18], [legend_y - 8, legend_y - 8], color='#FF5722', linewidth=4)
ax.text(20, legend_y - 8, 'Return Bus Route', fontsize=11, va='center', color='#333')

# ============ Recommended Itinerary ============
itinerary_text = """RECOMMENDED ITINERARY:

1. 9:00 AM - Enter through main entrance
2. Heroes & Legends (30-45 min)
   - Learn about space pioneers
3. Rocket Garden (20-30 min)
   - Walk among real rockets
4. Gateway Building (45-60 min)
   - Interactive exhibits
5. Take Bus Tour from Station (5 min ride)
6. The Gantry at LC-39 (30-45 min)
   - 360-degree launch pad views
7. Apollo/Saturn V Center (60-90 min)
   - See the massive Saturn V rocket!

>> Return to Main Complex by Bus"""

ax.text(48, 11, itinerary_text, fontsize=10, va='top', ha='left', color='#333',
        family='monospace',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#fffde7', edgecolor='#fbc02d',
                  alpha=0.95, linewidth=2),
        linespacing=1.4)

# Tips box
tips_text = """TIPS:
* Arrive early (9 AM)
* Allow full day
* Wear comfortable shoes
* Download KSC App"""
ax.text(5, -2, tips_text, fontsize=9, va='top', ha='left', color='#333',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#e8f5e9', edgecolor='#4CAF50',
                  alpha=0.95, linewidth=2),
        linespacing=1.3)

# Save
plt.tight_layout()
plt.savefig('/home/user/hello-world-project/ksc_route_map.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Route map saved to: ksc_route_map.png")
