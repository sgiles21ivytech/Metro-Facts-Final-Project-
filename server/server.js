// server.js

import express from "express";
import dotenv from "dotenv";
import cors from "cors";

// Import route files using your naming conventions
import authRoutes from "./routes/authRoutes.js";
import userRoutes from "./routes/userRoutes.js";
import departmentRoutes from "./routes/departmentRoutes.js";
import roleRoutes from "./routes/roleRoutes.js";
import metricsRoutes from "./routes/metricsRoute.js";
import reportsRoutes from "./routes/reportsRoutes.js";

// Load environment variables
dotenv.config();

const app = express();

// Middleware
app.use(
  cors({
    origin: "http://localhost:5173/",
    credentials: true,
  }));
app.use(express.json());

// Database connection
import connectDB from "./config/db.js";
connectDB();

// Routes
app.use("/api/auth", authRoutes);
app.use("/api/users", userRoutes);
app.use("/api/departments", departmentRoutes);
app.use("/api/roles", roleRoutes);
app.use("/api/metrics", metricsRoutes);
app.use("/api/reports", reportsRoutes);

// Root route
app.get("/", (req, res) => {
  res.send("Metro Facts API is running...");
});

// Start server
const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
