import matplotlib.pyplot as plt
import numpy as np

class House:
    def __init__(self, lower_limit, upper_limit, bottom_color, middle_color, upper_color, alignment):
        self.lower_limit = lower_limit / 100
        self.upper_limit = upper_limit / 100
        self.bottom_color = bottom_color
        self.middle_color = middle_color
        self.upper_color = upper_color
        self.alignment = alignment

    def get_rotated_corners(self, x, y, width, height):
        """
        Rotates the rectangle's corners based on the alignment.
        :param x, y: Bottom-left corner of the house.
        :param width, height: Width and height of the house.
        :return: List of rotated corners (x, y) coordinates.
        """
        # Define the corners of the house
        corners = np.array([
            [x, y],  # Bottom-left
            [x + width, y],  # Bottom-right
            [x + width, y + height],  # Top-right
            [x, y + height]  # Top-left
        ])

        # Rotation matrix for 90, 180, and 270 degrees
        if self.alignment == 0:  # 90 degrees
            rotation_matrix = np.array([[0, -1], [1, 0]])
        elif self.alignment == 1:  # 180 degrees
            rotation_matrix = np.array([[-1, 0], [0, -1]])
        elif self.alignment == 2:  # 270 degrees
            rotation_matrix = np.array([[0, 1], [-1, 0]])
        else:  # 0 degrees (no rotation)
            rotation_matrix = np.array([[1, 0], [0, 1]])

        # Rotate all corners and return the new coordinates
        rotated_corners = np.dot(corners - [x + width / 2, y + height / 2], rotation_matrix) + [x + width / 2, y + height / 2]
        return rotated_corners

def draw_vedic_chart(houses):
    """
    Draws a South Indian Vedic Astrology chart with 12 houses in the correct format.
    Each house is filled with three colors based on the lower and upper limits.
    :param houses: List of 12 House objects.
    """
    assert len(houses) == 12, "Input must be a list of 12 House objects."
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)
    
    # Define the house positions with House 12 at (0, 3) and numbering clockwise
    house_positions = {
        12: (0, 3), 1: (1, 3), 2: (2, 3), 3: (3, 3), 4: (3, 2), 5: (3, 1), 
        6: (3, 0), 7: (2, 0), 8: (1, 0), 9: (0, 0), 10: (0, 1), 11: (0, 2)
    }
    
    # Draw the 12 houses
    for house_num, (x, y) in house_positions.items():
        house = houses[house_num - 1]  # Get corresponding House object
        
        width, height = 1, 1
        
        # Get rotated corners
        rotated_corners = house.get_rotated_corners(x, y, width, height)

        # Fill the three color sections based on the rotation
        # Calculate heights for each section
        lower_height = house.lower_limit
        middle_height = house.upper_limit - house.lower_limit
        upper_height = 1 - house.upper_limit

        # Draw the bottom section (0 to lower_limit)
        bottom_corners = rotated_corners[:2]
        bottom_rect = plt.Polygon(rotated_corners[:2], closed=True, edgecolor='black', fill=True, color=house.bottom_color, alpha=0.6)
        ax.add_patch(bottom_rect)

        # Draw the middle section (lower_limit to upper_limit)
        middle_corners = rotated_corners[1:3]
        middle_rect = plt.Polygon(rotated_corners[1:3], closed=True, edgecolor='black', fill=True, color=house.middle_color, alpha=0.6)
        ax.add_patch(middle_rect)

        # Draw the upper section (upper_limit to 1)
        upper_corners = rotated_corners[2:]
        upper_rect = plt.Polygon(rotated_corners[2:], closed=True, edgecolor='black', fill=True, color=house.upper_color, alpha=0.6)
        ax.add_patch(upper_rect)

        # Add house number
        ax.text(x + width / 2, y + height - 0.1, str(house_num), ha='center', va='center', fontsize=12, color='black', fontweight='bold')
        
        # Add percentage values near the edges of each filled section
        ax.text(x + width / 2, y + house.lower_limit - 0.05, f"{int(house.lower_limit * 100)}%", ha='center', va='center', fontsize=10, color='black')
        ax.text(x + width / 2, y + house.upper_limit - 0.05, f"{int(house.upper_limit * 100)}%", ha='center', va='center', fontsize=10, color='black')

    plt.show()

# Example usage
houses = [
    House(20, 60, 'red', 'yellow', 'green', 0),
    House(10, 50, 'blue', 'purple', 'orange', 0),
    House(30, 70, 'cyan', 'magenta', 'lime', 0),
    House(15, 65, 'brown', 'pink', 'grey', 1),
    House(25, 55, 'navy', 'teal', 'gold', 1),
    House(5, 35, 'maroon', 'olive', 'beige', 2),
    House(40, 80, 'violet', 'turquoise', 'coral', 2),
    House(20, 60, 'red', 'yellow', 'green', 2),
    House(10, 50, 'blue', 'purple', 'orange', 2),
    House(30, 70, 'cyan', 'magenta', 'lime', 3),
    House(15, 65, 'brown', 'pink', 'grey', 3),
    House(25, 55, 'navy', 'teal', 'gold', 0)
]

draw_vedic_chart(houses)
