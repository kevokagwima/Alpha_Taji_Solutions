create TABLE members(
  id INTEGER IDENTITY(1,1) PRIMARY KEY,
  first_name VARCHAR(30) NOT NULL,
  second_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30) NOT NULL,
  email VARCHAR(50) NOT NULL,
  username VARCHAR(20) NOT NULL,
  password VARCHAR(30) NOT NULL,
  phone_number INTEGER NOT NULL
)
