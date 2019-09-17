# python-chess
Chess game written in Python

My last chess attempt turned out to be not so successful. I tried to consider all the downsides of my java chess and make something actually good. Current version comes with terminal interface - after implementing (at least bigger part of) chess logic i might as well make some sort of window interface.

# Running
After extracting the zip simply run 
```
python3 python-chess
```

# How to do stuff there
The game in console interface works with commands (list of those that are supported so far):

**start**: starts the new game

**move *src-field* *trg-field*** - moves a piece from one field to another

  example:
  ```
  move e2 e4 - moves piece from e2 to e4
  ```

**put *field* *piece-desc*** - puts a piece on desired space

  example:
  ```
  put g3 wk - puts white king onto g3 field
  ```

piece description:
  - colors:
  
    * w - white
  
    * b - black
  
  - types:
  
    * p - pawn
  
    * k - knight
  
    * b - bishop
  
    * r - rook
  
    * q - queen
  
    * k - king
  
  - special:
  
    * null - represents no piece at the field
 
 Piece is described with two-char literal - first color, then type. White pawn - wp, black bishop - bb etc
