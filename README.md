<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Domine&weight=500&size=30&pause=1000&color=1FF741&center=true&vCenter=true&width=200&lines=Higher" alt="Higher"/>
  <img src="https://readme-typing-svg.demolab.com?font=Domine&weight=500&size=30&pause=1000&color=F4F7F5&center=true&vCenter=true&width=100&lines=or" alt="or"/>
  <img src="https://readme-typing-svg.demolab.com?font=Domine&weight=500&size=30&pause=1000&color=F7132B&center=true&vCenter=true&width=200&lines=Lower" alt="Lower"/>
  <img src="https://readme-typing-svg.demolab.com?font=Domine&weight=500&size=30&pause=1000&color=F4F7F5&center=true&vCenter=true&width=200&lines=Game" alt="Game"/>
</p>


## Description
This is a simple Python-based game inspired by the popular "Higher or Lower" game. The objective is to guess which celebrity has more followers on social media. You will be presented with two random celebrities from a dataset, and you must choose the one you think has more followers.

## How to Play
1. You will be shown two random celebrities, their description, and their country.
2. Guess which one has the highest number of followers by typing `"A"` or `"B"`.
3. If you're correct, your score increases, and the game continues.
4. If you're wrong, the game ends and your final score will be displayed.

## Requirements
- Python 3.x
- `art` package (for displaying ASCII art)
- `game_data.py` file containing celebrity data

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/higher-lower-game.git
   ```
2. Install the required package:
   ```bash
   pip install art
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## Project Structure
- `main.py`: Contains the game logic.
- `game_data.py`: Contains a list of dictionaries with celebrity data (name, description, country, and follower count).
- `art.py`: Contains ASCII art for the logo and the "vs" symbol.

## Example Game Output
```
Compare A: John Doe, a musician, from the United States.
VS
Compare B: Jane Smith, a model, from the United Kingdom.
Who has more followers? Type "A" or "B": 
```

## Contributing
Feel free to submit issues or pull requests if you want to improve the game or add new features!
