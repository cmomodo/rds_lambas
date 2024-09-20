const express = require("express");
const mysql = require("mysql2");
const bodyParser = require("body-parser");

const app = express();
const port = 5000;

// Middleware
app.use(bodyParser.json());

// AWS RDS Database connection
const connection = mysql.createConnection({
  host: "your-rds-endpoint",
  user: "your-db-username",
  password: "your-db-password",
  database: "your-db-name",
  port: "your-db-port",
});

connection.connect((err) => {
  if (err) {
    console.error("Error connecting to the database:", err.stack);
    return;
  }
  console.log("Connected to the database.");
});

// API endpoint to handle POST requests
app.post("/api/customers", (req, res) => {
  const {
    customer_id,
    first_name,
    last_name,
    email,
    phone_number,
    address,
    city,
    state,
    postal_code,
  } = req.body;

  const query = `
        INSERT INTO customers (customer_id, first_name, last_name, email, phone_number, address, city, state, postal_code)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    `;

  connection.query(
    query,
    [
      customer_id,
      first_name,
      last_name,
      email,
      phone_number,
      address,
      city,
      state,
      postal_code,
    ],
    (error, results) => {
      if (error) {
        console.error("Error executing query:", error);
        return res.status(500).json({ error: "Database error" });
      }
      res
        .status(200)
        .json({ message: "Customer added successfully", data: results });
    },
  );
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
