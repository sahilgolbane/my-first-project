=== FOREIGN KEY (linking two tables) ===

- foreign key = a sticky note on each task saying which user owns it
- user_id column on tasks = holds the owner's id number
- FK is written as: user_id = Column(Integer, ForeignKey("users.id"))
- "users.id" = the TABLE name (lowercase), not the class name

- GET /users/1/tasks = find all tasks whose user_id == 1
  (filter tasks by user_id, not by task's own id)

=== REMEMBER ===
- change a model? DROP TABLE first, then restart (create_all only makes MISSING tables)
- put specific routes ABOVE flexible ones: /users/count before /users/{id}
- every def line ends with a colon :
- Ctrl+S after writing, then "cat filename" to confirm it saved